---
layout: project
title: "Ragweld Crucible"
description: "Operator range planner for estimating training cost, VRAM fit, and GPU availability across providers."
image: /assets/images/ragweld-crucible.png
repo: https://github.com/DMontgomery40/ragweld-crucible
live_url: https://ragweld.com/crucible/
tags:
  - MLOps
  - GPU
  - Training Cost
  - VRAM
featured: true
order: 4
---

Crucible is the estimator workbench behind [ragweld.com/crucible](https://ragweld.com/crucible/). It combines model metadata, hardware reference data, provider pricing, and planning heuristics so operators can compare likely training ranges before committing a run. Instead of guessing whether a fine-tune fits in VRAM or how much it will cost across providers, Crucible gives you a concrete range estimate upfront.

## Key Features

- **Training cost estimation** across GPU providers and hardware configurations
- **VRAM fit calculator** with model metadata and hardware reference data
- **Math code workbench** for inspecting the implementation behind planner calculations
- **Model catalog** with automated refresh scripts for up-to-date metadata
- **Shareable planning sessions** with URL-encoded state for team collaboration

## Technical Architecture

The front-end is a React + TypeScript + Vite application with estimator logic, normalization rules, and planner math in a dedicated engine module. It ships with reference datasets for model catalogs, GPU specs, and pricing fallback data.

This repository is a public mirror of the crucible subtree from the larger ragweld.com site repo, containing the full front-end app, estimator logic, data catalogs, and tests. The live production surface also depends on Netlify Functions from the parent repo for dynamic pricing data. Tests run via Vitest.
