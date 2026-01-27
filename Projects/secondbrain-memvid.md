---
layout: project
title: "SecondBrain + MemVid"
description: "Local-first visual memory system with RAG-enabled video search using MemVid and DeepSeek-OCR"
repository: "https://github.com/DMontgomery40/secondbrain"
tags: [Python, RAG, OCR, MemVid, Streamlit, ChromaDB, Vision AI]
category: ai-ml
featured: true
status: Active
last_updated: 2025-10-27
---

# SecondBrain + MemVid + DeepSeek-OCR

**Local-first visual memory system with RAG-enabled video search**

SecondBrain continuously captures your screen, extracts text via local OCR, and stores everything in a searchable RAG pipeline. Combined with MemVid for video-based memory storage and DeepSeek-OCR for enhanced document understanding, this is a complete **visual memory RAG system**.

---

## Why This Matters for RAG

This project demonstrates **cutting-edge RAG techniques** applied to visual/multimodal data:

- **Hybrid Search**: FTS5 full-text search + ChromaDB vector embeddings (MiniLM)
- **MemVid Integration**: Pack screen captures into `.mv2` video memory files with BM25 search
- **DeepSeek-OCR Enhancement**: Vision model extracts structured markdown from dense screenshots
- **99.3% Storage Compression**: 216 GB/day → 1.4 GB/day via smart capture + H.264

---

## Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                      Second Brain                            │
├─────────────────────────────────────────────────────────────┤
│                                                               │
│  Capture → OCR → Database → Embeddings → Summaries           │
│     │        │        │          │            │               │
│  Smart   Apple   SQLite    Chroma      GPT-5                  │
│  Frame   Vision   WAL      MiniLM                             │
│  Diff    (local)  Compress                                    │
│                                                               │
│  ↓                                                            │
│  Streamlit UI ← Query API ← Search (FTS5 + Semantic)         │
│                                                               │
└─────────────────────────────────────────────────────────────┘
```

---

## Key Features

### Smart Capture
- **Adaptive FPS**: 1.0 FPS active, 0.2 FPS idle (80% savings during idle)
- **Frame Deduplication**: Perceptual hashing skips identical frames (30-50% savings)
- **Activity Detection**: Keyboard/mouse monitoring for adaptive capture

### Local OCR Pipeline
- **Apple Vision Framework**: Native macOS OCR (< 1s per frame, 95% accuracy)
- **Zero API Cost**: 100% local processing
- **DeepSeek-OCR Enhancement**: For dense documents, run vision model to extract structured markdown

### MemVid Integration
The `sb_pack.py` script demonstrates packing SecondBrain captures into MemVid format:

```python
import memvid_sdk as memvid
from memvid_sdk import create

# Create searchable video memory
mem = create("sb_demo.mv2")
mem.enable_lex()  # BM25 search

# Ingest screenshots with OCR text
mem.put(title, "sb_image", meta, file=img_path, uri=img_uri)
mem.put(title, "sb_ocr_fast", meta, text=ocr_text, uri=ocr_uri)

# DeepSeek-OCR for rich documents
deep_md = run_ollama_dsocr(image_path)  # "deepseek-ocr" model
mem.put(title, "sb_ocr_deep", meta, text=deep_md, kind="markdown")

mem.seal()
```

### Search Capabilities
- **Full-Text Search**: FTS5 with trigram tokenization
- **Semantic Search**: ChromaDB + MiniLM embeddings
- **MemVid BM25**: Lexical search across video memories

---

## Performance

| Metric | Value |
|--------|-------|
| OCR Speed | < 1 second/frame |
| OCR Accuracy | 95% confidence |
| Storage Savings | 99.3% (216 GB → 1.4 GB/day) |
| CPU Usage | ~5% |
| Memory | ~500 MB |

---

## Tech Stack

- **Python 3.11+** - Core runtime
- **Apple Vision** - Native OCR
- **SQLite + WAL** - Frame metadata with compression
- **ChromaDB + MiniLM** - Vector embeddings
- **MemVid SDK** - Video-based memory storage
- **DeepSeek-OCR** - Vision model for document extraction
- **Streamlit** - Review UI
- **ffmpeg** - H.264 video compression

---

## Relevance to Enterprise RAG

This project directly applies to **SpectrumGPT-style systems**:

1. **Multimodal Ingestion**: Images → OCR → Text → Embeddings
2. **Hybrid Retrieval**: Lexical (BM25/FTS5) + Semantic (vectors)
3. **Compression at Scale**: Handle massive data volumes efficiently
4. **Local-First**: Privacy-compliant, on-prem ready
5. **Continuous Learning**: Vision model enhancement of base OCR

---

## Links

- [SecondBrain Repository](https://github.com/DMontgomery40/secondbrain)
- [MemVid SDK](https://github.com/memvid-ai/memvid-sdk)
- [DeepSeek-OCR](https://github.com/deepseek-ai/deepseek-ocr)
