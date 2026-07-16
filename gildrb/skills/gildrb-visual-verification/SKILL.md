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

- Homepage plus every changed case route.
- Desktop `1440px` wide and mobile `390px` wide; include `320px` for homepage-table changes and add the reported viewport when different.
- Dark and light themes for color or focus changes.
- Mouse and keyboard for interactive changes; touch emulation when hover behavior is involved.
- Fresh navigation and back/forward for navigation-state changes.

## Procedure

1. Record repository status and the exact commit/worktree under test.
2. Run `node scripts/build-page.mjs`, `node scripts/verify-page.mjs`, and `git diff --check`.
3. Start the static site locally from the built repository.
4. Open each matrix route and verify no console/page errors.
5. Measure the exact reported boundary or computed property; record selector, viewport, theme, and value.
6. Check horizontal overflow, image natural/displayed ratio, selected responsive source, heading structure, focus order, and interaction result when relevant.
7. Compare against the atomic skill's fixed contract, not visual intuition.
8. Report each failure under exactly one owner: spacing, typography, color audit, shell layout, media, interaction, or accessibility.

## Reject

- “Looks right” without a measurement for measurable claims.
- One-viewport or one-theme approval for a responsive/theme change.
- Approval with console errors, stale generated output, overflow, crop, or broken focus.
- Editing source while acting under this skill.

## Verify

Perform every applicable spot check below and record the measured result.

### Mandatory Spot Checks

- Name and case-title top alignment on desktop: both top edges resolve to `48px`, from the shared `.content` padding in `10-base.css`; mobile `.content` padding resolves to `0px`.
- Homepage header/row column alignment, contiguous row rhythm, and no overflow at `320px` and `390px`.
- Short case natural flow and long case ending at or above the desktop theme control.
- Full-frame media, no overflow, correct responsive source.
- Shared profile/contact content on all routes.
- Heph demo is absent from the homepage, appears once on `/heph`, accepts a question, and returns a cited answer.
- Keyboard focus is complete, ordered, visible, and unclipped.
- Selection, rest, hover, and focus colors are correct in both themes.

## Done

Return the tested commit, matrix, exact measurements, interaction results, console status, and a clear pass/fail. A failure names one owning skill and includes enough evidence for that skill to reproduce it.
