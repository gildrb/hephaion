---
name: gildrb-color-audit
description: Audit and enforce gildrb semantic color usage only. Use for dark or light theme colors, text hierarchy, selection colors, hover-state color assignments, image highlight color, borders, or Heph terminal surface and text tokens. Do not use for spacing, typography, layout, media encoding, event behavior, semantics, or copy.
---

# Gildrb Color Audit

## Mission

Prove that every visible color comes from the approved semantic system and correct any color-only drift.

## Owns

- Token values and semantic token assignment.
- Dark/light theme color parity.
- Selection, contour, highlight, terminal surface, and state colors.
- Detection of private flat colors.

## Excludes

- Do not change when a state activates; `gildrb-interaction` owns state behavior.
- Do not change focus semantics; `gildrb-accessibility` owns keyboard behavior.
- Do not change spacing, type metrics, geometry, assets, copy, or DOM structure.

## Fixed Contract

- Dark: `--bg #000000`, primary `#ffffff`, secondary `#b3b3b3`, tertiary `#767676`.
- Light: `--bg #ffffff`, primary `#000000`, secondary `#4d4d4d`, tertiary `#767676`.
- Highlight: background `#b3b3b3`, text `#ffffff` in both themes.
- Authored content and headings: primary unless the approved case-prose rule assigns secondary.
- Labels and supporting metadata: secondary.
- Inactive or actionable navigation, dates, metadata terms, captions, tool context: tertiary.
- Hovered actionable text and icon controls: primary.
- Case image contour: primary mixed at `14%`; homepage row separators: primary mixed at `12%`.
- Heph case terminal: terminal `96% bg / 4% primary`, prompt/composer `94% / 6%`, mobile frame `92% / 8%`.
- Terminal human content: primary; values: secondary; labels, tools, and complete materials source line: tertiary.
- Only private terminal flat colors allowed: `#f96664`, `#face2e`, `#3bc55d` for macOS lights.

## Procedure

1. Inventory hex, rgb, hsl, named colors, `color-mix`, and color-bearing CSS properties with `rg`.
2. Map each visible element to one semantic role before editing.
3. Replace private colors with existing tokens or the exact approved derived mix.
4. Inspect dark and light computed styles for rest, hover, focus, selection, and disabled states that exist.
5. Check artwork separately; do not rewrite colors inside authored image assets.

## Reject

- A new palette, project color, gradient, glow, translucent decorative panel, or shadow.
- A raw color where an approved token exists.
- Color as the only interaction signal.
- A color fix that changes opacity, layout, type, copy, or state logic.
- A contrast claim checked in only one theme.

## Verify

Run the build, repository verifier, Hephaion checker, and `git diff --check`. Audit both themes in the browser, including selection, project rows, links, theme icon, terminal labels/values/surfaces, and case-image contours. Confirm no unauthorized flat colors remain.

## Done

Every visible interface color has an approved semantic role in both themes, terminal exceptions are limited to the three lights, and the diff is color-only.
