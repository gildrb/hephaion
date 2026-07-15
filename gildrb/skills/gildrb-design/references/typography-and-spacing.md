# Typography And Spacing

## Type

- Shell location: `19px`, weight `400`.
- Default interface and prose: `16px/24px`, weight `400`.
- Case title desktop: `28px/36px`, weight `500`.
- Case title mobile: `24px/32px`, weight `500`.
- Case-study section heading: `19px/28px`, weight `500`. Write it as `###` in case-study Markdown; do not use `##` section wrappers.
- Case-code `pre` uses pure `"Geist Mono", monospace`; wrap arrow glyphs in an explicit `.case-code-arrow` span using `"Inter", sans-serif` so they match the breadcrumb and card arrows.
- Caption and metadata: `14px/20px`, weight `400`.
- Homepage project title: `16px/24px`, weight `400`.
- Homepage project date: `14px/20px`, weight `400`.
- Case-specific letter spacing: `0`.
- No fluid case typography.
- No negative case letter spacing.
- On desktop, align the case title's top edge exactly with the top edge of the persistent `Gil Rodrigues` location. Keep the title's top margin at `0`.

## Rhythm

Use `4`, `8`, `12`, `16`, `20`, `24`, `32`, `48`, `64`, `80`, and `120` pixel steps according to `../../../design.md`. Reuse homepage constants before adding a value.

- Use the optically compensated `32px` gap between every adjacent homepage project entry at every viewport.
- Use `32px` between the final project title and `Metadata`; do not use a negative footer offset.
- Keep the sidebar group gap at `24px`; text-to-text and text-to-media boundaries require different numerical gaps to look equal.
- Omit the visible `Portfolio` label. Keep adjacent homepage text groups at `24px` on mobile, use `32px` from the biography to the first project title on desktop, and always use `32px` from that title to its solid media.
- Keep `80px` for major case-study sections, not homepage project transitions.
- Keep every case article in natural block flow. Do not use article `min-height`, flex distribution, `margin-top: auto`, or last-child `padding-top` to force its ending downward.
- On desktop, the last article child receives only the bottom padding derived from the shared footer and theme-toggle tokens. This is a maximum endpoint for a long post: its final authored line must not finish below the theme control when the reader reaches the page bottom. It is not a target baseline, and short posts must never be stretched to reach it.
- Use `--text-media-gap: 32px` exactly once at each prose-to-media and media-to-prose boundary. Do not combine a media margin with padding on the preceding or following copy block; that double-counts the rhythm.
