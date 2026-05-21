# Codex AI-DLC Skill

이 저장소는 Codex에서 AWS AI-DLC workflow guidance를 사용할 수 있도록 만든 Codex skill 패키지입니다. Codex 세션이 시작될 때 bundled AI-DLC rules를 갱신하는 선택적 startup hook도 포함합니다.

영어 README는 [README.md](README.md)를 참고하세요.

## AI-DLC 파생 Codex Skill

이 저장소는 `https://github.com/awslabs/aidlc-workflows.git`의 AWS AI-DLC workflow 규칙을 Codex에서 사용할 수 있도록 파생시킨 Codex Skill을 제공합니다.

AI-DLC가 요구사항, 설계, 구현 계획을 구체화하기 위해 질의문을 생성하면, 이 skill은 Codex Plan Mode에서 사용 가능한 `request_user_input` UI를 우선 사용합니다. 사용자는 채팅에 자유 서술로 답을 입력하는 대신, 질의문별 선택지를 고르거나 `Other` 응답을 입력할 수 있습니다. 선택된 답변은 AI-DLC의 `[Answer]:` 값처럼 취급되어 요구사항 문서, 계획, 설계 문서, 검증 기준에 반영됩니다.

사용법은 Codex Plan Mode에서 다음처럼 입력합니다.

```text
$aidlc
```

## 포함 파일

- `aidlc/SKILL.md` - Codex skill 진입점
- `aidlc/scripts/update_aidlc_rules.py` - bundled AI-DLC rules updater
- `aidlc/references/aidlc-rules/` - 로컬 AI-DLC rule cache
- `aidlc/references/frontend-design-contract.md` - AI-DLC frontend work와 프로젝트 `DESIGN.md`를 연결하는 Codex 전용 mapping
- `install-aidlc-skill.sh` - skill을 Codex에 복사하고 `~/.codex/hooks.json`을 patch하는 installer

## 설치

저장소 root에서 실행합니다.

```bash
./install-aidlc-skill.sh
```

installer는 다음 작업을 수행합니다.

1. `aidlc/`를 `~/.codex/skills/aidlc/`로 복사하고, 기존 `aidlc` skill이 있으면 먼저 백업합니다.
2. 기존 `~/.codex/hooks.json`이 있으면 백업합니다.
3. AI-DLC updater를 실행하는 `SessionStart` startup hook을 추가합니다.
4. 설치 후 best-effort update를 한 번 실행합니다.

## 수동 Skill 설치

script를 사용하지 않으려면 다음 명령을 실행합니다.

```bash
mkdir -p "$HOME/.codex/skills"
rm -rf "$HOME/.codex/skills/aidlc"
cp -R "./aidlc" "$HOME/.codex/skills/aidlc"
```

설치 후 Codex에서 다음처럼 명시적으로 호출할 수 있습니다.

```text
$aidlc
```

또는 작업에서 `use AI-DLC` / `AI-DLC`라고 말하면 사용할 수 있습니다.

## 수동 Hook 설치

`~/.codex/hooks.json`에 아래 hook을 추가합니다.

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

이미 `hooks.json`에 `SessionStart` list가 있으면 파일을 교체하지 말고 startup hook entry를 append하세요.

## Rules 수동 업데이트

```bash
python3 "$HOME/.codex/skills/aidlc/scripts/update_aidlc_rules.py" --retries 3 --best-effort
```

network, GitHub, archive extraction, validation이 실패하면 updater는 기존 local cache를 보존합니다.

## DESIGN.md 사용

Frontend AI-DLC 작업에서는 target project의 `DESIGN.md`를 canonical design contract로 유지합니다. AI-DLC skill은 `aidlc/references/frontend-design-contract.md`를 참고하여 Codex에 다음 규칙을 적용합니다.

- application design 중 `DESIGN.md`가 없으면 생성합니다.
- frontend design 및 implementation 중 기존 `DESIGN.md`를 사용합니다.
- visual token을 AI-DLC 문서에 중복 복사하지 않습니다.
- 제안된 UI를 `DESIGN.md` 기준으로 평가합니다.
- 구현된 screen을 `DESIGN.md` 기준으로 audit합니다.

Project-specific `DESIGN.md` 파일은 이 script가 global로 설치하지 않습니다. UI 작업을 지배해야 하는 target project root 또는 frontend app root에 직접 두세요.

## 검증

```bash
test -f "$HOME/.codex/skills/aidlc/SKILL.md"
python3 "$HOME/.codex/skills/aidlc/scripts/update_aidlc_rules.py" --retries 1 --best-effort
```

`already current (...)` 또는 `updated to ...` 같은 updater message가 표시되어야 합니다.

## 라이선스

이 저장소는 MIT No Attribution license (MIT-0)로 공개합니다. Bundled AI-DLC workflow rules의 upstream인 `awslabs/aidlc-workflows`도 MIT-0로 공개되어 있어, 이 파생 Codex skill도 같은 MIT-0 라이선스로 배포할 수 있습니다.

자세한 내용은 [LICENSE](LICENSE)를 참고하세요.
