---
layout: project
title: agro‑rag‑engine
description: Domain‑focused RAG engine for agricultural content with structured chunking, vector indexing, and high‑signal retrieval.
category: AI / ML & Retrieval Systems
status: Active
date: 2025-11-10
github_url: https://github.com/DMontgomery40/agro-rag-engine
permalink: /projects/agro-rag-engine/
tags: [Python, TypeScript, RAG, Vector]
---

## Overview

agro‑rag‑engine is a domain‑focused Retrieval Augmented Generation (RAG) system specifically designed for agricultural content. It implements a complete pipeline from ingestion through retrieval, grounding AI‑generated outputs in authoritative agricultural sources.

The engine follows a structured workflow: **ingestion → structured chunking & embedding → vector indexing → high‑signal retrieval → prompt orchestration**. This architecture ensures that responses are factually grounded in domain‑specific knowledge while maintaining the fluency and helpfulness of large language models.

A demo UI is included for rapid iteration and testing, making it easy to experiment with different retrieval strategies, chunking approaches, and prompt configurations.

## Key Features

### Domain‑Focused Architecture

Optimized specifically for agricultural content:

- **Specialized Chunking**: Respects agricultural document structure (crop guides, research papers, technical bulletins)
- **Domain Embeddings**: Fine‑tuned embeddings capture agricultural terminology and concepts
- **Source Prioritization**: Rank authoritative sources (universities, extension services, research institutions)
- **Seasonal Context**: Incorporate temporal relevance for seasonal agricultural information

### Structured Ingestion Pipeline

Flexible content ingestion with format support:

- **Multiple Formats**: PDF, HTML, Markdown, plain text, and structured data
- **Metadata Extraction**: Capture authorship, publication date, source authority, and topics
- **Content Cleaning**: Remove boilerplate, navigation, and irrelevant content
- **Deduplication**: Identify and handle duplicate or near‑duplicate content

### Vector Indexing & Retrieval

High‑performance semantic search:

- **Embedding Generation**: Convert text chunks to dense vector representations
- **Vector Database**: Efficient storage and retrieval with similarity search
- **Hybrid Search**: Combine semantic similarity with keyword matching
- **Relevance Ranking**: Score and rank results by relevance to query

### Prompt Orchestration

Ground LLM outputs in retrieved content:

- **Context Injection**: Provide relevant passages to the language model
- **Source Attribution**: Track which sources contributed to each response
- **Hallucination Reduction**: Constrain outputs to information present in sources
- **Citation Generation**: Automatic references to source material

### Demo UI

Interactive interface for experimentation:

- **Query Testing**: Try different questions and see retrieval results
- **Parameter Tuning**: Adjust chunking size, embedding model, retrieval count
- **Response Visualization**: See retrieved passages and generated answers
- **Feedback Loop**: Iterate on configuration based on results

## Tech Stack

### Backend
- **Python**: Core RAG pipeline implementation
- **LangChain**: RAG framework and orchestration
- **Vector Database**: Efficient similarity search (Chroma/Pinecone/Weaviate)
- **Embedding Models**: Sentence transformers or OpenAI embeddings

### Frontend
- **TypeScript**: Type‑safe UI implementation
- **React**: Interactive demo interface
- **Tailwind CSS**: Styling and responsive design

### Processing & Indexing
- **Document Parsers**: PDF extraction, HTML parsing
- **Text Chunking**: Semantic and structural splitting
- **Embedding Pipeline**: Batch processing and optimization

## Images

<img src="https://raw.githubusercontent.com/DMontgomery40/agro-rag-engine/main/assets/agro-banner.svg" alt="Agro RAG Engine Banner" style="max-width: 100%; border-radius: 10px; margin: 1rem 0;">

### Dashboard Interface

<img src="https://raw.githubusercontent.com/DMontgomery40/agro-rag-engine/main/assets/dashboard.png" alt="Dashboard" style="max-width: 100%; border-radius: 10px; margin: 1rem 0;">

### Chat Interface

<img src="https://raw.githubusercontent.com/DMontgomery40/agro-rag-engine/main/assets/chat%20tab.png" alt="Chat Tab" style="max-width: 100%; border-radius: 10px; margin: 1rem 0;">

### Metrics & Monitoring

<img src="https://raw.githubusercontent.com/DMontgomery40/agro-rag-engine/main/assets/grafana-metrics.png" alt="Grafana Metrics" style="max-width: 100%; border-radius: 10px; margin: 1rem 0;">

## Use Cases

### Agricultural Extension Services

Provide expert advice at scale:

- **Farmer Q&A**: Answer common questions about crops, pests, and practices
- **Seasonal Guidance**: Deliver timely advice based on growing seasons
- **Local Recommendations**: Tailor responses to regional conditions
- **Knowledge Accessibility**: Make extension research accessible to all farmers

### Research & Development

Accelerate agricultural research:

- **Literature Review**: Quickly find relevant research across publications
- **Trend Analysis**: Identify emerging topics and research directions
- **Gap Identification**: Discover under‑researched areas
- **Cross‑Pollination**: Connect insights from different agricultural domains

### Education & Training

Support agricultural education:

- **Interactive Learning**: Students can query agricultural knowledge bases
- **Curriculum Support**: Ground coursework in authoritative sources
- **Self‑Paced Study**: Enable independent exploration of topics
- **Practical Guidance**: Connect theory to practical application

## Pipeline Workflow

1. **Ingestion**: Load agricultural documents from various sources
2. **Chunking**: Split documents into semantic chunks respecting structure
3. **Embedding**: Convert chunks to vector representations
4. **Indexing**: Store embeddings in vector database with metadata
5. **Query**: User submits a natural language question
6. **Retrieval**: Find most relevant chunks via similarity search
7. **Orchestration**: Compose prompt with query and retrieved context
8. **Generation**: LLM generates grounded response
9. **Attribution**: Return answer with source citations

## Getting Started

### Installation

```bash
# Clone the repository
git clone https://github.com/DMontgomery40/agro-rag-engine.git
cd agro-rag-engine

# Install Python dependencies
pip install -r requirements.txt

# Install UI dependencies
cd ui
npm install
cd ..
```

### Configuration

Set up your environment:

```env
# Vector database
VECTOR_DB_TYPE=chroma
VECTOR_DB_PATH=./data/vector_db

# Embedding model
EMBEDDING_MODEL=sentence-transformers/all-MiniLM-L6-v2

# LLM API
OPENAI_API_KEY=your_api_key_here
LLM_MODEL=gpt-4

# Chunking parameters
CHUNK_SIZE=512
CHUNK_OVERLAP=50
```

### Ingest Documents

```bash
# Ingest a directory of agricultural documents
python scripts/ingest.py --input ./documents/agricultural-guides --recursive
```

### Run Demo UI

```bash
# Start the backend
python app.py

# Start the frontend (in another terminal)
cd ui
npm run dev
```

Visit `http://localhost:3000` to interact with the demo UI.

### Query via API

```bash
# Query the RAG engine
curl -X POST http://localhost:8000/query \
  -H "Content-Type: application/json" \
  -d '{
    "question": "What are best practices for corn pest management?",
    "num_results": 5
  }'
```

## Links

- **GitHub Repository**: [https://github.com/DMontgomery40/agro-rag-engine](https://github.com/DMontgomery40/agro-rag-engine)
- **Documentation**: Available in the repository
- **Issue Tracker**: [GitHub Issues](https://github.com/DMontgomery40/agro-rag-engine/issues)

---

*agro‑rag‑engine demonstrates how domain‑focused RAG systems can provide more accurate and useful responses than general‑purpose AI by grounding outputs in authoritative sources.*
