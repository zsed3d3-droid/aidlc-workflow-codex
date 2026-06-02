# AI Studio Prompt Template

Use this template for `inception/AI_STUDIO_PROMPT.md`. The final document must be directly copyable into Google AI Studio Build/App generation and should not require AI Studio to read local files.

```markdown
# Google AI Studio Build Prompt

Build a production-quality first version of the following app.

## Build Target

- **App name**:
- **Platform**: Web app / Native Android app / Both
- **If web**: Use React by default. Use a Node server-side runtime only where server behavior is required.
- **If Android**: Use Kotlin and Jetpack Compose.
- **Primary user**:
- **Primary job-to-be-done**:

## Product Summary

Summarize the product in one paragraph. Include the problem, target user, and outcome.

## Required Screens

Implement these screens with complete empty, loading, error, and success states where relevant:

1. **Screen name**
   - Purpose:
   - Primary actions:
   - Key components:
   - States:
   - Acceptance:

## Core Functional Requirements

- `FR-001`:

## AI/Gemini Requirements

- `AIR-001`:
- Do not expose raw prompts, secrets, API keys, or service account material in the UI or source.
- Show clear generation status, user review affordances, retry behavior, and safe fallback copy.

## Data and Integrations

- **Entities**:
- **Persistence**:
- **External APIs**:
- **Auth**:
- **Stub policy**: If an integration cannot be completed in AI Studio, create a clearly named mock service with realistic data and a visible TODO.

## Design Requirements

Follow this design system summary:

- **Design movement/style lineage**:
- **Visual tone**:
- **Color roles**:
- **Typography**:
- **Layout and density**:
- **Components**:
- **Do not use**:

## Interaction Requirements

- Navigation:
- Forms and validation:
- Error handling:
- Undo/retry:
- Responsive behavior:
- Accessibility:

## Implementation Constraints

- Keep the implementation cohesive and runnable in Google AI Studio.
- Prefer simple, maintainable components and clear state management.
- Do not hard-code secrets.
- Use realistic placeholder data only when real integrations are not available.
- Include comments only where they clarify non-obvious logic.
- Avoid decorative UI that conflicts with the design requirements.

## Acceptance Criteria

- `AC-001`:

## Known Out of Scope

- `NG-001`:
```
