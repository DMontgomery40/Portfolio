---
layout: page
title: agro-rag-engine
description: Enterprise-grade local-first RAG workspace for codebases - 240K+ LOC platform with self-learning transformer, hybrid search, and full observability stack
tags: [Python, TypeScript, RAG, FastAPI, React, Qdrant, LangGraph, Cross-Encoder, MCP]
date: 2025-01-01
featured: true
---

# agro-rag-engine

<div class="project-header">
    <div class="project-badges">
        <span class="badge badge-primary">RAG</span>
        <span class="badge badge-primary">ML Pipeline</span>
        <span class="badge badge-secondary">Python</span>
        <span class="badge badge-secondary">TypeScript</span>
        <span class="badge badge-info">FastAPI</span>
        <span class="badge badge-info">React</span>
        <span class="badge badge-info">Qdrant</span>
    </div>
    <div class="project-links-header">
        <a href="https://github.com/DMontgomery40/agro-rag-engine" class="btn btn-primary" target="_blank">
            <i class="fab fa-github"></i> View on GitHub
        </a>
        <a href="https://dmontgomery40.github.io/agro-rag-engine/" class="btn btn-secondary" target="_blank">
            <i class="fas fa-book"></i> Documentation
        </a>
    </div>
</div>

## Overview

**agro-rag-engine** is an enterprise-grade, local-first **RAG Engine Workspace** for codebases. This isn't a demo or tutorial—it's a **240,000+ line production platform** featuring:

- **Self-Learning Transformer Model** that continuously improves from usage feedback
- **Full ML Pipeline**: mine triplets → train cross-encoder → evaluate → hot-reload to production
- **Rich GUI** with onboarding wizard, embedded VSCode, and Grafana dashboards
- **28 API Router Modules** (~5,000 lines of endpoint code)
- **MCP Servers** in Python and Node.js with 4 transport types (HTTP, SSE, STDIO, WebSocket)
- **Comprehensive Eval System** with golden tests, regression analysis, and MRR/Hit@K metrics

I built agro-rag-engine because existing RAG solutions were either toy demos or black boxes. I needed a system where I could point at any repo (or ten repos), index once, and live in a tight "ask → inspect citations → fix → re-ask" loop—with every knob explainable and every metric measurable.

---

## The Self-Learning Reranker

This is the crown jewel. AGRO includes a **complete ML pipeline** for training a cross-encoder specifically on YOUR codebase:

```
User searches → Clicks result → Feedback logged
                    ↓
        Mine triplets (query, good_doc, bad_doc)
                    ↓
        Train cross-encoder model
                    ↓
        Evaluate on golden tests (MRR, Hit@K)
                    ↓
        Hot-reload to production (no restart)
                    ↓
        Search quality improves automatically
```

The reranker GUI (28KB of JavaScript) tracks:
- **Implicit feedback**: Which code chunks users click on
- **Explicit feedback**: Thumbs up/down on search results
- **Real-time events**: Sent to `/api/telemetry/event` immediately

Training uses **triplet loss** to push relevant docs closer to queries. Models hot-reload every 60 seconds—no server restart required.

---

## Hybrid Search Architecture

AGRO doesn't pick one search strategy—it fuses them:

```
User Query
    ↓
┌─────────────────┬─────────────────┐
│  BM25 Sparse    │  Qdrant Vector  │
│  (keyword match)│  (semantic)     │
└────────┬────────┴────────┬────────┘
         │    RRF Fusion   │
         └────────┬────────┘
                  ↓
         Cross-Encoder Rerank
                  ↓
         Top K Results with Citations
```

**Configurable per-profile:**

| Profile | Embedding | Reranker | Retrieval |
|---------|-----------|----------|-----------|
| Docs-search (fast) | BGE-small (local) | bge-reranker-v2-m3 | BM25 only |
| Plan_Refactor (quality) | text-embedding-3-large | cohere/rerank-3.5 | BM25+Redis+Qdrant |

---

## Full Feature List

### Core RAG
- **Hybrid search**: BM25 (bm25s + Stemmer) + Qdrant dense vectors
- **RRF fusion** with configurable weights
- **Multi-query expansion**: Generate N query variants for broader recall
- **Cross-encoder reranking**: Local or cloud (Cohere, Voyage)
- **Confidence gating**: Filter by top1/avg5 thresholds
- **Local hydration**: Expand context around matches

### ML Pipeline
- **Triplet mining** from user feedback logs or golden tests
- **Cross-encoder training** with sentence-transformers
- **Evaluation harness**: MRR, Hit@1, Hit@3, Hit@5, Hit@10
- **Model promotion** with hot-reload
- **Regression analysis** against baselines

### Infrastructure
- **28 FastAPI routers** covering every operation
- **Pydantic config validation** with GUI propagation
- **Docker Compose** for Qdrant, Redis, Grafana, Prometheus
- **Embedded Grafana** with alerting on any metric
- **LangSmith + OpenAI Agents SDK** tracing

### MCP Integration
- **Python MCP server** (stdio + HTTP)
- **Node.js MCP server** (stdio + SSE + WebSocket)
- **Per-transport model configuration**
- **Direct Claude Code / Codex integration**

### GUI
- **React/Vite dashboard** with real-time search
- **Onboarding wizard** for repo setup
- **Embedded VSCode** (optional)
- **Profile management** for different use cases
- **Golden test editor** in-browser
- **Cost estimation** before running expensive profiles

---

## Repository Layout

| Folder | What Lives There | LOC |
|--------|------------------|-----|
| `server/` | FastAPI app, 28 routers, services, MCP servers | ~40K |
| `web/` | React/Vite GUI | ~30K |
| `retrieval/` | Hybrid search, embeddings, rerankers | ~15K |
| `indexer/` | Chunking pipeline (AST → BM25 → Qdrant) | ~10K |
| `reranker/` | Learning reranker training + config | ~5K |
| `eval/` | Golden tests, regression harness | ~8K |
| `scripts/` | Training, mining, setup helpers | ~20K |
| `infra/` | Docker, Grafana, Prometheus configs | ~5K |
| `tests/` | 200+ test files | ~50K |
| `docs/` | MkDocs documentation | ~20K |

---

## Why This Matters

Working with Claude Code and Codex, I found that **retrieval quality is the bottleneck**. Generic RAG solutions:
- Don't understand code structure (AST, imports, function boundaries)
- Can't be tuned for specific codebases
- Lack proper evaluation and regression testing
- Don't explain WHY an answer was produced

agro-rag-engine solves all of these:

1. **Code-aware chunking** using AST parsing
2. **Trainable reranker** that learns from YOUR usage
3. **Golden test framework** with regression analysis
4. **Full traceability** so you know exactly why results appear

The result: **massive reduction in token usage** with Claude Code/Codex, and **greatly increased accuracy** in generated code.

---

## Quick Start

```bash
git clone https://github.com/DMontgomery40/agro-rag-engine.git
cd agro-rag-engine
make dev  # Starts Qdrant, Redis, API, GUI, MCP servers

# GUI at http://127.0.0.1:8012/
# API docs at http://127.0.0.1:8012/docs
```

---

## Links

- **GitHub**: [github.com/DMontgomery40/agro-rag-engine](https://github.com/DMontgomery40/agro-rag-engine)
- **Documentation**: [dmontgomery40.github.io/agro-rag-engine](https://dmontgomery40.github.io/agro-rag-engine/)
- **API Reference**: [docs/API_REFERENCE.md](https://github.com/DMontgomery40/agro-rag-engine/blob/main/docs/API_REFERENCE.md)
