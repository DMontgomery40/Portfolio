---
layout: project
title: "Ragweld"
description: "Open-source MLOps platform for API-first RAG and agent systems with versioned config, tri-hybrid retrieval, and MCP integration."
image: /assets/images/ragweld.png
repo: https://github.com/DMontgomery40/ragweld
live_url: https://ragweld.com
tags:
  - RAG
  - MLOps
  - MCP
  - Knowledge Graph
featured: true
order: 1
---

Ragweld is a full-stack MLOps platform for building and operating RAG and agent systems. It runs three retrieval methods in parallel -- vector search via pgvector, sparse BM25 search via PostgreSQL full-text search, and graph traversal via Neo4j -- then fuses their results with reciprocal rank fusion and optional reranking. The result is a retrieval layer that covers semantic similarity, lexical precision, and relational structure simultaneously.

The platform is API-first, with independent model and provider routing for API, chat, CLI, and MCP channels. All configuration is Pydantic-backed and versioned, with over 500 tunable parameters exposed via both UI and API.

## Key Features

- **Tri-hybrid retrieval** -- vector, sparse, and graph search with reciprocal rank fusion
- **Embedded MCP server** on Streamable HTTP for Claude Desktop and IDE integration
- **Dual training studios** with checkpoint promote/rollback and run telemetry
- **Synthetic Data Lab** for eval datasets, semantic cards, and autotune patches
- **Knowledge graph** with automatic entity extraction and community detection
- **Semantic cache** with recall gates for cost-efficient repeated queries
- **Evaluation workbench** with run diffs for A/B comparison across configurations

## Technical Architecture

Ragweld's backend is Python/FastAPI with PostgreSQL (pgvector for embeddings, FTS for sparse retrieval) and Neo4j for the knowledge graph layer. The frontend is React/TypeScript. Observability is built in through Grafana and Loki integration, with tracing across the full retrieval and generation pipeline.

Training workflows use manifest-backed artifact management with provenance tracking. The Synthetic Data Lab generates evaluation datasets and autotune patches, feeding into the dual training studios where operators can fine-tune both a learning reranker and an in-product agent model. All training runs are instrumented with telemetry for reproducibility.

The platform ships 500+ config parameters, but operators interact with them through sensible defaults and progressive disclosure -- you only touch what you need to.
