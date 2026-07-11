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
- Reuse shared CSS and JavaScript.
- Keep one project template per authored case unless evidence proves a safe content abstraction.
- Do not add a client-side router.
