---
layout: project
title: Faxbot
description: The only known open-source, self-hosted fax server and API with distinct inbound vs. outbound provider routing.
description: The only known open‑source, self‑hosted fax server and API with distinct inbound vs. outbound provider routing.
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
tags: [TypeScript, Python, Docker, REST, MCP, HIPAA]
---

## Overview

Faxbot is the only known open-source, self-hosted fax server and API — and the only fax server (as far as known) that supports distinct inbound vs. outbound provider routing. This unique architecture enables cost optimization, reliability improvements, and compliance flexibility by allowing different fax providers for sending and receiving.

Built with a HIPAA-aligned design, Faxbot offers a clean REST API surface and Model Context Protocol (MCP) integration, enabling AI assistants to send and receive faxes via auditable actions. Whether you're handling healthcare communications, legal documents, or any scenario requiring fax transmission, Faxbot provides a modern, containerized solution.

## Key Features

- **Dual Provider Routing**: Separate inbound and outbound fax providers for maximum flexibility
- **HIPAA-Aligned Architecture**: Designed with healthcare compliance requirements in mind
- **REST API**: Clean, well-documented REST interface for integration
- **MCP Integration**: AI assistant compatibility for conversational fax operations
- **Docker Deployment**: Containerized for easy deployment and scaling
- **Self-Hosted**: Complete control over your fax infrastructure and data
- **Auditable Actions**: Comprehensive logging for compliance and troubleshooting
- **Open Source**: Transparent, community-driven development

## Images

<img src="https://raw.githubusercontent.com/DMontgomery40/Faxbot/main/assets/faxbot-ios-txt-to-fax.png" alt="Faxbot iOS Text to Fax" style="max-width: 100%; height: auto; margin: 1rem 0; border-radius: 10px;">

<img src="https://raw.githubusercontent.com/DMontgomery40/Faxbot/main/assets/faxbot-ios-connect.png" alt="Faxbot iOS Connection" style="max-width: 100%; height: auto; margin: 1rem 0; border-radius: 10px;">

## Tech Stack

- **Backend**: TypeScript, Node.js
- **Scripting**: Python for automation and utilities
- **API**: RESTful architecture with OpenAPI documentation
- **Protocol**: Model Context Protocol (MCP) integration
- **Deployment**: Docker containerization
- **Security**: HIPAA-aligned design patterns
- **Storage**: Configurable persistence layer
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
Faxbot is the only known open‑source, self‑hosted fax server and API — and, as far as we know, the only fax server (regardless of license) that supports **distinct inbound vs. outbound provider routing**. This architectural flexibility enables organizations to optimize for cost, reliability, and compliance requirements by using different fax service providers for incoming and outgoing transmissions.

Built with HIPAA‑aligned design principles, Faxbot provides a clean REST API surface and integrates with the Model Context Protocol (MCP), enabling AI assistants to send and receive faxes through auditable, controlled actions. Whether you're modernizing legacy healthcare workflows, implementing compliant document transmission, or building automated fax capabilities into your applications, Faxbot offers the flexibility and transparency that proprietary solutions lack.

## Key Features

### Dual Provider Routing

Faxbot's standout feature is its ability to route inbound and outbound faxes through different providers:

- **Cost Optimization**: Use economical providers for outbound while maintaining premium inbound reliability
- **Compliance Flexibility**: Route sensitive inbound faxes through BAA‑covered providers while using standard services for outbound
- **Redundancy**: Configure failover providers independently for each direction
- **Geographic Optimization**: Route based on source/destination regions for better delivery rates

### HIPAA‑Aligned Design

Designed from the ground up with healthcare compliance in mind:

- **Audit Logging**: Comprehensive tracking of all fax transmissions and access
- **Encryption at Rest**: All stored faxes and metadata encrypted
- **Access Controls**: Role‑based permissions for viewing and transmitting faxes
- **PHI Handling**: Proper safeguards for Protected Health Information
- **BAA Ready**: Architecture supports Business Associate Agreement requirements

### Docker Deployment

Single‑command deployment with Docker and Docker Compose:

- **Containerized**: Isolated environment with all dependencies included
- **Orchestrated**: Multi‑container setup with database, queue, and API components
- **Scalable**: Horizontal scaling for high‑volume environments
- **Portable**: Deploy on‑premises, in the cloud, or hybrid environments

### Clean REST API

Intuitive HTTP API for integration with any language or platform:

- **RESTful Design**: Standard HTTP verbs and status codes
- **JSON Payloads**: Easy to consume and generate
- **Webhook Support**: Real‑time notifications for inbound faxes
- **OpenAPI Spec**: Complete API documentation with Swagger/OpenAPI

### Model Context Protocol Integration

AI‑native capabilities through MCP:

- **Natural Language Interface**: Send faxes through conversational commands
- **Auditable Actions**: All AI‑initiated faxes logged with full context
- **Controlled Access**: Granular permissions for AI agents
- **Workflow Automation**: Chain fax operations with other MCP tools

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
- **TypeScript**: Type‑safe server implementation
- **Node.js**: Runtime environment
- **Express**: HTTP server framework
- **PostgreSQL**: Persistent storage for metadata and audit logs

### Services Integration
- **Python**: Provider integration libraries
- **Redis**: Job queue and caching
- **Docker**: Containerization and orchestration

### API & Protocol Support
- **REST**: Standard HTTP API
- **MCP**: Model Context Protocol for AI integration
- **Webhooks**: Real‑time event notifications

## Images

<img src="https://raw.githubusercontent.com/DMontgomery40/Faxbot/main/assets/social-preview.png" alt="Faxbot Social Preview" style="max-width: 100%; border-radius: 10px; margin: 1rem 0;">

<img src="https://raw.githubusercontent.com/DMontgomery40/Faxbot/main/assets/faxbot_full_logo.png" alt="Faxbot Logo" style="max-width: 400px; border-radius: 10px; margin: 1rem 0;">

### Mobile App Screenshots

<div style="display: flex; gap: 1rem; flex-wrap: wrap; margin: 1rem 0;">
  <img src="https://raw.githubusercontent.com/DMontgomery40/Faxbot/main/assets/connect-to-server.png" alt="Connect to Server" style="max-width: 300px; border-radius: 10px;">
  <img src="https://raw.githubusercontent.com/DMontgomery40/Faxbot/main/assets/txt-to-fax.png" alt="Text to Fax" style="max-width: 300px; border-radius: 10px;">
</div>

## Use Cases

### Healthcare Organizations
- **Patient Document Transmission**: HIPAA‑compliant fax capabilities for medical records
- **Provider Communication**: Referrals, prescriptions, and care coordination
- **Insurance Claims**: Automated submission and retrieval of claim documents
- **Lab Results**: Secure transmission of diagnostic reports

### Legal Firms
- **Court Filings**: Reliable delivery of time‑sensitive legal documents
- **Client Communications**: Secure document exchange
- **Discovery**: Managing document production and requests
- **Compliance**: Meeting jurisdictional requirements for fax transmission

### Enterprise IT
- **Legacy System Integration**: Bridge modern applications with fax‑dependent workflows
- **Vendor Communications**: Automated purchase orders and invoices
- **Compliance Documentation**: Audit trails for regulatory requirements
- **Process Automation**: Integrate fax into broader automation workflows

## Getting Started

### Quick Start with Docker

```bash
# Clone the repository
git clone https://github.com/DMontgomery40/Faxbot.git
cd Faxbot

# Configure environment
cp .env.example .env
# Edit .env with your provider credentials

# Start with Docker Compose
docker-compose up -d

# API will be available at http://localhost:3000
```

### Configuration

Set up your inbound and outbound providers in `.env`:

```env
# Inbound Provider (e.g., premium BAA‑covered service)
INBOUND_PROVIDER=telnyx
INBOUND_API_KEY=your_inbound_key

# Outbound Provider (e.g., cost‑effective service)
OUTBOUND_PROVIDER=twilio
OUTBOUND_API_KEY=your_outbound_key

# Database
DATABASE_URL=postgresql://user:pass@db:5432/faxbot

# Redis
REDIS_URL=redis://redis:6379

# API Keys for access control
API_KEY=your_secure_api_key
```

### Sending Your First Fax

```bash
# Send a fax via REST API
curl -X POST http://localhost:3000/api/fax/send \
  -H "Authorization: Bearer your_secure_api_key" \
  -H "Content-Type: application/json" \
  -d '{
    "to": "+15555551234",
    "from": "+15555556789",
    "document": "https://example.com/document.pdf"
  }'
```

## Links

- **Live Site**: [https://faxbot.net](https://faxbot.net)
- **GitHub Repository**: [https://github.com/DMontgomery40/Faxbot](https://github.com/DMontgomery40/Faxbot)
- **Documentation**: Available in repository README

---

*Faxbot brings modern software engineering practices to fax technology, making it accessible, maintainable, and compliant for today's needs.*
- **Documentation**: Available in the repository
- **Issue Tracker**: [GitHub Issues](https://github.com/DMontgomery40/Faxbot/issues)

---

*Faxbot brings modern development practices to legacy fax infrastructure, enabling compliant, flexible, and transparent fax capabilities for organizations that need them.*
