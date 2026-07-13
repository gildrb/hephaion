---
name: gildrb-design
description: Use for gildrb typography, color, spacing, portfolio shell, project navigation, responsive layout, media optimization, no-crop behavior, interaction, accessibility, or visual verification.
---

# Design

Apply the exact portfolio system.

## Workflow

1. Read current CSS and rendered pages.
2. Read `../../design.md` completely.
3. Load the relevant reference below.
4. Reuse existing shell selectors and tokens.
5. Reject arbitrary type, spacing, dividers, and crop.
6. Verify desktop, mobile, focus, theme, and media behavior.
7. If the behavior is reusable, update `../../design.md`, the matching reference, and `../../scripts/check_design_docs.py` before shipping.

## References

- `references/typography-and-spacing.md`: exact type and rhythm.
- `references/shell-and-navigation.md`: shared location and responsive shell.
- `references/media-and-interaction.md`: image, preview, focus, and theme contracts.
- `references/verification.md`: visual acceptance matrix.

## Done

- Approved tokens and type steps are used.
- Persistent location remains stable.
- Images remain full-frame and optimized.
- No middle-dot or rule dividers appear.
- Mobile and desktop match the same system.
- Short case pages remain in natural flow; long case pages respect the desktop theme-toggle endpoint.
- Reused interfaces have one canonical partial rather than copied markup.
- The design document, skill reference, and executable checker agree with the implementation.
