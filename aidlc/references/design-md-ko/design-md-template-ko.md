# Frontend DESIGN.md 템플릿

compact scaffold로 사용한다. 최종 파일을 쓰기 전에 모든 placeholder를 project-specific decision으로 채운다.

```markdown
---
version: alpha
name: <Project Design System Name>
description: <visual identity와 product context를 설명하는 한 문장.>
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

<design movement/style lineage, target audience, product mood, density, 금지할 visual direction을 적는다.>

## Colors

- **Primary** (`{colors.primary}`): <role>
- **Canvas** (`{colors.canvas}`): <role>
- **Surface** (`{colors.surface}`): <role>
- **Ink** (`{colors.ink}`): <role>
- **Hairline** (`{colors.hairline}`): <role>
- **Error** (`{colors.error}`): <role>

## Typography

<type family, scale, hierarchy, weights, decorative 또는 mono font를 쓰지 말아야 할 위치를 설명한다.>

## Layout

<spacing base, max width, grid behavior, page density, section rhythm을 정의한다.>

## Elevation & Depth

<hierarchy를 만드는 방식을 정의한다: shadows, borders, tonal surfaces, color blocks, flat composition 등.>

## Shapes

<buttons, cards, boards, panels, icons, domain-specific surfaces의 radius language를 정의한다.>

## Components

<각 component token을 state와 usage constraint와 함께 문서화한다.>

## Do's and Don'ts

- Do <구체적이고 enforceable한 rule>.
- Don't <구체적인 anti-pattern>.

## Responsive Behavior

<breakpoints, touch targets, collapsing rules, fixed-format element constraints, image behavior를 정의한다.>

## Agent Prompt Guide

UI를 만들 때 이 파일을 source of truth로 사용한다. token name을 재사용한다. 필요한 component 또는 state가 없으면 one-off style을 추가하기 전에 DESIGN.md를 좁은 범위로 업데이트한다.
```
