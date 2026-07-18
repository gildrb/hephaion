---
name: gildrb-typography
description: Enforce gildrb typography only. Use for Inter or Geist Mono usage, font size, weight, line height, letter spacing, heading hierarchy, caption type, or title alignment caused by text metrics. Do not use for spacing, colors, page geometry, media, interactions, accessibility semantics, or copy.
---

# Gildrb Typography

## Mission

Change or audit text metrics while preserving layout spacing, color, behavior, and wording.

## Owns

- Font family, size, weight, line height, and letter spacing.
- Heading and prose type roles.
- Font rendering declarations and self-hosted font usage.

## Excludes

- Do not change margins, padding, gaps, colors, widths, columns, ordering, assets, JavaScript, HTML semantics, or authored copy.
- A position problem caused by margins belongs to `gildrb-spacing`; shell coordinates belong to `gildrb-shell-layout`.

## Fixed Contract

- Family: self-hosted Inter Variable with existing system fallbacks.
- Case-study Markdown uses compact `###` headings at `19px/28px`; do not introduce `##` section wrappers.
- Case-code `pre` uses pure `"Geist Mono", monospace`. Arrow glyphs use an explicit `.case-code-arrow` span with `"Inter", sans-serif` so they match navigation arrows.
- Shell location: `19px`, weight `400`.
- Default interface and prose: `16px/24px`, weight `400`.
- Homepage table remains Inter `16px/24px`, weight `400`, on mobile; long Field values truncate inside the flexible track rather than shrinking the type.
- Desktop case title: `28px/36px`, weight `500`.
- Mobile case title: `24px/32px`, weight `500`.
- Section heading: `24px/32px`, weight `500`.
- Compact heading: `19px/28px`, weight `500`.
- Caption and metadata: `14px/20px`, weight `400`.
- Case code: `14px/20px`, weight `400`.
- Case-title letter spacing: `-0.02em`; other case-study text: `0`.
- Never use weights below `400`, fluid case type, `clamp()`, negative letter spacing outside the case-title role, or invented intermediate sizes.
- Never change font weight between rest, hover, focus, active, or selected states.
- On desktop, the title's top edge aligns with the top edge of `Gil Rodrigues`; the title margin remains `0` and neither column is independently nudged.

## Procedure

1. Read the rendered text and its computed font properties.
2. Read `src/styles/10-base.css`, `src/styles/50-case-study.css`, `src/styles/90-responsive.css`, and the owning markup.
3. Assign the element to exactly one documented type role.
4. Change only the declarations owned by this skill.
5. Rebuild and inspect computed style at desktop and `390px`; include `320px` for homepage-table type.
6. Compare line wrapping before and after; ensure the new role does not create overflow.

## Reject

- Any undocumented type step.
- Any viewport-scaled case heading.
- Any typography change used to repair spacing or width.
- Any copy edit, including punctuation or capitalization.
- Any state-dependent weight change.

## Verify

Run the build, repository verifier, and `git diff --check`. In the browser verify computed family, size, weight, line height, and letter spacing at desktop and mobile. Confirm one semantic page heading, stable wrapping, no overflow, and exact desktop title/name top alignment.

## Done

Every changed text element maps to one fixed role, all computed metrics match that role, and the diff contains no unrelated design or copy changes.
