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
