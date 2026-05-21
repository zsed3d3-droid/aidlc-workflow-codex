#!/usr/bin/env python3
"""Update bundled AI-DLC rules from awslabs/aidlc-workflows.

The script is designed for Codex SessionStart hooks:
- retry transient network failures a bounded number of times;
- preserve the existing cache on failure;
- exit 0 in best-effort mode so other startup hooks continue.
"""

from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
import tempfile
import time
import urllib.error
import urllib.request
import zipfile
from pathlib import Path


API_URL = "https://api.github.com/repos/awslabs/aidlc-workflows/releases/latest"
REPO_ZIP_FALLBACK = "https://github.com/awslabs/aidlc-workflows/archive/refs/heads/main.zip"
RULES_DIR_NAME = "aidlc-rules"
DEFAULT_TIMEOUT_SECONDS = 20


def log(message: str) -> None:
    print(f"[aidlc-update] {message}", file=sys.stderr)


def request_json(url: str, timeout: int) -> dict:
    request = urllib.request.Request(
        url,
        headers={
            "Accept": "application/vnd.github+json",
            "User-Agent": "codex-aidlc-skill-updater",
        },
    )
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            return json.loads(response.read().decode("utf-8"))
    except urllib.error.URLError:
        output = curl_read(url, timeout, accept="application/vnd.github+json")
        return json.loads(output.decode("utf-8"))


def download_file(url: str, destination: Path, timeout: int) -> None:
    request = urllib.request.Request(
        url,
        headers={
            "Accept": "application/octet-stream",
            "User-Agent": "codex-aidlc-skill-updater",
        },
    )
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            with destination.open("wb") as output:
                shutil.copyfileobj(response, output)
    except urllib.error.URLError:
        curl_download(url, destination, timeout, accept="application/octet-stream")


def curl_base_command(url: str, timeout: int, accept: str) -> list[str]:
    return [
        "curl",
        "-fsSL",
        "--connect-timeout",
        str(timeout),
        "--max-time",
        str(timeout),
        "-H",
        f"Accept: {accept}",
        "-H",
        "User-Agent: codex-aidlc-skill-updater",
        url,
    ]


def curl_read(url: str, timeout: int, accept: str) -> bytes:
    try:
        return subprocess.check_output(curl_base_command(url, timeout, accept), stderr=subprocess.STDOUT)
    except (FileNotFoundError, subprocess.CalledProcessError) as error:
        raise RuntimeError(f"curl fallback failed: {error}") from error


def curl_download(url: str, destination: Path, timeout: int, accept: str) -> None:
    command = curl_base_command(url, timeout, accept)
    command.extend(["-o", str(destination)])
    try:
        subprocess.check_call(command)
    except (FileNotFoundError, subprocess.CalledProcessError) as error:
        raise RuntimeError(f"curl fallback failed: {error}") from error


def choose_download(release: dict) -> tuple[str, str]:
    tag = str(release.get("tag_name") or "unknown")
    assets = release.get("assets") or []
    zip_assets = [
        asset
        for asset in assets
        if str(asset.get("name", "")).lower().endswith(".zip")
        and any(token in str(asset.get("name", "")).lower() for token in ("aidlc", "rule", "workflow"))
    ]
    if zip_assets:
        return tag, str(zip_assets[0]["browser_download_url"])

    zipball_url = release.get("zipball_url")
    if zipball_url:
        return tag, str(zipball_url)

    return "main", REPO_ZIP_FALLBACK


def metadata_path(rules_dir: Path) -> Path:
    return rules_dir.parent / ".aidlc-update.json"


def read_current_tag(rules_dir: Path) -> str | None:
    path = metadata_path(rules_dir)
    if not path.exists():
        return None
    try:
        return str(json.loads(path.read_text()).get("tag") or "")
    except (json.JSONDecodeError, OSError):
        return None


def write_metadata(rules_dir: Path, tag: str, source_url: str) -> None:
    metadata_path(rules_dir).write_text(
        json.dumps(
            {
                "tag": tag,
                "source_url": source_url,
                "updated_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            },
            indent=2,
            sort_keys=True,
        )
        + "\n"
    )


def find_rules_root(extract_root: Path) -> Path:
    candidates = [path for path in extract_root.rglob(RULES_DIR_NAME) if path.is_dir()]
    candidates.sort(key=lambda path: len(path.parts))
    for candidate in candidates:
        if (candidate / "aws-aidlc-rules").is_dir():
            return candidate
    raise RuntimeError("downloaded archive does not contain aidlc-rules/aws-aidlc-rules")


def replace_rules(zip_path: Path, rules_dir: Path, tag: str, source_url: str) -> None:
    with tempfile.TemporaryDirectory(prefix="aidlc-extract-") as extract_tmp:
        extract_root = Path(extract_tmp)
        with zipfile.ZipFile(zip_path) as archive:
            archive.extractall(extract_root)

        extracted_rules = find_rules_root(extract_root)
        if not (extracted_rules / "aws-aidlc-rules" / "core-workflow.md").exists():
            raise RuntimeError("downloaded rules are missing aws-aidlc-rules/core-workflow.md")

        rules_dir.parent.mkdir(parents=True, exist_ok=True)
        with tempfile.TemporaryDirectory(prefix="aidlc-rules-next-", dir=str(rules_dir.parent)) as next_tmp:
            next_rules = Path(next_tmp) / RULES_DIR_NAME
            shutil.copytree(extracted_rules, next_rules)
            backup_rules = rules_dir.with_name(f"{rules_dir.name}.previous")
            if backup_rules.exists():
                shutil.rmtree(backup_rules)
            if rules_dir.exists():
                rules_dir.rename(backup_rules)
            next_rules.rename(rules_dir)
            if backup_rules.exists():
                shutil.rmtree(backup_rules)

        write_metadata(rules_dir, tag, source_url)


def update_once(rules_dir: Path, timeout: int, force: bool) -> str:
    release = request_json(API_URL, timeout)
    tag, download_url = choose_download(release)
    current_tag = read_current_tag(rules_dir)
    if current_tag == tag and not force and (rules_dir / "aws-aidlc-rules" / "core-workflow.md").exists():
        return f"already current ({tag})"

    with tempfile.TemporaryDirectory(prefix="aidlc-download-") as download_tmp:
        zip_path = Path(download_tmp) / "aidlc-workflows.zip"
        download_file(download_url, zip_path, timeout)
        replace_rules(zip_path, rules_dir, tag, download_url)
    return f"updated to {tag}"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--rules-dir",
        default=str(Path(__file__).resolve().parents[1] / "references" / RULES_DIR_NAME),
    )
    parser.add_argument("--retries", type=int, default=3)
    parser.add_argument("--timeout", type=int, default=DEFAULT_TIMEOUT_SECONDS)
    parser.add_argument("--force", action="store_true")
    parser.add_argument("--best-effort", action="store_true")
    args = parser.parse_args()

    rules_dir = Path(args.rules_dir).expanduser().resolve()
    attempts = max(1, args.retries)
    last_error: Exception | None = None

    for attempt in range(1, attempts + 1):
        try:
            log(update_once(rules_dir, args.timeout, args.force))
            return 0
        except (OSError, RuntimeError, zipfile.BadZipFile, urllib.error.URLError, urllib.error.HTTPError) as error:
            last_error = error
            log(f"attempt {attempt}/{attempts} failed: {error}")
            if attempt < attempts:
                time.sleep(min(2 * attempt, 5))

    log(f"using existing cache after update failure: {last_error}")
    return 0 if args.best_effort else 1


if __name__ == "__main__":
    raise SystemExit(main())
