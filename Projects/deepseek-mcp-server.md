---
title: Deepseek MCP Server
layout: default
parent: Projects
nav_order: 1
---

## Deepseek MCP Server

https://github.com/DMontgomery40/deepseek-mcp-server

### Installation

```bash
git clone https://github.com/DMontgomery40/deepseek-mcp-server.git
cd deepseek-mcp-server
npm install
```

### Usage

```bash
npm start
```

### Usage with Docker

```bash
docker-compose up
```

```bash
docker-compose down
```

### Configuration

```bash
cp .env.example .env
```

```bash
vi .env
```
```bash
DEEPSEEK_API_KEY=sk-...
```
```bash
docker-compose up
```
```bash
docker-compose down
```

## Features

- Basic search functionality
- Customizable API key
- Dockerized for ease of use
- Real-time results
- Cached results for faster response




