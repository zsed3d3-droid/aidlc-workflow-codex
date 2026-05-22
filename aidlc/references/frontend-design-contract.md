# Frontend Design Contract for AI-DLC

Use this reference when `$aidlc` work includes frontend UI. It maps AI-DLC lifecycle artifacts to a project `DESIGN.md` without modifying the upstream AI-DLC rule cache.

## Core Rule

`DESIGN.md` is the canonical frontend design contract. It owns visual direction, tokens, component variants, responsive behavior, interaction states, and accessibility constraints. AI-DLC documents own product intent, lifecycle traceability, functional behavior, and implementation planning.

Avoid copying token tables into AI-DLC artifacts. Reference `DESIGN.md` by path and cite the relevant sections or component keys.

## Detection

Activate this contract when the AI-DLC task mentions or discovers:

- Frontend, UI, UX, screens, routes, components, layout, visual design, interaction design, accessibility, responsive behavior, or screenshots.
- Web, mobile, desktop UI, Flutter, React, Next.js, Vue, Svelte, CSS, Tailwind, design system, component library, or app shell.
- Existing `DESIGN.md`, `design.md`, design tokens, theme files, mockups, Stitch output, Figma exports, or visual QA requests.

## Lifecycle Mapping

| AI-DLC phase | DESIGN.md action |
| --- | --- |
| Requirements Analysis | Ask only product/design questions that affect the contract: audience, brand tone, visual lineage, accessibility level, supported devices, and whether an existing design system must be preserved. |
| Application Design | If no `DESIGN.md` exists, use `create-design-md`. If one exists, use `use-design-md` and reference it from application design artifacts. |
| Functional Design | For frontend units, generate `frontend-components.md` from the functional behavior plus `DESIGN.md`. Do not invent raw colors, spacing, typography, radii, or shadows outside the contract. |
| Code Generation | Before UI edits, use `use-design-md`; map tokens to the local stack's theme system or reusable components. Add missing reusable states/components to `DESIGN.md` only when the task requires them. |
| Build and Test | Use `eval-design-md` for proposed/generated UI artifacts and `check-design-md` for implemented screens, rendered screenshots, or route/component audits. |

## Design Provider Ladder

Use Stitch as an optional ideation provider, not as the source of truth. Always keep `DESIGN.md` canonical.

Preferred order:

1. `DESIGN.md` plus Stitch SDK/MCP, only after the Stitch auth gate succeeds.
2. User-provided Stitch export artifacts, such as HTML, ZIP, screenshots, or copied screen code.
3. Local `DESIGN.md`-driven static prototype created in the target repo or a disposable prototype area.
4. Framework-native UI draft using the project's existing components and theme system.
5. Screen-by-screen interaction spec and wireframe document, without generated UI code.

Evaluate every provider output with `eval-design-md` before accepting it into implementation. Audit implemented UI with `check-design-md`.

## Design Movement References

When a frontend task needs a new `DESIGN.md` and the visual direction is not already explicit, use the bundled references under `design-md/`:

1. Read `design-md/design-movements.md` as the routing index.
2. Pick the smallest relevant movement detail file, usually one of:
   - `design-md/movements-product-web.md`
   - `design-md/movements-game-ui.md`
   - `design-md/movements-learning-edtech.md`
3. Load a second detail file only for a clearly hybrid product.
4. Use `design-md/design-md-template.md` when drafting the design contract.
5. Validate manually with `design-md/design-md-validation.md` when `npx @google/design.md lint DESIGN.md` is unavailable.

Do not paste whole movement catalogs into AI-DLC artifacts. Record only the selected movement or hybrid, the rationale, enforceable UI rules, and forbidden anti-patterns.

## Stitch Auth Gate

Before any Stitch SDK/MCP call, inspect the environment:

- `STITCH_ENABLED=false` means do not call Stitch, even if credentials exist.
- API key auth requires `STITCH_API_KEY`.
- OAuth auth requires both `STITCH_ACCESS_TOKEN` and `GOOGLE_CLOUD_PROJECT`.
- Optional values: `STITCH_HOST` and `STITCH_MAX_CALLS_PER_RUN`.

If Stitch credentials are missing and `request_user_input` is available, ask which path to use:

- Set `STITCH_API_KEY` in the local environment and retry preflight.
- Use OAuth/gcloud credentials and retry preflight.
- Skip Stitch for this task and use the fallback ladder.

Do not ask the user to paste raw API keys, access tokens, or service account material into chat, question files, AI-DLC docs, `DESIGN.md`, or completion reports. Ask for the authentication method only, then instruct the user to set credentials in their local environment or secret store.

If the user gives no answer, gives an empty answer, or chooses to skip Stitch, proceed with the fallback ladder.

## Stitch Preflight

Run a low-cost preflight before generating screens. Acceptable preflights include listing tools through the SDK/MCP client or another read-only connectivity check. Generate screens only after preflight succeeds.

Fall back without retry loops when:

- Authentication fails.
- The Google Cloud project has not enabled the Stitch MCP service.
- Quota, billing, beta access, regional availability, or policy prevents use.
- Network access is blocked.
- SDK/MCP schema or endpoint behavior has changed.
- `STITCH_MAX_CALLS_PER_RUN` is missing and the caller requires a call budget, or the budget is exhausted.

Record the failure category and selected fallback path in the relevant AI-DLC artifact when traceability is needed.

## Artifact Rules

- Place `DESIGN.md` at the frontend root that owns UI code. If the repository has one UI app, this is usually the app root; otherwise use the specific package/app root.
- If AI-DLC traceability is needed, create or update `aidlc-docs/inception/application-design/frontend-design-contract.md` with the `DESIGN.md` path, selected style lineage, key constraints, and open design risks.
- In `aidlc-docs/construction/{unit-name}/functional-design/frontend-components.md`, reference `DESIGN.md` component keys and state rules. Keep behavior, props, data flow, and validation in the functional design doc.
- Do not create parallel design-token artifacts unless the target framework requires generated theme files. Generated theme files should be derived from `DESIGN.md` or explicitly mapped back to it.
- If Stitch or another external provider returns HTML, screenshots, or screen metadata, store only non-secret metadata in AI-DLC artifacts: provider, prompt summary or hash, project/screen IDs when safe, generated timestamp, local artifact paths, evaluation verdict, and fallback status.

## Question Bridge Additions

When the Codex question bridge is available and the answers are not discoverable from repository artifacts, include concise questions for:

- Whether the frontend must create a new `DESIGN.md` or follow an existing one.
- The preferred design movement or style lineage, when product docs do not imply one.
- Primary target form factors and accessibility constraints.
- Whether visual evaluation/audit gates should block implementation completion.
- If Stitch is requested and credentials are missing, which auth path to use: local API key env, OAuth/gcloud env, or fallback without Stitch.

If the user does not answer and the work is not high-risk, choose a defensible default from product context and record it in the generated artifact.

For Stitch auth questions, the default is stricter: no answer means fallback without Stitch.

## Completion Evidence

For frontend AI-DLC completion, report:

- The `DESIGN.md` path used or created.
- Which DESIGN.md skill was applied at each relevant phase.
- Any `DESIGN.md` additions made by `use-design-md`.
- Whether Stitch was used, skipped, failed preflight, or replaced by fallback. Do not report secret values.
- Evaluation or audit results from `eval-design-md` or `check-design-md`, including unresolved design risks.
