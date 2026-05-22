---
name: create-design-md
description: Use when creating a frontend DESIGN.md, design.md, design-md, create_design_md, or design-system markdown for AI-generated UI, especially when a project needs a clear design movement, visual identity, tokens, components, responsive rules, or agent-readable frontend design guidance.
---

# Create DESIGN.md

## Overview

Create a project-root `DESIGN.md` that acts like `AGENTS.md` for frontend design: exact tokens in YAML front matter plus human design rationale in Markdown. The file must name a concrete design movement or design philosophy and translate it into enforceable UI constraints.

## Workflow

1. Locate the frontend root. Prefer the app/package root that owns UI code; otherwise use the repository root.
2. Inspect existing UI, brand assets, screenshots, CSS/theme files, component libraries, and product docs before asking questions.
3. Resolve the design movement using the Plan Mode Movement Selection rules below when direction is not explicit.
4. Generate `DESIGN.md` from [design-md-template.md](references/design-md-template.md).
5. Fill tokens first, then prose. Tokens are normative; prose explains how and why to apply them.
6. Define component entries for the UI that will actually be built: app shell, navigation, buttons, inputs, cards, panels, tables/lists, lesson/content surfaces, modals, toasts, and domain-specific controls.
7. Add responsive behavior, accessibility constraints, and an Agent Prompt Guide.
8. Validate with `npx @google/design.md lint DESIGN.md` when npm/network access is available. If not, manually check the lint topics in [design-md-validation.md](references/design-md-validation.md).

## Plan Mode Movement Selection

If the design direction is already explicit in the user prompt, brand docs, existing UI, screenshots, or product artifacts, use that direction and record the rationale in `DESIGN.md`.

When this skill is installed from the AI-DLC-CODEX package, Korean translations of the movement references are available in the sibling AI-DLC skill at `../aidlc/references/design-md-ko/`. Use those translated files for Korean-language planning while keeping the generated `DESIGN.md` token schema compatible with the template in `references/design-md-template.md`.

If the direction is unclear and `request_user_input` is available, ask the user to choose a design movement before generating `DESIGN.md`:

1. Read [design-movements.md](references/design-movements.md) as the compact routing index.
2. Pick the most relevant movement detail file from the routing table and read only that file. Load a second detail file only for a clear hybrid case.
3. Do not load all movement detail files just to choose options.
4. Propose two or three fitting movement options.
5. Put the recommended option first.
6. Make every option description concrete enough to justify the recommendation.
7. Include the main tradeoff for each option.

Each option description must cite specific evidence from the project context:

- target audience, such as children, operators, developers, learners, or executives
- workflow, such as dashboard scanning, guided learning, content reading, game interaction, or monitoring
- product domain, such as education, SaaS operations, creative portfolio, technical tooling, or commerce
- existing visual cues from logos, screenshots, CSS, typography, image assets, or brand colors
- accessibility and usability needs, such as contrast, tap targets, density, or restrained motion
- implementation tradeoff, such as density, playfulness, production seriousness, readability, or complexity

Avoid generic descriptions like "modern and clean." Use descriptions like:

- Productivist dashboard: fits repeated scanning, status comparison, dense tables, and calm error states; tradeoff is less expressive brand personality.
- Constructivist learning: fits step-by-step teaching, progress feedback, geometric focus areas, and high-contrast learning states; tradeoff is less corporate polish.
- Swiss/International: fits neutral credibility, strict alignment, text-heavy clarity, and low decorative overhead; tradeoff is less playful emotional tone.

If `request_user_input` is unavailable, fall back according to the active collaboration mode: ask a concise clarification question when needed, or use [design-movements.md](references/design-movements.md) to pick the smallest relevant detail file, choose a defensible movement from that file, and record it as an assumption.

## AI-DLC Use

When invoked from `aidlc`, create `DESIGN.md` during Inception/Application Design for frontend work that has no existing design contract. Use AI-DLC product artifacts, requirements, user stories, and application design notes as source material. If AI-DLC traceability is required, add or update a short `aidlc-docs/inception/application-design/frontend-design-contract.md` note that points to `DESIGN.md` and records the chosen design lineage, key constraints, and open visual risks; do not duplicate token tables there.

If AI-DLC requests Stitch for initial screen ideation, follow the Stitch auth gate in `aidlc/references/frontend-design-contract.md`. Missing credentials should trigger the Codex question UI when available; empty answers, skipped auth, or failed preflight should fall back to local `DESIGN.md` creation without remote Stitch calls.

## Requirements

- Use the canonical section order: Overview, Colors, Typography, Layout, Elevation & Depth, Shapes, Components, Do's and Don'ts.
- Extended sections may follow canonical sections: Responsive Behavior, Agent Prompt Guide, Iteration Guide, Known Gaps.
- Include `version`, `name`, `description`, `colors`, `typography`, `rounded`, `spacing`, and `components` in YAML front matter.
- Use token references like `{colors.primary}` inside component tokens.
- Express variants as separate component keys, such as `button-primary`, `button-primary-hover`, `text-input-error`, `lesson-card-complete`.
- Keep brand/style prose concrete. Avoid vague phrases like "modern and clean" unless they are tied to token and component rules.
- For frontend apps, prefer practical component contracts over brand-analysis essays.

## Design Movement Rule

Every new `DESIGN.md` must include a `## Overview` paragraph that states:

- The chosen design movement or style lineage.
- Why it fits the product audience and workflow.
- Which visual decisions it forbids.

Example: "Playful constructivist learning UI" is useful only if it produces rules such as high-contrast teaching panels, geometric board-area blocks, limited primary colors, restrained motion, and large tap targets.

## Validation Note

`npx @google/design.md lint DESIGN.md` is the official Google DESIGN.md CLI validator, not a Codex skill. It checks structural correctness, broken token references, contrast warnings, missing primary/typography tokens, orphaned tokens, optional missing sections, and section order. Treat lint errors as blockers; treat warnings as review items.
