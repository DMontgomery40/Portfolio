---
layout: project
title: "Faxbot"
description: "Open-source, self-hostable fax platform with GUI-first Admin Console, multi-backend adapters, MCP integration, and iOS companion app."
image: /assets/images/faxbot.png
repo: https://github.com/DMontgomery40/Faxbot
live_url: https://faxbot.net
tags:
  - HIPAA
  - MCP
  - Self-Hosted
  - iOS
featured: true
order: 10
---

Faxbot is the first and only open-source, self-hostable fax platform with a GUI-first Admin Console. Healthcare still runs on fax -- Faxbot makes it possible to operate that infrastructure without vendor lock-in or black-box SaaS.

It supports over 20 provider backends, from cloud services like Phaxio, Documo, Sinch, and SignalWire to self-hosted options like FreeSWITCH and SIP/Asterisk, with full freedom to mix and match outbound and inbound providers.

## Key Features

- **20+ provider backends** with mix-and-match outbound/inbound support
- **GUI-first Admin Console** with traits-based feature gating (screens render only what the active provider supports)
- **HIPAA-aligned security** -- HMAC webhook verification, short-TTL tokens, compliant logging with no PHI in logs
- **Official MCP servers** in both Node and Python for stdio/HTTP/SSE transport, enabling AI assistant integration
- **iOS companion app** for sending faxes and checking status from mobile
- **Published SDKs** -- `npm install faxbot` and `pip install faxbot`

## Technical Architecture

The platform uses a traits-first UI architecture: the Admin Console introspects the active provider's capabilities and renders only the configuration surfaces that provider supports. This avoids the "greyed-out features" antipattern and keeps the interface clean regardless of which backend is active.

HIPAA compliance is built into the architecture, not bolted on. Webhook verification uses HMAC, authentication uses short-TTL tokens, and the logging pipeline is designed to never include protected health information. The MCP servers ship in both Node and Python with stdio, HTTP, and SSE transport options.

The iOS companion app is on TestFlight. A live admin demo is available at [faxbot.net/admin-demo](https://faxbot.net/admin-demo).
