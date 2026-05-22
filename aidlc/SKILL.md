---
name: aidlc
description: Apply AWS AI-DLC development lifecycle guidance from awslabs/aidlc-workflows when explicitly invoked as $aidlc, "use AI-DLC", or "AI-DLC". Use for structured AI-assisted software delivery with requirements, design, implementation, review, and verification gates. Do not use implicitly for ordinary coding requests.
---

# AI-DLC

Use the AWS AI-DLC workflow only when the user explicitly invokes `$aidlc`, says "use AI-DLC", or otherwise names AI-DLC directly.

## Source Rules

Use the bundled rules under `references/aidlc-rules/` as the local source of truth. They are synchronized from `https://github.com/awslabs/aidlc-workflows` by `scripts/update_aidlc_rules.py`.

Before starting substantive AI-DLC work:

1. Read `references/aidlc-rules/aws-aidlc-rules/core-workflow.md` if present.
2. Read only the relevant files from `references/aidlc-rules/aws-aidlc-rule-details/` for the current task phase.
3. If bundled rules are missing or stale, run `scripts/update_aidlc_rules.py --retries 3 --best-effort` and continue with the best available local rules.

## Codex Question Bridge

When AI-DLC rules require a dedicated question file, adapt that requirement to the active Codex interface instead of forcing the user to edit a markdown questionnaire.

Use this bridge only when a question-capable planning interface is available. In this environment, that means the `request_user_input` tool is listed for the current turn. Otherwise, fall back to the original AI-DLC question-file workflow.

Bridge behavior:

1. Generate the questions using AI-DLC's completeness, ambiguity, option-quality, and extension opt-in rules.
2. Ask questions through `request_user_input` in small batches of one to three questions. This is a per-batch UI limit, not a total question limit.
3. Convert each AI-DLC option to a `request_user_input` option. Keep the recommended/default option first when there is a clear default.
4. Treat the user's selected option or free-form "Other" response as equivalent to an AI-DLC `[Answer]:` value.
5. Analyze the collected answers for missing detail, ambiguity, or contradiction before proceeding.
6. Ask follow-up question batches through the same bridge until AI-DLC completeness checks are satisfied or the user explicitly asks to proceed despite remaining ambiguity.
7. Feed the collected answers directly into the required AI-DLC artifacts, such as requirements, story plans, workflow plans, or design documents.

Question files are no longer the primary input mechanism in Codex Plan Mode. Do not create an unanswered `*questions.md` file just to make the user fill it in. If an AI-DLC audit trail or resumable state needs the answers, create or update a completed record file after answers are collected, with each question and resolved answer already filled in.

Interpret AI-DLC's "never ask questions in chat" rule as "do not ask free-form inline chat questions when the structured Codex question UI is available." The structured question UI is the preferred Codex equivalent of AI-DLC's questionnaire file.

### Plan Mode Completeness Gate

Before emitting a final Plan Mode `<proposed_plan>`, confirm the plan has enough answered context for:

- goal and success criteria
- user or audience and scope boundaries
- functional requirements
- non-functional requirements
- technical context and integration boundaries
- selected AI-DLC extension gates
- standard terminology coverage for Inception artifacts, when Inception is in scope
- testing and verification expectations
- implementation handoff constraints

Do not emit a final plan after only one `request_user_input` batch unless every category is answered, irrelevant, or recorded as a low-impact assumption. If any category remains unresolved and materially affects implementation, ask another `request_user_input` batch instead of finalizing.

## Plan Mode Implementation Handoff

When explicit AI-DLC work produces a Plan Mode `<proposed_plan>`, include this implementation handoff command in the plan or immediately adjacent handoff text:

```text
Implement the plan with $aidlc constraints preserved.
```

The plan must state that implementation preserves AI-DLC-derived requirements, selected extension gates, acceptance criteria, frontend `DESIGN.md` constraints when applicable, and verification obligations. If implementation conflicts with these constraints, the implementer should revise the plan or ask for clarification instead of silently relaxing them.

## Operating Flow

Follow the AI-DLC rules while staying under the active Codex, AGENTS.md, and tool safety instructions.

1. Identify the current lifecycle phase from the user's request and the repository state.
2. Gather repository facts before asking product or architecture questions.
3. Produce the minimum required AI-DLC artifact for the phase before implementation.
4. Keep artifacts local to the target project unless the user requests a global artifact.
5. Verify changes with the project's existing test, lint, typecheck, and static-analysis commands when available.

## Standard Terms Contract

For every explicit `$aidlc` Inception flow, create or update `standard_terms.md` at the target project root. This is a project-level terminology contract and is an intentional local Codex adaptation of AI-DLC; do not place the canonical glossary only under `aidlc-docs/`.

If `standard_terms.md` is missing, initialize it from [standard_terms_template.md](references/standard_terms_template.md) and populate it from the user request, existing project docs, reverse-engineering artifacts, code identifiers, API/domain models, UI copy, and AI-DLC Inception outputs.

Terminology rules:

1. Treat `standard_terms.md` as the canonical glossary for requirements, user stories, workflow plans, application design, unit decomposition, construction design docs, and review artifacts.
2. Before finalizing any AI-DLC document, check it against `standard_terms.md` and correct synonym drift, renamed concepts, ambiguous labels, or inconsistent role/entity/API names.
3. When a new term, acronym, role, external system, domain concept, migration concept, or overloaded label appears, either define it in `standard_terms.md` from strong local evidence or ask the user through the active question gate if the definition affects scope, API, data model, UX, security, compliance, migration behavior, or acceptance criteria.
4. For migrations, refactors, and modernization work, preserve existing project terminology by default. Rename terms only when the user decides to do so or when evidence shows the current term is misleading or conflicting.
5. AI-DLC artifacts should reference `standard_terms.md` instead of duplicating full glossary tables. Short local clarifications are allowed only when needed for readability.
6. If terminology changes after documents are written, update the affected documents so they use the preferred terms.

### Human Terminology Review Gate

During Inception artifact validation, `standard_terms.md` is a mandatory human review artifact. Do not self-approve this gate.

Before treating Inception outputs as approved:

1. Present `standard_terms.md` at the project root as a required review target together with the Inception artifacts.
2. Tell the human reviewer to read `standard_terms.md` and verify that requirements, user stories, workflow planning, application design, and unit decomposition use its preferred terms and definitions consistently.
3. Require explicit confirmation that `standard_terms.md` was reviewed. When `request_user_input` is available, use it to collect that confirmation; otherwise include the requirement in the approval message and stop for the user's approval.
4. If the reviewer or agent finds missing, unclear, duplicated, deprecated, or conflicting terms, update `standard_terms.md` first, then update affected AI-DLC documents before approval.
5. Append the terminology review result, reviewer response, and any terminology corrections to `aidlc-docs/audit.md`.

Use this wording in Inception completion or approval messages:

```text
Before approving Inception outputs, read `standard_terms.md` at the project root and verify that all Inception artifacts follow its preferred terms and definitions. If any new or unclear term appears, define it in `standard_terms.md` and update the affected AI-DLC documents before approval.
```

## Integration Rules

- Do not auto-start AI-DLC for normal development requests.
- Do not override stricter local `AGENTS.md` instructions.
- Do not add new runtime dependencies to the target project just to follow AI-DLC.
- Prefer existing Codex skills and local workflows for execution mechanics; use AI-DLC as lifecycle guidance.
- If AI-DLC guidance conflicts with higher-priority system, developer, or user instructions, follow the higher-priority instruction and state the conflict briefly.

## Generated Code Ralph Review Gate

When AI-DLC Code Generation Part 2 completes for a unit, replace the human generated-code approval gate with a Codex-owned `$ralph` loop that runs `$code-review` until the generated code is genuinely clean. This is a local Codex adaptation of the AI-DLC approval gate; do not edit the upstream `references/aidlc-rules/` cache for this behavior.

Gate behavior:

1. Start `$ralph` immediately after Unit n code, tests, and code artifacts are generated.
2. Scope `$code-review` to all files created or modified for that unit, related tests, `contracts`, and the unit AI-DLC design/code artifacts. If the project has `apps/api`, `apps/mobile`, or `contracts`, explicitly verify those areas match the unit design intent and shared contracts.
3. Persist each review iteration under `aidlc-docs/construction/{unit-name}/code-review/iteration-{n}.md`. The final passing review should be stored as or linked from `aidlc-docs/construction/{unit-name}/code-review/generated-code-review.md`.
4. Treat every `$code-review` issue as blocking, regardless of severity. `COMMENT`, `REQUEST CHANGES`, or any `Total Issues` value above zero means the gate has failed.
5. `$ralph` must fix the reported issues, rerun relevant verification, and rerun `$code-review` on the same unit scope until the review report contains both `RECOMMENDATION: APPROVE` and `Total Issues: 0`.
6. Only after both approval conditions are true, append `Generated code approved` plus the final review verdict and timestamp to `aidlc-docs/audit.md`, then mark the unit Code Generation stage complete in `aidlc-docs/aidlc-state.md`.
7. If a finding requires a product, architecture, contract, or design decision that cannot be inferred from existing AI-DLC artifacts, stop the automatic loop and use the active question/planning gate instead of guessing.
8. If Ralph runtime support is unavailable, do not auto-approve generated code. Report the missing runtime as a blocker and leave the AI-DLC code approval gate unresolved.

Build and Test remains a separate AI-DLC stage after all unit code generation gates pass.

## Frontend DESIGN.md Integration

When explicit AI-DLC work includes frontend UI, treat `DESIGN.md` as the frontend design contract. Frontend UI includes web, mobile, desktop, Flutter, React, CSS, Tailwind, app screens, components, visual design, responsive behavior, accessibility, or any existing/new `DESIGN.md`.

Use [frontend-design-contract.md](references/frontend-design-contract.md) for the lifecycle mapping and artifact rules.

- Use the bundled DESIGN.md references under `references/design-md/` as the local source for DESIGN.md templates, validation checks, and design movement/style-lineage selection. Korean translations are available under `references/design-md-ko/` with `-ko` filename suffixes.
- During Plan Mode, choose DESIGN.md movement options only after reading existing project documents and frontend evidence. If bundled references are insufficient and web access is available, do targeted external research before presenting options.
- For migrations, refactors, modernization, enhancements, or existing frontend work, ask whether to preserve, evolve, or replace the current design movement and component system. Default to preserving existing movement/components unless the user requests redesign or evidence shows they conflict with accessibility, usability, or product requirements.
- If no project `DESIGN.md` exists, use `create-design-md` during Inception/Application Design before frontend implementation.
- If a project `DESIGN.md` exists, use `use-design-md` for frontend Functional Design, Code Generation, and any UI implementation.
- If Stitch SDK/MCP is used for screen ideation, apply the Stitch auth gate and fallback ladder in [frontend-design-contract.md](references/frontend-design-contract.md). Ask for an authentication method through `request_user_input` only when that tool is available; never ask the user to paste raw secrets into chat.
- For proposed UI, generated mockups, or component drafts, use `eval-design-md` before treating the design as accepted.
- For implemented frontend screens, components, screenshots, or routes, use `check-design-md` during review/build/test gates.
- Keep `DESIGN.md` canonical for visual tokens, components, responsive rules, and accessibility constraints. AI-DLC artifacts should reference it instead of duplicating token definitions.

## Updating Rules

Run this when the user asks to update AI-DLC rules or when bundled references are missing:

```bash
python3 ~/.codex/skills/aidlc/scripts/update_aidlc_rules.py --retries 3 --best-effort
```

The updater preserves the existing rule cache on download, extraction, or validation failure.
