---
name: gildrb-publishing
description: Use for gildrb private preview branches, protected Vercel deployments, draft pull requests, release validation, merge decisions, production promotion, or rollback safety.
---

# Publishing

Keep unfinished portfolio work private and production unchanged.

## Workflow

1. Inspect branch, worktree, remote, and current deployment state.
2. Build and verify locally.
3. Keep work on a non-production branch.
4. Commit only the intended portfolio scope.
5. Push the branch and use a draft PR.
6. Wait for the Vercel preview.
7. Confirm deployment protection with an unauthenticated request.
8. Share the protected preview URL.
9. Merge or promote only after explicit user approval.

## References

- `references/preview.md`: protected preview contract.
- `references/release.md`: merge, production, and rollback gates.

## Done

- Preview is ready and protected.
- Draft PR contains the intended diff.
- Main and production remain unchanged without approval.
