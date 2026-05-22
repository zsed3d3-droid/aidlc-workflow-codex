---
name: check-design-md
description: Use when auditing an existing frontend implementation, app screen, route, component library, or screenshot against DESIGN.md, design.md, design-md, check_design_md, or a project design-system markdown contract.
---

# Check DESIGN.md

## Overview

Check whether the current frontend implementation actually follows `DESIGN.md`. This skill is for implementation audits after or during build work, while `eval-design-md` is for reviewing proposed/generated UI artifacts.

## Workflow

1. Locate `DESIGN.md` and the frontend root.
2. Read framework/theme files, component primitives, route/page code, and CSS/Tailwind/Flutter theme definitions.
3. If a running app or screenshots are available, inspect the rendered UI. Prefer rendered evidence over code inference.
4. Use [audit-rubric.md](references/audit-rubric.md) to check token usage, component compliance, layout, responsive behavior, accessibility, and drift.
5. Run `npx @google/design.md lint DESIGN.md` if available. This validates the design file, not the frontend code.
6. Run the project's normal frontend checks when relevant: typecheck, lint, unit tests, visual tests, or screenshot checks.
7. Report findings first, ordered by severity, with file references or screenshot evidence where possible.

## AI-DLC Use

When invoked from `aidlc`, use this during Review, Build and Test, or completion checks for implemented frontend screens, routes, components, or screenshots. Treat significant DESIGN.md drift, inaccessible states, broken responsive behavior, or undocumented component variants as findings that must be resolved or recorded as risks before frontend completion is claimed.

If the implementation started from Stitch SDK/MCP output or a Stitch export, audit the final project code against `DESIGN.md`, not against Stitch's raw HTML. Flag unreviewed provider styles, undocumented variants, or copied prototype-only markup as implementation drift.

## What To Check

- Raw colors, fonts, shadows, radii, spacing, or breakpoints that bypass DESIGN.md tokens.
- Component variants implemented in code but absent from `DESIGN.md`.
- `DESIGN.md` component rules present but not implemented.
- Pages using a different design movement or palette.
- Responsive breakpoints that cause overlap, truncation, unreadable text, or broken touch targets.
- Accessibility issues: contrast, focus rings, disabled states, tap target size, motion sensitivity.
- Repeated one-off styling that should become a token or component entry.

## Output Shape

Use code-review style:

1. Findings by severity.
2. Open questions or assumptions.
3. Verification run and results.
4. Suggested `DESIGN.md` updates, if any.

Do not claim compliance without reading both `DESIGN.md` and implementation evidence.
