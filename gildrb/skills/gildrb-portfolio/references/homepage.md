# Homepage

## Index

The homepage is a text-only index. It contains no `<img>`, showcase, gallery, or Heph demo markup. Case pages retain their media and the shared Heph demo.

The template includes, in order:

```text
portfolio-open
portfolio-engineering
portfolio-design
portfolio-close
```

The Engineering group contains newest-first:

- `This website` → `/site`
- `Heph` → `/heph`

The Design group contains newest-first:

- `Filen` → `/filen`
- `n0thing` → `/n0thing`
- `mL7` → `/ml7`

The old per-project homepage section files no longer exist. Keep the group `role="group"` and `aria-labelledby` contracts.

## Rows

Each project is a full-row `.portfolio-card-link` target containing the ISO date, plain-text title, and real arrow element:

```html
<span class="portfolio-card-arrow" aria-hidden="true">→</span>
```

The whole row is clickable. A shared subgrid aligns the date column, title column, and right-hand arrows across both groups. Dates use regular numerals and `YYYY-MM-DD` text. `This website` updates its date daily through `updatePortfolioSiteDate()` in `src/scripts/10-core.js`.

Group labels use `.section-title` in `--text-secondary` with `margin-bottom: var(--section-content-gap)`. The label-to-first-entry gap is `--section-content-gap` plus the row's intrinsic `8px` top padding. Every entry keeps symmetric `padding: 8px 0`, including the first, so its optical rhythm matches later entries and separators.

## Biography

Use exactly:

```text
Designing brands, interfaces, and the systems that connect them.
```

Keep this sentence synchronized across visible and machine-readable surfaces. The biography remains first with `margin-bottom: var(--text-media-gap)` before the first project group.

## Shell

Keep the homepage content in the shared `760px` column. The group gap is `28px`. Metadata is bottom-aligned on desktop through `.references-links { margin-top: auto; }` at `min-width: 769px`. Mobile keeps `.content { display: contents; }` and the existing ordering.
