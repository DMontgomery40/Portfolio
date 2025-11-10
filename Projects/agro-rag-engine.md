---
layout: project
title: agro-rag-engine
description: Domain-focused RAG engine for agricultural content - ingestion, structured chunking, embeddings, vector indexing, retrieval, and prompt orchestration.
category: AI / ML & Retrieval Systems
status: Active
date: 2025-11-10
github_url: https://github.com/DMontgomery40/agro-rag-engine
permalink: /projects/agro-rag-engine/
tags:
  - Python
  - TypeScript
  - RAG
  - Vector
  - AI/ML
---

## Overview

**agro-rag-engine** is a domain-focused Retrieval-Augmented Generation (RAG) system purpose-built for agricultural content. It provides end-to-end functionality: document ingestion → structured chunking & embedding → vector indexing → high-signal retrieval → prompt orchestration that grounds LLM outputs in authoritative agricultural sources.

Unlike general-purpose RAG systems, agro-rag-engine is optimized for the unique challenges of agricultural data: seasonal variations, regional differences, scientific terminology, and the critical need for accuracy in farming recommendations.

## Key Features

### Intelligent Document Ingestion
- **Multi-Format Support**: PDFs, Word docs, web pages, spreadsheets
- **Metadata Extraction**: Automatic extraction of publication dates, authors, regions
- **Source Tracking**: Maintain provenance for every piece of information
- **Update Detection**: Automatically refresh when sources change

### Structured Chunking & Embedding
- **Semantic Chunking**: Split documents at natural boundaries (sections, topics)
- **Context Preservation**: Keep critical context with each chunk
- **Domain-Specific Embeddings**: Fine-tuned for agricultural terminology
- **Metadata Enrichment**: Tag chunks with season, region, crop type

### Vector Indexing
- **High-Performance Search**: Sub-millisecond retrieval at scale
- **Hybrid Search**: Combine semantic and keyword matching
- **Filtered Retrieval**: Search within specific crops, regions, or seasons
- **Similarity Scoring**: Confidence metrics for every result

### Prompt Orchestration
- **Grounded Responses**: LLM outputs cite authoritative sources
- **Answer Synthesis**: Combine information from multiple documents
- **Confidence Levels**: Indicate certainty based on source quality
- **Follow-Up Questions**: Suggest natural next queries

### Demo UI
- **Rapid Iteration**: Test queries and see results in real-time
- **Source Inspection**: View original documents for every answer
- **Query Analytics**: Track which questions get good answers
- **Feedback Loop**: Improve the system based on user interactions

## Images

### System Architecture Banner
<img src="https://raw.githubusercontent.com/DMontgomery40/agro-rag-engine/main/assets/agro-banner.svg" alt="agro-rag-engine Architecture" style="max-width: 100%; border-radius: 8px; margin: 1rem 0;" />

### Dashboard Interface
<img src="https://raw.githubusercontent.com/DMontgomery40/agro-rag-engine/main/assets/dashboard.png" alt="agro-rag-engine Dashboard" style="max-width: 100%; border-radius: 8px; margin: 1rem 0;" />

### Chat Interface
<img src="https://raw.githubusercontent.com/DMontgomery40/agro-rag-engine/main/assets/chat%20tab.png" alt="agro-rag-engine Chat" style="max-width: 100%; border-radius: 8px; margin: 1rem 0;" />

### Grafana Metrics
<img src="https://raw.githubusercontent.com/DMontgomery40/agro-rag-engine/main/assets/grafana-metrics.png" alt="agro-rag-engine Metrics" style="max-width: 100%; border-radius: 8px; margin: 1rem 0;" />

## Tech Stack

### Backend
- **Python**: Core RAG pipeline and orchestration
- **FastAPI**: High-performance API server
- **LangChain**: LLM integration and prompt templates
- **Sentence Transformers**: Domain-specific embeddings

### Vector Database
- **Qdrant**: High-performance vector search
- **PostgreSQL**: Metadata and relational data
- **Redis**: Caching layer for frequent queries

### Frontend
- **TypeScript**: Type-safe UI implementation
- **React**: Interactive demo interface
- **TailwindCSS**: Responsive design
- **Chart.js**: Query analytics visualization

### LLM Integration
- **OpenAI GPT-4**: Answer generation
- **Anthropic Claude**: Alternative model support
- **Local Models**: Option for on-premises deployment

### Monitoring
- **Prometheus**: Metrics collection
- **Grafana**: Real-time dashboards
- **OpenTelemetry**: Distributed tracing

## Links

- **GitHub Repository**: [github.com/DMontgomery40/agro-rag-engine](https://github.com/DMontgomery40/agro-rag-engine)
- **Live Demo**: [agro-rag.demo.site](https://agro-rag.demo.site)
- **Documentation**: [docs.agro-rag.site](https://docs.agro-rag.site)

---

*agro-rag-engine: Because farming decisions deserve answers grounded in authoritative knowledge, not hallucinations.*
