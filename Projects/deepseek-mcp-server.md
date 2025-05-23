---
title: Deepseek MCP Server
layout: default
parent: Projects
nav_order: 1
---

# Deepseek MCP Server

A Python and NPM-based Model Context Protocol (MCP) server implementation for running large language models locally using the Deepseek framework.

{% if site.github %}
[![GitHub stars](https://img.shields.io/github/stars/{{ site.github.repository_nwo | uri_escape }}?style=social)](https://github.com/{{ site.github.repository_nwo }}/stargazers)
{% endif %} |
[View on GitHub](https://github.com/DMontgomery40/deepseek-mcp-server) | [Report Issues](https://github.com/DMontgomery40/deepseek-mcp-server/issues)

## Overview

The Deepseek MCP Server provides a lightweight, efficient way to deploy and interact with large language models on your local infrastructure. Built with simplicity and performance in mind, it offers a clean REST API interface for text generation and embedding tasks.

## Key Features

- **Local LLM Inference**: Run models entirely on your hardware without external dependencies
- **REST API Interface**: Simple HTTP endpoints for easy integration
- **Docker Support**: Containerized deployment for consistency across environments
- **Response Caching**: Built-in caching mechanism for faster repeated queries
- **Configurable Models**: Support for various Deepseek model configurations
- **Real-time Streaming**: Stream responses for better user experience
- **Low Latency**: Optimized for minimal response times

## Technical Stack

- **Language**: Python 3.9+
- **Framework**: FastAPI for high-performance async operations
- **Containerization**: Docker & Docker Compose
- **Model Framework**: Deepseek inference engine

## Installation

### Prerequisites
- Python 3.9 or higher
- Docker (optional, for containerized deployment)
- NVIDIA GPU with CUDA support (recommended for optimal performance)

### Quick Start

```bash
# Clone the repository
git clone https://github.com/DMontgomery40/deepseek-mcp-server.git
cd deepseek-mcp-server

# Install dependencies
pip install -r requirements.txt

# Run the server
python main.py
```

### Docker Deployment

```bash
# Build and run with Docker Compose
docker-compose up -d

# Check logs
docker-compose logs -f

# Stop the service
docker-compose down
```

## Configuration

Create a `.env` file from the example:

```bash
cp .env.example .env
```

Edit the configuration:

```env
# Model Configuration
MODEL_NAME=deepseek-7b
MODEL_PATH=/models/deepseek-7b

# Server Configuration
HOST=0.0.0.0
PORT=8000
WORKERS=4

# Performance Settings
MAX_BATCH_SIZE=32
MAX_SEQUENCE_LENGTH=2048
CACHE_SIZE=1000

# Optional: API Key for authentication
API_KEY=your-secret-key
```

## API Usage

### Generate Text

```bash
curl -X POST http://localhost:8000/v1/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer your-api-key" \
  -d '{
    "prompt": "Explain quantum computing in simple terms:",
    "max_tokens": 200,
    "temperature": 0.7
  }'
```

### Generate Embeddings

```bash
curl -X POST http://localhost:8000/v1/embeddings \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer your-api-key" \
  -d '{
    "input": "The quick brown fox jumps over the lazy dog",
    "model": "deepseek-embeddings"
  }'
```

## Performance Optimization

- **GPU Acceleration**: Automatically detects and utilizes available CUDA devices
- **Batch Processing**: Groups requests for efficient inference
- **Memory Management**: Intelligent model loading and unloading
- **Response Caching**: LRU cache for frequently requested completions

## Use Cases

- **Local AI Development**: Test and develop AI applications without cloud dependencies
- **Privacy-Sensitive Applications**: Keep data on-premises for compliance
- **Edge Computing**: Deploy models closer to data sources
- **Research & Experimentation**: Rapid prototyping with different model configurations

## Contributing

Contributions are welcome! Please see the [contributing guidelines](https://github.com/DMontgomery40/deepseek-mcp-server/blob/main/CONTRIBUTING.md) for details.

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/DMontgomery40/deepseek-mcp-server/blob/main/LICENSE) file for details.

## Acknowledgments

Built on top of the excellent Deepseek framework and inspired by the Model Context Protocol specification.

---

[← Back to Projects]({{ site.baseurl }}/Projects/) | [View Next Project →]({{ site.baseurl }}/Projects/intel-npu-top.html)
