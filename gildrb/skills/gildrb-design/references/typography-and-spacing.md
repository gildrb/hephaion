# Typography And Spacing

## Type

- Shell location: `19px`, weight `400`.
- Default interface and prose: `16px/24px`, weight `400`.
- Case title desktop: `40px/48px`, weight `600`.
- Case title mobile: `32px/40px`, weight `600`.
- Section heading: `32px/40px`, weight `600`.
- Compact heading: `20px/28px`, weight `600`.
- Caption and metadata: `14px/20px`, weight `400`.
- Homepage project title: `16px/24px`, weight `400`.
- Homepage project date: `14px/20px`, weight `400`, with Inter tabular numerals enabled through `font-variant-numeric: tabular-nums` and `font-feature-settings: "tnum" 1`.
- Case-specific letter spacing: `0`.
- No fluid case typography.
- No negative case letter spacing.

## Rhythm

Use `4`, `8`, `12`, `16`, `20`, `24`, `32`, `48`, `64`, `80`, and `120` pixel steps according to `../../../design.md`. Reuse homepage constants before adding a value.

- Use the optically compensated `32px` gap between every adjacent homepage project entry at every viewport.
- Use `32px` between the final project title and `Metadata`; do not use a negative footer offset.
- Keep the sidebar group gap at `24px`; text-to-text and text-to-media boundaries require different numerical gaps to look equal.
- Keep `80px` for major case-study sections, not homepage project transitions.
