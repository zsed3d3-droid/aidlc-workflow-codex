# DESIGN.md 검증

가능하면 `npx @google/design.md lint DESIGN.md`를 사용한다. 이 명령은 built UI가 아니라 DESIGN.md 파일 자체를 검증한다.

## Official Lint Topics

- `colors.primary`가 없는데 `{colors.primary}`를 참조하는 등 깨진 token reference.
- primary color 누락.
- component text/background contrast가 WCAG AA 아래인 경우.
- component에서 참조하지 않는 orphaned color token.
- token summary.
- spacing 또는 rounded 같은 optional section 누락.
- typography 누락.
- section order drift.

## Manual Fallback

CLI를 실행할 수 없으면 다음을 확인한다.

1. YAML fence와 indentation 오류를 수동으로 확인한다.
2. `name`, `colors.primary`, typography, spacing, rounded, components가 있는지 확인한다.
3. 모든 `{path.to.token}` reference가 실제 token으로 resolve되는지 확인한다.
4. component foreground/background contrast를 확인한다.
5. canonical section order를 확인한다.
6. 주요 frontend component마다 token entry 또는 prose rule이 있는지 확인한다.
7. design movement rule이 구체적이고 enforceable한지 확인한다.
