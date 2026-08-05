# Verification

## Commands

```sh
export HEPHAION_REPO="${HEPHAION_REPO:-$HOME/Documents/Repos/hephaion}"
export PORTFOLIO_REPO="${PORTFOLIO_REPO:-$HOME/Documents/Repos/web}"

cd "$PORTFOLIO_REPO"
npm run build
npm run verify
node scripts/check-public.mjs
git diff --check

cd "$HEPHAION_REPO"
python3 gildrb/scripts/check_design_docs.py \
  --portfolio-repo "$PORTFOLIO_REPO"
```

## Generated contract

- Generated source equals templates, Markdown, sections, partials, and bundle configuration.
- Every referenced asset exists.
- Every configured project has one homepage row, one canonical route, one Markdown source, one generated index, and synchronized public mirrors.
- `/all` contains every case once; each case View-next table contains every other project once and excludes itself.
- Legacy redirects resolve to canonical routes.
- JSON, XML, discovery documents, and route manifests parse.

## Browser matrix

```text
homepage: / at 1440px, 390px, 320px
cases:    /site /t3 /ben-davis /heph /filen /n0thing /curves /ml7
footer:   every case at 1440×900 and 1440×2000
color:    dark + explicit light + system light
engine:   WebKit first; Chromium for intrinsic font/table comparison
input:    mouse, keyboard; touch emulation for mobile hover/drag behavior
```

- Click every project row, `Gil Rodrigues`, All, theme, email, and relevant Heph controls.
- Sort Date, Project, and Scope in both directions. DOM row elements remain stable while values change; Project/Scope X coordinates do not shift.
- Hold each sort control: pressed Y delta is `+1px`; release is `0px`.
- On mobile, compare widest visible year/project gutters and require Contact X to equal Scope X.
- On every case footer, compare the final project text line-box center with the visible theme SVG center; tolerance is `1.5px`. For screenshot disputes, compare luminance-weighted rendered-pixel centroids.
- Confirm all portfolio and case-table dates resolve to `font-variant-numeric: normal`.
- Confirm every `.theme-adaptive-monochrome-artwork` instance has equivalent contrast on each standalone and aggregate route that renders it, in explicit and system themes. Ben Davis on `/ben-davis` and `/all` is the current `21:1` cross-route fixture.
- Check no horizontal overflow, console errors, crop, stale animation, broken focus, or route mismatch.

## Production

```sh
cd "$PORTFOLIO_REPO"
commit="$(git rev-parse HEAD)"
git ls-remote origin refs/heads/main
npx wrangler pages deployment list --project-name web
```

Require local `HEAD`, `origin/main`, GitHub `main`, and the active Pages deployment `Source` to identify the same commit. Then repeat changed browser and HTTP checks on `https://gildrb.com` after route-edge propagation.
