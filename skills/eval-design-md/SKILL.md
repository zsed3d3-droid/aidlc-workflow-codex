---
name: eval-design-md
description: Use when evaluating whether generated frontend components, mockups, screenshots, or UI proposals match DESIGN.md, a design movement, design.md rules, design-md tokens, or the user's requested visual direction before implementation or iteration.
---

# Evaluate DESIGN.md

## Overview

Evaluate UI artifacts against `DESIGN.md` and the declared design movement. This is a design-quality review, not a code review: lead with mismatches that would make the interface feel off-brand or inconsistent.

## Inputs

Use any available combination:

- `DESIGN.md`
- Component code
- Screenshots
- Figma/Stitch/exported mockups
- User prompt or product brief
- Existing app pages for comparison

## Workflow

1. Read `DESIGN.md` first. Identify the design movement, token system, signature components, and explicit do/don't rules.
2. Inspect the UI artifact. If screenshots are available, judge visible output; if only code exists, inspect styles and component structure.
3. Evaluate with [evaluation-rubric.md](references/evaluation-rubric.md).
4. Classify findings by severity:
   - Blocking: violates core design movement, token contract, accessibility, or responsive usability.
   - Major: visible drift from component rules, spacing, typography, or color roles.
   - Minor: polish issue that does not undermine the design system.
5. Provide concrete fixes using token/component names from `DESIGN.md`.
6. If the artifact exposes a missing design-system rule, recommend a `use-design-md` update instead of silently accepting drift.

## AI-DLC Use

When invoked from `aidlc`, use this as the frontend design review gate for proposed screens, generated mockups, component drafts, or UI plans before they are accepted into implementation artifacts. Record the verdict in the relevant AI-DLC design/review note when traceability is needed. If the artifact reveals a missing reusable rule, route that change through `use-design-md`.

Apply the same rubric to Stitch SDK/MCP outputs, user-exported Stitch HTML/ZIP/screenshots, and local fallback prototypes. The provider does not lower the bar: findings should still cite `DESIGN.md` tokens, components, states, responsive rules, or accessibility constraints.

## Output Shape

Start with a verdict:

- `Pass`: artifact fits the design contract with only minor polish notes.
- `Needs revision`: visible design drift or missing states exist.
- `Fail`: core movement/tokens/accessibility are wrong.

Then list findings with:

- Severity
- Evidence
- Relevant `DESIGN.md` token/section
- Exact fix

Keep summaries brief. The value is in actionable visual corrections.
