---
layout: project
title: "Cathode"
description: "Local-first explainer video pipeline with React/FastAPI control room, MCP server, and Remotion-backed motion rendering."
image: /assets/images/cathode.png
repo: https://github.com/DMontgomery40/cathode
tags:
  - Video Generation
  - MCP
  - Remotion
  - React
featured: true
order: 2
---

Cathode is a local-first video generation pipeline that turns rough notes, source text, or a finished script into a rendered MP4. It operates through four distinct lanes: a React/FastAPI control room, a legacy Streamlit app, an MCP server for agent-driven runs, and a live product demo capture workflow.

The pipeline supports three composition modes -- classic (image + video with ffmpeg), hybrid (mixed media with Remotion), and motion-only (template-driven motion scenes). Narration audio drives all timing, keeping scenes synchronized across render backends.

## Key Features

- **Brief-driven storyboard generation** with multiple composition modes
- **React/FastAPI control room** with background job pipeline and live status
- **MCP server** for agent-driven video generation from Claude or other MCP clients
- **Live demo capture** using Playwright with structured QC review loop
- **Local-first rendering** with Remotion, ffmpeg, and hardware H.264 encoding
- **Pluggable providers** for storyboard generation, image creation, TTS, and video rendering

## Technical Architecture

Cathode is env-driven with pluggable providers at every stage. For narration, it supports Kokoro TTS locally or cloud TTS services. Image generation can run locally via Qwen on MLX or through cloud APIs. Video rendering uses either ffmpeg for simple compositions or Remotion for template-driven motion scenes.

The live demo lane uses Playwright to capture real running applications, with a sub-agent evaluating extracted frames in a structured QC review loop before the final render. All project state, storyboards, and job logs persist locally under a `plan.json` source of truth.

The MCP server exposes the full pipeline to any MCP client, so an AI assistant can generate, review, and iterate on explainer videos within a single conversation.
