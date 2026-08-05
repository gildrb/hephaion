---
name: gildrb-interaction
description: Implement gildrb interface state behavior only. Use for hover and pointer states, project sorting, row navigation, email copying, theme behavior, scroll restoration, touch behavior, or Heph demo state. Do not use for staged entry/reveal animation or transition timing; use gildrb-motion. Do not use for visual tokens, spacing, typography, layout, semantics, media encoding, or copy.
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
- Do not design staged entry motion, keyframes, transition timing, easing, or animated evidence; use `gildrb-motion`.
## Fixed Contract

- Links navigate; buttons act.
- Hover CSS exists only inside `@media (hover:hover)`.
- Homepage project rows are anchors; Date, Project, and Scope sort controls are buttons. All links to `/all` with the active sort state.
- Each project row is one full-width link with aligned date, project, scope, and affordance columns.
- Hover/focus affordance reads `View →`; it changes no font weight and causes no layout shift.
- Decorative layers use `pointer-events:none`.
- Interactive controls have no dead visual areas.
- Click does not leave a permanent hover/selected appearance; blur mouse-activated controls when required.
- Theme applies immediately, persists when storage works, tolerates storage failure, and causes no broad transition.
- On the mobile homepage and every case route, switching themes keeps the toggle's fixed row-height hit box and shared icon center stationary even though the sun and moon SVGs have different sizes.
- Back/forward restores per-tab scroll; fresh navigation starts normally.
- A touch drag on the mobile homepage scrolls project rows inside the locked table region; the filter row and shared header do not move with row overscroll.
- Mobile intentionally locks document overflow while the table owns scrolling. Keep table `overscroll-behavior: auto`, conditional top/bottom edge fades, and a suppressed inner scrollbar; do not add scroll-chaining workarounds or claim document pull-to-refresh.
- The Heph demo lives only on `/heph` and uses the canonical shared partial and live scripts.
- Interaction feedback is absent unless necessary, no longer than `200ms`, and respects reduced motion.
- The approved homepage entry, Heph cursor, mobile edge fade, and animated case evidence follow `gildrb-motion`; do not generalize their timing to other states.
- Every ordinary interactive element, including Date/Project/Scope sort buttons, uses the shared pressed feedback: `position: relative; top: 1px` only while `:active`. The Heph close control remains the sole exclusion.
- Homepage sorting preserves stable DOM row slots. Sort the data, then copy href, datetime, IDs, date text, title, and scope into existing rows. Never append sorted row nodes; WebKit can detach reordered nested-subgrid rows.
- Set `data-homepage-entry-complete` before the first sorted value update. Desktop entry timing stays unchanged; mobile Links/Contact timing follows visual rows.
- On mobile, measure `.portfolio-card-scope` or `.case-next-scope` against the active Links container and set `--mobile-contact-start`. Re-run after relevant resize/font/layout changes.
## Procedure

1. Trace the native element, full hit box, listeners, state, and cleanup path.
2. Reproduce with mouse, touch emulation, keyboard activation, and back/forward when relevant.
3. Route visual interpolation, staged reveals, or animation timing to `gildrb-motion`; this skill owns the state transition that triggers it.
4. Edit the shared source handler or component only; do not fork route behavior.
5. Keep DOM updates local and synchronous unless the action is genuinely asynchronous.
6. Rebuild and test rest, hover, active, completed, navigation-return, and failure states.
7. For sort controls, hold pointer-down and prove a `1px` Y delta, then release and prove `0px`; test Date, Project, and Scope after the entry sequence completes.

## Reject

- A clickable-looking dead area.
- Non-native clickable containers when an anchor or button fits.
- Hover left active on touch.
- A row affordance that shifts its columns or intercepts the row link.
- Reparenting sorted project rows or measuring one fixed Project width for every case table.
- Opacity-only affordances or state-dependent font weight.
- Duplicate Heph demo implementations.

## Verify

Run the build, repository verifier, and `git diff --check`. Exercise the interaction in WebKit on desktop and mobile, plus Chromium for font-metric-sensitive table work. Check target bounds, `1px` pressed feedback, URL/result, sort-slot stability, Scope/Contact equality, cleanup, theme persistence/failure tolerance, back/forward scroll, reduced motion, and console errors as applicable.

## Done

The complete hit area behaves correctly in every relevant input/lifecycle state, uses shared implementation, and changes no unrelated visual or editorial concern.
