---
layout: project
title: "GaitSignal"
description: "Live football pricing-edge concept demo using player-specific movement surprise and venue-grade tracking for in-play market information."
image: /assets/images/gaitsignal.png
repo: https://github.com/DMontgomery40/GaitSignal
tags:
  - Sports Analytics
  - Football
  - Biomechanics
  - In-Play
featured: true
order: 6
---

GaitSignal is a synthetic React prototype demonstrating how contracted in-stadium player tracking combined with player-specific movement models could surface in-play pricing edges before standard market digestion. The core thesis: per-player temporal models with prediction-surprise scoring, gated by football context (possession, ball access, pitch zone, role demand), reveal commercially relevant signals that universal thresholds miss.

This is a concept demo -- the companion piece to Acoustic Momentum. One modality from the player, one from the crowd. Both explore in-play information that the market may not yet fully price.

## Key Features

- **Player-specific movement surprise scoring** with football context gating
- **Synthetic biomechanical vector generation** for three match scenarios (Saka recovery-run reprice, Pedri press-decay edge, Musiala contact reset)
- **Trading desk UI** with match state, player motion lens, pricing workflow timeline, and in-play pricing edge panels
- **Football-native workflow** -- venue-grade data assumption, not reskinned basketball analytics
- **Companion concept** to Acoustic Momentum for multi-modal pricing edge exploration

## Technical Architecture

The demo generates synthetic 20-feature biomechanical vectors, player-specific movement-surprise proxies, and venue-style football context streams. The UI is built in React with TypeScript, using D3.js and Recharts for visualization. It is organized like a live trading desk -- multiple coordinated panels showing match state, individual player motion analysis, pricing workflow progression, and edge state indicators.

Three built-in scenarios demonstrate different signal patterns: a recovery-run reprice event, a press-decay edge, and a contact reset. Each scenario shows how the same pipeline produces different actionable signals depending on player role, pitch zone, and match context.
