---
title: MCP 3D Printer Server
layout: default
parent: Projects
nav_order: 9
permalink: /projects/mcp-3d-printer-server/
---

# MCP 3D Printer Server

Model Context Protocol server for AI-powered 3D printer control and monitoring, supporting multiple printer types and slicing engines.

[View on GitHub](https://github.com/DMontgomery40/mcp-3D-printer-server) | [NPM Package](https://www.npmjs.com/package/mcp-3d-printer-server)

## Overview

MCP 3D Printer Server bridges the gap between AI assistants and 3D printing, enabling natural language control, intelligent monitoring, and automated optimization of 3D printing workflows through the Model Context Protocol.

## Key Features

- **Universal Printer Support**: Compatible with OctoPrint, Klipper, Duet, RepRap, and more
- **AI-Powered Control**: Natural language commands for printer operation
- **Intelligent Monitoring**: Real-time status updates and predictive failure detection
- **Automated Slicing**: Integration with PrusaSlicer, Cura, and other slicing engines
- **Print Optimization**: AI suggests optimal settings based on model analysis
- **Multi-Printer Management**: Control multiple printers from a single interface
- **Safety Features**: Automatic pause on anomaly detection

## Supported Platforms

### Printer Firmware/Servers
- OctoPrint (including OctoPi)
- Klipper with Moonraker
- Duet Web Control
- RepRapFirmware
- Marlin with web interface
- PrusaLink
- Bambu Studio API

### Slicing Engines
- PrusaSlicer
- Cura Engine
- Slic3r
- SuperSlicer
- IdeaMaker

## Technical Architecture

- **Core**: Node.js with TypeScript
- **MCP Implementation**: Official MCP SDK
- **Communication**: WebSocket for real-time updates
- **File Handling**: Support for STL, 3MF, OBJ formats
- **Database**: SQLite for print history and settings

## Installation

```bash
# Install via npm
npm install -g mcp-3d-printer-server

# Or clone and build from source
git clone https://github.com/DMontgomery40/mcp-3D-printer-server.git
cd mcp-3D-printer-server
npm install
npm run build
```

## Configuration

```javascript
// config.json
{
  "printers": [
    {
      "name": "Prusa MK3S+",
      "type": "octoprint",
      "url": "http://octopi.local",
      "apiKey": "your-api-key"
    },
    {
      "name": "Voron 2.4",
      "type": "klipper",
      "url": "http://voron.local:7125",
      "apiKey": "your-moonraker-key"
    }
  ],
  "slicers": {
    "prusaslicer": "/usr/local/bin/prusa-slicer",
    "cura": "/usr/local/bin/CuraEngine"
  }
}
```

## Usage Examples

### Natural Language Commands

```
"Start printing the vase model on the Prusa"
"Pause all prints immediately"
"What's the status of my Voron printer?"
"Slice this STL with 0.2mm layers and 20% infill"
```

### MCP Protocol Examples

```json
// Get printer status
{
  "method": "printer.status",
  "params": {
    "printer": "Prusa MK3S+"
  }
}

// Start a print
{
  "method": "printer.print",
  "params": {
    "printer": "Voron 2.4",
    "file": "model.gcode",
    "preheat": true
  }
}
```

## AI Integration Features

### Print Quality Optimization
- Analyzes model geometry to suggest optimal orientation
- Recommends support structures based on overhangs
- Predicts print time and material usage

### Failure Prevention
- Monitors first layer adhesion via camera (if available)
- Detects stringing, warping, and layer shifts
- Automatic pause and notification on issues

### Learning Capabilities
- Learns from successful prints to improve recommendations
- Adapts to specific printer characteristics
- User preference learning for settings

## Advanced Features

### Batch Processing
```bash
# Print multiple models with optimal bed arrangement
mcp-3d-printer batch --models "*.stl" --printer "Prusa MK3S+"
```

### Remote Monitoring
- Web dashboard for print progress
- Mobile notifications via webhooks
- Integration with home automation systems

### Print Farm Management
- Queue management across multiple printers
- Load balancing for optimal throughput
- Maintenance scheduling and reminders

## API Reference

Full API documentation available at [GitHub Wiki](https://github.com/DMontgomery40/mcp-3D-printer-server/wiki)

### Core Methods
- `printer.list()` - List available printers
- `printer.status(name)` - Get printer status
- `printer.print(name, file, options)` - Start print job
- `printer.pause(name)` - Pause active print
- `printer.resume(name)` - Resume paused print
- `printer.cancel(name)` - Cancel active print
- `slicer.slice(file, profile, options)` - Slice STL/3MF file

## Safety & Best Practices

- Always verify generated G-code before printing
- Set temperature limits in printer firmware
- Use thermal runaway protection
- Regular maintenance scheduling
- Proper ventilation for printing area

## Contributing

Contributions welcome! See [CONTRIBUTING.md](https://github.com/DMontgomery40/mcp-3D-printer-server/blob/main/CONTRIBUTING.md) for guidelines.

## License

MIT License - see [LICENSE](https://github.com/DMontgomery40/mcp-3D-printer-server/blob/main/LICENSE)

---

[← Back to Projects]({{ site.baseurl }}/Projects/) | [View All Projects]({{ site.baseurl }}/Projects/)
