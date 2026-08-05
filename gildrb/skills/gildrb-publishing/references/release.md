# Release

## Gate

Do not change production without explicit user approval.

Require:

- intended diff committed and pushed;
- local `HEAD`, `origin/main`, and GitHub `main` equal;
- `npm run build`, `npm run verify`, public-safety, and secret scans passing;
- desktop/mobile/reduced-motion and changed-route browser checks passing;
- relevant API, MCP, discovery, DNS, redirect, and `404` checks passing.

## Push

```sh
cd "$PORTFOLIO_REPO"

git status --short --branch
npm run build
npm run verify
node scripts/check-public.mjs
git diff --check

git add <approved-paths>
git commit -m "<message>"
git push origin main

commit="$(git rev-parse HEAD)"
origin="$(git ls-remote origin refs/heads/main | cut -f1)"
test "$commit" = "$origin"
```

## Match Pages source

```sh
npx wrangler pages deployment list --project-name web
```

Wait for a Production row with:

```text
Branch: main
Source: first 7 characters of the exact commit
Deployment: recorded *.web-2qb.pages.dev URL
```

A successful push is not yet a successful release. The deployment source and custom domain must pass.

## Propagation

Cloudflare may briefly mix route versions immediately after activation. For every changed route:

```sh
for path in / /site /t3 /ben-davis /heph /filen /n0thing /curves /ml7; do
  curl -fsS -H 'Cache-Control: no-cache' "https://gildrb.com$path"
done
```

Check a source fragment unique to the commit. Wait and retry until every route is new; then launch a fresh browser context. Do not use one updated route as proof that all route copies converged.

## Smoke test

Verify the deployment URL and `https://gildrb.com`:

- homepage HTML and Markdown negotiation;
- every canonical case and `/all`;
- changed browser geometry/interactions in WebKit;
- `/api/profile`, `/api/status`, and `/mcp`;
- discovery files and exact media types;
- unknown route `404`;
- complete `www` canonical redirect;
- `/index/filen` and `/index/filen/` permanent redirects;
- approved motion/reduced-motion behavior when motion changed;
- clean console and no mixed old/new source fragments.

## Exceptional Direct Upload

Direct Upload is not the normal production path. If explicitly approved:

```sh
npm run build
npx wrangler pages deploy public \
  --project-name web \
  --branch main \
  --commit-hash "$(git rev-parse HEAD)" \
  --commit-message "<message>" \
  --commit-dirty=false
```

The exact commit must already be on GitHub. Recheck that production did not move ahead of `origin/main`.

## Rollback

- Identify the prior successful Pages deployment before release.
- Use Pages deployment history to restore the production alias when required.
- Re-run source matching, propagation polling, and the complete smoke test.
- Keep account-specific deployment identifiers out of public documentation.

## Done

```text
commit:
origin/main:
GitHub main:
Pages Source:
deployment URL:
custom-domain matrix:
propagation complete:
rollback target:
worktree clean:
```
