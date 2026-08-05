# Hephaion

Permanent agent documentation for product work. Small root router, product-owned packages, executable checks.

## Use

```sh
export HEPHAION_REPO="${HEPHAION_REPO:-$HOME/Documents/Repos/hephaion}"
cd "$HEPHAION_REPO"

cat AGENTS.md
git status --short
git ls-files
```

Identify the product from task paths, commands, source, or UI. Read `<product>/AGENTS.md`, then load only the skills that own the task's failure classes.

## Commands

| Command | Purpose |
| --- | --- |
| `git status --short` | Expose existing work before edits |
| `git ls-files` | List tracked documentation and package paths |
| `awk 'NF{c++} END{print c}' AGENTS.md` | Enforce the root router's filled-line budget |
| `python3 gildrb/scripts/check_design_docs.py --portfolio-repo "$PORTFOLIO_REPO"` | Check the gildrb package and live portfolio source |
| `git diff --check` | Reject whitespace errors |

## Files

```text
hephaion/
  AGENTS.md                      root router and shared safety
  README.md                      this entry point
  .agents/skills/
    hephaion-system/             package architecture
    hephaion-design/             product-neutral design rules
  heph/
    AGENTS.md                    Heph router
    README.md                    Heph package map
    design.md                    Heph product contract
    cli-design.md                Heph CLI contract
  gildrb/
    AGENTS.md                    portfolio router
    README.md                    commands, paths, build, routes, release
    design.md                    visual/interaction source contract
    case-studies.md              routes, writing, evidence, generation
    platform.md                  Cloudflare runtime and production
    scripts/check_design_docs.py package + live-source drift checker
    skills/                      atomic failure owners
```

Root owns routing, package shape, shared safety, and shared checks. Product folders own vocabulary, source paths, commands, runtime behavior, UI rules, and verification.

## Product package

```text
<product>/
  AGENTS.md            short router; under 80 filled lines
  README.md            OptMem-style entry: commands, files, dataflow, prompt
  <product docs>.md    durable product contracts
  scripts/             executable drift checks
  skills/
    <atomic-skill>/
      SKILL.md         mission, ownership, fixed contract, procedure, rejection,
                       verification, done
      agents/
        openai.yaml    discoverable invocation state
      references/      detailed paths, examples, matrices, transcripts
```

Prefer progressive disclosure. Put the shortest complete route at the top, exact commands and paths in copyable blocks, detailed failure-specific material in references, and enforce durable claims in code.

## Products

| Product | Entry | Scope |
| --- | --- | --- |
| `heph/` | `heph/AGENTS.md` | Heph product and CLI |
| `gildrb/` | `gildrb/AGENTS.md` | Portfolio, case studies, design, Cloudflare publishing |

## Agent contract

This is the whole root integration:

```markdown
### At startup

1. Run `git status --short`.
2. Read root `AGENTS.md`.
3. Identify the product.
4. Read `<product>/AGENTS.md`.
5. Load only matching atomic skills.

### While working

1. Read implementation and tests before product prose.
2. Change product rules in the product package.
3. Write executable norms: trigger, action, check.
4. Keep examples and edge cases in skill references.
5. Update drift checks with durable public contracts.

### Before handoff

1. Run product checks and touched-surface tests.
2. Verify source, generated output, docs, and runtime agree.
3. Check router line budgets and `git diff --check`.
4. Preserve unrelated user work.
```

## Safety

Never publish secrets, private source content, prompts, traces, credentials, or unredacted user data. Source, tests, and validated runtime behavior outrank docs; when they disagree, inspect implementation first and update guidance only after intent is confirmed.
