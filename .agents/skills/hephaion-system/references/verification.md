# Hephaion System Verification

Use these checks when changing root guidance, product package routing, or reusable skills.

## Text Checks

Search for and remove:

- outside provenance statements
- fixed repository owner/name strings
- local machine paths
- clone URLs in guidance files
- unnecessary quality-label wording
- product-specific command rules in root files

## Structure Checks

Verify:

- root `AGENTS.md` routes to product folders
- each product folder has `AGENTS.md` and `README.md`
- every `SKILL.md` has front matter
- relative reference paths resolve
- product-specific skills live under the product folder
- old product-specific top-level skill paths were removed or redirected deliberately

## Review Checks

Reject changes that:

- duplicate a product rule in root guidance
- require a fixed repository owner to work
- mention a local development path that is not a product runtime contract
- hide a product-specific migration in universal wording
- add a new product package without routing guidance
