# Homepage

## Table

- Use one Date / Project / Scope / All header and one global project list.
- Keep `Date`, `Project`, and `Scope` as native sort buttons; make `All` a link to `/all` with the active sort state.
- Make each complete project row an accessible link to its case route.
- On mobile, let `.portfolio-scroll-frame` own the four table tracks and let both the header and `.portfolio-section` subgrid into it so body rows and headings share their columns. Keep the width query container on the frame.
- Measure the mobile Links/Contact second-column start from the first body-row Scope cell, then the case-page `View next` Scope cell, then the header Scope cell; store it in `--mobile-contact-start`. Keep the `3fr 4fr` fallback on routes without a table, such as `/all`.
- Keep `var(--section-gap)` between the table container and Links/Contact. The 48px case article-to-`View next` gap is separate.
- Default to newest-first: gildrb.com, T3, Ben Davis, Heph, Filen, n0thing, CURVES, then mL7.
- `portfolio-engineering.html` and `portfolio-design.html` are ordered segments of that one list, not categories. A new row goes where its date belongs.
- Hold the whole table hidden until first paint is ready, then reveal it as one staggered diagonal. See the homepage entry contract in `design.md`.
- Reveal `View →` on direct row hover and keyboard focus without layout shift.
- Do not add summaries, images, category wrappers, or a visible Portfolio heading.

## Biography

Use exactly:

```text
Brand designer based in Germany, building identity systems for software.
```

Keep this sentence synchronized across visible and machine-readable surfaces.

## Current Projects

- gildrb.com links to `/site` and uses `Design Engineering`.
- T3 links to `/t3` and uses `Logomark`.
- Ben Davis links to `/ben-davis` and uses `Logomark`.
- CURVES links to `/curves` and uses `Typeface`.
- Heph links to `/heph` and uses `Product/Design Engineering`; the repository link appears inside that article.
- Filen links to `/filen` and uses `Brand Identity`.
- n0thing links to `/n0thing` and uses `Wordmark`.
- mL7 links to `/ml7` and uses `Wordmark`.
- Do not use `/index/<project>` for canonical navigation.

## Metadata Footer

- Desktop homepage only. It lists `humans.txt`, `llms.txt`, and `source`.
- `source` points at the public site repository and opens in a new tab with `rel="noopener noreferrer"`.
