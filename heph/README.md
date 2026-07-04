# Heph Package

The Heph package contains product-specific agent guidance for Heph.

Heph is a local document agent. It indexes files in an armory, answers from those files, and shows cited source passages.

## Quick Start

```text
Read heph/AGENTS.md
Choose the Heph skill for the task
Inspect current Heph source and tests
Apply the relevant Heph contracts
Verify the changed surface
```

## Armory Layout

Heph work uses local armories:

```text
<armory>/
├── materials/
├── .harness/
└── README.md
```

`materials/` contains user source files. `.harness/` contains Heph local state: indexes, memory, chats, traces, usage snapshots, and ignore rules.

## Package Map

```text
heph/AGENTS.md
  Heph product router.

heph/skills/heph/
  Heph operations, commands, troubleshooting, trust, SDK, and automation.

heph/skills/cli-ux/
  Heph CLI/TUI UX, copy, command contracts, machine output, and verification.

heph/skills/design-engineering/
  Heph web, brand, terminal, and TUI design engineering.
```

## Source Of Truth

For Heph tasks, inspect the current Heph repository first. Use source, tests, docs, command help, and design docs as immediate truth. Update this package after confirming durable rules.

## Safety

Do not expose source document text, retrieved chunks, prompts, traces, API keys, credentials, or private user data unless the user asks for an inspection surface that should show it.
