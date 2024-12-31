---
layout: default
title: The Birth of Bird GPT
parent: Storytime
nav_order: 6
---

# The Birth of BirdStatsGPT (and later the Birdstats MCP Server)

After building out the detection system, I faced a new challenge: making sense of the massive amount of data being collected. The BirdWeather.app database and eBird's API both offered valuable data, but their interfaces were cumbersome for complex queries. The former has an API with too few endpoints, the latter has quite the opposite problem (but they're equally cumbersome problems). 

This led me to build a custom GPT-powered interface that could handle natural language queries across both datasets.

The technical implementation involved:
- OpenAI's Assistants endpoint, as well as the 'CustomGPT Interface', with both eBird and Birdweather APIs structured in OpenAPI yaml
- Later on, Creating a Model Context Protocol server to handle the integration 
- Developing a custom prompt engineering system that could translate natural language queries into structured API calls
- Creating a geospatial index to efficiently compare local observations with regional patterns

The system could handle simple queries like:
```
# Example query handling
complex_query = "Compare my BirdNetPi Cedar Waxwing detections 
                with eBird sightings within 5 miles over the last week"

# Translates to structured data operations:
async def process_bird_query(query):
    local_detections = await get_birdnet_detections(
        species="Cedar Waxwing",
        timeframe="7d",
        confidence_threshold=0.85
    )
    
    ebird_sightings = await get_ebird_observations(
        species_code="cedwax",
        lat=station_lat,
        lng=station_lng,
        radius=5,
        days=7
    )
    
    return analyze_detection_patterns(local_detections, ebird_sightings)
```

As well as far more complex research involving historical data across multiple timeframes to track things like changes in migration patterns. 
