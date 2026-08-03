# Routing

## Canonical

- Use `/<project>`.
- Generate `<project>/index.html`.
- Use one canonical URL.
- Update homepage link, canonical metadata, Open Graph, Twitter, JSON-LD, sitemap, feed, Markdown, LLM mirrors, humans file, analytics route, and structured profile graph.

## Migration

- Add a permanent redirect for a previously exposed route.
- Remove the old generated canonical page.
- Verify both slash forms when the deployment platform distinguishes them.
- Keep redirects out of visible navigation.

## Generation

- Extend the existing static builder.
- Register the case study in `scripts/site-config.mjs`; the builder generates a route for every registered slug.
- Reuse shared CSS and JavaScript. Add a route-scoped `30-<project>.css` only for rules that belong to one route, and register it in that case study's `styles` array alone.
- Keep hyphenated slugs identical across route, template, content file, media directory, row id, and mirrors.
- Keep one project template per authored case unless evidence proves a safe content abstraction.
- Do not add a client-side router.

## Case-Study Suggestions

- Include exactly one `<!-- @case-next -->` token after the article and inside the case template's content column.
- Let `scripts/build-page.mjs` replace the token with every other project in deterministic tier/date order; the first three are the no-JavaScript default. `/all` must not receive the token or block.
- Register the shared `25-case-next.js` script through `sharedCaseScripts`. It may reveal three existing build-generated anchors per visit using guarded localStorage and must never fetch or construct suggestion rows.
- Keep the suggestion targets and their date/title/scope fields derived from homepage rows rather than hand-written route metadata.
