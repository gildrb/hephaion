# Case Study

## Source

```text
content/<project>.md
  -> scripts/render-case-markdown.mjs
  -> <!-- @case-markdown:<project> --> in src/<project>.template.html
  -> scripts/build-page.mjs
  -> <project>/index.html
```

Edit visible writing only in `content/<project>.md`. Templates own chrome; `src/case-media/<project>/` owns responsive media HTML; generated route HTML is output.

## Navigation

- Reuse the homepage shell.
- Keep the persistent location at the homepage name coordinate.
- Link `Gil Rodrigues` home and the current project to `#top`; no other location text navigates away.
- Render arrow and project at the same inherited size.
- Remove Index links and tiny project kickers.

## Narrative

The user owns every title, deck, caption, metadata description, and body paragraph. Do not draft or alter publishable prose unless the user explicitly requests copy work. Layout, image, route, metadata, or generation tasks never imply permission to edit copy.

- Preserve existing and supplied wording verbatim.
- When the user requests media descriptions, keep captions concise and evidence-specific. Approved captions remain verbatim and have no hard word-count limit.
- Use visibly unfinished `[Author: ...]` placeholders for missing sections.
- Keep requested suggestions outside source files until the user approves them.
- Treat spelling, grammar, tone, and clarity changes as copy work requiring explicit authorization.

When evidence exists:

1. State the visual or product problem.
2. Name constraints and objectives.
3. Show exploration before resolution.
4. Explain rejected directions.
5. Explain typography, color, geometry, visual language, and implementation.
6. End with tradeoffs and next improvements.

## Evidence

- Use original artifacts.
- Explain why each artifact matters.
- Never crop process evidence.
- Never invent research, metrics, authorship, or outcomes.
- Use code only when it demonstrates implementation responsibility.

## View next

`scripts/build-page.mjs` generates every other configured project once, in homepage order, and excludes the current slug.

```text
scripts/site-config.mjs:siteConfig.caseStudies
  - current slug
  -> <nav class="case-next">
  -> <div class="case-next-list">
  -> Date / Project / Scope / View → rows
```

The table uses the same `--portfolio-table-columns` contract as the homepage. Widths derive from visible rows, so `/site` uses Ben Davis as its widest Project while other tables containing `gildrb.com` use that value.

Desktop footer source:

```css
/* src/styles/50-case-study.css */
@media (min-width: 769px) {
  .case-next {
    margin-top: auto;
    padding-top: 48px;
    padding-bottom: calc(
      var(--footer-title-center-offset) +
      (var(--theme-toggle-size) / 2) -
      (24px / 2)
    );
  }
}
```

- Authored article content remains natural.
- Spare desktop height belongs only before `.case-next`.
- The `48px` top padding preserves the article-to-table boundary when auto margin collapses to zero on long pages.
- The final row line box directly centers with the visible theme icon. Do not subtract the retired `4px` footer-title optical offset.
- Test every case at `1440×900` and `1440×2000`; include `/ml7` with no scroll and scroll long pages to their true bottom.
- Mobile restores `margin-top: 48px`, uses `7px` row padding, proportional years, and the shared `10px` Date/Project trailing reserve.

## Structure

Follow `../../../case-studies.md`. Do not copy project-specific claims between case studies.

- Keep the template limited to its `<!-- @case-markdown:<project> -->` token and structural shell.
- Put exactly one `<!-- @case-next -->` token after the article and inside the same content column. The builder replaces it with the homepage project table excluding the current project; every other row is a generated route anchor. Do not put suggestion markup in Markdown or templates.
- Use `![Caption](media:<media-id>)` for existing responsive media; the matching HTML partial owns technical image attributes. Adjacent references form the two-column grid, so a blank line between them is meaningful.
- Adding a case study means: `content/<project>.md`, `src/<project>.template.html`, `src/case-media/<project>/`, a `scripts/site-config.mjs` entry, a homepage row in date order, every metadata mirror, extended verifiers, and rebuilt generated output.
- Run the build and verifier after every Markdown edit.
