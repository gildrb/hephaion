---
name: gildrb-publishing
description: Release gildrb through Git-backed Cloudflare Pages. Use for previews, production promotion, commit-to-deployment traceability, edge propagation, rollback, or exceptional Direct Upload. Do not use for interface implementation, protocol design, DNS key handling, or private material that cannot be published safely.
---

# Gildrb Publishing

## Mission

Release one verified Git commit to Cloudflare Pages without letting production and Git diverge.

## Owns

- Preview/production choice, exact commit, push, Pages source mapping, propagation, smoke tests, and rollback evidence.
- Exceptional Direct Upload safety and reconciliation.
- Preventing production from moving ahead of `origin/main`.

## Excludes

- Do not implement visual, content, API, MCP, or DNS behavior.
- Do not commit credentials, account IDs, private endpoints, DNS keys, deployment IDs, or registrar values.
- Do not upload unfinished private evidence without independently verified Access protection.

## Fixed Contract

- Normal production is Git-backed: GitHub repository `gildrb/web`, branch `main`, Pages project `web`.
- Build output is `public/`; Functions remain in repository-root `functions/`.
- Production requires explicit approval, a clean exact commit, and a Pages deployment whose `Source` matches that commit.
- Local `HEAD`, `origin/main`, GitHub `main`, and active production source must agree.
- Cloudflare can briefly serve mixed route versions after activation. Poll changed routes before declaring a defect or success.
- Direct Upload is exceptional. It does not update Git and may never leave production ahead of `origin/main`.

## Procedure

1. Inspect branch, status, upstream, current active deployment, and changed routes.
2. Run build, verification, public-safety, browser, and machine-contract checks.
3. Commit only approved scope and push exact `main`.
4. Record `git rev-parse HEAD` and `git ls-remote origin refs/heads/main`; require equality.
5. Poll `npx wrangler pages deployment list --project-name web` until Production `Source` matches the commit prefix.
6. Poll every changed route for a commit-specific fragment until edge copies converge.
7. Verify deployment URL and custom domain: HTML, Markdown, Functions, headers, redirects, 404, and changed browser behavior.
8. Keep the prior successful Pages deployment identifiable for rollback.

## References

- `references/preview.md`: Git preview and exceptional Direct Upload privacy contract.
- `references/release.md`: production push, source matching, propagation, smoke tests, rollback.

## Reject

- Deploying or pushing a dirty, unverified, or unapproved state.
- Treating `git push` completion as proof that Pages is active.
- Treating a Pages deployment as valid when its Source does not match GitHub `main`.
- Direct Upload that creates production code absent from GitHub.
- Publishing private material to a public preview.
- Declaring production from the hash URL without custom-domain verification.

## Verify

Run `../../platform.md` checks. Record exact commit, GitHub equality, Pages source, changed-route propagation, custom-domain browser/HTTP matrix, console status, and rollback target.

## Done

The approved commit is pushed, active production reports that source, every changed route has converged, the custom domain passes, the worktree is clean, and rollback remains available.
