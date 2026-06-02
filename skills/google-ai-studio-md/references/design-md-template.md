# Frontend DESIGN.md Template

Use this as a compact scaffold. Fill every placeholder with project-specific decisions before writing the final file.

```markdown
---
version: alpha
name: <Project Design System Name>
description: <One sentence describing the visual identity and product context.>
colors:
  primary: "#000000"
  on-primary: "#ffffff"
  canvas: "#ffffff"
  surface: "#f7f7f7"
  ink: "#111111"
  ink-muted: "#666666"
  hairline: "#e5e5e5"
  error: "#b42318"
typography:
  display:
    fontFamily: Inter, system-ui, sans-serif
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.05
    letterSpacing: 0px
  headline:
    fontFamily: Inter, system-ui, sans-serif
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0px
  body:
    fontFamily: Inter, system-ui, sans-serif
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
  label:
    fontFamily: Inter, system-ui, sans-serif
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
rounded:
  sm: 4px
  md: 8px
  lg: 12px
  full: 9999px
spacing:
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 32px
  section: 64px
components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label}"
    rounded: "{rounded.md}"
    padding: "12px 16px"
  button-secondary:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.label}"
    rounded: "{rounded.md}"
    padding: "12px 16px"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.md}"
    padding: "12px 14px"
  card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.lg}"
    padding: "{spacing.lg}"
---

# Design System

## Overview

<State the design movement/style lineage, target audience, product mood, density, and forbidden visual directions.>

## Colors

- **Primary** (`{colors.primary}`): <role>
- **Canvas** (`{colors.canvas}`): <role>
- **Surface** (`{colors.surface}`): <role>
- **Ink** (`{colors.ink}`): <role>
- **Hairline** (`{colors.hairline}`): <role>
- **Error** (`{colors.error}`): <role>

## Typography

<Explain type families, scale, hierarchy, weights, and where not to use decorative or mono fonts.>

## Layout

<Define spacing base, max widths, grid behavior, page density, and section rhythm.>

## Elevation & Depth

<Define how hierarchy is created: shadows, borders, tonal surfaces, color blocks, or flat composition.>

## Shapes

<Define radius language for buttons, cards, boards, panels, icons, and domain-specific surfaces.>

## Components

<Document each component token with states and usage constraints.>

## Do's and Don'ts

- Do <specific enforceable rule>.
- Don't <specific anti-pattern>.

## Responsive Behavior

<Define breakpoints, touch targets, collapsing rules, fixed-format element constraints, and image behavior.>

## Agent Prompt Guide

When building UI, use this file as the source of truth. Reuse token names. If a required component or state is missing, update DESIGN.md narrowly before adding one-off styles.
```
