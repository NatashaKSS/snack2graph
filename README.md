# Exploring MCP Knowledge Graph Servers

An MCP Server built with FastMCP w/ KuzuDB for embedded Cypher-backed knowledge graph storage.

This is purely for exploration purposes.

## Setup

Install `uv` (see [the doc site](https://docs.astral.sh/uv)), our Python package manager of choice. Here is a [quick start guide](https://docs.astral.sh/uv/getting-started/features/) of `uv` that contains some basic features.

Verify your setup by running the command below.

```bash
uv run fastmcp version
```

You should see something like

```bash
FastMCP version:  2.9.2
MCP version:      1.9.4
Python version:   3.13.5
Platform:         macOS-15.5-arm64-arm-64bit-Mach-O
FastMCP root path: /Users/xxx/Documents/<path_to_root>
```

**Tip:** Whenever this command is run, `uv` automatically installs the needed packages from the lockfile into your `.venv` project environment and even creates it if hasn't been yet (see [the doc site about 'project environment'](https://docs.astral.sh/uv/concepts/projects/layout/#the-project-environment) for more info).

## Running the MCP Server

### Developer Mode

The FastMCP framework provides on out-of-the-box solution for inspecting your MCP server's resources, prompts, tools, etc, and allows for a more user-friendly debugging experience.

### Running

Run the MCP Inspector Tool (it will prompt you to install the inspector package if not already done so).

```bash
uv run fastmcp dev main.py
```

Follow the instructions on your CLI and open the inspector with token pre-filled in your browser on localhost. You should see a user interface that allows you to explore the MCP server's capabilities and see debug log statements on the sidebar.

### Example - Run a 'Hello World' Tool

There is a sample MCP tool named `hello` that takes in a name as an argument. On your inspector UI, navigate to `Tools > List Tools > Click on 'hello' in the dropdown list below`. On the righthand pane, enter your `name` and click on `Run Tool`. You should see the tool's result after that.

### Stopping

Close your development session by pressing `CTRL-C`.
