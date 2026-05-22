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
- `aidlc/references/design-md/` - bundled DESIGN.md template, validation checklist, design movement reference catalog
- `aidlc/references/design-md-ko/` - bundled DESIGN.md reference의 한국어 번역본. 파일명은 `-ko` suffix를 사용합니다.
- `skills/create-design-md/` - project `DESIGN.md` 생성을 위한 bundled skill
- `skills/use-design-md/` - 기존 `DESIGN.md` 적용 및 확장을 위한 bundled skill
- `skills/eval-design-md/` - 제안된 UI를 `DESIGN.md` 기준으로 평가하는 bundled skill
- `skills/check-design-md/` - 구현된 UI를 `DESIGN.md` 기준으로 audit하는 bundled skill
- `install-aidlc-skill.sh` - AI-DLC와 DESIGN.md skills를 Codex에 복사하고 `~/.codex/hooks.json`을 patch하는 installer

## 설치

저장소 root에서 실행합니다.

```bash
./install-aidlc-skill.sh
```

installer는 다음 작업을 수행합니다.

1. `aidlc/`를 `~/.codex/skills/aidlc/`로 복사하고, 기존 `aidlc` skill이 있으면 먼저 백업합니다.
2. bundled DESIGN.md skills를 `~/.codex/skills/create-design-md/`, `use-design-md/`, `eval-design-md/`, `check-design-md/`에 복사하고, 기존 skill directory가 있으면 먼저 백업합니다.
3. 기존 `~/.codex/hooks.json`이 있으면 백업합니다.
4. AI-DLC updater를 실행하는 `SessionStart` startup hook을 추가합니다.
5. 설치 후 best-effort update를 한 번 실행합니다.

## 수동 Skill 설치

script를 사용하지 않으려면 다음 명령을 실행합니다.

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

설치 후 Codex에서 `$aidlc`와 bundled DESIGN.md skills를 명시적으로 호출할 수 있습니다.

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
- design direction이 명시되지 않은 경우 `aidlc/references/design-md/`에서 design movement 또는 style lineage를 선택합니다.
- 한국어 DESIGN.md planning reference가 필요하면 `aidlc/references/design-md-ko/`를 사용합니다.

Project-specific `DESIGN.md` 파일은 이 script가 global로 설치하지 않습니다. UI 작업을 지배해야 하는 target project root 또는 frontend app root에 직접 두세요.

## Stitch MCP/API 연동

Frontend AI-DLC 작업에서는 이 skill이 Google Stitch를 Stitch MCP 또는 Stitch SDK/API를 통해 선택적으로 사용할 수 있습니다. Stitch는 screen ideation, variant 생성, Stitch screen artifact 조회에 사용할 수 있습니다. 단, Stitch output은 ideation provider일 뿐이며 target project의 `DESIGN.md`가 계속 canonical design contract입니다.

Stitch는 필수 dependency가 아닙니다. credential이 없거나, authentication이 실패하거나, quota/billing/access 문제로 호출할 수 없거나, Stitch MCP/API surface가 바뀐 경우에는 `aidlc/references/frontend-design-contract.md`에 정의된 fallback ladder로 계속 진행해야 합니다.

### Stitch API Key 가져오기

Google account에 Stitch access가 있다면 다음 순서로 가져옵니다.

1. `https://stitch.withgoogle.com/settings`를 엽니다.
2. Stitch project를 소유할 Google account로 sign in합니다.
3. API Keys section을 엽니다.
4. API key를 생성하거나 복사합니다.
5. key는 local environment, MCP client config, secret store에만 저장합니다.

실제 Stitch key를 이 repository, AI-DLC artifact, `DESIGN.md`, chat transcript, completion report에 commit하거나 붙여 넣지 마세요.

### Codex 또는 MCP Client 설정

Codex에서는 Stitch를 MCP server로 Codex config file에 등록하는 방식이 가장 간편합니다. 일반적으로 `~/.codex/config.toml`에 아래처럼 설정합니다. Stitch MCP endpoint를 사용하고 key를 HTTP header로 전달합니다.

```toml
[mcp_servers.stitch]
url = "https://stitch.googleapis.com/mcp"

[mcp_servers.stitch.http_headers]
"X-Goog-Api-Key" = "<your-stitch-api-key>"
```

Environment 기반 설정에서는 Codex 또는 MCP client를 시작하기 전에 key를 export합니다.

```bash
export STITCH_API_KEY="<your-stitch-api-key>"
```

AI-DLC Stitch auth gate는 다음 값도 인식합니다.

- `STITCH_ENABLED=false` - credential이 있어도 Stitch를 비활성화합니다.
- `STITCH_API_KEY` - API key authentication.
- `STITCH_ACCESS_TOKEN` plus `GOOGLE_CLOUD_PROJECT` - OAuth-style authentication.
- `STITCH_HOST` - default MCP endpoint override.
- `STITCH_MAX_CALLS_PER_RUN` - 한 run에서 Stitch 호출 횟수 제한.

일부 MCP client 또는 Stitch SDK flow는 API key 대신 OAuth/gcloud credential을 선호할 수 있습니다. 이 경우 Google Cloud에 local authentication을 수행하고, Stitch access가 있는 project를 선택한 뒤, raw secret을 repository에 저장하지 말고 access token/project ID 방식으로 client를 설정하세요.

## 검증

```bash
test -f "$HOME/.codex/skills/aidlc/SKILL.md"
python3 "$HOME/.codex/skills/aidlc/scripts/update_aidlc_rules.py" --retries 1 --best-effort
```

`already current (...)` 또는 `updated to ...` 같은 updater message가 표시되어야 합니다.

## 라이선스

이 저장소는 MIT No Attribution license (MIT-0)로 공개합니다. Bundled AI-DLC workflow rules의 upstream인 `awslabs/aidlc-workflows`도 MIT-0로 공개되어 있어, 이 파생 Codex skill도 같은 MIT-0 라이선스로 배포할 수 있습니다.

자세한 내용은 [LICENSE](LICENSE)를 참고하세요.
