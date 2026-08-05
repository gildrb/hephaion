# Homepage

## Source

```text
src/page.template.html
  -> src/sections/profile-summary.html
  -> src/sections/portfolio-open.html
  -> src/sections/portfolio-engineering.html
  -> src/sections/portfolio-design.html
  -> scripts/build-page.mjs
  -> index.html
```

## Table

- Use one Date / Project / Scope / All header and one global project list.
- Keep `Date`, `Project`, and `Scope` as native sort buttons. `All` links to `/all` with active `sort` and `direction` parameters.
- Make each complete project row an accessible case-route link.
- Default newest-first: gildrb.com, T3, Ben Davis, Heph, Filen, n0thing, CURVES, then mL7.
- `portfolio-engineering.html` and `portfolio-design.html` are ordered source segments of that one list, not visible categories. Insert a new row where its date belongs.
- Reveal `View →` on direct row hover and keyboard focus without weight or layout change.
- Do not add summaries, images, category wrappers, or a visible Portfolio heading.

The shared track source is:

```css
/* src/styles/10-base.css */
--portfolio-arrow-column: 19px;
--portfolio-table-gap: 16px;
--portfolio-mobile-table-gap: clamp(8px, 3vw, 16px);
--portfolio-mobile-cell-end-space: 10px;
--portfolio-table-columns:
  max-content max-content minmax(0, 1fr)
  minmax(var(--portfolio-arrow-column), max-content);
--portfolio-mobile-table-columns: var(--portfolio-table-columns);
```

- Date and Project widths come from the longest value visible in that table.
- Dates use proportional Inter figures; never add `tabular-nums`.
- Mobile Date and Project cells each add `10px` inline-end space. Measure visible Date → Project and Project → Scope gutters; do not assume equal CSS gaps imply equal whitespace.
- Scope truncates in the flexible track. The arrow track keeps its `19px` minimum.
- Header labels contain a literal non-breaking space before the indicator. Preserve Project `translateX(2.3px)` and Scope `translateX(1.3px)` optical offsets.
- On mobile, `.portfolio-scroll-frame` owns these tracks and its inline-size container; the header and `.portfolio-section` subgrid into it.

## Mobile scrolling

The mobile homepage locks document overflow to the dynamic viewport. Project rows are the only scrolling region; the filter row and shared name/theme row stay fixed. Preserve automatic table overscroll, hidden scrollbars, and conditional top/bottom edge fades from `updatePortfolioScrollIndicators()`. Links and Contact remain below the dynamically sized table region; document pull-to-refresh is intentionally unavailable.

## Sorting

```text
src/scripts/15-portfolio-sort.js
  rows  = current `.portfolio-card-link` elements
  slots = stable copy of those same elements
  sort rows by requested value
  serialize href/date/IDs/title/scope
  copy serialized values into slots
```

Do not append or reparent sorted row nodes. WebKit can temporarily detach reordered rows from nested `subgrid`, shifting Project and Scope. Before the first value update, set `document.documentElement.dataset.homepageEntryComplete = "true"` so stagger selectors stop owning sorted rows.

All ordinary controls, including sort headings, use the shared pressed state:

```css
:is(/* interactive elements */):active {
  position: relative;
  top: 1px;
}
```

Press must measure `+1px`; release must measure `0px`. The Heph close control is the only exclusion.

## Biography

Use exactly:

```text
Brand designer based in Germany, building identity systems for software.
```

Keep this sentence synchronized across visible and machine-readable surfaces.

## Current projects

| Project | Route | Scope |
| --- | --- | --- |
| gildrb.com | `/site` | `Design Engineering` |
| T3 | `/t3` | `Logomark` |
| Ben Davis | `/ben-davis` | `Logomark` |
| Heph | `/heph` | `Product/Design Engineering` |
| Filen | `/filen` | `Brand Identity` |
| n0thing | `/n0thing` | `Wordmark` |
| CURVES | `/curves` | `Typeface` |
| mL7 | `/ml7` | `Wordmark` |

The Heph repository link appears inside its article. Do not use `/index/<project>` for canonical navigation.

## Metadata footer

Desktop homepage only. List `humans.txt`, `llms.txt`, and the public `source` repository. Open `source` in a new tab with `rel="noopener noreferrer"`. Do not render this footer on mobile, case routes, or `/all`.

## Mobile Links and Contact

```text
src/scripts/10-core.js:updateMobileLinksLayout
  `.portfolio-card-scope` or `.case-next-scope`
      minus active `.links` left edge
      -> `--mobile-contact-start`
      -> `.links.mobile-links-grid` first track
```

Contact must start at the rendered Scope coordinate on every page. `/site` omits its own `gildrb.com` suggestion, so Ben Davis becomes its widest visible project and the Contact start changes with that narrower table. Preserve `var(--section-gap)`, currently `24px`, between the mobile table and Links/Contact.

## Motion

Keep identity and biography immediate. Load `../../gildrb-motion/SKILL.md` and `../../gildrb-motion/references/gildrb-entry.md`. Desktop timings remain unchanged. Mobile Links and Contact are side by side, so equal visual rows share delay values. Sorting must not replay entry motion.
