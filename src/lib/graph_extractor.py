from typing import Any

from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

from lib.graph.knowledge_graph import KnowledgeGraph


def compose_prompt() -> ChatPromptTemplate:
    """Obtains the prompt template and returns the full prompt"""
    with open("prompt_for_entity_extraction.txt", "r", encoding="utf-8") as f:
        prompt_template_str = f.read()

    return ChatPromptTemplate.from_template(prompt_template_str)


def create_extraction_chain() -> Any:
    """Create a chain for entity and relationship extraction."""
    prompt = compose_prompt()
    llm = ChatOpenAI(
        model="gpt-4o", temperature=0.1, verbose=True, max_retries=2, timeout=30.0
    ).with_structured_output(schema=KnowledgeGraph)

    return prompt | llm


def extract_knowledge_graph_from_text(text: str, ontology: str) -> KnowledgeGraph:
    """Extract entities and relationships from text using the extraction chain."""
    chain = create_extraction_chain()
    result = chain.invoke({"text": text, "ontology": ontology})
    return result
