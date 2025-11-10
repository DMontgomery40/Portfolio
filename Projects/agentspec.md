---
layout: project
title: agentspec
description: Schema-enforced, machine-readable docstrings for Python codebases enabling reliable AI/LLM tooling and CI validation.
description: Schema‑enforced, machine‑readable docstrings for Python codebases enabling reliable AI/LLM tooling and CI validation.
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
agentspec brings schema‑enforced, machine‑readable docstrings to Python codebases, enabling reliable AI/LLM tooling integrations and continuous integration validation. By making function contracts parseable and enforceable, agentspec reduces ambiguity for both automated tooling and AI model integrations.

Traditional docstrings are helpful for human readers but vary widely in format, completeness, and accuracy. agentspec establishes a structured specification that can be validated, parsed, and consumed by tools — particularly AI coding assistants that need to understand function behavior, parameters, and return values with precision.

## Key Features

### Schema‑Enforced Docstrings

Structured documentation with validation:

- **Formal Specification**: Define function contracts in a machine‑readable format
- **Type Information**: Capture parameter types, return types, and constraints
- **Behavior Contracts**: Document preconditions, postconditions, and side effects
- **Validation Rules**: Enforce completeness and consistency of documentation

### Machine‑Readable Format

Enable automated consumption:

- **Parseable Structure**: Structured format that tools can reliably parse
- **Semantic Meaning**: Machine‑understandable descriptions of behavior
- **Tool Integration**: Direct consumption by IDEs, linters, and AI assistants
- **Backwards Compatible**: Works alongside existing docstring formats

### CI Validation

Catch documentation issues early:

- **Automated Checks**: Validate docstrings in continuous integration
- **Coverage Reporting**: Track which functions have complete specifications
- **Breaking Change Detection**: Identify contract changes that affect consumers
- **Quality Gates**: Enforce documentation standards before merge

### AI/LLM Integration

Improve AI coding assistance:

- **Precise Function Understanding**: LLMs get accurate parameter and behavior information
- **Reduced Hallucination**: Clear contracts reduce incorrect code generation
- **Better Code Completion**: More accurate suggestions based on contracts
- **Automated Testing**: Generate tests from specifications

## Tech Stack

### Core
- **Python**: Native Python implementation for maximum compatibility
- **AST Parsing**: Leverage Python's abstract syntax tree for analysis

### Validation & Tooling
- **Pydantic**: Schema validation and parsing
- **JSON Schema**: Standard format for specifications
- **CI Integration**: GitHub Actions, GitLab CI, Jenkins support

### Development Tools
- **Pre‑commit Hooks**: Validate on commit
- **Editor Plugins**: IDE integration for real‑time feedback
- **CLI Tools**: Command‑line validation and generation

## Images

### Terminal User Interface

<img src="https://raw.githubusercontent.com/DMontgomery40/agentspec/main/assets/TUI-secreenshot.png" alt="TUI Screenshot" style="max-width: 100%; border-radius: 10px; margin: 1rem 0;">

### AI Agent Response

<img src="https://raw.githubusercontent.com/DMontgomery40/agentspec/main/assets/sgent-response-to-rules-screenshot.png" alt="Agent Response to Rules" style="max-width: 100%; border-radius: 10px; margin: 1rem 0;">

## Use Cases

### AI Coding Assistants

Improve AI‑generated code quality:

- **Function Contracts**: Give AI assistants precise function signatures
- **Behavior Specifications**: Help AI understand what functions should do
- **Parameter Constraints**: Validate generated code against contracts
- **Integration Testing**: Generate tests from specifications

### Team Development

Maintain documentation quality:

- **Onboarding**: New team members understand code through clear contracts
- **API Design**: Design‑by‑contract approach to API development
- **Code Review**: Automated checks for documentation completeness
- **Breaking Changes**: Track contract changes across versions

### Open Source Projects

Improve contributor experience:

- **Clear Interfaces**: Contributors understand function expectations
- **Automated Documentation**: Generate API docs from specifications
- **Quality Assurance**: Maintain documentation standards at scale
- **External Integration**: Consumers can rely on machine‑readable contracts

## Specification Format

### Example Function Specification

```python
from agentspec import spec

@spec(
    description="Calculate the total cost including tax",
    parameters={
        "subtotal": {
            "type": "float",
            "description": "Pre‑tax amount",
            "constraints": {"min": 0}
        },
        "tax_rate": {
            "type": "float",
            "description": "Tax rate as decimal (e.g., 0.08 for 8%)",
            "constraints": {"min": 0, "max": 1}
        }
    },
    returns={
        "type": "float",
        "description": "Total cost including tax",
        "constraints": {"min": 0}
    },
    raises={
        "ValueError": "If subtotal or tax_rate is negative"
    },
    examples=[
        {
            "input": {"subtotal": 100.0, "tax_rate": 0.08},
            "output": 108.0
        }
    ]
)
def calculate_total(subtotal: float, tax_rate: float) -> float:
    """Calculate total cost with tax."""
    if subtotal < 0 or tax_rate < 0:
        raise ValueError("Values must be non‑negative")
    return subtotal * (1 + tax_rate)
```

### Validation

```bash
# Validate all specifications in a project
agentspec validate ./src

# Check coverage
agentspec coverage ./src --min 80

# Generate report
agentspec report ./src --format html
```

## Getting Started

### Installation

```bash
# Install via pip
pip install agentspec

# Or from source
git clone https://github.com/DMontgomery40/agentspec.git
cd agentspec
pip install -e .
```

### Basic Usage

Add specifications to your functions:

```python
from agentspec import spec

@spec(
    description="Greet a user by name",
    parameters={
        "name": {
            "type": "str",
            "description": "User's name"
        }
    },
    returns={
        "type": "str",
        "description": "Greeting message"
    }
)
def greet(name: str) -> str:
    return f"Hello, {name}!"
```

Validate in CI:

```yaml
# .github/workflows/validate.yml
name: Validate Specs
on: [push, pull_request]

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.9'
      - name: Install agentspec
        run: pip install agentspec
      - name: Validate specifications
        run: agentspec validate ./src --strict
```

### Integration with AI Tools

Export specifications for AI consumption:

```bash
# Generate machine‑readable specs
agentspec export ./src --format json --output specs.json

# AI tools can then parse specs.json to understand function contracts
```

## Benefits

### For Developers

- **Clear Contracts**: Unambiguous function documentation
- **Automated Validation**: Catch documentation issues early
- **Better Tooling**: Improved IDE support and code completion
- **Less Ambiguity**: Precise specifications reduce misunderstandings

### For AI Tools

- **Reliable Parsing**: Consistent format for consumption
- **Type Safety**: Accurate parameter and return type information
- **Behavior Understanding**: Clear documentation of side effects and constraints
- **Test Generation**: Specifications enable automated test creation

### For Teams

- **Documentation Standards**: Enforce consistent documentation
- **Onboarding**: New members understand code faster
- **API Stability**: Track contract changes over time
- **Quality Assurance**: Maintain documentation quality at scale

## Links

- **GitHub Repository**: [https://github.com/DMontgomery40/agentspec](https://github.com/DMontgomery40/agentspec)
- **Documentation**: Available in repository README
- **PyPI Package**: Installation via pip

---

*agentspec bridges the gap between human-readable documentation and machine-consumable specifications, making Python codebases more accessible to AI assistants and automated tooling.*
- **Documentation**: Available in the repository
- **Issue Tracker**: [GitHub Issues](https://github.com/DMontgomery40/agentspec/issues)

---

*agentspec bridges the gap between human‑readable documentation and machine‑consumable specifications, enabling better collaboration between developers, tools, and AI assistants.*
