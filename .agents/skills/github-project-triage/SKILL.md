---
name: "github-project-triage"
description: "Use whenever the user types triage or asks to triage GitHub issues, PRs, queues, CI, blockers, risk, proof, or next actions."
---

# GitHub Project Triage

Use this skill when the user types `triage`, unless the request targets a non-GitHub domain.

Triage produces maintainer-facing item cards: URL, summary, impact, author trust, fit, risk, proof state, blocker, and next action. Never return only queue numbers or opaque refs.

## Scope

- From inside a GitHub repo, triage only that repo by default.
- For broad triage, use Gil's authenticated GitHub account.
- Resolve the account with `gh api user --jq .login`.
- Resolve active repositories with `gh repo list "$(gh api user --jq .login)" --limit 200 --json nameWithOwner,isArchived,isFork,url`.
- Exclude archived repositories unless Gil asks for them.
- Exclude forks unless Gil asks for them or the fork is the current repo.
- Include other owners or organizations only when Gil names them.
- Do not infer repository ownership from names alone.

## Setup

Require `gh`.

```bash
gh --version
gh auth status
```

Use RepoBar for broad queue discovery when installed. Fall back to `gh` when it is unavailable.

```bash
repobar_cmd() {
  if command -v repobar >/dev/null 2>&1; then
    repobar "$@"
  else
    return 127
  fi
}
```

## Local Gate

Before changing or judging local work, verify the checkout:

```bash
git status --short --branch
git branch --show-current
git pull --ff-only
git status --short --branch
```

Proceed only when the branch is `main`, the pull succeeds, and the worktree is clean. If not, stop and ask Gil what to do. Do not switch branches, stash, commit, reset, restore, or clean without explicit direction.

## Current Repo

Find the current project:

```bash
repo=$(gh repo view --json nameWithOwner --jq .nameWithOwner 2>/dev/null || true)
if [ -z "$repo" ]; then
  url=$(git remote get-url origin 2>/dev/null || true)
  repo=$(printf '%s\n' "$url" |
    sed -E 's#^git@github.com:##; s#^https://github.com/##; s#\\.git$##')
fi
printf '%s\n' "$repo"
```

Start current-repo triage with:

```bash
gh issue list --repo "$repo" --state open --limit 50 \
  --json number,title,author,labels,createdAt,updatedAt,url
gh pr list --repo "$repo" --state open --limit 50 \
  --json number,title,author,isDraft,reviewDecision,mergeStateStatus,createdAt,updatedAt,url
```

If the repo has `VISION.md`, read it before judging fit. Otherwise use the fit rules below.

Before acting on any issue or PR, read all comments and treat Gil or maintainer comments as authoritative routing instructions. If no maintainer comment exists, use maintainer judgment and say that the call is yours.

Inspect enough detail to explain every surfaced item. For small queues, inspect all items. For larger queues, inspect the top priority slice and say what was not expanded.

```bash
gh issue view <n> --repo "$repo" \
  --json number,title,author,body,comments,labels,createdAt,updatedAt,url
gh pr view <n> --repo "$repo" \
  --json number,title,author,body,comments,files,commits,isDraft,reviewDecision,mergeStateStatus,statusCheckRollup,createdAt,updatedAt,url
gh pr diff <n> --repo "$repo" --patch
```

Only comment, close, merge, rerun, or patch with strong evidence and explicit permission.

## Broad Scan

Use this only when Gil asks for broad, all, everything, owned queues, or cross-repo triage.

Prefer RepoBar:

```bash
owner=$(gh api user --jq .login)
repobar_cmd repos --scope all --only-with work --owner "$owner" --sort prs --json
repobar_cmd repos --scope all --only-with work --owner "$owner" --sort issues --json
```

Fallback with `gh`:

```bash
owner=$(gh api user --jq .login)
gh repo list "$owner" --limit 200 --json nameWithOwner,isArchived,isFork,pushedAt,url \
  --jq '.[] | select((.isArchived|not) and (.isFork|not)) | .nameWithOwner'
```

Then inspect selected queues:

```bash
gh issue list --repo <owner/name> --state open --limit 50 --json number,title,author,labels,updatedAt,url
gh pr list --repo <owner/name> --state open --limit 50 --json number,title,author,isDraft,reviewDecision,mergeStateStatus,updatedAt,url
gh pr view <n> --repo <owner/name> --json number,title,state,author,isDraft,mergeStateStatus,reviewDecision,statusCheckRollup,updatedAt,url
gh pr diff <n> --repo <owner/name> --patch
gh run list --repo <owner/name> --branch <branch> --limit 10
```

Preserve PR-count order when summarizing a PR-sorted queue. Do not include a lower-PR repo while omitting a higher-PR repo from the same owner scope.

## Triage Output

For `triage`, always scan open issues and open PRs for the scoped repo set.

Return:

- `Autonomous candidates`: items that appear fixable or landable without more product input. Include URL, why it qualifies, required verification, and confidence. This is not permission to start work unless Gil also asks for autonomous execution.
- `Needs Gil`: items blocked on Gil's product decision, missing credentials/access, unavailable live-provider proof, security/privacy judgment, or authoritative maintainer direction.
- `Defer/close/supersede`: stale, duplicate, lower-quality, or overlapping items where likely action is not new code.

For every plausible autonomous candidate, use an available high-reasoning subagent, oracle, or independent review to check feasibility before presenting it when tool support exists. Give the reviewer only task-local evidence. Ask whether the item can be completed autonomously, what verification is required, and what could make it unsafe. If no such tool is available, do the same depth yourself and say so.

## Autonomous Work

When Gil says `do work autonomously`, `work you can do autonomously`, `keep going`, or similar, process eligible items sequentially until no safe autonomous item remains, each item is landed/closed/deferred with proof, or a blocker requires Gil.

Never work multiple tickets at once.

For each item:

1. Read the issue/PR, related code, docs, CI, and `VISION.md` if present.
2. Search official docs when facts may be stale or unclear.
3. Decide if it is autonomous:
   - Go: bug fixes with repro/root cause and verification path; small UI/UX tweaks; docs fixes; narrow tests/internal fixes; low-risk dependency or CI cleanup with green proof; performance improvements where design stays bounded.
   - Ask first: new features, product/vision choices, broad behavior changes, risky dependencies, security-sensitive changes without strong proof, live-provider work without usable credentials, anything that cannot be end-to-end tested.
   - Refactor when it is the cleaner bounded fix. Do not prefer a small patch that leaves worse design.
4. Implement or fix the PR in the best maintainable way. Prefer updating a writable contributor PR. Otherwise recreate locally with credit.
5. Verify locally and live end-to-end when possible.
6. For UI behavior, use the repo's expected UI proof path: screenshots, browser proof, VM proof, or the documented local equivalent.
7. For API/provider behavior, use a real usable key/account through the expected secret workflow when available.
8. If access is missing, stop before claiming completion and ask Gil for the exact access or waiver.
9. Run Codex Auto Review before commit/land unless trivial/docs-only or explicitly skipped. Address accepted findings.
10. Ensure CI is green, PR description/changelog are correct, land/close/comment with evidence, return to `main`, pull `--ff-only`, and verify a clean worktree before selecting the next item.
11. After every landed PR, post a proof comment with exact local commands, live/UI/API proof, CI state, landed commit, and caveats. If verification images apply, upload or attach them when supported; otherwise include the screenshot path or alternate proof.

Do not end autonomous mode with dirty files or an unpushed local fix unless blocked. If blocked, state the exact blocker, branch/status, proof gathered, and the next decision needed.

## Trust Signals

Include author/opener trust for every non-maintainer item recommended for action. For low-risk bot/internal items, a terse line is enough.

Prefer the bundled helper:

```bash
skills/github-project-triage/scripts/github-activity.sh --repo <owner/repo> --global <login>
```

Trust output must stay factual:

```text
Trust: @login; acct 2021-04-03; repo 2 PRs/1 issue/0 commits in 12mo; GitHub 9 PRs/3 issues/12 reviews; signal: known contributor / new drive-by / bot / unknown.
```

Do not treat trust as proof. It changes review depth, not correctness.

## Item Evaluation

Classify each item:

- `bug`: require repro, log, failing test, or current-main proof when feasible. Identify root cause before recommending fix or merge.
- `feature`: require end-to-end test plan. If live validation needs a provider key, account, device, service, model access, or paid API, state the missing access.
- `dependency`: explain package group, major/minor risk, failing checks, runtime/engine changes, and whether to split.
- `security`: raise priority, require careful code-path proof, tests, and trust/context. Do not merge on rationale alone.
- `docs/internal`: lower risk, but still explain user-visible relevance and stale/generated churn risk.

Judge:

- `Fit`: good / mixed / poor, with one reason.
- `Risk`: low / medium / high, with blast radius.
- `Proof`: current CI, local repro, failing test, live E2E, or missing proof.
- `Blocker`: first-time contributor CI approval, failing check, missing key, unclear product direction, stale branch, untrusted/broad diff, no repro, conflicts.
- `Next`: approve CI, run test, request repro, split PR, patch locally, merge after green, close with proof, or defer.

## Priority

Prioritize:

- PRs with green or nearly-green CI, recent maintainer activity, or low-risk dependency/docs/test changes.
- Repos with high open PR counts and recent activity.
- Reproducible issues, recent reports, and release blockers.
- Security, release, auth, install, CI, and data-loss reports before cosmetic items.
- Bugs with clear current-main reproduction and narrow owner path.
- Features only when live validation is possible or missing access is explicit.

Deprioritize:

- Archived repos unless Gil asked for them.
- Fork-only queues unless Gil asked for them or the fork is active work.
- Old broad feature requests with no reproduction or owner signal.
- Repos with missing/removable remotes until local state is clarified.
- Feature/provider PRs that need unavailable API keys or accounts for end-to-end proof.
- Broad generated changes without a clear user problem, test plan, or trusted author signal.

## Output Shape

For current-project triage:

```text
Repo: owner/name
Source: gh list/view/diff/checks, local source/tests where inspected

Immediate:
- https://github.com/owner/name/pull/123
  What: one-line summary.
  Type/Fit/Risk: bug|feature|dependency; good|mixed|poor; low|medium|high because ...
  Trust: @login; acct date; repo/global activity; known/unknown/bot.
  Proof: CI/repro/test/e2e state.
  Blocker: none / missing key / first-time CI approval / failing lint / unclear direction.
  Next: exact maintainer action.

Needs Gil:
- https://github.com/owner/name/issues/124
  What: ...
  Decision: exact choice or access needed.

Defer/close:
- https://github.com/owner/name/issues/125
  Why: ...

Skipped:
- <why>
```

For broad triage:

```text
Owner scanned: <authenticated GitHub login>
Source: RepoBar or gh command summary, plus gh for selected PRs/issues

Top queues:
- owner/repo: X issues, Y PRs; why it matters; next action

Immediate actions:
- <small obvious merge/fix/comment/rerun, with item URL>

Needs Gil:
- <larger/ambiguous queues, with item URL>

Skipped:
- archived/forks/missing access/etc.
```

When Gil asks to act, keep going: inspect selected PRs/issues with `gh`, rerun/fix CI, comment/close/merge only with evidence, and report exact commands/proof.
