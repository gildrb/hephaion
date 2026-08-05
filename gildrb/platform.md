# Platform

Cloudflare Pages runtime and release contract for `gildrb.com`. Static first, bounded Functions, Git-backed production.

## Authority

1. Explicit user instruction.
2. Validated production behavior at `https://gildrb.com`.
3. Portfolio source, generated output, and verifiers.
4. This document and product skills.

Never store deployment identifiers, account IDs, API tokens, DNS keys, registrar values, or private endpoints here.

## Commands

| Command | Purpose |
| --- | --- |
| `npm run build` | Generate routes and recreate the allowlisted `public/` artifact |
| `npm run verify` | Verify page and agent-readiness contracts |
| `node scripts/check-public.mjs` | Reject unsafe public content |
| `npx wrangler pages dev public` | Serve `public/` with repository-root Functions |
| `npx wrangler pages deployment list --project-name web` | Map Pages deployments to Git source commits |

## Runtime files

```text
$PORTFOLIO_REPO/
  package.json
    build -> build-page + agent-readiness + prepare-cloudflare-output
  public/                    generated upload directory; never hand-edit
  functions/                 Pages Functions source, kept outside public/
  _headers                   headers, media types, cache, CORS, Content-Signal
  _redirects                 path migrations copied into public/
  _routes.json               narrow Functions invocation boundary
  scripts/prepare-cloudflare-output.mjs
                             deletes/recreates public/ from an allowlist
```

`public/` contains static routes, images, fonts, discovery documents, `_headers`, `_redirects`, and `_routes.json`. `functions/` remains at repository root for Pages to compile. No public runtime secret or environment variable is required.

## Build

```text
scripts/build-page.mjs
        -> generated HTML + Markdown/LLM/profile/feed/sitemap artifacts
        -> scripts/verify-agent-readiness.mjs
        -> scripts/prepare-cloudflare-output.mjs
        -> public/
```

```sh
cd "$PORTFOLIO_REPO"
npm run build
npm run verify
node scripts/check-public.mjs
git diff --check
```

`scripts/prepare-cloudflare-output.mjs` deletes and recreates `public/`, copies only its explicit `publishedEntries`, limits the uncompressed homepage to `128 KiB`, and rejects superseded first-paint gates. Public authored case Markdown under `content/`, generated mirrors, and API/auth documentation are intentionally allowlisted. Non-allowlisted source, package files, private material, and operational repository documentation must not leak into Pages output.

## Function boundary

```text
_routes.json include
  / /all /site /t3 /ben-davis /heph /filen /n0thing /curves /ml7
  /api/profile /api/status
  /mcp /mcp/server-card

functions/[[path]].js
  canonical HTML routes + Accept: text/markdown negotiation

functions/api/status.js
  uncached public status

functions/mcp.js
  bounded read-only MCP JSON-RPC

all other static assets
  bypass Functions
```

The MCP endpoint accepts `POST` and `OPTIONS`, caps declared bodies at `65,536` bytes, supports `initialize`, `ping`, `tools/list`, and `tools/call`, and exposes only `list_portfolio_pages` plus `get_portfolio_page`. It reads fixed authored slugs and performs no arbitrary filesystem or network access.

WebMCP registers equivalent read-only browser tools through supported `modelContext` APIs. Unsupported browsers retain the complete website.

## Redirects

Source: `$PORTFOLIO_REPO/_redirects`.

```text
https://www.gildrb.com/* https://gildrb.com/:splat 301
/gil /
/gil/ /
/gildrb /
/gildrb/ /
/gildrb.html /
/gil-rodrigues /
/gil-rodrigues/ /
/gil-rodrigues.html /
/gil-rodrigues-barbosa /
/gil-rodrigues-barbosa/ /
/gil-rodrigues-barbosa.html /
/gil-domingos-rodrigues-barbosa /
/gil-domingos-rodrigues-barbosa/ /
/gil-domingos-rodrigues-barbosa.html /
/work /
/work/ /
/work.html /
/index/filen /filen 301
/index/filen/ /filen 301
```

The Cloudflare zone Single Redirect is the operational owner of complete `www.gildrb.com` → `gildrb.com` canonicalization. `_redirects` remains the deployed path-migration source and preserves the compatibility domain rule. Do not create a second canonical page at an old path.

Verify:

```sh
curl -I https://www.gildrb.com/ml7
curl -I https://gildrb.com/index/filen
curl -I https://gildrb.com/index/filen/
curl -I https://gildrb.com/unknown-route
```

## Headers and discovery

Publish and verify:

| Contract | Route |
| --- | --- |
| API Linkset catalog | `/.well-known/api-catalog` |
| AI catalog | `/.well-known/ai-catalog.json` |
| MCP Server Card | `/.well-known/mcp/server-card.json` |
| Agent Skills index | `/.well-known/agent-skills/index.json` |
| Portfolio discovery skill | `/.well-known/agent-skills/portfolio-discovery/SKILL.md` |
| OpenAPI | `/openapi.json` |
| API documentation | `/api-docs.md` |
| Public auth contract | `/auth.md` |
| Full public Markdown | `/llms-full.txt` |

HTML routes return authored Markdown when `Accept` contains `text/markdown`, with `Vary: Accept` and the negotiated `Content-Type`.

Public APIs and MCP tools are read-only and unauthenticated. `auth.md` states that no registration, credentials, or `Authorization` header is required. OAuth, OIDC, protected-resource, and authorization-server metadata stay absent until real protected infrastructure exists; absent routes return `404`, never homepage fallback.

## Production

Production is connected to GitHub `gildrb/web`, branch `main`. A release is one exact pushed commit and one Pages deployment whose `Source` identifies that commit.

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

npx wrangler pages deployment list --project-name web
# Require the active Production row Source to equal ${commit:0:7}.
```

Cloudflare can briefly serve mixed old/new route copies immediately after activation. Poll every changed route for a commit-specific source fragment, then run browser checks against `https://gildrb.com`. Do not diagnose an isolated old route until propagation converges.

A Direct Upload is an explicit emergency/preview exception:

```sh
npm run build
npx wrangler pages deploy public \
  --project-name web \
  --branch <explicit-branch> \
  --commit-hash "$(git rev-parse HEAD)" \
  --commit-message "<message>" \
  --commit-dirty=false
```

Direct Upload does not update Git. If used, the exact deployment source must already exist on GitHub; production may never remain ahead of `origin/main`.

## Production checks

```sh
curl -I https://gildrb.com/
curl -H 'Accept: text/markdown' -I https://gildrb.com/
curl -H 'Content-Type: application/json' \
  --data '{"jsonrpc":"2.0","id":1,"method":"ping"}' \
  https://gildrb.com/mcp
npx wrangler pages deployment list --project-name web
dig +short DS gildrb.com
dig @1.1.1.1 +dnssec _index._agents.gildrb.com HTTPS
```

Verify canonical HTML and Markdown, every case and `/all`, profile/status/MCP, discovery media types, redirect targets, unknown-route `404`, no absent OAuth fallback, DNSSEC, and Agent Ready DNS-AID.

## DNS-AID and DNSSEC

The public zone is DNSSEC-signed. The `.com` parent DS must match Cloudflare DNSKEY/RRSIG data; validating responses return `AD=true`.

Agent Ready discovers DNSSEC-validated HTTPS ServiceMode records under:

```text
_index._agents.gildrb.com
_a2a._agents.gildrb.com
_mcp._agents.gildrb.com
```

DNS-AID is transport discovery, not proof that every protocol label has an implemented endpoint. Never invent or hand-edit Cloudflare-generated DS values.
