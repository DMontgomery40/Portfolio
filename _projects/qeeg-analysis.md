---
layout: project
title: "qEEG Council"
description: "6-stage LLM deliberation workflow for analyzing qEEG/ERP reports, with multi-model peer review and clinician portal publishing."
image: /assets/images/qeeg-analysis.png
repo: https://github.com/DMontgomery40/qEEG-analysis
tags:
  - Neuroscience
  - qEEG
  - Multi-Model
  - Healthcare
featured: true
order: 9
---

qEEG Council is a multi-model AI deliberation system for analyzing quantitative EEG and event-related potential reports. It orchestrates a 6-stage workflow across multiple LLM providers -- OpenAI, Anthropic, and Google -- via a CLIProxyAPI router. The deliberation pattern (initial analysis, anonymized peer review, revision, consolidation, final review vote, and publication-ready draft) produces higher-quality clinical reports than any single model pass.

## Key Features

- **6-stage multi-model deliberation** with peer review and revision cycles
- **Multimodal analysis** -- vision-capable models receive PDF page images in Stage 1
- **Patient management** with report upload, OCR via Tesseract, and page extraction
- **SSE-streamed real-time progress** during analysis runs
- **Explainer video pipeline integration** with clinician portal publishing
- **Markdown and PDF export** for the final consolidated report

## Technical Architecture

The backend is FastAPI with SQLite for patient and report management. PDF uploads are processed with Tesseract OCR for text extraction and page image rendering for vision-capable models. The 6-stage pipeline routes through multiple LLM providers, with each model producing independent analysis before the anonymized peer review stage.

The consolidation stage synthesizes all model revisions into a unified report, and a final review vote determines publication readiness. The React/Vite frontend provides real-time progress via server-sent events. The platform also integrates with an explainer video pipeline for patient education, with QC verification against council artifacts and automatic publishing to a clinician portal sync folder.

Released under a noncommercial license.
