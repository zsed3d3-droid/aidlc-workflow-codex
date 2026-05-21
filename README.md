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
- `install-aidlc-skill.sh` - installer that copies the skill into Codex and patches `~/.codex/hooks.json`.

## Install

From this repository root:

```bash
./install-aidlc-skill.sh
```

The installer will:

1. Copy `aidlc/` to `~/.codex/skills/aidlc/`, backing up an existing `aidlc` skill first.
2. Back up `~/.codex/hooks.json` if it already exists.
3. Add a `SessionStart` startup hook that runs the AI-DLC updater.
4. Run one best-effort update after installation.

## Manual Skill Install

If you do not want to use the script:

```bash
mkdir -p "$HOME/.codex/skills"
rm -rf "$HOME/.codex/skills/aidlc"
cp -R "./aidlc" "$HOME/.codex/skills/aidlc"
```

After that, Codex can use the skill when you explicitly invoke:

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

Project-specific `DESIGN.md` files are not installed globally by this script. Copy them into each target project root or frontend app root where they should govern UI work.

## Verify

```bash
test -f "$HOME/.codex/skills/aidlc/SKILL.md"
python3 "$HOME/.codex/skills/aidlc/scripts/update_aidlc_rules.py" --retries 1 --best-effort
```

You should see an updater message such as `already current (...)` or `updated to ...`.

## License

This repository is licensed under the MIT No Attribution license (MIT-0). The bundled AI-DLC workflow rules are derived from `awslabs/aidlc-workflows`, which is also published under MIT-0.

See [LICENSE](LICENSE).
