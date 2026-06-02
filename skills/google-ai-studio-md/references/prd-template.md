# PRD Template

Use this template for `inception/PRD.md`.

```markdown
# Product Requirements Document

## 1. Summary

- **Product name**:
- **Platform target**: Web app / Native Android app / Both
- **Primary user**:
- **Problem statement**:
- **Outcome goal**:

## 2. Context

Describe the business, user, or workflow context. Include relevant local evidence inspected during Inception.

## 3. Goals and Non-Goals

### Goals

- `G-001`:

### Non-Goals

- `NG-001`:

## 4. Users and Roles

| Role | Description | Primary needs | Permissions |
| --- | --- | --- | --- |
|  |  |  |  |

## 5. Core User Journeys

| Journey ID | User | Trigger | Desired outcome | Related requirements |
| --- | --- | --- | --- | --- |
| `UJ-001` |  |  |  |  |

## 6. Functional Requirements

| ID | Requirement | Priority | Acceptance signal |
| --- | --- | --- | --- |
| `FR-001` |  | Must |  |

## 7. AI and Automation Requirements

Document Gemini or AI-powered behavior, prompts, grounding, user review, failure modes, safety constraints, and fallback behavior.

| ID | Requirement | Guardrails | Acceptance signal |
| --- | --- | --- | --- |
| `AIR-001` |  |  |  |

## 8. Data and Integrations

### Data Model

| Entity | Purpose | Key fields | Persistence |
| --- | --- | --- | --- |
|  |  |  |  |

### Integrations

| Integration | Purpose | Auth method | Failure behavior |
| --- | --- | --- | --- |
|  |  |  |  |

## 9. Non-Functional Requirements

| ID | Category | Requirement | Acceptance signal |
| --- | --- | --- | --- |
| `NFR-001` | Accessibility |  |  |
| `NFR-002` | Performance |  |  |
| `NFR-003` | Privacy/Security |  |  |
| `NFR-004` | Reliability |  |  |

## 10. Google AI Studio Build Constraints

- **Web app default**: Use React unless the user selected another web stack.
- **Server-side runtime**: Use Node when server behavior is needed unless the user selected another runtime.
- **Android default**: Use Kotlin and Jetpack Compose for native Android generation.
- **Secrets**: Do not hard-code API keys, OAuth tokens, or service account material.
- **Iteration**: Build the first complete version from the prompt, then refine by screen and behavior.

## 11. Acceptance Criteria

| ID | Scenario | Given | When | Then |
| --- | --- | --- | --- | --- |
| `AC-001` |  |  |  |  |

## 12. Risks, Assumptions, and Open Questions

### Risks

- `R-001`:

### Assumptions

- `A-001`:

### Open Questions

- `OQ-001`:
```
