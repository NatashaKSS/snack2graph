from typing import Any

from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

from lib.graph.knowledge_graph import KnowledgeGraph


def init_prompt(text: str, ontology: str) -> ChatPromptTemplate:
    """Generates the prompt template from any specified input parameters and returns the full prompt"""
    with open(
        "src/lib/prompts/prompt_for_entity_extraction.txt", "r", encoding="utf-8"
    ) as f:
        prompt_template_str = f.read()

    return ChatPromptTemplate.from_template(
        template=prompt_template_str, text=text, ontology=ontology
    )


def init_llm() -> Any:
    """Initialize the LLM used for for entity and relationship extraction."""
    llm = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0.1,
        verbose=True,
        max_retries=2,
        timeout=30.0,
        max_completion_tokens=5000,
    ).with_structured_output(schema=KnowledgeGraph, method="json_schema")

    return llm


def extract_knowledge_graph_from_text(text: str, ontology: str) -> KnowledgeGraph:
    """Extract entities and relationships from text using the extraction chain."""
    prompt = init_prompt(text, ontology)
    llm = init_llm()

    chain = prompt | llm
    result = chain.invoke({"text": text, "ontology": ontology})

    return result
