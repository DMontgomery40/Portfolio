---
layout: project
title: "Bambu Printer MCP"
description: "MCP server for controlling Bambu Lab 3D printers -- STL manipulation, auto-slicing, FTPS upload, and MQTT print control from Claude."
image: /assets/images/bambu-printer-mcp.png
repo: https://github.com/DMontgomery40/bambu-printer-mcp
tags:
  - 3D Printing
  - MCP
  - Bambu Lab
  - npm
featured: true
order: 11
---

bambu-printer-mcp is a Model Context Protocol server that gives Claude Desktop, Claude Code, or any MCP client direct control over Bambu Lab 3D printers. It handles the full print workflow: manipulate an STL (scale, rotate, merge, flatten), auto-slice with BambuStudio CLI, upload the resulting 3MF over FTPS, and start the print via MQTT -- all without leaving a conversation.

Published on npm for instant use via `npx bambu-printer-mcp`.

## Key Features

- **Full print workflow** -- STL manipulation, auto-slice, FTPS upload, MQTT print start
- **Detailed printer status** with temperatures, progress, layer count, and AMS slot data
- **Multi-slicer support** -- BambuStudio, OrcaSlicer, PrusaSlicer, Cura, and Slic3r
- **Correct AMS mapping** parsed from 3MF slicer config per OpenBambuAPI spec
- **Dual transport** -- stdio for Claude Desktop/Code, Streamable HTTP for other clients
- **Optional Blender MCP bridge** for advanced mesh operations

## Technical Architecture

The server is TypeScript/Node.js, published on npm. It communicates with Bambu Lab printers over two protocols: MQTT for status monitoring and print job control, and FTPS for file management and upload. STL manipulation uses Three.js for geometry operations before handing off to the slicer.

The slicer integration supports five backends, with BambuStudio CLI as the default. AMS (Automatic Material System) mapping is parsed directly from the 3MF slicer configuration, following the OpenBambuAPI spec for correct filament slot assignment. This is a focused Bambu-only fork of the broader mcp-3D-printer-server project, stripped to its Bambu core for a smaller, faster install.
