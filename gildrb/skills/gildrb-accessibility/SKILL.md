---
name: gildrb-accessibility
description: Audit and enforce gildrb accessibility only. Use for semantic HTML, heading order, accessible names, alt text presence, keyboard navigation, focus order, focus-visible rings, status announcements, reduced motion exposure, or screen-reader behavior. Do not use for pointer interaction logic, spacing, typography, colors, layout geometry, media optimization, or copywriting.
---

# Gildrb Accessibility

## Mission

Ensure the existing interface is operable and understandable without a mouse or visual inference.

## Owns

- Native semantics, heading structure, accessible names, ARIA only when native HTML is insufficient.
- Keyboard reachability/order/activation, `:focus-visible`, status announcements, and decorative exposure.
- Presence and correctness checks for image alternatives supplied by the user.

## Excludes

- Do not invent descriptive or editorial alt text; request it or preserve supplied text.
- Do not change pointer behavior, visual spacing, type metrics, color tokens, shell geometry, image encoding, or prose.
- Use existing primary token for focus visibility; color changes belong to `gildrb-color-audit`.

## Fixed Contract

- One semantic page heading with ordered section headings.
- Anchors navigate; buttons act; icon-only controls have explicit accessible names.
- Meaningful images have specific supplied alt text; decorative images use empty alt and are hidden where appropriate.
- Visible DOM order and Tab order agree. No positive `tabindex`.
- Case mobile order: location, article, shared navigation; theme control remains reachable in its visible position.
- The Heph terminal exposes only its chat input as an internal Tab stop, then the case repository link; decorative terminal chrome is not focusable.
- Homepage project rows use an unclipped `1px` primary focus ring with `6px` offset.
- Date, Title, and Field expose their active sort state and announce each completed ordering.
- Status changes such as email copy are announced near the trigger.
- Link purpose remains clear without relying on hover or color alone.
- Page remains operable at `320px` and `390px` without horizontal overflow.

## Procedure

1. Inspect the accessibility tree and DOM source order before CSS order.
2. Tab from the first control through the complete route and record every stop.
3. Activate each control with keyboard only.
4. Prefer native semantics; add ARIA only to fill a real semantic gap.
5. Confirm focus visibility in dark and light themes and at clipped/rounded boundaries.
6. Rebuild and repeat on homepage and every changed case route.

## Reject

- Positive `tabindex`, duplicate focus targets, focusable decorative UI, or CSS order contradicting DOM order.
- `outline:none` without an equivalent visible focus state.
- Tooltip-only meaning, color-only state, or inaccessible disabled explanation.
- Invented alt text or copy edits.

## Verify

Run the build, repository verifier, and `git diff --check`. Complete a keyboard-only pass in both themes and at desktop/mobile widths. Inspect headings, names, roles, states, announcements, image alternatives, focus clipping, and console accessibility errors.

## Done

Every visible control is reached once in predictable order, activated natively, visibly focused, and correctly named without unrelated visual or editorial changes.
