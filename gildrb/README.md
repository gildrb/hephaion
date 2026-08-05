# gildrb

Agent documentation for the gildrb portfolio. One package, atomic skills, executable drift checks.

## Use

```sh
export HEPHAION_REPO="${HEPHAION_REPO:-$HOME/Documents/Repos/hephaion}"
export PORTFOLIO_REPO="${PORTFOLIO_REPO:-$HOME/Documents/Repos/web}"

cd "$PORTFOLIO_REPO"
git status --short
npm run build
npm run verify

cd "$HEPHAION_REPO"
python3 gildrb/scripts/check_design_docs.py \
  --portfolio-repo "$PORTFOLIO_REPO"
```

Read `gildrb/AGENTS.md` first. Load only the atomic skills that own the failure. The rendered, approved portfolio and its source outrank this package; update both checker and docs when a reusable contract changes.

## Commands

| Command | Purpose |
| --- | --- |
| `npm run build` | Generate every HTML route, verify agent discovery, and recreate `public/` |
| `npm run verify` | Verify generated pages, assets, routing, interaction, and public agent contracts |
| `node scripts/check-public.mjs` | Reject unsafe public output |
| `npx wrangler pages dev public` | Serve the built Pages artifact with Functions locally |
| `python3 gildrb/scripts/check_design_docs.py --portfolio-repo "$PORTFOLIO_REPO"` | Check this package and live source for drift |
| `git diff --check` | Reject whitespace errors |

## Files

```text
gildrb/
  AGENTS.md               the agent router: setup, sources, checks, hard boundaries
  README.md               this entry point: commands, paths, build, routes, release
  design.md               visible and interaction contracts
  case-studies.md         project registry, authoring, generation, and evidence
  platform.md             Cloudflare runtime, discovery, redirects, and production
  scripts/
    check_design_docs.py  package checks + portfolio-source drift checks
  skills/
    gildrb-portfolio/     homepage, cases, routes, generated mirrors
    gildrb-spacing/       margins, padding, gaps, measured optical relationships
    gildrb-typography/    font families and metrics; proportional dates
    gildrb-color-audit/   semantic colors, themes, SVG contrast
    gildrb-shell-layout/  shared columns, ordering, sticky shell, footer geometry
    gildrb-media/         full-frame responsive evidence
    gildrb-interaction/   sorting, active feedback, theme, Contact alignment
    gildrb-motion/        complete motion inventory and exact timing
    gildrb-accessibility/ semantics, keyboard, focus, names, announcements
    gildrb-visual-verification/
                          browser measurement and acceptance evidence
    gildrb-publishing/    Git-backed Pages release, propagation, rollback
```

Each atomic skill owns one failure class. Its `SKILL.md` contains `Mission`, `Owns`, `Excludes`, a deterministic contract, `Procedure`, `Reject`, `Verify`, and `Done`. Detailed examples stay in that skill's `references/`.

## Portfolio files

```text
$PORTFOLIO_REPO/
  content/<project>.md                 user-owned case-study prose
  src/page.template.html               homepage document source
  src/<project>.template.html          case route chrome
  src/all.template.html                continuous case route
  src/sections/                        authored homepage rows and biography
  src/partials/                        shared sidebar, theme, media, demo
  src/case-media/<project>/             responsive case evidence markup
  src/styles/10-base.css               tokens, shell, global active feedback
  src/styles/15-homepage-entry.css     desktop/mobile entry choreography
  src/styles/20-portfolio-media.css    homepage table and sort controls
  src/styles/40-preview-content.css    shared preview/SVG theme behavior
  src/styles/50-case-study.css         case content and View-next table
  src/styles/90-responsive.css         responsive shell and mobile Contact grid
  src/scripts/10-core.js               dates, Contact alignment, scroll lifecycle
  src/scripts/15-portfolio-sort.js     stable-slot homepage sorting
  scripts/site-config.mjs              canonical routes and bundle order
  scripts/build-page.mjs               static generator
  scripts/verify-page.mjs              generated-page regression contract
  scripts/verify-agent-readiness.mjs   discovery/API contract
  scripts/prepare-cloudflare-output.mjs
                                        allowlisted `public/` artifact owner
  _headers                             response headers and media types
  _redirects                           path migrations
  _routes.json                         Pages Functions invocation boundary
  functions/                           bounded Pages runtime
```

## Build

```text
content/*.md + src/*.template.html + src/sections/ + src/partials/
                              |
                              v
                  scripts/build-page.mjs
                              |
                              +--> index.html
                              +--> <project>/index.html
                              +--> all/index.html
                              +--> Markdown/LLM/profile/feed/sitemap mirrors
                              |
                              v
            scripts/verify-agent-readiness.mjs
                              |
                              v
          scripts/prepare-cloudflare-output.mjs
                              |
                              v
                           public/
```

The exact build command is:

```sh
npm run build
# node scripts/build-page.mjs \
# && node scripts/verify-agent-readiness.mjs \
# && node scripts/prepare-cloudflare-output.mjs
```

Never edit generated route HTML as the source of a change. Edit Markdown, templates, sections, partials, CSS, scripts, or `site-config.mjs`; rebuild; then verify generated equality.

## Routes and redirects

```text
scripts/site-config.mjs
  siteConfig.caseStudies[]
      -> scripts/build-page.mjs
      -> /<slug>/index.html
      -> sitemap.xml + feed.xml + profile graph + Markdown mirrors

src/all.template.html + src/scripts/60-all-sort.js
      -> /all/index.html

_routes.json
      -> only listed HTML/API/MCP paths invoke functions/[[path]].js or API code
      -> static fonts, images, and discovery files bypass Functions

_redirects
      -> old public paths redirect to canonical static routes
      -> /index/filen and /index/filen/ redirect to /filen with 301

Cloudflare zone redirect
      -> https://www.gildrb.com/* redirects to https://gildrb.com/:splat
```

Inspect the deployed redirect source directly:

```sh
sed -n '1,200p' "$PORTFOLIO_REPO/_redirects"
cat "$PORTFOLIO_REPO/_routes.json"
curl -I https://www.gildrb.com/ml7
curl -I https://gildrb.com/index/filen
```

## Production

Production is Git-backed Cloudflare Pages. Commit and push the exact approved `main` state; then require a Pages deployment whose `Source` is that commit.

```sh
cd "$PORTFOLIO_REPO"
npm run build
npm run verify
node scripts/check-public.mjs
git diff --check
git push origin main

commit="$(git rev-parse HEAD)"
npx wrangler pages deployment list --project-name web
# Require Source == ${commit:0:7}, then verify https://gildrb.com.
```

A Direct Upload is an explicit exception, not the normal release path. It does not update Git and must never leave production ahead of `origin/main`.

## Agent contract

This is the complete integration sequence for portfolio work:

```markdown
### Before editing

1. Run `git status --short` in both repositories.
2. Read `gildrb/AGENTS.md`.
3. Read live portfolio source before Hephaion prose.
4. Load only the atomic skills that own the failure.

### While editing

1. Change canonical source, never generated HTML alone.
2. Preserve user-owned case copy unless explicitly authorized.
3. Measure browser geometry; do not approve by eye.
4. Update `design.md` or `platform.md`, the owning skill/reference,
   and `scripts/check_design_docs.py` with every reusable behavior.

### Before handoff

1. Build and verify the portfolio.
2. Run the Hephaion drift checker against the portfolio checkout.
3. Run desktop/mobile and reported-viewport browser checks.
4. Commit and push the exact approved state.
5. Require a Git-backed Pages deployment with the same commit source.
6. Verify the custom domain after edge propagation.
```
