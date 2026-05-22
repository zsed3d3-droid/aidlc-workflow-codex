---
name: use-design-md
description: Use when frontend work must follow an existing DESIGN.md, design.md, design-md, use_design_md, or AI-readable design system file, and when UI implementation may need safe additions to DESIGN.md for missing components, states, responsive rules, or design constraints.
---

# Use DESIGN.md

## Overview

Use the project's `DESIGN.md` as the design contract for frontend work. Implement from existing tokens and rules first; update the file only when the current UI task exposes a real missing design decision.

## Workflow

1. Find `DESIGN.md` in the frontend root or nearest app root. If absent, use `create-design-md` before UI implementation.
2. Read the YAML tokens and the Markdown guidance. Tokens are normative; prose resolves ambiguous application.
3. Map the requested UI to existing component tokens before inventing new styles.
4. Implement using the project's frontend stack and existing component system.
5. Add to `DESIGN.md` only when a needed token, component variant, state, breakpoint, accessibility rule, or domain component is missing.
6. Keep additions narrow and reusable. Do not rewrite the design direction during normal implementation.
7. Validate the edited `DESIGN.md` with `npx @google/design.md lint DESIGN.md` when available, or use [update-policy.md](references/update-policy.md).
8. When finishing UI work, summarize which design tokens/components were used and any `DESIGN.md` additions.

## AI-DLC Use

When invoked from `aidlc`, use `DESIGN.md` during frontend Functional Design, Code Generation, and UI implementation. For `aidlc-docs/construction/{unit-name}/functional-design/frontend-components.md`, reference relevant `DESIGN.md` component keys, states, responsive rules, and accessibility constraints instead of copying visual token tables. If the functional design or implementation needs a reusable missing state or domain component, add it to `DESIGN.md` with this skill before using it in code.

If Stitch SDK/MCP or a Stitch export is used, treat the result as a candidate design artifact. Re-map useful ideas into existing `DESIGN.md` tokens/components, and add only missing reusable variants or states. Do not let raw Stitch HTML, colors, spacing, typography, or shadows become the production source of truth.

## Update Policy

Allowed additions:

- New component variants required by implemented UI, such as `lesson-card-locked` or `button-primary-loading`.
- State rules for hover, focus, pressed, disabled, loading, empty, error, success, selected, and completed.
- Responsive behavior discovered during implementation.
- Domain-specific UI primitives that will recur.
- Accessibility constraints that prevent visual ambiguity.

Avoid:

- Adding one-off tokens for a single element.
- Changing primary colors, font families, spacing scale, or design movement without explicit user direction.
- Burying variants in prose when they should be component tokens.
- Using raw colors or spacing values in code when matching tokens exist.

## Implementation Checklist

- Read [implementation-checklist.md](references/implementation-checklist.md) for frontend coding checks.
- Prefer existing UI components and theme APIs.
- If the stack uses Tailwind, map tokens to config/theme classes or CSS variables before adding ad hoc classes.
- If the stack uses Flutter, map tokens to `ThemeData`, `ColorScheme`, `TextTheme`, shape themes, and reusable widgets.
- If the stack uses CSS variables, generate or maintain variables from DESIGN.md token names.
