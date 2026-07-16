---
name: gildrb-interaction
description: Implement gildrb interface behavior only. Use for hover and pointer states, project sorting, row navigation, email copying, theme-toggle behavior and persistence, scroll restoration, touch behavior, or Heph demo interaction. Do not use for visual token selection, spacing, typography, layout geometry, accessibility semantics, media encoding, or copy.
---

# Gildrb Interaction

## Mission

Make one interaction behave predictably across pointer, touch, navigation, and browser lifecycle states.

## Owns

- Native link/button choice and event behavior.
- Hit-area coverage, pointer handling, hover activation, click cleanup, and state persistence.
- Project sorting, row navigation, theme switching, email copy, scroll restoration, and live Heph demo behavior.

## Excludes

- Do not choose new colors; use approved tokens and `gildrb-color-audit` for color changes.
- Do not change tab order, ARIA, labels, or focus-ring semantics; use `gildrb-accessibility`.
- Do not change spacing, type, shell geometry, media encoding, or copy.

## Fixed Contract

- Links navigate; buttons act.
- Hover CSS exists only inside `@media (hover:hover)`.
- Homepage project rows are anchors; Date, Title, and Field sort controls are buttons.
- Each project row is one full-width link with aligned date, title, field, and reserved affordance columns.
- Hover/focus affordance reads `View →`; it changes no font weight and causes no layout shift.
- Decorative layers use `pointer-events:none`.
- Interactive controls have no dead visual areas.
- Click does not leave a permanent hover/selected appearance; blur mouse-activated controls when required.
- Theme applies immediately, persists when storage works, tolerates storage failure, and causes no broad transition.
- Back/forward restores per-tab scroll; fresh navigation starts normally.
- A touch drag on the mobile homepage moves the name, theme control, and content as one page; it must not treat the top row as a sticky navbar.
- Pull-to-refresh remains available; viewport fitting must not set `overflow: hidden` or `overscroll-behavior: none` on the page root.
- The Heph demo lives only on `/heph` and uses the canonical shared partial and live scripts.
- Motion is absent unless necessary, no longer than `200ms`, and respects reduced motion.

## Procedure

1. Trace the native element, full hit box, listeners, state, and cleanup path.
2. Reproduce with mouse, touch emulation, keyboard activation, and back/forward when relevant.
3. Edit the shared source handler or component only; do not fork route behavior.
4. Keep DOM updates local and synchronous unless the action is genuinely asynchronous.
5. Rebuild and test rest, hover, active, completed, navigation-return, and failure states.

## Reject

- A clickable-looking dead area.
- Non-native clickable containers when an anchor or button fits.
- Hover left active on touch.
- A row affordance that shifts its columns or intercepts the row link.
- Opacity-only affordances or state-dependent font weight.
- Duplicate Heph demo implementations.

## Verify

Run the build, repository verifier, and `git diff --check`. Exercise the interaction in a browser on desktop and mobile. Check target bounds, URL/result, cleanup, theme persistence/failure tolerance, back/forward scroll, reduced motion, and console errors as applicable.

## Done

The complete hit area behaves correctly in every relevant input/lifecycle state, uses shared implementation, and changes no unrelated visual or editorial concern.
