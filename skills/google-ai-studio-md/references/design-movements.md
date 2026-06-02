# Design Movement Routing Index

Use this compact index first. Do not load every movement detail file. Pick the smallest relevant reference, then propose two or three `request_user_input` options with concrete fit rationale and tradeoffs.

## Context-Budget Guardrail

- Inspect the project first: audience, workflow, domain, assets, screenshots, CSS/theme, platform, and accessibility needs.
- Load one detail file by default.
- Load a second detail file only when the product is clearly hybrid, such as an educational game or a technical dashboard with a marketing landing page.
- If the domain is unclear and `request_user_input` is available, ask for the domain before loading detail files.
- Never paste or summarize whole movement catalogs into the final answer.

## Routing Table

| Product context | Load this file | Use when |
|---|---|---|
| Web app, SaaS, dashboard, portfolio, ecommerce, brand site, technical tool, general frontend | `movements-product-web.md` | The UI is primarily a web/product frontend rather than a game or education-specific experience. |
| Game HUD, mobile game, tablet game, TCG/CCG, RPG/MMO, strategy game, arcade/casual game, diegetic/FUI interface | `movements-game-ui.md` | The UI is part of a game loop, game shell, fantasy/SF HUD, reward loop, or in-game command surface. |
| Learning app, edtech, puzzle, flashcard, course platform, sandbox education, scrollytelling lesson | `movements-learning-edtech.md` | The UI primarily teaches, drills, tests, explains, or supports learner progress. |

## Shortlist Rules

- Choose two or three movements from the loaded detail file.
- Put the recommended option first.
- Each option must mention: audience fit, workflow fit, visual cues, accessibility/usability implication, and tradeoff.
- Prefer enforceable UI rules over design-history exposition.
- Use hybrids only when they produce clear rules, such as `Constructivist Learning + Bento Grid` for a dense but guided lesson dashboard.

## Required DESIGN.md Output

In `## Overview`, include:

1. Chosen movement or hybrid.
2. Why it fits the product.
3. Three visual rules it creates.
4. Three anti-patterns it forbids.
