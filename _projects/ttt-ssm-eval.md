---
layout: project
title: "TTT SSM Eval"
description: "Safety research infrastructure for Test-Time Training with external safety gates, canary rollback, and wake/sleep consolidation."
image: /assets/images/ttt-ssm-eval.png
repo: https://github.com/DMontgomery40/ttt_ssm_eval
tags:
  - Safety
  - State Space Models
  - Test-Time Training
  - PyTorch
featured: true
order: 8
---

ttt_ssm_eval is research infrastructure for studying how to make Test-Time Training safe. The core problem: in standard transformers, garbage in means garbage out. In TTT, garbage in means garbage *learned*. This repo implements safety checks deliberately outside the computation graph -- gradients cannot flow through regex gates, making them immune to gradient-based bypass attacks.

Implements the approach described in [arXiv 2407.04620](https://arxiv.org/abs/2407.04620).

## Key Features

- **External safety gates** immune to gradient-based bypass attacks (outside the computation graph)
- **Canary rollback** with pre/post update probing and threshold breach detection
- **Wake/sleep consolidation** -- fast per-session weights (hippocampus) + offline core model updates (neocortex)
- **Branchable artifact store** ("git for plastic weights") with session forking
- **React dashboard** for real-time safety mechanism observation across three domains

## Technical Architecture

The architecture stacks four defense layers with different failure modes: a fast static gate for known attack patterns and entropy anomalies, dynamic canary probes for catastrophic corruption detection, a slow auditor for cross-session pattern detection, and human review as the final layer.

The complementary learning system is inspired by biological memory. Fast context weights update per-session (analogous to hippocampal learning), core model weights are frozen during inference (analogous to neocortical storage), and offline sleep consolidation replays filtered chat traces into the core model.

The repo includes three domains: a Nano SSM with branchable plastic matrices and system identification benchmarks, a TTT Sentry monitor with instrumented safety loops, and a TinyLM chat system with per-session fast weights trained via Muon optimizer. All three domains are observable through a unified React dashboard.
