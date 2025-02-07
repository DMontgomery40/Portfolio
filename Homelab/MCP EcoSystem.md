---
title: MCP EcoSystem
layout: default
parent: Homelab
nav_order: 2
has_toc: true
---

# MCP Is a Powerful Beast 

![MCP Ecosystem Diagram]({{ site.baseurl }}/assets/mermaid-digram-mcp-ecosystem.webp)

# Clients and Servers

## Clients

> Note: These things can change by the week... this is up to date to 2/7/2025

- **Claude Desktop** is an odd thing... Barely aware of it's environemnt, and yet the default option for one of the most powerful protocols every created for AI. 
  - I think it's uncool it's "advanced MPC'ing to admit you use it -- pretty secure though, I'll say it -- I use it (sometimes) 
- **continue.dev** have a love/hate, more on this later
- **sageapp.ai** Intrigued, early days, but mobile access is HUGE
- **glamaa.ai** I have a lot to say here, message me if you have questions or thoughts and I'll get to this when I can
- **Cursor** my go to

## Servers 

### Current Config: 
> Note: This can change by the hour lol 
```
{
  "mcpServers": {
    "fetch": {
      "command": "/opt/homebrew/bin/uvx",
      "args": [
        "mcp-server-fetch",
        "--ignore-robots-txt",
        "--user-agent=YourUserAgent"
      ]
    },
    "wcgw": {
      "command": "/opt/homebrew/bin/uv",
      "args": [
        "tool",
        "run",
        "--from",
        "wcgw@latest",
        "--python",
        "3.12",
        "wcgw_mcp"
      ]
    },
    "filesystem": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-filesystem",
        "/Users/davidmontgomery/",
        "/Users/davidmontgomery/Library/Application Support/Claude",
        "/Users/"
      ]
    },
    "mcp-birdstats": {
      "command": "npx",
      "args": [
        "mcp-birdstats"
      ],
      "env": {}
    },
    "memory": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-memory"
      ]
    },
    "webresearch": {
      "command": "npx",
      "args": [
        "-y",
        "@mzxrai/mcp-webresearch"
      ]
    },
    "server-sequential-thinking": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-sequential-thinking"
      ]
    },
    "@mcp-get-community-server-curl": {
      "runtime": "node",
      "command": "npx",
      "args": [
        "-y",
        "@mcp-get-community/server-curl"
      ]
    },
    "github": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-github"
      ],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "-----------"
      }
    },
    "deepseek": {
      "command": "npx",
      "args": [
        "-y",
        "deepseek-mcp-server"
      ],
      "env": {
        "DEEPSEEK_API_KEY": "sk--------"
      }
    },
    "brave-search": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-brave-search"
      ],
      "env": {
        "BRAVE_API_KEY": "----------"
      }
    },
    "mcp-installer": {
      "command": "npx",
      "args": [
        "@anaisbetts/mcp-installer"
      ]
    }
  }
}
```

