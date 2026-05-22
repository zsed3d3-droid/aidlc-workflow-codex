# Frontend DESIGN.md Audit Rubric

Use this for implementation checks.

## Evidence Sources

- `DESIGN.md`
- Theme files and CSS variables
- Tailwind config or design-token exports
- Component primitives
- Route/page code
- Storybook or preview pages
- Screenshots or Playwright captures

## Audit Checks

1. Token plumbing: project theme exposes DESIGN.md colors, typography, spacing, radius, and component styles.
2. Raw values: code avoids hardcoded colors, shadows, radii, font sizes, and breakpoints when tokens exist.
3. Component coverage: recurring UI maps to `components:` entries.
4. State coverage: hover, focus, pressed, disabled, selected, loading, empty, error, and success are covered where applicable.
5. Design movement: pages preserve the declared style lineage and do not drift into generic SaaS/default Tailwind.
6. Responsive behavior: breakpoints match DESIGN.md; no overlap, clipping, or unreadable text.
7. Accessibility: contrast, focus, target size, reduced motion, and text scaling are acceptable.
8. Drift candidates: repeated one-off styles should become DESIGN.md additions.

## Finding Template

- Severity:
- Location:
- Evidence:
- DESIGN.md rule/token:
- Fix:
