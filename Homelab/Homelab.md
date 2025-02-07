---
title: Enterprise AI and Security Homelab
layout: default
parent: Homelab
nav_order: 1
has_toc: true
---

# Enterprise-Grade AI and Security Homelab

A sophisticated home laboratory environment architected for AI/ML research, advanced computer vision, and multi-layered cybersecurity, demonstrating enterprise-level implementation of modern technologies.

![Homelab Network Diagram]({{ site.baseurl }}/assets/homelab.jpg)

## Architecture Overview

### Network Security Infrastructure
- **Firewalla Gold**: Primary gateway security with IDS/IPS capabilities
- **pfSense VM**: Secondary firewall in DMZ configuration
- **Pi-hole**: Network-wide DNS sinkhole for ad blocking and security
- **Layered DMZ Architecture**: Enterprise-grade network segmentation
- **Multi-DNS Strategy**: Redundant DNS with security filtering

### AI/ML Compute Cluster
- **Proxmox Cluster Infrastructure**:
  - 2× Intel i13500h Nodes: High-performance AI compute
  - AMD 7125h Node: Dedicated ML processing
  - Intel n100 NUC: Edge computing node
  - Distributed workload management across nodes

### Computer Vision and Security Systems
- **Scrypted AI Vision Platform**:
  - Custom YOLO v9 Implementation
  - INT4-quantized model for efficient inference
  - Distributed processing across cluster nodes
  - Real-time object detection and tracking
- **Multi-Camera Security System**:
  - Enterprise-grade Axis, Hikvision, and Dahua cameras
  - AI-powered motion detection and analysis
  - Automated threat detection and response

### Local LLM Infrastructure
- **On-premises AI Models**:
  - Ollama: Containerized LLM deployment
  - LM Studio: Model fine-tuning and optimization
  - Custom model distillation pipeline
  - Secure API endpoints for internal services

### Network Topology
- **Segmented Network Design**:
  - Dedicated IoT VLAN
  - Isolated Camera Network
  - AI/ML Compute VLAN
  - Management Network
- **PoE Infrastructure**:
  - Distributed PoE switches
  - Redundant power delivery
  - Smart power management

### Monitoring and Analytics
- **HomeAssistant Integration**:
  - Centralized automation control
  - AI-powered scene detection
  - Security event correlation
- **BirdNET-Pi**:
  - Audio ML processing
  - Environmental monitoring
- **Heimdall Dashboard**:
  - System-wide monitoring
  - Performance analytics
  - Security metrics

This advanced homelab demonstrates professional-grade implementation of AI/ML technologies, computer vision systems, and cybersecurity practices. The architecture showcases expertise in:

- Enterprise network security and segmentation
- Distributed AI/ML compute infrastructure
- Custom model optimization and deployment
- Real-time computer vision processing
- Local LLM hosting and API development
- Advanced automation and monitoring

The lab serves as a practical testing ground for cutting-edge technologies while maintaining enterprise-level security standards and performance optimization.