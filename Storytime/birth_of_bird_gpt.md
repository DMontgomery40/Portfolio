---
layout: default
title: The Birth of BirdStatsGPT
parent: Storytime
nav_order: 6
---

# BirdStatsGPT (and now MCP)

Another challenge I considered was combining visual and audio detection into a unified system. While no one has fully solved this yet due to the complexity of directionalizing cardioid microphone patterns with the required sensitivity levels, the project led me into some fascinating work with large language models.

I built a Model Context Protocol server and Custom GPT to interface between two major bird databases - eBird and BirdWeather.app (where BirdNetPi uploads its data). Both have powerful and complex APIs, so I created a natural language interface to analyze and compare data between them, and vizualize relationships. This allows people to ask questions like "Has anyone else in my area reported cedar waxwings since my system detected one this morning?" or "Show me migration patterns for my top detected species over the last two years."

The scale of data made this particularly interesting - my station alone generates around a million detection points annually. Being able to efficiently process and compare this against broader regional data opened up endless possibilities for pattern analysis and visualization, especially for understanding unusual sightings and migration patterns. None of those insights are novel, but one would have to be well versed in R and Python to garner that data. Now it's accessible via a poorly worded prompt, and it's neat to see people are enjoying it. 

[Next Chapter: Accidental Enterprise AI](/Portfolio/Storytime/accidental_enterprise_ai.html)
