#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CODEX_HOME="${CODEX_HOME:-$HOME/.codex}"
SKILLS_DIR="$CODEX_HOME/skills"
TARGET_SKILL_DIR="$SKILLS_DIR/aidlc"
HOOKS_FILE="$CODEX_HOME/hooks.json"
UPDATER_COMMAND="python3 \"$TARGET_SKILL_DIR/scripts/update_aidlc_rules.py\" --retries 3 --best-effort"
BUNDLED_SKILLS=(
  "aidlc:$SCRIPT_DIR/aidlc"
  "create-design-md:$SCRIPT_DIR/skills/create-design-md"
  "use-design-md:$SCRIPT_DIR/skills/use-design-md"
  "eval-design-md:$SCRIPT_DIR/skills/eval-design-md"
  "check-design-md:$SCRIPT_DIR/skills/check-design-md"
)

for skill_spec in "${BUNDLED_SKILLS[@]}"; do
  skill_name="${skill_spec%%:*}"
  source_dir="${skill_spec#*:}"
  if [[ ! -f "$source_dir/SKILL.md" ]]; then
    echo "Missing skill source for $skill_name: $source_dir/SKILL.md" >&2
    exit 1
  fi
done

mkdir -p "$SKILLS_DIR"
for skill_spec in "${BUNDLED_SKILLS[@]}"; do
  skill_name="${skill_spec%%:*}"
  source_dir="${skill_spec#*:}"
  target_dir="$SKILLS_DIR/$skill_name"
  if [[ -e "$target_dir" ]]; then
    mv "$target_dir" "$target_dir.bak-$(date +%Y%m%d%H%M%S)-$$"
  fi
  cp -R "$source_dir" "$target_dir"
done

python3 - "$HOOKS_FILE" "$UPDATER_COMMAND" <<'PY'
import json
import sys
import time
from pathlib import Path

hooks_file = Path(sys.argv[1]).expanduser()
updater_command = sys.argv[2]
hook_entry = {
    "matcher": "startup",
    "hooks": [
        {
            "type": "command",
            "command": updater_command,
            "statusMessage": "Updating AI-DLC rules",
            "timeout": 90,
        }
    ],
}

hooks_file.parent.mkdir(parents=True, exist_ok=True)
if hooks_file.exists():
    backup = hooks_file.with_suffix(hooks_file.suffix + f".bak-{time.strftime('%Y%m%d%H%M%S')}")
    backup.write_text(hooks_file.read_text(), encoding="utf-8")
    try:
        data = json.loads(hooks_file.read_text(encoding="utf-8"))
    except json.JSONDecodeError as error:
        raise SystemExit(f"Invalid JSON in {hooks_file}; backup written to {backup}: {error}")
else:
    data = {}

root_hooks = data.setdefault("hooks", {})
session_start = root_hooks.setdefault("SessionStart", [])
if not isinstance(session_start, list):
    raise SystemExit(f"{hooks_file}: hooks.SessionStart must be a list")

def is_aidlc_update_hook(entry):
    if not isinstance(entry, dict):
        return False
    for hook in entry.get("hooks", []):
        if isinstance(hook, dict) and "aidlc/scripts/update_aidlc_rules.py" in str(hook.get("command", "")):
            return True
    return False

if not any(is_aidlc_update_hook(entry) for entry in session_start):
    session_start.append(hook_entry)

hooks_file.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
PY

python3 "$TARGET_SKILL_DIR/scripts/update_aidlc_rules.py" --retries 3 --best-effort

echo "Installed AI-DLC skill to: $TARGET_SKILL_DIR"
echo "Installed DESIGN.md skills to:"
for skill_spec in "${BUNDLED_SKILLS[@]}"; do
  skill_name="${skill_spec%%:*}"
  if [[ "$skill_name" != "aidlc" ]]; then
    echo "  $SKILLS_DIR/$skill_name"
  fi
done
echo "Updated Codex hooks file: $HOOKS_FILE"
