# Domain and Ontology

## Overview

This document defines the comprehensive entity and relationship framework for modeling Zendesk Agent Workspace messaging and ticketing functionality. The organizing principle follows a multi-level hierarchical structure that captures information at component, document, and domain levels.

## Multi-level hierarchical structure as a strategy

The multi-level hierarchical structure addresses the challenge of representing knowledge at varying levels of abstraction while ensuring semantic coherence. It organizes information into component, document, and domain levels for effective knowledge representation.

### Component-Level Framework

Capturing 15 keyphrases per document section ensures granularity and aligns with established practices in information extraction. This approach balances detail and computational efficiency, optimizing document-level relation extraction.

### Document-Level Aggregation

Aggregating sentence-level and document-level embeddings captures global context while maintaining precision in co-reference resolution. This strategy leverages advances in document-level information extraction research for improved accuracy.

### Domain-Level Abstraction

Abstract hierarchical concepts enhance cross-document knowledge integration and improve knowledge graph completion. Research demonstrates that multi-level knowledge generation significantly benefits few-shot scenarios.

References:

- A Novel Information Representation for Exploratory Search Tasks - Bahareh Sarrafzadeh, Adam Roegiest, Edward Lank"(<https://arxiv.org/abs/2005.01716>)

## Ontology

### Chosen Domain

Zendesk Agent Workspace Messaging:

1. User Interface Components
2. Communication Channels
3. Features
4. Actors & Domain Objects
5. Configuration & Settings

### Core Entities

#### Interface Components

- The unified interface environment where agents manage multichannel customer support interactions within a single ticketing system[2].

- A configurable sidebar interface that displays customer information, interaction history, knowledge base content, and integrated applications[3][4][5].

- The system component managing alerts, sounds, and visual indicators that notify agents of incoming conversations, assignments, and updates.

- The primary conversation interface where agents view conversation history and compose responses across all communication channels.

- The notification interface element that appears when new messaging, chat, or voice requests require agent response.

#### Communication Channels

- Persistent messaging channel embedded on customer websites enabling asynchronous conversations.

- Communication through social media platforms including Facebook, WhatsApp, Instagram, and other social channels.

- Traditional email-based customer communication integrated within the unified workspace.

- Real-time synchronous communication channel for immediate customer assistance.

- Phone-based communication system integrated within the workspace interface.

#### Data Objects

- Core data structures representing customer support requests throughout their complete lifecycle from creation to resolution.

- Individual communication units within conversations, containing content, attachments, and metadata.

- Persistent message threads maintaining history across channel switches and time periods.

- Files, images, and documents shared within conversations with size and format restrictions.

- Aggregated customer information including interaction history, custom fields, and behavioral data.

#### User Roles

- Customer service representatives using the Agent Workspace to manage and respond to customer interactions.

- End users initiating support requests through various communication channels.

- System administrators configuring workspace features, routing rules, and business processes.

- Automated conversational agents handling initial customer interactions before human agent handoff.

#### Automation Components

- Predefined sets of actions enabling agents to execute common tasks with single-click efficiency.

- Event-based business rules automatically executing actions when specific conditions are met.

- Automated workflows including triggers, automations, and routing configurations.

- Configuration determining how incoming requests are distributed to appropriate agents or groups.

### Key Relationships

#### Structural Relationships

- Agent Workspace **contains** Context Panel, Message Window, Notification System
- Context Panel **displays** Customer Context, Knowledge Articles, Integrated Apps
- Tickets **aggregate** Messages into persistent Conversations
- Conversations **span** multiple Communication Channels

#### Operational Relationships

- Incoming Messages **trigger** Notification System alerts
- Agents **accept** incoming requests through Accept Button
- Macros **update** Ticket properties and status
- Triggers **route** Tickets to appropriate Agent groups
- Business Rules **automate** repetitive workflow processes

#### Hierarchical Relationships

- Specific Channel Types **inherit from** base Communication Channel
- Individual Messages **compose** larger Conversation units
- Component-level features **aggregate to** Document-level capabilities
- Domain-level concepts **abstract** operational workflows

#### Contextual Relationships

- Customer Context **informs** Agent responses and decisions
- Interaction History **provides** continuity across channel switches
- Bot conversations **transfer** context to human Agents
- Knowledge Articles **suggest** relevant help content

### Information Flow Patterns

#### Message Lifecycle

1. Customer initiates conversation via Web Widget or social channel
2. Message creates Ticket and routes to appropriate Agent queue
3. Agent receives notification and accepts conversation ownership
4. Asynchronous conversation exchange with context preservation
5. Resolution process returns control to Bot or closes conversation

#### Context Propagation

- Customer information automatically surfaces across all channels
- Conversation history persists during channel transitions
- Bot interaction context transfers to human agents
- Previous ticket information informs current conversation handling

#### Automation Workflows

- Triggers execute immediately upon ticket creation or updates
- Macros provide one-click execution of common agent tasks
- Business rules route tickets based on content, customer, or channel
- Routing rules determine agent notification and assignment patterns

### Usage Notes

This ontology serves as the semantic foundation for knowledge graph construction.

**Key features:**

1. Hierarchical class structure enabling inheritance of properties
2. Rich relationship modeling capturing operational workflows
3. Constraint definitions ensuring data consistency
4. Complex class definitions enabling automated reasoning
5. Business rule encoding through axioms and restrictions

**Construction Usage:**

- NLP systems identify text spans as instances of these classes
- Text processing identifies relationships between entities
- Constraints validate extracted information consistency
- OWL reasoners derive new facts from existing relationships
- Applications query using this structured vocabulary

## 2. RDF Representation

- See definition in the corresponding [RDF File](/data/rdfs/agent_workspace_messaging.ttl). Visualise the RDF Graph this generates using VS Code extensions such as "RDF Preview" or "RDF Sketch".

## 3. Implementation Notes

### Entity Recognition

The ontology provides a comprehensive taxonomy for NLP systems to classify extracted entities. Each class definition includes sufficient context for automated classification of text spans as instances of specific entity types.

### Relationship Extraction

The extensive property definitions enable relationship extraction systems to identify and classify semantic connections between entities. The domain and range specifications guide extraction systems in determining valid relationship instances.

### Constraint Validation

The OWL constraints serve as validation rules for extracted information. Cardinality restrictions, disjoint classes, and property characteristics ensure logical consistency in the constructed knowledge graph.

### Automated Reasoning

The ontology structure enables OWL reasoners to derive new knowledge. For example, agents with assigned tickets are automatically classified as "AgentWithActiveConversations," and urgent unassigned tickets can be automatically identified for priority handling.

### Evolution and Extension

The hierarchical structure supports ontology evolution. New channel types inherit from CommunicationChannel, new interface components inherit from InterfaceComponent, and new automation features inherit from AutomationComponent. This design ensures backward compatibility while enabling feature expansion.

This comprehensive framework provides the semantic foundation for constructing accurate, queryable, and reasoning-enabled knowledge graphs from Zendesk Agent Workspace documentation and operational data.

## References (about the domain)

- <https://support.zendesk.com/hc/en-us/articles/4408828503450-Configuring-the-context-panel-in-the-Zendesk-Agent-Workspace>
- <https://support.zendesk.com/hc/en-us/articles/4408836526362-Using-the-context-panel>
- <https://support.zendesk.com/hc/en-us/articles/4408821476378-Changing-your-chat-sounds-and-notification-settings>
- <https://support.zendesk.com/hc/en-us/articles/5020833543450-Setting-up-notification-routing-for-messaging>
- <https://support.zendesk.com/hc/en-us/articles/4408829019162-Routing-messaging-tickets-and-notifying-agents>
- <https://www.zendesk.com/sg/blog/zendesk-messaging/>
- <https://support.zendesk.com/hc/en-us/articles/4408846454682-About-conversational-support-with-messaging>
- <https://support.zendesk.com/hc/en-us/articles/4408883355546-Introduction-to-the-Support-agent-interface-standard-agent-interface>
- <https://support.zendesk.com/hc/en-us/articles/4408836490138-Setting-up-notification-routing-for-live-chat>
- <https://support.zendesk.com/hc/en-us/articles/4408837480474-What-is-the-agent-experience-with-assigned-and-broadcast-chat-routing>
- <https://support.zendesk.com/hc/en-us/articles/4408882039450-Resources-for-working-with-tickets>
- <https://support.zendesk.com/hc/en-us/articles/6272487169434-Managing-agent-interface-settings-for-Support>
- <https://support.zendesk.com/hc/en-us/articles/4408885959066-Lesson-5-Business-rules>
- <https://support.demeterict.com/hc/en-us/articles/4411563912601-Enabling-Zendesk-messaging>
- <https://support.zendesk.com/hc/en-us/articles/4408844187034-Creating-macros-for-repetitive-ticket-responses-and-actions>
- <https://support.zendesk.com/hc/en-us/articles/4408828286234-Creating-business-rules-for-CCs-and-followers>
