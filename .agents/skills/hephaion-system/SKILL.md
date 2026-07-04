---
name: hephaion-system
description: Use for Hephaion root architecture, product package structure, agent routing, reusable rule authoring, cross-product guidance, repository hardening, or verification rules that apply across product folders.
---

# Hephaion System

Use this skill when the task changes the parent agent system rather than one product's commands or UI.

## Stance

Maintain an evolving product architecture.

- Keep the root small and durable.
- Route product-specific work into product folders.
- Prefer source discovery over fixed repository ownership assumptions.
- Avoid duplicating product rules in root guidance.
- Make every root rule useful for future products, not only the first product.

## Workflow

1. Inspect root `AGENTS.md`, `README.md`, and product folders.
2. Identify whether the change is root-wide or product-specific.
3. If product-specific, edit only the product package unless root routing must change.
4. If root-wide, update the reusable guidance and verify no product assumptions leaked into it.
5. Check all relative links and skill paths.

## References

- `references/routing.md`: product package routing and structure.
- `references/rule-authoring.md`: how to write durable agent rules.
- `references/verification.md`: hardening checks for root and product packages.

## Done State

- Root files route clearly to product packages.
- Product-specific assumptions stay inside product folders.
- No brittle repository-owner, local-machine, or provenance language remains.
- New or changed product package paths resolve.
