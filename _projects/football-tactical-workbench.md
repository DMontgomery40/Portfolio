---
layout: project
title: "Football Tactical Workbench"
description: "Browser-first football analysis workbench with YOLO detection, tracking, automatic pitch calibration, and detector fine-tuning studio."
image: /assets/images/football-tactical-workbench.png
repo: https://github.com/DMontgomery40/football-tactical-workbench
tags:
  - Sports Analytics
  - Computer Vision
  - YOLO
  - Football
featured: true
order: 5
---

Football Tactical Workbench is a browser-first analysis and detector fine-tuning platform built with React and FastAPI. It has three top-level surfaces: an Analysis Workspace for loading clips, streaming live preview, and reviewing overlay/diagnostics; a Training Studio for scanning YOLO datasets, fine-tuning from the football-pretrained soccana detector, and managing checkpoints; and a Benchmark Lab for running suite-by-recipe benchmark matrices across detectors and pipelines.

## Key Features

- **Browser-first analysis workspace** with live video preview and overlay export
- **Training Studio** for YOLO detector fine-tuning with checkpoint management
- **Benchmark Lab** with suite-by-recipe matrices and multi-metric comparison
- **Automatic pitch calibration** using soccana_keypoint field registration (refreshed every 10 frames)
- **Hybrid appearance-aware player tracking** with jersey-colour home/away team separation

## Technical Architecture

The active analysis pipeline uses soccana for player/referee/ball detection, hybrid appearance-aware tracking with tracklet stitching, jersey-colour-based team separation, and soccana_keypoint field registration for automatic pitch calibration. Live preview streams directly to the browser.

Training runs in isolated Python subprocesses with full config, logs, and artifact persistence. The Benchmark Lab supports first-class recipes including `detector:soccana`, `pipeline:soccermaster`, and `pipeline:tracklab-sn-gamestate`, with matrix-synced charts and explicit handling of blocked or unsupported suite cells.

On Apple Silicon, detector inference uses MPS while field calibration falls back to CPU. The platform integrates with the SoccerNet ecosystem and provides three distinct product surfaces covering the full workflow from analysis through training to benchmarking.
