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

**09 August 2025:**

1. As a first-pass, I'll use the simple `RecursiveCharacterTextSplitter` from LangChain and split using simple chunk size configuration parameters just to approximate of the no. of characters in a paragraph. I've also added some custom Regular Expressions to be able to handle text documents with messy newline and paragraph separators. I wanted to use LangChain's `SemanticChunker` but it needs to make a request to OpenAI API. Not against that and I do expect semantic chunking to fair better, but I just wanted to try using a basic method that doesn't require us to reach for any foundational models first.

**Literature & Article Write-ups:**

1. [Article: 5 Levels Of Text Splitting](https://github.com/FullStackRetrieval-com/RetrievalTutorials/blob/main/tutorials/LevelsOfTextSplitting/5_Levels_Of_Text_Splitting.ipynb). This is a good starting introduction to text splitting using LangChain library methods, however, don't be constrained by the ranking and the number of techniques here as a mixture may be required for every extraction task.
2. [Common Chunking Techniques from Microsoft](https://learn.microsoft.com/en-us/azure/search/vector-search-how-to-chunk-documents)
3. The research paper [From Local to Global: A GraphRAG Approach to Query-Focused Summarization](https://arxiv.org/pdf/2404.16130) talks about the limitations of LLMs in answering questions at the "global" perspective, such as "Whys" and global questions directed at an entire corpus. Jonathan Larson also mentions this in his talk & demonstrates this at [AI Engineer here on YouTube: 'GraphRAG methods to create optimized LLM context windows for Retrieval — Jonathan Larson, Microsoft'](https://youtu.be/c5qJHr3DnT4?si=1qCreImL8EEkqIyR).

### 3. Entity Extraction & Relationship Mining

This step will focus on extracting connected Triples (Subject, Predicate, Object).

Together, these triples will form the base of the 1-hierarchy knowledge graph.

In subsequent iterations, it is possible to explore constructing a multi-level hierarchical knowledge graphs (i.e. class-subclass relationships). In this realm, it may be possible to abstract domain concepts and meta-relationships from specific clusters as outputs for other use cases that may require a more "global" perspective of the knowledge base.

**10 August 2025:**

1. As a first-pass, I'm going with the approach of performing entity & relationship extraction using a generic LLM such as GPT-4o.
2. The one unique thing I'll be doing is to:
   1. Guide the extraction process using a custom-made prompt
   2. Provide the LLM my semi-handwritten ontology to guide the extraction process.
   3. Provide some few-shot examples to the LLM.
3. Even before running my experiment, I can already foresee some improvements to try implementing in the future:
   1. Split this entire task into smaller sub-tasks so as to reduce its complexity & room for misinterpretation especially if the input text and resulting ontology is going to be very large.
   2. **(Performance)** The entire pipeline could be chained in such a way where the result of the first sub-task would be passed to the second and so on: `[(Sub-task 1) First pass entity and relationship extraction] -> [(Sub-task 2) Apply ontological constraints to filter away mistakes] -> [(Sub-task 3) De-duplicate entities and relationships]`. While this process is fundamentally sequential, there remains flexibility to parallelize by assigning resources to handle each document independently. In fact, only Sub-task 1 is strictly needed on every document.
   3. **(Design Question)** Another open question is how this pipeline will integrate with an existing knowledge graph. The sub-task involving de-duplication may need to be performed on not only the extracted entities & relationships but also the knowledge graph itself. This may require the use of vector embeddings so that concepts similar to each other in Vector Space can be retrieved and therefore de-duplicated against a set of criteria.

#### Post-processing

Like every other ETL pipeline for extracting concepts from unstructured data, we may need a few post-processing steps to clean up the results of our data. Multiple research papers have quoted the efficacy of this post-processing step too. The steps are:

1. Entity Disambiguation - Related entities should undergo deduplication to create coherent knowledge representations.
2. ...

**Literature & Article Write-ups:**

1. [Blogpost with Graphiti folks sharing their approach for building Graphiti - a Python library for building and querying dynamic, temporally aware knowledge graphs](https://blog.getzep.com/llm-rag-knowledge-graphs-faster-and-more-dynamic/). The Reddit thread where I found this [is located here](https://www.reddit.com/r/LLMDevs/comments/1ffngte/scaling_llm_information_extraction_learnings_and/).
2. [A curated list of 'LLM for Information Extraction' research papers](https://github.com/quqxui/Awesome-LLM4IE-Papers). We can study & explore more Entity Extraction, Relationship Extraction and Entity Disambiguation techniques here.
3. [Interesting & simple research paper regarding Entity Extraction from Electronic Health Record data](https://arxiv.org/html/2505.08704v2). In particular, the strategy of using a "Prompt ensemble w/ majority voting" prompt engineering strategy turned out to not be as good as using a Few-shot prompt. The reason for this was "...ensemble prompting’s result reflects the conservative nature of majority voting. Although less accurate, the ensemble output is more reliable due to its stricter agreement criteria...". The Few-shot prompt that was most effective was the one that "...includes a comprehensive list of training entities (excluding those present in the test document), which likely helps the model recognize similar entities through exposure to extensive medical terminology..."

### 4. Graph Database Storage

Any.

### 5. Vector Embedding Generation

(To be explored. We want to explore what different kinds of embeddings can be generated and for what use case are they good for?) At the very minimum, the embeddings should try to preserve the overall structure and connectedness of the knowledge graph and not just resort to using the pure-text form of the context.

## Open Source Frameworks or Libraries to try

1. [Google's LangExtract](https://github.com/google/langextract) for entity & relationship extraction. LangExtract is a Python library that uses LLMs to extract structured information from unstructured text documents based on user-defined instructions.
2.
