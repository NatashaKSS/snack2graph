from pathlib import Path


def load_data(file_path: Path) -> str:
    """Read the input file and prepare text chunks for further processing."""
    try:
        if not file_path.exists():
            return "File does not exist at '{file_path}'"

        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        return content

    except Exception:
        return "failure"
