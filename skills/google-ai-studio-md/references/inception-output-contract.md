# Inception Output Contract

Generate all files under the target project root's `inception/` directory. English files are canonical. Korean files use the same basename plus `-KO`.

## Required Tree

```text
inception/
  state.md
  audit.md
  interview-log.md
  PRD.md
  PRD-KO.md
  PDR.md
  PDR-KO.md
  DESIGN.md
  DESIGN-KO.md
  AI_STUDIO_PROMPT.md
  AI_STUDIO_PROMPT-KO.md
```

Do not create `units-generation.md`, unit plans, unit maps, or construction-stage documents.

## File Contracts

### state.md

Record:

- Project name
- Workspace root
- Existing code/docs detected
- Platform selection: web, Android, or both
- Current stage: Inception complete or blocked
- Generated artifact list
- Open decisions

### audit.md

Record:

- Initial user request
- Local evidence inspected
- Interview batches and resolved answers
- Key assumptions
- Validation results
- Human approval status, if provided

### interview-log.md

Record each question, answer, follow-up, and resolution. If `request_user_input` was used, summarize the selected option and any user note.

### PRD.md

Use [prd-template.md](prd-template.md). Focus on product purpose, requirements, scope, platform, data, AI behavior, NFRs, and acceptance criteria.

### PDR.md

Use [pdr-template.md](pdr-template.md). `PDR` means Product Design Requirements. It bridges PRD behavior to screens, flows, components, interaction states, and `DESIGN.md`.

### DESIGN.md

Use [design-md-template.md](design-md-template.md). It is the canonical visual and component contract. Include YAML front matter tokens and enforceable UI rules.

### AI_STUDIO_PROMPT.md

Use [ai-studio-prompt-template.md](ai-studio-prompt-template.md). It must be directly copyable into Google AI Studio Build/App generation and include enough detail that AI Studio does not need the rest of the files.

## Korean Files

For every canonical English file that has a `-KO` counterpart:

- Preserve decisions, constraints, acceptance criteria, and file references.
- Translate section headings and prose into Korean.
- Keep technical identifiers, file names, component keys, token names, API names, and code-facing labels in English unless the source explicitly defines Korean names.

## Traceability Rules

- PRD requirements should have stable IDs such as `FR-001`, `NFR-001`, and `AC-001`.
- PDR screens and components should reference relevant PRD IDs.
- `AI_STUDIO_PROMPT.md` should reference PRD/PDR/DESIGN decisions by summary, not by requiring AI Studio to read local files.
- Open questions must appear in all affected documents.
