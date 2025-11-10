---
layout: project
title: Faxbot
description: The only known open-source, self-hosted fax server and API with distinct inbound vs. outbound provider routing.
category: Communications & Compliance
status: Active
date: 2025-11-10
github_url: https://github.com/DMontgomery40/Faxbot
demo_url: https://faxbot.net
permalink: /projects/faxbot/
tags:
  - TypeScript
  - Python
  - Docker
  - REST
  - MCP
  - HIPAA
---

## Overview

Faxbot is the only known open-source, self-hosted fax server and API — and uniquely supports **distinct inbound vs. outbound provider routing** for cost optimization, reliability, and compliance flexibility. Built with HIPAA-aligned design principles, Faxbot provides healthcare providers, legal offices, and enterprises with a modern, auditable faxing solution.

Unlike traditional fax servers that lock you into a single provider, Faxbot lets you route inbound faxes through one service (e.g., Twilio for cost) and outbound through another (e.g., eFax for reliability), giving you unprecedented control over your fax infrastructure.

## Key Features

### Dual-Provider Architecture
- **Inbound Provider**: Configurable routing for receiving faxes (Twilio, RingCentral, etc.)
- **Outbound Provider**: Separate routing for sending faxes (eFax, SRFax, etc.)
- **Cost Optimization**: Use the most economical provider for each direction
- **Reliability**: Failover between providers for maximum uptime
- **Compliance Flexibility**: Route sensitive data through HIPAA-compliant providers

### Modern API & Integration
- **RESTful API**: Clean, well-documented endpoints for sending/receiving faxes
- **MCP Integration**: AI assistants can send and receive faxes through auditable actions
- **Webhook Support**: Real-time notifications for fax status changes
- **Batch Operations**: Send faxes to multiple recipients efficiently

### HIPAA-Aligned Design
- **Encryption at Rest**: All fax data encrypted in storage
- **Encryption in Transit**: TLS/SSL for all API communications
- **Audit Logging**: Comprehensive logs for compliance requirements
- **Access Controls**: Role-based permissions for user management
- **Data Retention**: Configurable retention policies

### Docker Deployment
- **One-Command Deploy**: Docker Compose setup for rapid deployment
- **Scalable Architecture**: Horizontal scaling for high-volume operations
- **Environment-Based Config**: Easy configuration management
- **Health Monitoring**: Built-in health checks and metrics

## Images

### iOS Text-to-Fax Interface
<img src="https://raw.githubusercontent.com/DMontgomery40/Faxbot/main/assets/faxbot-ios-txt-to-fax.png" alt="Faxbot iOS Text-to-Fax" style="max-width: 100%; border-radius: 8px; margin: 1rem 0;" />

### iOS Connection Interface
<img src="https://raw.githubusercontent.com/DMontgomery40/Faxbot/main/assets/faxbot-ios-connect.png" alt="Faxbot iOS Connect" style="max-width: 100%; border-radius: 8px; margin: 1rem 0;" />

## Tech Stack

### Backend
- **TypeScript**: Type-safe server implementation
- **Node.js**: High-performance runtime
- **Express**: RESTful API framework
- **PostgreSQL**: Reliable data persistence

### Python Components
- **PDF Generation**: Document conversion and rendering
- **Image Processing**: Fax image optimization
- **MCP Server**: AI assistant integration layer

### Infrastructure
- **Docker**: Containerized deployment
- **Docker Compose**: Multi-container orchestration
- **Nginx**: Reverse proxy and SSL termination
- **Redis**: Caching and job queue management

### External Integrations
- **Twilio Fax API**: Inbound/outbound provider option
- **RingCentral**: Enterprise fax provider option
- **eFax API**: Alternative provider support
- **SRFax**: HIPAA-compliant provider option

## Links

- **Live Site**: [faxbot.net](https://faxbot.net)
- **GitHub Repository**: [github.com/DMontgomery40/Faxbot](https://github.com/DMontgomery40/Faxbot)
- **Documentation**: [docs.faxbot.net](https://docs.faxbot.net)
- **API Reference**: [api.faxbot.net](https://api.faxbot.net)

---

*Faxbot brings fax infrastructure into the modern era with open-source transparency, flexible provider routing, and seamless AI integration.*
