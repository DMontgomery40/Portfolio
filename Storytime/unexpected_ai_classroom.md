---
layout: default
title: The Unexpected AI Classroom
parent: Storytime
nav_order: 4
---

# unexpected_ai_classroom.md

BirdNet Pi turned out to be my gateway drug into practical AI applications. Based on Cornell Lab of Ornithology's BirdNet Analyzer, it's essentially the always-on version of their Merlin app. But what fascinated me most was how it worked under the hood.

The system doesn't actually analyze bird sounds directly - that would be too computationally intensive for a Pi. Instead, it performs image classification on spectrograms of bird calls. This was my first exposure to CNN architecture in a practical setting, and watching TensorFlow Lite run inference locally on a tiny Pi with just 4GB of RAM was mind-blowing. The efficiency of analyzing a 2D spectrogram versus processing raw WAV files through an RNN was a masterclass in practical AI implementation.

This project taught me more about AI architectures than any online course could have. It showed me how clever design choices and optimization could make AI accessible even on modest hardware. Who knew that identifying a chickadee would teach me so much about neural networks?

[Next Chapter: Surveillance State for Songbirds](surveillance_state_for_songbirds.html)
