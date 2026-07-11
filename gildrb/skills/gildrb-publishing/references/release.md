# Release

- Do not merge a draft without explicit approval.
- Do not deploy or promote with `--prod` without explicit approval.
- Re-run build, verifier, browser checks, and route checks before release.
- Preserve permanent redirects for changed public routes.
- Record the preview commit before promotion.
- Prefer promoting the verified artifact over rebuilding when the platform supports it.
- Confirm production routes and error logs after release.
