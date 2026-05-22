# Implementation Checklist

- Resolve all design choices through `DESIGN.md` tokens or component entries.
- Keep raw color literals out of component code unless the token system has no mapping yet.
- Prefer app theme APIs over local inline styles.
- Implement states documented in `DESIGN.md`, not just the default state.
- Check mobile layout, text fitting, and 44px touch targets.
- Preserve the declared design movement when composing new screens.
- If a component needs a new state, update `DESIGN.md` before or with the code change.
- After UI changes, run available frontend verification and inspect screenshots when possible.
