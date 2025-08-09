# Knowledge Graph Construction Strategy

## Overview

This document describes the approach(es) tried & chosen for the purposes of building a knowledge graph from unstructured text.

### 0. Ontology Preparation

The one thing I'll do a little differently in this pipeline is to incorporate the ontology of the knowledge graph into each step of the pipeline. An ontology is a structured representation of the concepts, relationships and constraints of a particular domain of knowledge. It can permit or deny certain entities & relationships and even prevent the logical boundaries of the domain from being violated.

**Goal:** I believe that maintaining ontological boundaries throughout the pipeline ensures semantic consistency and improves extraction quality. By incorporating domain-specific constraints at each stage, the system can make more informed decisions about chunk boundaries, entity relationships, and vector representations, ultimately producing a more accurate and coherent knowledge graph that respects the logical structure of the domain.

### 1. Data Ingestion

Read source files which will serve as the input to the next step.

### 2. Text Chunking

A simple text chunker will be used to parse input text. The main criteria for this chunker is that it must:

1. Maintain Boundary Clarity - Preserve semantic meaning as much as possible across sentence boundaries and content structure.
2. Preserve Context - Each chunk maintains references to its parent document and sequential relationships with adjacent chunks to promote the explainability of the data source.

so that the data is in a form that retains the clarity needed for entity & relationships parsing that happens later.

#### References

1. [Article: 5 Levels Of Text Splitting](https://github.com/FullStackRetrieval-com/RetrievalTutorials/blob/main/tutorials/LevelsOfTextSplitting/5_Levels_Of_Text_Splitting.ipynb). This is a good starting introduction to text splitting using LangChain library methods, however, don't be constrained by the ranking and the number of techniques here as a mixture may be required for every extraction task.
2. [Common Chunking Techniques from Microsoft](https://learn.microsoft.com/en-us/azure/search/vector-search-how-to-chunk-documents)

### 3. Entity Extraction & Relationship Mining

This step will focus on extracting connected Triples (Subscription, Predicate, Object).

Together, these triples will form the base of the 1-hierarchy knowledge graph.

In subsequent iterations, it is possible to explore the building of multi-level hierachical knowledge graphs (i.e. class-subclass relationships). In this realm, it may be possible to abstract domain concepts and meta-relationships from specific clusters as outputs for other use cases that may require a more "global" perspective of the knowledge base.

#### Post-processing

Like every other ETL pipeline for extracting concepts from unstructured data, we may need a few post-processing steps to clean up the results of our data. Multiple research papers have quoted the efficacy of this post-processing step too. The steps are:

1. Entity Disambiguation - Related entities should undergo deduplication to create coherent knowledge representations.
2. ...

### 4. Graph Database Storage

Any.

### 5. Vector Embedding Generation

(To be explored. We want to explore what different kinds of embeddings can be generated and for what use case are they good for?) At the very minimum, the embeddings should try to preserve the overall structure and connectedness of the knowledge graph and not just resort to using the pure-text form of the context.

## Open Source Frameworks or Libraries to try

1. [Google's LangExtract](https://github.com/google/langextract) for entity & relationship extraction. LangExtract is a Python library that uses LLMs to extract structured information from unstructured text documents based on user-defined instructions.
2.
