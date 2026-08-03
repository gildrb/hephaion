# Verification

- Run the static builder.
- Run the repository verifier.
- Check generated source equality.
- Check every referenced asset exists.
- Check canonical route count.
- Check exactly one full-width homepage row link per configured project.
- Check Date, Project, and Scope sorting across the complete list.
- Check `View →` appears without layout shift on row hover and focus.
- Check no external project link when explicitly prohibited.
- Check legacy redirects.
- Validate JSON and XML.
- Run `node scripts/verify-crawlability.mjs` against a local server that emits the Vercel headers from `vercel.json`; a plain static server omits `Content-Signal` and `Link` and fails for the wrong reason.
- Extend the project counts, chronological id order, scope counts, route markers, and media assertions in both verifiers whenever a case study is added.
- Check each theme-inverting mark under the system preference and both explicit themes, and that its class is scoped to one route.
- Render mobile and desktop.
- Click every project row.
- Click `Gil Rodrigues` and confirm `/`.
- Check browser errors.
