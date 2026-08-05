# Preview

## Git-backed preview

Use a named remote branch so the preview artifact has a durable Git source:

```sh
cd "$PORTFOLIO_REPO"
npm run build
npm run verify
node scripts/check-public.mjs
git diff --check

git push origin HEAD:refs/heads/<preview-branch>
commit="$(git rev-parse HEAD)"
npx wrangler pages deployment list --project-name web
# Require Branch == <preview-branch> and Source == ${commit:0:7}.
```

Do not merge or move `main`. Record the preview URL and commit.

## Exceptional Direct Upload

Use only when the user explicitly requests it and the exact commit already exists on GitHub:

```sh
npm run build
npx wrangler pages deploy public \
  --project-name web \
  --branch <preview-branch> \
  --commit-hash "$(git rev-parse HEAD)" \
  --commit-message "<message>" \
  --commit-dirty=false
```

Run from the repository root so Wrangler sees both `public/` and `functions/`. Dashboard drag-and-drop is invalid because it does not compile repository-root Functions.

## Privacy

Pages preview URLs are public unless Access is configured. Do not upload private evidence, drafts, attachments, secrets, or unfinished claims to an unprotected preview.

When protection is required:

1. Configure Cloudflare Access for preview hostnames.
2. Request HTML, one static asset, and one Function route without credentials.
3. Require Access denial or login challenge for all three.
4. Share only after every unauthenticated request fails closed.

## Acceptance

```text
commit:          exact Git SHA
branch:          preview branch
Pages Source:    same SHA prefix
preview URL:     recorded
production main: unchanged
custom domain:   unchanged
privacy:         public-safe or Access fail-closed
```

Verify homepage and changed cases at desktop/mobile widths; Functions, headers, redirects, unknown-route `404`, Markdown negotiation, and `noindex`; no production state changes.
