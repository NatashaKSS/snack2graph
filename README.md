# Snack2Graph

## Exploring Knowledge Graphs

An application that parses unstructured text and constructs a Knowledge Graph with a rich web of inter-connected relationships using FalkorDB.

In essence, this tool snacks stuff and outputs a knowledge graph of what it snacked on.

This is purely for exploration purposes.

## Setup

Install `uv` (see [the doc site](https://docs.astral.sh/uv)), our Python package manager of choice. Here is a [quick start guide](https://docs.astral.sh/uv/getting-started/features/) of `uv` that contains some basic features.

Verify your setup by running the command below.

```bash
uv run python src/main.py --help
```

**Tip:** Whenever this command is run, `uv` automatically installs the needed packages from the lockfile into your `.venv` project environment and even creates it if hasn't been yet (see [the doc site about 'project environment'](https://docs.astral.sh/uv/concepts/projects/layout/#the-project-environment) for more info).

## Running the CLI

The project includes a CLI for processing text files. Show all available commands using `help`.

```bash
uv run python src/main.py --help
```

A successful run should look like:

```bash
Usage: main.py [OPTIONS] COMMAND [ARGS]...

Snack2Graph parses unstructured text and constructs a Knowledge Graph with a rich web of inter-connected relationships using FalkorDB.

╭─ Options ───────────────────────────────────────────────────────╮
│ --help          Show this message and exit.                     │
╰─────────────────────────────────────────────────────────────────╯
╭─ Commands ──────────────────────────────────────────────────────╮
│ construct Create a knowledge graph with the given text file.    │
│ version   Show the current version of the CLI tool.             │
╰─────────────────────────────────────────────────────────────────╯
```

## Development

### Code Formatting

[`ruff`](https://docs.astral.sh/ruff/) is the chosen linter & formatter for this project.

Check for lint violations for all files in the project with the configured lint rules:

```bash
uv run ruff check
```

Update all files in the project with the configured formatting rules:

```bash
uv run ruff format
```

#### Recommended VS Code Extensions

You can also install extensions in your own IDE that support `ruff` to help you run these linting & formatting check as your develop. The recommended plugin for this project is `Ruff` by `Astral Software`, and here is a sample JSON you can use in `settings.json` to lint & format code and organize imports automatically.

```json
"[python]": {
  "editor.formatOnSave": true,
  "editor.defaultFormatter": "charliermarsh.ruff",
  "editor.codeActionsOnSave": {
    "source.fixAll": "explicit",
    "source.organizeImports": "explicit"
  }
}
```
