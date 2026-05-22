# Codex AI-DLC Skill

This repository packages a Codex skill for using AWS AI-DLC workflow guidance inside Codex. It also includes an optional Codex startup hook that refreshes the bundled AI-DLC rules when a Codex session starts.

Korean documentation is available in [README_KO.md](README_KO.md).

## AI-DLC-Derived Codex Skill

This repository provides a Codex skill derived from the AWS AI-DLC workflow rules published at `https://github.com/awslabs/aidlc-workflows.git`.

When AI-DLC asks questions to clarify requirements, design, or implementation plans, this skill uses Codex Plan Mode's `request_user_input` UI when it is available. Instead of answering open-ended questions directly in chat, users can choose from structured answer options or provide an `Other` response. The selected answer is treated as the AI-DLC `[Answer]:` value and is fed into requirements, plans, design documents, and verification criteria.

Use it in Codex Plan Mode by typing:

```text
$aidlc
```

## Included Files

- `aidlc/SKILL.md` - Codex skill entry point.
- `aidlc/scripts/update_aidlc_rules.py` - updater for the bundled AI-DLC rules.
- `aidlc/references/aidlc-rules/` - local AI-DLC rule cache.
- `aidlc/references/frontend-design-contract.md` - Codex-specific mapping between AI-DLC frontend work and a project `DESIGN.md`.
- `aidlc/references/design-md/` - bundled DESIGN.md template, validation checklist, and design movement reference catalog.
- `aidlc/references/design-md-ko/` - Korean translations of the bundled DESIGN.md references, using `-ko` filename suffixes.
- `skills/create-design-md/` - bundled skill for creating project `DESIGN.md` files.
- `skills/use-design-md/` - bundled skill for applying and extending existing `DESIGN.md` files.
- `skills/eval-design-md/` - bundled skill for evaluating proposed UI against `DESIGN.md`.
- `skills/check-design-md/` - bundled skill for auditing implemented UI against `DESIGN.md`.
- `install-aidlc-skill.sh` - installer that copies AI-DLC and DESIGN.md skills into Codex and patches `~/.codex/hooks.json`.

## Install

From this repository root:

```bash
./install-aidlc-skill.sh
```

The installer will:

1. Copy `aidlc/` to `~/.codex/skills/aidlc/`, backing up an existing `aidlc` skill first.
2. Copy bundled DESIGN.md skills to `~/.codex/skills/create-design-md/`, `use-design-md/`, `eval-design-md/`, and `check-design-md/`, backing up existing skill directories first.
3. Back up `~/.codex/hooks.json` if it already exists.
4. Add a `SessionStart` startup hook that runs the AI-DLC updater.
5. Run one best-effort update after installation.

## Manual Skill Install

If you do not want to use the script:

```bash
mkdir -p "$HOME/.codex/skills"
for skill in aidlc create-design-md use-design-md eval-design-md check-design-md; do
  rm -rf "$HOME/.codex/skills/$skill"
done
cp -R "./aidlc" "$HOME/.codex/skills/aidlc"
cp -R "./skills/create-design-md" "$HOME/.codex/skills/create-design-md"
cp -R "./skills/use-design-md" "$HOME/.codex/skills/use-design-md"
cp -R "./skills/eval-design-md" "$HOME/.codex/skills/eval-design-md"
cp -R "./skills/check-design-md" "$HOME/.codex/skills/check-design-md"
```

After that, Codex can use `$aidlc` and the bundled DESIGN.md skills when you explicitly invoke:

```text
$aidlc
```

or when you say `use AI-DLC` / `AI-DLC` in the task.

## Manual Hook Install

Add this hook to `~/.codex/hooks.json`.

```json
{
  "hooks": {
    "SessionStart": [
      {
        "matcher": "startup",
        "hooks": [
          {
            "type": "command",
            "command": "python3 \"$HOME/.codex/skills/aidlc/scripts/update_aidlc_rules.py\" --retries 3 --best-effort",
            "statusMessage": "Updating AI-DLC rules",
            "timeout": 90
          }
        ]
      }
    ]
  }
}
```

If `hooks.json` already has a `SessionStart` list, append the startup hook entry instead of replacing the file.

## Update Rules Manually

```bash
python3 "$HOME/.codex/skills/aidlc/scripts/update_aidlc_rules.py" --retries 3 --best-effort
```

The updater preserves the existing local cache if the network, GitHub, archive extraction, or validation fails.

## DESIGN.md Usage

For frontend AI-DLC work, keep the target project's `DESIGN.md` as the canonical design contract. The AI-DLC skill references `aidlc/references/frontend-design-contract.md`, which tells Codex to:

- create `DESIGN.md` during application design when one is missing;
- use existing `DESIGN.md` during frontend design and implementation;
- avoid duplicating visual tokens into AI-DLC documents;
- evaluate proposed UI against `DESIGN.md`;
- audit implemented screens against `DESIGN.md`.
- resolve design movement or style lineage from `aidlc/references/design-md/` when the direction is not already explicit.
- use `aidlc/references/design-md-ko/` when Korean-language DESIGN.md planning references are needed.

Project-specific `DESIGN.md` files are not installed globally by this script. Copy them into each target project root or frontend app root where they should govern UI work.

## Stitch MCP/API Integration

For frontend AI-DLC work, this skill can optionally use Google Stitch through Stitch MCP or the Stitch SDK/API to ideate screens, generate variants, or retrieve Stitch screen artifacts. Stitch output is treated as an ideation provider only; the target project's `DESIGN.md` remains the canonical design contract.

Stitch is not required. If credentials are missing, authentication fails, quota or billing blocks the call, or the Stitch MCP/API surface changes, AI-DLC should continue with the fallback ladder described in `aidlc/references/frontend-design-contract.md`.

### Get a Stitch API Key

If your Google account has Stitch access:

1. Open `https://stitch.withgoogle.com/settings`.
2. Sign in with the Google account that should own the Stitch projects.
3. Open the API Keys section.
4. Create or copy an API key.
5. Store the key only in your local environment, MCP client config, or secret store.

Do not commit a real Stitch key to this repository, AI-DLC artifacts, `DESIGN.md`, chat transcripts, or completion reports.

### Configure Stitch for Codex or an MCP Client

For direct HTTP MCP configuration, use the Stitch MCP endpoint and pass the key as an HTTP header:

```toml
[mcp_servers.stitch]
url = "https://stitch.googleapis.com/mcp"

[mcp_servers.stitch.http_headers]
"X-Goog-Api-Key" = "<your-stitch-api-key>"
```

For environment-based setup, export the key before starting Codex or your MCP client:

```bash
export STITCH_API_KEY="<your-stitch-api-key>"
```

The AI-DLC Stitch auth gate also recognizes:

- `STITCH_ENABLED=false` - disable Stitch even if credentials exist.
- `STITCH_API_KEY` - API key authentication.
- `STITCH_ACCESS_TOKEN` plus `GOOGLE_CLOUD_PROJECT` - OAuth-style authentication.
- `STITCH_HOST` - override the default MCP endpoint.
- `STITCH_MAX_CALLS_PER_RUN` - cap Stitch calls for a run.

Some MCP clients or Stitch SDK flows may prefer OAuth/gcloud credentials instead of an API key. In that case, authenticate locally with Google Cloud, select the project that has Stitch access, and configure the client with the resulting access token/project ID rather than storing raw secrets in the repo.

## Verify

```bash
test -f "$HOME/.codex/skills/aidlc/SKILL.md"
python3 "$HOME/.codex/skills/aidlc/scripts/update_aidlc_rules.py" --retries 1 --best-effort
```

You should see an updater message such as `already current (...)` or `updated to ...`.

## License

This repository is licensed under the MIT No Attribution license (MIT-0). The bundled AI-DLC workflow rules are derived from `awslabs/aidlc-workflows`, which is also published under MIT-0.

See [LICENSE](LICENSE).
