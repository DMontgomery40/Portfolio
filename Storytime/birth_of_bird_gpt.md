---
layout: default
title: The Birth of BirdStatsGPT
parent: Storytime
nav_order: 6
---

# The Birth of BirdStatsGPT

I discovered the BirdNet Pi project on GitHub. BirdNet Pi is a project based on the BirdNet Analyzer by Cornell Lab of Ornithology. Anybody can download an app called Merlin to your phone totally free and it will tell you exactly what bird you're hearing and a bunch of fun facts, etc. It's pretty cool. I wanted to take a deeper dive into this, the back end of this AI technology. 

So, a BirdNet Pi is essentially Merlin, but it's always running in the background. And it runs inference locally, which was also very intriguing to me. No cloud, but a little tiny device that could run TensorFlow Lite completely local on such a tiny processor with 4 gigs of RAM.

This was my first interaction with AI outside of natural language processing and purely just language models. The BirdNet analyzer does not analyze sound at all. That's actually a lot harder. What it does is object detection or image classification. It takes the spectrogram left by the vocalization of the bird and compares that. This was my first lesson on the efficiency of CNN architecture for the simplification and speed and low latency of analyzing a 2D spectrogram, as opposed to the RNN approach of actually analyzing a WAV sound file.

[Next Chapter: Accidental Enterprise AI](/Portfolio/Storytime/accidental_enterprise_ai.html)
