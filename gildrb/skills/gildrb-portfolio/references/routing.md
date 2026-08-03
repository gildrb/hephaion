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
