from pathlib import Path

import typer
from typing_extensions import Annotated

from lib.data_ingestor import load_data
from lib.graph_extractor import extract_knowledge_graph_from_text
from lib.text_chunker import generate_chunks

APP_NAME = "Snack2Graph"
APP_VERSION = "0.1.0"
APP_DESCRIPTION = "Snack2Graph parses unstructured text and constructs a Knowledge Graph with a rich web of inter-connected entities & relationships."

cli = typer.Typer(
    name=APP_NAME,
    help=APP_DESCRIPTION,
)


@cli.command("version")
def show_version() -> None:
    """Display the current version of the CLI tool."""
    typer.echo(APP_NAME + " Version: " + APP_VERSION)


@cli.command("construct")
def generate_knowledge_graph(
    file_path: Annotated[
        Path,
        typer.Option(
            "--file-path",
            "-f",
            exists=True,
            file_okay=True,
            dir_okay=False,
            readable=True,
            resolve_path=True,
            help="Path to the input file",
        ),
    ],
    print_chunks: Annotated[
        bool,
        typer.Option(
            "--print-chunks",
            help="Pretty print each chunk before processing",
            is_flag=True,
            default=False,
        ),
    ] = False,
) -> None:
    """Process the input file and construct a knowledge graph."""
    document = load_data(file_path)
    chunks = generate_chunks(document)

    if print_chunks:
        for i, chunk in enumerate(chunks, 1):
            typer.echo(f"\n{'=' * 30}\nChunk {i}\n{'=' * 30}\n{chunk.strip()}\n")

    with open(
        "data/rdfs/agent_workspace_messaging.ttl",
        "r",
        encoding="utf-8",
    ) as f:
        ontology = f.read()

    # TODO:
    # 1. Process each chunk instead
    # 2. Make prompt simpler
    # 3. Add OPENAI_API_KEY and test
    # 4. Add few-shot examples to help in the extraction process
    # 5. Add a prompt to help the LLM interpret the RDF file (can be part of a future process in the chain too)
    # References:
    # * LangChain describes its process here: https://python.langchain.com/docs/how_to/structured_output
    result = extract_knowledge_graph_from_text(document, ontology)
    type.echo(result)
