import typer
from pathlib import Path
from typing_extensions import Annotated

from lib.data_ingestor import generate_text_chunks

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
    file_path: Annotated[Path, 
        typer.Option(
            "--file-path", "-f",
            exists=True,
            file_okay=True,
            dir_okay=False,
            readable=True,
            resolve_path=True,
            help="Path to the input file"
        )]) -> None:
    """Process the input file and construct a knowledge graph."""
    result = generate_text_chunks(file_path)
    typer.echo(result)
