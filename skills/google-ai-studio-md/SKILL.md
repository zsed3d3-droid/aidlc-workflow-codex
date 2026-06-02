---
name: google-ai-studio-md
description: Use when creating Google AI Studio Build/App handoff documents, including AI-DLC-style Inception interviews, PRD, Product Design Requirements (PDR), DESIGN.md, Korean -KO variants, and a copyable AI Studio implementation prompt. Use for "$google-ai-studio-md", "Google AI Studio PRD", "AI Studio Build prompt", "PDR", or "DESIGN.md for AI Studio" requests.
---

# Google AI Studio MD

Create an `inception/` documentation bundle that is ready to hand to Google AI Studio Build/App generation. This skill borrows AI-DLC's Inception discipline: ground in local facts, interview until requirements are complete, generate traceable artifacts, and stop before implementation.

Do not generate unit decomposition or `units-generation.md`.

## References

Load these files only when needed:

- [interview-guide.md](references/interview-guide.md): required before interviewing.
- [inception-output-contract.md](references/inception-output-contract.md): required before writing artifacts.
- [prd-template.md](references/prd-template.md): required for `PRD.md`.
- [pdr-template.md](references/pdr-template.md): required for `PDR.md`.
- [ai-studio-prompt-template.md](references/ai-studio-prompt-template.md): required for `AI_STUDIO_PROMPT.md`.
- [design-md-template.md](references/design-md-template.md): required for `DESIGN.md`.
- [design-md-validation.md](references/design-md-validation.md): required for DESIGN.md validation.
- [design-movements.md](references/design-movements.md): use when the visual direction is not explicit. Load one matching movement detail file, not the whole catalog.

## Workflow

1. Inspect the workspace before asking questions. Identify existing code, product docs, screenshots, theme files, `DESIGN.md`, AI-DLC docs, and likely app platform.
2. Interview using [interview-guide.md](references/interview-guide.md). Prefer `request_user_input` when available; otherwise ask concise chat questions. Ask in small batches, analyze answers for ambiguity, and ask follow-ups before drafting.
3. Select platform scope during the interview: web app, native Android app, or both. For Google AI Studio Build handoff, web app prompts should assume React by default and Node for server-side runtime unless the user chooses otherwise; Android prompts should assume Kotlin and Jetpack Compose.
4. Generate the complete artifact bundle described in [inception-output-contract.md](references/inception-output-contract.md). English files are canonical. Always generate Korean equivalents with `-KO` suffix.
5. Make `DESIGN.md` the canonical frontend design contract. PRD and PDR may reference `DESIGN.md`, but they should not duplicate full token tables.
6. Make `AI_STUDIO_PROMPT.md` a copyable implementation prompt. Prioritize AI Studio Build/App instructions, screen inventory, interaction requirements, data/integration boundaries, constraints, and acceptance criteria.
7. Validate artifacts:
   - Confirm all required files exist under `inception/`.
   - Confirm no `units-generation.md` or unit-decomposition artifact was created.
   - Validate `DESIGN.md` with `npx @google/design.md lint inception/DESIGN.md` when available; otherwise use [design-md-validation.md](references/design-md-validation.md).
   - Confirm `*-KO.md` files preserve the same decisions as the English canonical files.

## Output Rules

- Keep application code out of `inception/`.
- Do not ask the user to paste API keys, OAuth tokens, service account material, or other secrets into chat or documents.
- If Google AI Studio, Gemini, or Build mode capabilities are material to the handoff and the user asks for current behavior, verify current official docs before making time-sensitive claims.
- If a required product decision remains ambiguous after follow-up questions, record it in each affected artifact's Open Questions or Assumptions section instead of silently choosing.
- Completion should report the generated file paths and any unresolved risks.
