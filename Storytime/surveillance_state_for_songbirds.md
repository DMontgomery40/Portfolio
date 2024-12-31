---
layout: default
title: Surveillance State for Songbirds
parent: Storytime
nav_order: 5
---

# Surveillance State for Songbirds

Once I started combining cameras with home automation, things escalated quickly. I needed a bird feeder cam, a bird bath cam, and a proper NVR setup. I set up a home server running Scrypted as the NVR  and dove deep into training YOLO models on OpenVINO, specifically leveraging the optimization capabilities of OpenVINO's architecture with Intel's low-power iGPU.

While I later discovered that Scrypted had solid detection models built in, they weren't specialized for bird species detection. This led me down the fascinating rabbit hole of training custom models. I started pulling datasets from CalTech and iNaturalist and quickly discovered why bird classification is an exceptional challenge in computer vision.

The technical challenges were numerous:
- Birds molt multiple times per year, completely changing their appearance
- Classification needs to be sensitive to both precise location and time of year
- Many species, especially in the sparrow and finch families, are nearly identical
- Hybrid species introduce edge cases that even expert naturalists debate
- Varying light conditions and angles make feature detection incredibly complex
- Training data needs to account for seasonal variations in plumage

I ended up implementing a multi-stage classification pipeline that considered temporal and geographical context alongside visual features, significantly improving accuracy over standard object detection approaches.

[Next Chapter: The Birth of BirdStatsGPT](/Portfolio/Storytime/birth_of_bird_gpt.html)
