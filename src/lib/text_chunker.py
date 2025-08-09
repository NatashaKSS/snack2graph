from langchain_experimental.text_splitter import SemanticChunker
from langchain_openai.embeddings import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

REGEX_NEWLINE_PATTERNS = [
    # For standard text documents
    r"\n\s*\n\s*\n+",  # 3+ newlines (with optional spaces/tabs) - hard section/page break
    r"\n\s*\n+",  # 2+ newlines (with optional whitespace) - paragraph break
    r"\n{2,}",  # 2+ consecutive newlines (simple version)
    r"\n",  # single newline (fallback, least preferred)
    r"(?:\r?\n\s*){2,}",  # handles \r\n and \n, 2+ times
    # For markdown documents
    r"\n-+\n",  # horizontal rule or section divider (e.g. '-----')
    r"\n\s*#.+\n",  # markdown heading (e.g. '# Heading')
    r"\n\s*\*\s*\n",  # bullet point separator (e.g. '*')
    r"\n\s*\d+\.\s+",  # numbered list (e.g. '1. ')
    r"\n\s*\u2022\s*\n",  # bullet (unicode)
    r"\n\s*\|\s*\n",  # table row separator (pipe)
    r"\n\s*\t+\n",  # tabbed section
    r"\n\s*\n?\s*-\s*\n",  # single dash line
]

# an approximation of the no. of characters in a paragraph of text.
CHARS_PER_CHUNK = 1000
# just an approximation. This is 20% of the chunk size.
CHARS_PER_CHUNK_OVERLAP = 200


# Note: Needs OpenAI API Token set in .env variable OPENAI_API_KEY
# see https://python.langchain.com/docs/how_to/semantic-chunker
def with_semantic_chunker():
    return SemanticChunker(OpenAIEmbeddings())


def with_generic_text_chunker():
    return RecursiveCharacterTextSplitter(
        chunk_size=CHARS_PER_CHUNK,
        chunk_overlap=CHARS_PER_CHUNK_OVERLAP,
        separators=REGEX_NEWLINE_PATTERNS,
        length_function=len,
        is_separator_regex=True,
    )


def generate_chunks(content: str) -> list[str]:
    """Generates text chunks from the provided content"""
    text_splitter = with_generic_text_chunker()
    docs = text_splitter.create_documents([content])
    return [doc.page_content for doc in docs]
