---
layout: project
title: agentspec
description: Schema‑enforced, machine‑readable docstrings for Python codebases enabling reliable AI/LLM tooling and CI validation.
category: AI Developer Tooling
status: Active
date: 2025-11-10
github_url: https://github.com/DMontgomery40/agentspec
permalink: /projects/agentspec/
tags: [Python, Tooling, CI, Spec]
---

## Overview

agentspec provides schema-enforced, machine-readable docstrings for Python codebases, enabling reliable AI/LLM tooling and CI validation. By transforming docstrings into parseable, enforceable contracts, agentspec reduces ambiguity for both automated tooling and AI model integrations.

The system defines a structured format for documenting functions, classes, and modules that can be validated at build time and consumed by AI assistants, code analysis tools, and documentation generators. This ensures that documentation stays synchronized with code and provides the rich semantic information needed for advanced tooling.

## Key Features

- **Schema-Enforced Format**: Structured docstring format with validation rules
- **Machine-Readable**: Parseable by tools, IDEs, and AI models
- **CI Integration**: Validate documentation completeness in continuous integration
- **Type Awareness**: Full integration with Python type hints and annotations
- **Contract Enforcement**: Ensure documented behavior matches implementation
- **AI/LLM Compatible**: Optimized for consumption by language models
- **Extensible Schema**: Customize docstring requirements per project
- **Developer-Friendly**: Intuitive syntax that enhances readability

## Images

<img src="https://raw.githubusercontent.com/DMontgomery40/agentspec/main/assets/TUI-secreenshot.png" alt="Terminal UI Screenshot" style="max-width: 100%; height: auto; margin: 1rem 0; border-radius: 10px;">

<img src="https://raw.githubusercontent.com/DMontgomery40/agentspec/main/assets/sgent-response-to-rules-screenshot.png" alt="Agent Response Screenshot" style="max-width: 100%; height: auto; margin: 1rem 0; border-radius: 10px;">

## Tech Stack

- **Language**: Python 3.8+
- **Parser**: Custom docstring parser with AST analysis
- **Validation**: Schema validation engine with configurable rules
- **CI/CD**: GitHub Actions, GitLab CI, and Jenkins support
- **Tooling**: Integration with mypy, pylint, and other static analyzers
- **Documentation**: Sphinx and MkDocs compatibility
- **Testing**: pytest plugin for docstring validation

## Links

- **GitHub Repository**: [https://github.com/DMontgomery40/agentspec](https://github.com/DMontgomery40/agentspec)
- **Documentation**: Available in repository README
- **PyPI Package**: Installation via pip

---

*agentspec bridges the gap between human-readable documentation and machine-consumable specifications, making Python codebases more accessible to AI assistants and automated tooling.*
