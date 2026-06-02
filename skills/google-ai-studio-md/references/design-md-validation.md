# DESIGN.md Validation

Use `npx @google/design.md lint DESIGN.md` when possible. It validates the file, not the built UI.

## Official Lint Topics

- Broken token references such as `{colors.primary}` when `colors.primary` does not exist.
- Missing primary color.
- Component text/background contrast below WCAG AA.
- Orphaned color tokens not referenced by components.
- Token summary.
- Missing optional sections such as spacing or rounded.
- Missing typography.
- Section order drift.

## Manual Fallback

If the CLI cannot run:

1. Check YAML fences and parse mentally for indentation errors.
2. Confirm `name`, `colors.primary`, typography, spacing, rounded, and components exist.
3. Confirm every `{path.to.token}` reference resolves.
4. Check component foreground/background contrast.
5. Verify canonical section order.
6. Ensure every major frontend component has a token entry or prose rule.
7. Ensure design movement rules are specific and enforceable.
