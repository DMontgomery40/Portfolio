---
layout: project
title: agentspec
description: Schema-enforced, machine-readable docstrings for Python codebases enabling reliable AI/LLM tooling and CI validation.
category: AI Developer Tooling
status: Active
date: 2025-11-10
github_url: https://github.com/DMontgomery40/agentspec
permalink: /projects/agentspec/
tags:
  - Python
  - Tooling
  - CI
  - Spec
---

## Overview

**agentspec** provides schema-enforced, machine-readable docstrings for Python codebases, enabling reliable AI/LLM tooling and CI validation. It transforms Python docstrings from human-readable documentation into parseable, enforceable contracts that reduce ambiguity for both human developers and AI tools.

When AI assistants work with your code, they need more than comments—they need structured specifications. agentspec bridges this gap by making your code's contract explicit, testable, and machine-readable while remaining human-friendly.

## Key Features

### Schema-Enforced Specifications
- **Structured Format**: JSON Schema-based docstring validation
- **Type Safety**: Enforce parameter types, return types, and exceptions
- **Contract Definition**: Explicit preconditions and postconditions
- **Version Control**: Track specification changes alongside code

### Machine-Readable Contracts
- **Parseable Syntax**: AI tools can reliably extract specifications
- **Semantic Understanding**: Rich metadata for intelligent tooling
- **Cross-Reference**: Link related functions and dependencies
- **Example Encoding**: Machine-executable usage examples

### CI Integration
- **Validation Pipeline**: Automatically verify docstrings match schemas
- **Coverage Metrics**: Track which functions have complete specifications
- **Breaking Change Detection**: Alert when contracts change
- **Documentation Generation**: Auto-generate docs from specifications

### AI/LLM Tooling Support
- **Context Injection**: Feed structured specs to AI assistants
- **Code Generation**: AI tools generate code matching contracts
- **Test Generation**: Automatically create tests from specifications
- **Refactoring Safety**: AI refactors with contract guarantees

### Developer Experience
- **IDE Integration**: Autocomplete and validation in editors
- **Migration Tools**: Convert existing docstrings to agentspec format
- **Template System**: Project-specific specification templates
- **Documentation Browser**: Interactive spec exploration

## Images

### TUI Interface
<img src="https://raw.githubusercontent.com/DMontgomery40/agentspec/main/assets/TUI-secreenshot.png" alt="agentspec TUI" style="max-width: 100%; border-radius: 8px; margin: 1rem 0;" />

### Agent Response to Rules
<img src="https://raw.githubusercontent.com/DMontgomery40/agentspec/main/assets/sgent-response-to-rules-screenshot.png" alt="Agent Response to agentspec Rules" style="max-width: 100%; border-radius: 8px; margin: 1rem 0;" />

## Tech Stack

### Core Implementation
- **Python 3.9+**: Core library and CLI tools
- **Pydantic**: Schema validation and parsing
- **AST Analysis**: Python code parsing and transformation
- **JSON Schema**: Specification format standard

### CLI & TUI
- **Click**: Command-line interface framework
- **Rich**: Terminal UI components and formatting
- **Textual**: Interactive TUI for spec browsing

### CI Integration
- **GitHub Actions**: Pre-built workflows for validation
- **pre-commit**: Git hooks for local validation
- **pytest**: Test generation and validation
- **mypy**: Static type checking integration

### IDE Support
- **Language Server Protocol**: Editor integration
- **VSCode Extension**: Native VSCode support
- **PyCharm Plugin**: JetBrains IDE integration

### Documentation
- **Sphinx**: Documentation generation
- **MkDocs**: Static site generation
- **Mermaid**: Diagram generation from specs

## Links

- **GitHub Repository**: [github.com/DMontgomery40/agentspec](https://github.com/DMontgomery40/agentspec)
- **Documentation**: [agentspec.dev](https://agentspec.dev)
- **PyPI Package**: [pypi.org/project/agentspec](https://pypi.org/project/agentspec)
- **Examples**: [github.com/DMontgomery40/agentspec/tree/main/examples](https://github.com/DMontgomery40/agentspec/tree/main/examples)

---

*agentspec: Making Python contracts explicit, parseable, and enforceable—because AI tools deserve better than comments.*
