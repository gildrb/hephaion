# Armories

An armory is a local folder with materials, chat history, retrieval index, traces, usage snapshots, and memory.

## Structure

```text
~/.armories/<name>/
  materials/        source documents
  .harness/         local state
    armory.toml     armory marker
    rag_index.json  retrieval index
    memory.json     armory memory
    chats/          saved sessions
    traces/         JSONL traces when enabled
    usage/          token and cost snapshots
    ignore          indexing ignore rules
  README.md         optional notes
```

## Ownership

- `materials/` is source of truth.
- `.harness/` is local state.
- Index files are rebuildable.
- Provider credentials stay machine-local.
- Copy or sync `.armories` to move work between machines.

## Create

```bash
heph armory init <name>
```

Use names such as `research-course` or `q3-reports`. Avoid opaque names.

## Move

Copy the armory folder or armory home. On another machine, install the app, place the folder under armory home, configure provider credentials, and run `heph <name>`.

## Maintain

- Add files to `materials/`.
- Use `.harness/ignore` for ignore patterns.
- Run `heph index <path>` after large changes.
- Run `heph health <path>` when retrieval quality is poor.
- Use `/evidence` to inspect retrieval for a turn.

## Recover

1. Check that `materials/` exists.
2. Check `.harness/armory.toml`.
3. Check legacy state if the armory came from an older release.
4. Avoid guessing when two state directories conflict.
