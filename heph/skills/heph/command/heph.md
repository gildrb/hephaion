# Commands

Common public commands. Check `heph --help` and `heph <command> --help` for current flags.

## App

```bash
heph                         # open current armory or plain chat
heph <name-or-path>          # open an armory by name or path
heph tui [path]              # explicit TUI alias
heph armory init <name>      # create a named armory
heph armory open <path>      # open and validate an armory
```

## Materials

```bash
heph materials list <path>   # list material files
heph materials count <path>  # count material files
heph materials index <path>  # build or refresh the RAG index
heph index [path]            # refresh materials index, defaults to current armory
heph health [path]           # check indexed materials for extraction problems
```

## Local Models

```bash
heph local search [query]
heph local install <repo-or-path>
heph local status
heph local revalidate <model-id>
heph local stop
```

## Trust, Config, SDK

```bash
heph trust [path]
heph config show
heph config set <key> <value>
heph chat ask <path> [prompt]
heph chat ask --jsonl <path> [prompt]
heph sdk serve
heph sdk capabilities
```

## Release

```bash
heph update
heph release status
heph --version
```

## Env Vars

```bash
HARNESS_API_KEY=<api-key>
HARNESS_BASE_URL=<url>
HARNESS_MODEL=<provider-model-name>
HARNESS_ARMORY_HOME=<path>
HARNESS_ANALYTICS_ENABLED=true|false
HARNESS_CRASH_REPORTS_ENABLED=true|false
HARNESS_LOG_FORMAT=json|text
HARNESS_LOG_LEVEL=DEBUG|INFO|WARNING|ERROR
```

Use env vars or `/login` for credentials. Do not put real API keys in examples, logs, PR descriptions, or suggested commands.
