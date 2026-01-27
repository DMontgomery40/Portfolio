---
layout: project
title: "local-explainer-video"
description: "AI-powered text-to-video system that converts documents into narrated, illustrated MP4 videos"
repository: "https://github.com/DMontgomery40/local-explainer-video"
tags: [Python, Streamlit, TTS, Image Generation, Video, Claude, GPT]
category: ai-ml
featured: true
status: Active
last_updated: 2026-01-26
---

# local-explainer-video

**Document-to-Video AI Pipeline**

Transform dense documents (qEEG reports, technical docs, research papers) into AI-narrated, visually illustrated MP4 videos. The system uses LLMs as "directors" to storyboard scenes, generate images, synthesize speech, and assemble the final video.

---

## The Problem

Technical documents are hard to understand. Patients receive medical reports full of jargon. Developers write docs nobody reads. This tool converts any document into an engaging video explanation.

---

## Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                  local-explainer-video                       │
├─────────────────────────────────────────────────────────────┤
│                                                               │
│  Input Document (PDF, Markdown, Text)                        │
│     ↓                                                         │
│  LLM Director (Claude/GPT)                                   │
│     ├─ Parse document structure                              │
│     ├─ Generate scene breakdown                              │
│     └─ Write narration scripts                               │
│     ↓                                                         │
│  Asset Generation (Parallel)                                 │
│     ├─ TTS: Kokoro / ElevenLabs / OpenAI                     │
│     └─ Images: Replicate / DashScope Qwen                    │
│     ↓                                                         │
│  Video Assembly (MoviePy + ffmpeg)                           │
│     ├─ Sync audio to visuals                                 │
│     ├─ Add transitions                                       │
│     └─ Export MP4                                            │
│     ↓                                                         │
│  QC Review (Gemini Vision)                                   │
│     └─ Visual inspection for artifacts                       │
│                                                               │
└─────────────────────────────────────────────────────────────┘
```

---

## Key Features

### LLM-Directed Storyboarding
- **Scene Planning**: LLM breaks document into logical segments
- **Visual Direction**: AI describes what each scene should show
- **Narration Writing**: Natural, conversational script generation

### Multi-Provider TTS
- **Kokoro**: Local, free, fast
- **ElevenLabs**: Premium voice quality
- **OpenAI TTS**: Consistent, reliable

### AI Image Generation
- **Replicate**: Stable Diffusion, FLUX models
- **DashScope Qwen**: Fast, cost-effective
- **Image Editing**: AI can modify/enhance generated images

### Video Assembly
- **MoviePy**: Pythonic video editing
- **ffmpeg**: Professional encoding
- **Transitions**: Fade, dissolve, cut
- **Timing**: Audio-synced visual pacing

### Quality Control
- **Gemini Vision**: Automated visual inspection
- **Artifact Detection**: Catch rendering issues
- **Scene Regeneration**: Fix individual scenes without full re-render

---

## Streamlit UI

Beautiful web interface for:
- Document upload (PDF, MD, TXT)
- Style selection (educational, corporate, casual)
- Voice selection (multiple providers)
- Real-time generation progress
- Scene-by-scene preview and regeneration

---

## Integration with qEEG Council

This tool is designed to work with [qEEG Council]({{ site.baseurl }}/projects/qeeg-council/):

```
Patient's qEEG Report
    ↓
qEEG Council (multi-LLM analysis)
    ↓
Consensus Report (markdown)
    ↓
local-explainer-video
    ↓
Patient-Friendly Video Explanation
```

---

## Tech Stack

| Component | Technology |
|-----------|------------|
| UI | Streamlit |
| LLM Director | Claude 3.5 / GPT-4 |
| TTS | Kokoro, ElevenLabs, OpenAI |
| Image Gen | Replicate, DashScope |
| Video | MoviePy, ffmpeg |
| QC | Gemini 1.5 Pro Vision |

---

## Why This Matters

This project demonstrates:

1. **Multimodal AI Orchestration**: Text → Image → Audio → Video
2. **Complex Prompt Engineering**: LLM as creative director
3. **Multi-Provider Integration**: Fallbacks and cost optimization
4. **Production Pipeline**: Error handling, regeneration, QC
5. **Real-World Application**: Medical patient education

---

## Links

- [GitHub Repository](https://github.com/DMontgomery40/local-explainer-video)
