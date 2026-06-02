# AI Studio Inception Interview Guide

Use this guide to conduct an AI-DLC-style Inception interview for Google AI Studio Build/App handoff docs.

## Interview Rules

- Inspect local evidence first: existing docs, code, UI files, screenshots, theme files, `DESIGN.md`, and product notes.
- Ask only questions that materially affect PRD, PDR, DESIGN.md, or the AI Studio prompt.
- Prefer `request_user_input` when available. Ask one to three questions per batch.
- Put the recommended/default option first when there is a defensible default.
- Treat free-form answers as authoritative if they are specific.
- After each batch, check for vague, conflicting, or missing answers. Ask follow-ups before drafting.
- Do not request secrets. Ask for integration shape, auth method, and runtime assumptions only.

## Required Decision Areas

Resolve these before drafting. If a decision is discoverable from local evidence, record it without asking.

| Area | What to resolve |
| --- | --- |
| Product intent | Product name, problem, target users, job-to-be-done, success criteria |
| Platform | Web app, native Android app, or both |
| AI Studio mode | Build/App generation goal, initial prompt usage, follow-up iteration expectations |
| Users and roles | Primary users, secondary users, admin/operator roles, permissions |
| Core workflows | End-to-end user journeys and priority flows |
| Screens | Screen inventory, navigation, empty/loading/error/success states |
| Data | Entities, user inputs, generated outputs, persistence needs, import/export |
| AI features | Gemini usage, prompts, grounding, tools, safety constraints, human review |
| Integrations | APIs, auth providers, files, payments, analytics, notifications |
| Non-functional requirements | Performance, privacy, accessibility, reliability, offline needs |
| Design direction | Brand tone, visual movement, density, responsive targets, component system |
| Acceptance | Testable scenarios, launch readiness, known non-goals |

## Suggested Question Batches

### Batch 1: Product and Platform

Ask when product intent or platform is not already clear:

- What is the product trying to help users accomplish?
- Which platform should Google AI Studio generate first: web app, native Android app, or both?
- What must be true for the first generated version to be considered useful?

### Batch 2: Users and Workflows

Ask when user journeys are underspecified:

- Who is the primary user, and what is their most frequent workflow?
- Which secondary roles or permissions matter for the first version?
- Which workflows are in scope for the first AI Studio build, and which are explicitly out of scope?

### Batch 3: Screens and UX

Ask when screen design is underspecified:

- What screens should exist in the first version?
- Which states must be represented: onboarding, empty, loading, error, success, review, history, settings?
- Should the experience optimize for dense productivity, guided creation, learning, commerce, entertainment, or another usage mode?

### Batch 4: Data, AI, and Integrations

Ask when implementation boundaries are unclear:

- What data should the app store locally or remotely?
- Which Gemini-powered features should AI Studio implement?
- Which external integrations, APIs, files, or auth methods are required?

### Batch 5: Design and Handoff

Ask when visual direction or prompt format is unclear:

- Should the app preserve an existing design system, evolve it, or create a new `DESIGN.md`?
- Which design movement best fits the audience and workflow?
- Should `AI_STUDIO_PROMPT.md` be optimized for a single paste into AI Studio, or for staged prompts by screen/feature?

## Follow-Up Triggers

Ask a follow-up when an answer includes:

- "depends", "maybe", "hybrid", "somewhere between", or "not sure" without decision rules.
- Multiple platform choices without priority.
- A feature list without acceptance criteria.
- AI behavior without safety, fallback, or review expectations.
- Design adjectives without enforceable UI constraints.
- Integrations without auth, data shape, or failure behavior.
