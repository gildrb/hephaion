# Typography And Spacing

## Type

- Shell location: `19px`, weight `400`.
- Default interface and prose: `16px/24px`, weight `400`.
- Homepage project date, title, and arrow: `16px/24px`, weight `400`.
- Homepage group label: `.section-title` in `--text-secondary`.
- Case title desktop: `28px/36px`, weight `500`.
- Case title mobile: `24px/32px`, weight `500`.
- Case-study section heading: `19px/28px`, weight `500`. Write it as `###` in case-study Markdown; do not use `##` section wrappers.
- Caption and metadata: `14px/20px`, weight `400`.
- Case-specific letter spacing: `0`.
- No fluid case typography.
- On desktop, align the case title's top edge exactly with the top edge of the persistent `Gil Rodrigues` location. Keep the title's top margin at `0`.

## Rhythm

Use `4`, `6`, `8`, `12`, `16`, `20`, `24`, `28`, `32`, `48`, `64`, `80`, and `120` pixel steps according to `../../../design.md`. Reuse homepage constants before adding a value.

- The homepage biography uses `margin-bottom: var(--text-media-gap)` (`32px`) before the first project group.
- Group labels use `margin-bottom: var(--section-content-gap)` (`6px`).
- Every `.portfolio-card-link`, including the first in each group, uses symmetric `padding: 8px 0`.
- Therefore the group-label-to-first-entry optical gap is `--section-content-gap` plus the row's intrinsic `8px` top padding. Do not zero the first row's padding.
- Adjacent rows retain their `8px` padding and faint top separators; the Engineering-to-Design group gap is `28px`.
- Metadata is bottom-aligned on desktop with `.references-links { margin-top: auto; }`; mobile preserves `display: contents`.
- Keep every case article in natural block flow. Do not use article `min-height`, flex distribution, `margin-top: auto`, or last-child `padding-top` to force its ending downward.
- On desktop, the last article child receives only the bottom padding derived from the shared footer and theme-toggle tokens. This is a maximum endpoint for a long post: its final authored line must not finish below the theme control when the reader reaches the page bottom. It is not a target baseline, and short posts must never be stretched to reach it.
- Use `--text-media-gap: 32px` exactly once at each prose-to-media and media-to-prose boundary. Do not combine a media margin with padding on the preceding or following copy block; that double-counts the rhythm.
