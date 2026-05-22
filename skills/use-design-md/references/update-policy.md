# DESIGN.md Update Policy

Update `DESIGN.md` during implementation only when the implementation needs a reusable design decision that the file does not cover.

## Add

- Component variant: `button-primary-loading`, `lesson-card-locked`, `pet-reaction-toast`.
- State rule: focus, hover, pressed, disabled, selected, complete, error, empty, loading.
- Responsive rule: board resize, toolbar collapse, panel stacking, mobile touch sizing.
- Domain primitive: board cell, lesson stepper, reward panel, progress badge.
- Accessibility rule: focus treatment, contrast exception, reduced motion fallback.

## Do Not Add

- One-off colors for a single screen.
- New font families without product-level reason.
- Extra spacing scales for local layout convenience.
- Decorative gradients or effects that contradict the design movement.
- Large rewrites while implementing a narrow UI task.

## Patch Shape

- Add tokens in YAML first.
- Add prose in the matching section.
- Add component variants as separate `components:` keys.
- Mention why the addition is reusable.
