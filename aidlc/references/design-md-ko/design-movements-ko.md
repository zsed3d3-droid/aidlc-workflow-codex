# 디자인 사조 라우팅 인덱스

이 compact index를 먼저 사용한다. 모든 movement detail 파일을 한꺼번에 읽지 말고, 가장 작은 관련 reference를 고른 뒤 `request_user_input` 옵션 두세 개를 구체적인 적합성 근거와 tradeoff와 함께 제안한다.

## Context-Budget Guardrail

- 먼저 프로젝트를 조사한다: audience, workflow, domain, assets, screenshots, CSS/theme, platform, accessibility needs.
- 기본적으로 detail file 하나만 읽는다.
- 교육용 게임이나 marketing landing page가 함께 있는 technical dashboard처럼 제품이 명확히 hybrid일 때만 두 번째 detail file을 읽는다.
- domain이 불명확하고 `request_user_input`을 사용할 수 있으면 detail file을 읽기 전에 domain을 질문한다.
- 최종 답변에 movement catalog 전체를 붙여넣거나 길게 요약하지 않는다.

## Routing Table

| Product context | Load this file | Use when |
|---|---|---|
| Web app, SaaS, dashboard, portfolio, ecommerce, brand site, technical tool, general frontend | `movements-product-web-ko.md` | UI가 game 또는 education 특화 경험보다 web/product frontend에 가깝다. |
| Game HUD, mobile game, tablet game, TCG/CCG, RPG/MMO, strategy game, arcade/casual game, diegetic/FUI interface | `movements-game-ui-ko.md` | UI가 game loop, game shell, fantasy/SF HUD, reward loop, in-game command surface의 일부다. |
| Learning app, edtech, puzzle, flashcard, course platform, sandbox education, scrollytelling lesson | `movements-learning-edtech-ko.md` | UI가 주로 가르치고, 훈련시키고, 테스트하고, 설명하거나 learner progress를 지원한다. |

## Shortlist Rules

- 읽은 detail file에서 두세 개 movement를 고른다.
- recommended option을 첫 번째에 둔다.
- 각 option은 audience fit, workflow fit, visual cues, accessibility/usability implication, tradeoff를 언급해야 한다.
- design-history exposition보다 enforceable UI rules를 우선한다.
- hybrid는 명확한 규칙을 만들 때만 사용한다. 예: dense하지만 guided lesson dashboard에는 `Constructivist Learning + Bento Grid`.

## Required DESIGN.md Output

`## Overview`에는 다음을 포함한다.

1. 선택한 movement 또는 hybrid.
2. 제품에 적합한 이유.
3. 그 movement가 만드는 세 가지 visual rule.
4. 금지하는 세 가지 anti-pattern.
