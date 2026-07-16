---
name: gildrb-spacing
description: Enforce gildrb spacing rhythm only. Use for margins, padding, CSS gap values, section separation, optical text-to-media balance, homepage project transitions, or case-study ending whitespace. Do not use for font metrics, colors, content widths, grid ordering, media encoding, interaction logic, or copy.
---

# Gildrb Spacing

## Mission

Change or audit spatial distance without changing any other design dimension.

## Owns

- `margin`, `padding`, `gap`, `row-gap`, and `column-gap` values.
- Spacing tokens and their call sites.
- Optical compensation between text, media, captions, and following copy.
- Natural-flow ending space on case pages.

## Excludes

- Do not change font family, size, weight, line height, or letter spacing.
- Do not change colors, widths, columns, DOM order, breakpoints, image files, behavior, or prose.
- Do not use transforms or relative positioning to imitate spacing.
- If the task requires another concern, load that concern's separate skill.

## Fixed Contract

- Allowed scale: `4`, `8`, `12`, `16`, `20`, `24`, `32`, `48`, `64`, `80`, `120` pixels.
- Image-grid gap: `20px`.
- Sidebar text-to-text group gap: `24px`.
- Homepage biography to project table: `32px`.
- Project table header and rows form one contiguous block with no category or section gap.
- Project header and row block padding: `8px` vertically.
- Homepage table column gap: `16px` on desktop and `clamp(8px, 3vw, 16px)` on mobile.
- Desktop `.content` padding: `48px 0`, declared once in shared `src/styles/10-base.css` so homepage and case titles align with the sidebar name. Mobile resets it to `0` in `90-responsive.css`.
- Case section gap: `80px`.
- Prose-to-media and media-to-following-copy: `var(--text-media-gap)`, exactly `32px`, applied once per boundary.
- Case articles remain in natural block flow. Desktop bottom padding is a maximum endpoint for long posts, not a target baseline. Never use article `min-height`, flex distribution, `margin-top: auto`, or last-child top padding.

## Procedure

1. Read the rendered failing boundary and its two adjacent elements.
2. Read `src/styles/10-base.css`, the owning stylesheet, and the matching markup.
3. Identify every CSS contribution to the measured distance: margin collapse, parent gap, padding, line box, caption margin, and media wrapper.
4. Measure the current boundary in the browser. Do not infer it from one declaration.
5. Reuse an existing token. Add no value outside the fixed scale.
6. Apply the distance once at the owning boundary; remove double-counted adjacent spacing.
7. Measure desktop and mobile after rebuilding.

## Reject

- Any arbitrary pixel value.
- Any fix based only on visual guessing.
- Any equal numeric gap claimed as optically equal without rendered comparison.
- Any negative margin used to pull unrelated sections together.
- Any short post stretched toward the theme control.
- Any copy, typography, color, width, order, or behavior change in the diff.

## Verify

Run:

```sh
node scripts/build-page.mjs
node scripts/verify-page.mjs
git diff --check
```

Measure the changed boundary at desktop, `390px`, and `320px` when the homepage table is involved. Verify no overlap, no horizontal overflow, no double-applied `--text-media-gap`, and no new value outside the scale. For a short case, confirm natural flow. For a long case, confirm the final line does not finish below the desktop theme toggle.
For desktop shell alignment, confirm `.content` has `48px` top padding and the case title and `Gil Rodrigues` have the same top coordinate. At mobile width, confirm `.content` resolves to `0px` padding.

## Done

The measured boundary matches the fixed contract at both viewport classes, the diff contains only spacing changes, and repository plus Hephaion contract checks pass.
