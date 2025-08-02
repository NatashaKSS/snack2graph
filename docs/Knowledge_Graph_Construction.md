# The Plan

## Overview

This document describes the overall strategy for Knowledge Graph construction.

I will extract entities and relationships to build a knowledge graph that captures the semantic richness of the domain’s key participants. This involves processing unstructured text through a data pipeline that combines traditional NLP pre-processing with modern LLM-based extraction techniques.

## Pipeline Architecture

### 1. Data Preprocessing Pipeline

#### 1.1 Message Normalization

- **Input**: Raw conversation messages between customer service agent and customer
- **Tokenization**: Use NLTK's `word_tokenize()` for initial token splitting
- **Lowercasing**: Convert all text to lowercase for consistency
- **Stop Word Removal**: Remove common stop words using NLTK's English stopwords corpus
- **Stemming**: Apply Porter Stemmer (`PorterStemmer()`) for word normalization
- **Synonym Expansion**: Enhance tokens with common synonyms using WordNet or custom synonym dictionaries

#### 1.2 Conversation Structure Analysis

- **Message Sequencing**: Maintain temporal order and conversation flow
- **Intent Classification**: Categorize message intents (complaint, request, resolution, etc.)

### 2. Entity Extraction Pipeline

#### 2.1 Traditional NER (NLTK/spaCy)

- **Person Names**: Extract customer and agent names
- **Organizations**: Identify company names, departments
- **Products/Services**: Detect mentioned products or services
- **Monetary Values**: Extract refund amounts, prices
- **Dates/Times**: Capture temporal references
- **Locations**: Identify geographical references

#### 2.2 Domain-Specific Entity Extraction

- **Ticket Numbers**: Extract support ticket identifiers
- **Order IDs**: Capture transaction references
- **Account Information**: Identify account numbers, user IDs
- **Issue Categories**: Extract problem types (billing, technical, shipping)
- **Resolution Status**: Identify outcome states

### 3. LLM-Enhanced Concept Extraction

#### 3.1 OpenAI API Integration

```python
# Concept extraction prompt structure
system_prompt = """
Extract semantic entities and relationships from customer service conversations.
Focus on:
- Customer concerns and pain points
- Agent actions and responses
- Problem resolution steps
- Emotional states and satisfaction levels
- Business process references
"""
```

#### 3.2 Advanced Entity Types

- **Abstract Concepts**: Customer satisfaction, urgency level, complexity
- **Process Steps**: Escalation, investigation, resolution phases
- **Emotional States**: Frustration, satisfaction, confusion
- **Business Rules**: Policies, procedures, exceptions
- **Causal Relationships**: Problem causes, solution effectiveness

### 4. Relationship Extraction

#### 4.1 Direct Action Relationships

- **Agent → Actions**: Agent handles refund requests, processes orders, escalates issues
- **Customer → Requests**: Customer makes refund orders, reports problems, asks questions
- **Entity → Entity**: Issues relate to products, orders connect to customers, policies apply to cases
- **Time → Events**: Temporal sequence of actions and responses

#### 4.2 Implicit Relationships (LLM-derived)

- **Process → Effectiveness**: Resolution method success patterns
- **Category → Resolution Time**: Issue complexity and resolution duration correlations
- **Policy → Application**: Business rule usage in specific scenarios

### 5. Graph Schema Design

#### 5.1 Node Types

```cypher
// Core entities
(:Customer {id, name, tier, history})
(:Agent {id, name, department, experience})
(:Conversation {id, date, channel, duration})
(:Message {id, timestamp, content, speaker, sentiment})

// Domain entities
(:Issue {id, category, severity, description})
(:Product {id, name, category, price})
(:Resolution {id, type, success, time_taken})
(:Policy {id, name, category, restrictions})

// Abstract concepts
(:Emotion {type, intensity, context})
(:ProcessStep {name, order, success_rate})
(:Outcome {type, satisfaction_score, resolution_time})
```

#### 5.2 Relationship Types

```cypher
// Direct relationships
(Customer)-[:HAS_ISSUE]->(Issue)
(Agent)-[:HANDLES]->(Conversation)
(Message)-[:REFERENCES]->(Product)
(Issue)-[:RESOLVED_BY]->(Resolution)

// Process relationships
(Message)-[:FOLLOWS]->(Message)
(Issue)-[:ESCALATED_TO]->(Agent)
(Resolution)-[:APPLIES]->(Policy)

// Semantic relationships
(Customer)-[:FEELS]->(Emotion)
(Agent)-[:PERFORMS]->(ProcessStep)
(Issue)-[:CAUSES]->(Emotion)
(Resolution)-[:RESULTS_IN]->(Outcome)
```

## Success Metrics

### Extraction Quality

- **Entity Recall**: `R = TP / (TP + FN)` where TP = correctly identified entities, FN = missed entities. This measures what percentage of actual entities in the conversation were successfully extracted. Computed by manually annotating a test set of conversations and comparing against automated extraction results.

- **Relationship Precision**: `P = TP / (TP + FP)` where TP = correct relationships, FP = incorrectly identified relationships. This measures the accuracy of extracted relationships like "Agent handles RefundOrder". Validation requires manual verification of relationship correctness against conversation context.

- **Processing Speed**: `Speed = Total_Messages / Processing_Time_Seconds` measuring throughput in messages per second. Critical for real-time or batch processing of large conversation datasets. Benchmarked by processing standardized conversation sets and measuring wall-clock time.

### Graph Quality

- **Node Coverage**: `Coverage = Unique_Entities_in_Graph / Total_Entities_in_Conversations` representing what percentage of conversation content is captured as graph nodes. Higher coverage indicates more comprehensive knowledge representation from the source conversations.

- **Relationship Density**: `Density = Total_Relationships / Total_Nodes` showing average connections per entity. Optimal density balances comprehensive relationship capture without creating overly complex or noisy graph structures that impede querying and analysis.

- **Query Performance**: `Response_Time = Query_Execution_Time_MS` for standard graph traversal queries. Essential for interactive applications and real-time analytics. Measured using representative queries like finding all issues handled by an agent or tracing customer interaction histories.
