---
layout: project
title: "qEEG Council"
description: "6-stage multi-LLM deliberation workflow for analyzing brain scan reports with consensus review"
repository: "https://github.com/DMontgomery40/qEEG-analysis"
tags: [Python, FastAPI, React, Multi-LLM, Vision AI, Medical AI]
category: ai-ml
featured: true
status: Active
last_updated: 2026-01-26
---

# qEEG Council

**Multi-LLM Deliberation Workflow for Medical Report Analysis**

A sophisticated 6-stage pipeline that orchestrates multiple LLMs (GPT-4o, Claude 3+, Gemini 1.5+) to analyze qEEG/ERP brain scan reports. Each model reviews the document independently, then a consolidation stage synthesizes findings into a consensus report.

---

## The Problem

qEEG (Quantitative Electroencephalogram) reports are dense medical documents containing:
- Brain wave frequency analysis
- Coherence/connectivity maps
- Comparison to normative databases
- Clinical interpretations

A single LLM can miss nuances or hallucinate. This system uses **multi-model consensus** to improve accuracy.

---

## Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                     qEEG Council                             │
├─────────────────────────────────────────────────────────────┤
│                                                               │
│  Stage 1: PDF Upload + OCR Extraction                        │
│     ↓                                                         │
│  Stage 2: Parallel Analysis (3 Vision Models)                │
│     ├─ GPT-4o Analysis                                       │
│     ├─ Claude 3.5 Sonnet Analysis                            │
│     └─ Gemini 1.5 Pro Analysis                               │
│     ↓                                                         │
│  Stage 3: Cross-Model Comparison                             │
│     ↓                                                         │
│  Stage 4: Discrepancy Resolution                             │
│     ↓                                                         │
│  Stage 5: Consensus Building                                 │
│     ↓                                                         │
│  Stage 6: Final Report Generation                            │
│                                                               │
└─────────────────────────────────────────────────────────────┘
```

---

## Key Features

### Multi-Model Orchestration
- **CLIProxyAPI Router**: Unified interface to OpenAI, Anthropic, Google
- **Parallel Processing**: All 3 models analyze simultaneously
- **Streaming Responses**: Real-time progress via SSE

### Vision-First Analysis
- **PDF → Image Conversion**: Each page rendered for vision models
- **Multimodal Understanding**: Models see charts, graphs, brain maps
- **OCR Fallback**: Text extraction for models without vision

### Deliberation Logic
- **Agreement Detection**: Identify where models align
- **Discrepancy Flagging**: Highlight conflicts for human review
- **Confidence Scoring**: Weight findings by model agreement

### Production-Ready
- **FastAPI Backend**: Async, scalable API
- **React Frontend**: Real-time streaming UI
- **SQLite Storage**: Artifact and session management
- **Docker Deployment**: Single-command startup

---

## Tech Stack

| Layer | Technology |
|-------|------------|
| Backend | Python 3.11+, FastAPI |
| Frontend | React, Vite |
| LLM Router | CLIProxyAPI (custom) |
| Models | GPT-4o, Claude 3.5, Gemini 1.5 |
| Database | SQLite |
| PDF Processing | pdf2image, pytesseract |

---

## Why This Matters

This project demonstrates:

1. **LLM Orchestration**: Managing multiple models with different strengths
2. **Multimodal RAG**: Treating PDFs as images, not just text
3. **Consensus Algorithms**: Resolving model disagreements
4. **Medical Domain Expertise**: Understanding specialized vocabulary
5. **Production Architecture**: FastAPI + React + streaming

---

## Integration with local-explainer-video

The qEEG Council output feeds into [local-explainer-video]({{ site.baseurl }}/projects/local-explainer-video/) to generate patient-friendly explanation videos. The full pipeline:

```
qEEG PDF → qEEG Council Analysis → Explainer Video Script → AI-Narrated MP4
```

---

## Links

- [GitHub Repository](https://github.com/DMontgomery40/qEEG-analysis)
