---
name: gildrb-shell-layout
description: Maintain gildrb page-shell geometry only. Use for wrapper width, sidebar and content columns, sticky positioning, shared navigation placement, responsive grid structure, DOM/visual ordering, case reading width, or theme-control placement. Do not use for local spacing rhythm, typography, colors, media encoding, interactions, accessibility labels, or copy.
---

# Gildrb Shell Layout

## Mission

Preserve one shared responsive shell and its exact structural geometry across every route.

## Owns

- Wrapper, layout, sidebar, content, and article widths.
- Grid/flex structure, position mode, responsive order, and breakpoint geometry.
- Shared shell partial placement and route consistency.

## Excludes

- Do not tune local margins or padding; use `gildrb-spacing`.
- Do not change type, colors, media files, event logic, accessibility labels, or prose.
- Do not duplicate shared navigation or the Heph demo.

## Fixed Contract

- Stack remains static HTML, CSS, and vanilla JavaScript.
- Desktop wrapper maximum: `1900px`, centered.
- Desktop composition: `240px` sidebar + `48px` gap + `760px` content, centered as one unit.
- Below `1400px`: wrapper padding `32px`, layout gap `32px`.
- Desktop sidebar: sticky at `top: 0`, `100vh`, `48px` vertical padding.
- Case article maximum: `760px`, centered; copy stays left-aligned.
- Mobile at `768px`: content plus `32px` theme-control column and wrapper inline padding `12px`. The layout and `.content` have `0` padding; the sticky name/theme row supplies `24px` top and `8px` bottom padding.
- Mobile uses the existing shared shell and `display: contents`; case article order `5`, shared navigation order `6`.
- Shared sidebar content appears on every route from one partial. Project location uses two lines: `Gil Rodrigues` then `→ <Project>`.
- Homepage and case Links groups begin at the same desktop coordinate by reserving two location lines.
- Heph demo markup has one canonical owner: `src/partials/heph-demo.html`.

## Procedure

1. Read all shared templates/partials before route-specific markup.
2. Read `10-base.css`, `20-portfolio-media.css`, `50-case-study.css`, and `90-responsive.css`.
3. Record current DOM order and computed grid at desktop and `390px`.
4. Change the shared owner, not generated HTML or route copies.
5. Preserve source order for keyboard users; CSS order may only reflect the same intended DOM sequence.
6. Rebuild every route and compare shell coordinates.

## Reject

- Route-specific forks of sidebar, profile links, contact links, email, or theme control.
- A second navigation system, breadcrumb, Index, Back, or repeated footer email.
- Independent nudges that align one route while moving another.
- Width or order changes used to solve spacing or typography problems.
- Frameworks, routers, or new build systems.

## Verify

Run the build, repository verifier, and `git diff --check`. At desktop and `390px`, verify all routes have identical name coordinates, shared links, no overflow, the article before shared mobile navigation, and the theme control in its documented column. Tab order must match visual order.

## Done

One shared shell produces identical persistent navigation and correct reading geometry on every route without unrelated changes.
