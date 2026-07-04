---
name: hephaion-system
description: Use for root routing, product packages, rule authoring, shared guidance, hardening, or verification rules that apply across product folders.
---

# System

Use this skill when the task changes root rules instead of one product's commands or UI.

## Stance

Maintain product package rules.

- Keep the root small.
- Route product work into product folders.
- Prefer source discovery over fixed repository ownership assumptions.
- Avoid duplicating product rules in root guidance.
- Make root rules useful for future products.

## Workflow

1. Inspect root `AGENTS.md`, `README.md`, and product folders.
2. Decide whether the change is root-wide or product-specific.
3. If product-specific, edit only the product package unless root routing must change.
4. If root-wide, update shared guidance and check for product leakage.
5. Check relative links and skill paths.

## References

- `references/routing.md`: product routing and structure.
- `references/rule-authoring.md`: durable agent rules.
- `references/verification.md`: root and product package checks.

## Done

- Root files route to product packages.
- Product assumptions stay inside product folders.
- No brittle owner, machine, or provenance language remains.
- New or changed package paths resolve.
