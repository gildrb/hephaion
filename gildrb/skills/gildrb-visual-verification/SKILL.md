---
name: gildrb-visual-verification
description: Verify a rendered gildrb visual or interaction change without editing source. Use after any spacing, typography, color, shell, media, interaction, or accessibility implementation, or when diagnosing screenshot-reported drift that requires measured desktop/mobile evidence. Do not use this skill to edit implementation; it reports pass/fail and routes failures to the owning skill.
---

# Gildrb Visual Verification

## Mission

Produce measured, reproducible acceptance evidence without changing implementation.

## Owns

- Local build/run, browser inspection, screenshots, computed-style measurements, interaction checks, and console review.
- Pass/fail reporting and identification of the single owning skill for each failure.

## Excludes

- Do not edit source, generated output, documentation, or assets.
- Do not prescribe a visual fix by guessing. Report measurements and the owning failure category.

## Required Matrix

- Homepage plus every changed case route. For shared table or case-footer rules, test all canonical cases: `/site`, `/t3`, `/ben-davis`, `/heph`, `/filen`, `/n0thing`, `/curves`, `/ml7`.
- Desktop `1440×900` and mobile `390px`; include `320px` for homepage-table changes, `1440×2000` for short-footer behavior, and the reported viewport when different.
- Dark and light themes for color or focus changes.
- Mouse and keyboard for interactive changes; touch emulation when hover behavior is involved.
- Fresh navigation and back/forward for navigation-state changes.

## Procedure

1. Record repository status and the exact commit/worktree under test.
2. Run `npm run build`, `npm run verify`, and `git diff --check`.
3. Start the static site locally from the built repository.
4. Open each matrix route and verify no console/page errors.
5. Measure the exact reported boundary or computed property; record selector, viewport, theme, browser, and value.
6. Use WebKit for reported Safari/subgrid/layout defects. Add Chromium when proportional font metrics or cross-engine intrinsic sizing can change tracks.
7. Check horizontal overflow, selected responsive source, heading/focus order, interaction result, motion frames, and console status as relevant.
8. Compare against the atomic skill's fixed contract, not intuition.
9. Route each failure to exactly one owner: spacing, typography, color audit, shell layout, media, interaction, motion, or accessibility.
## Reject

- “Looks right” without a measurement for measurable claims.
- One-viewport or one-theme approval for a responsive/theme change.
- Approval with console errors, stale generated output, overflow, crop, or broken focus.
- Editing source while acting under this skill.

## Verify

Perform every applicable spot check below and record the measured result.

### Mandatory Spot Checks

- Name and case-title top alignment on desktop: both top edges resolve to `48px`, from the shared `.content` padding in `10-base.css`; mobile `.content` padding resolves to `0px`.
- Homepage and every case table: computed Date/Project tracks derive from visible `max-content`; Scope stays flexible; mobile visible gutters match after the widest values; Contact start equals Scope start.
- Sorting: press/release is `+1px/0px`; Project and Scope coordinates remain stable after Date/Project/Scope sorts; row DOM slots are not reparented.
- Case footer: on every desktop case at `1440×900` and `1440×2000`, final row and visible theme icon centers differ by no more than `1.5px`. Include `/ml7` with `scrollY === 0`; scroll long pages to their document bottom.
- Screenshot disputes: capture one full viewport, crop the final project text and visible SVG by measured rectangles, compute luminance-weighted Y centroids, and report the pixel delta.
- Full-frame media, no overflow, correct responsive source.
- Shared profile/contact content on all routes.
- Heph demo is absent from the homepage, appears once on `/heph`, accepts a question, and returns a cited answer.
- Motion inventory matches source; changed motion has early/middle/final frames, reduced-motion evidence, and baseline metric comparison.
- Keyboard focus is complete, ordered, visible, and unclipped.
- Selection, rest, hover, and focus colors are correct in both themes.

## Done

Return the tested commit, route matrix, exact measurements, browser/runtime, screenshot or temporary-script paths, interaction results, console status, and pass/fail. A failure names one owning skill and includes enough commands and selectors to reproduce it.
