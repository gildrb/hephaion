# Routing

## Canonical source

```text
scripts/site-config.mjs
  siteConfig.caseStudies[]
      -> scripts/build-page.mjs
      -> content/<slug>.md
      -> src/<slug>.template.html
      -> <slug>/index.html
      -> sitemap.xml
      -> feed.xml
      -> src/data/profile.json graph
      -> Markdown + LLM mirrors
```

- Use `/<project>` as the public URL and `<project>/index.html` as static output. Preserve a hyphenated slug unchanged across registry, route, template, content file, media directory, row ID, and mirrors.
- Keep one canonical URL.
- Update homepage row, metadata, sitemap, feed, mirrors, profile graph, and verifier together.
- `/all/index.html` comes from `src/all.template.html`, generated cases, and `src/scripts/60-all-sort.js`.
- Do not add a client-side router.

## Functions

```text
_routes.json include
  -> canonical HTML/API/MCP routes invoke Pages Functions
  -> static assets bypass Functions

functions/[[path]].js
  -> HTML by default
  -> authored Markdown when Accept includes text/markdown
  -> Vary: Accept
```

## Redirects

Source: `_redirects`.

```text
https://www.gildrb.com/* https://gildrb.com/:splat 301
/index/filen /filen 301
/index/filen/ /filen 301
```

The source also maps legacy Gil/work aliases to `/`. Keep complete `www` canonicalization in the Cloudflare zone redirect, preserve the deployed compatibility line, remove old canonical output, and never expose redirect aliases in navigation.

Verify:

```sh
sed -n '1,200p' "$PORTFOLIO_REPO/_redirects"
cat "$PORTFOLIO_REPO/_routes.json"
curl -I https://www.gildrb.com/ml7
curl -I https://gildrb.com/index/filen
curl -I https://gildrb.com/index/filen/
```

## Generation

- Extend the existing static builder and register each case in `scripts/site-config.mjs`.
- Reuse shared CSS and JavaScript bundles. Add `30-<project>.css` only for route-owned sizing or presentation and list it only in that case's `styles` array.
- Keep one project template per authored case unless source proves a safe abstraction.
- Build and verify after registry, route, redirect, or mirror changes.

## Case suggestions

Each case template contains one `<!-- @case-next -->` token after the article and inside the content column. `scripts/build-page.mjs` replaces it with every other configured homepage project in default order, using date/title/scope values parsed from homepage rows. Exclude the current slug; never hand-write a second registry or add client JavaScript. `/all` contains no token or case-next block.
