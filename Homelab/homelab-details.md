---
layout: default
title: Enterprise AI and Security Homelab
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
  - 2x Intel i13500h Nodes: High-performance AI compute
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

### Storage and Infrastructure
- **TrueNAS Scale**: ZFS-based storage with Kubernetes integration
- **Proxmox Cluster**: Full VM and LXC container orchestration
- **Automated Backup Pipeline**: Multi-tier backup strategy
- **Network-wide Monitoring**: Grafana/Prometheus stack

### AI/ML Development Environment
- **Local LLM Infrastructure**:
  - Multiple model serving frameworks
  - Custom fine-tuning pipeline
  - RAG implementation with vector databases
- **Training Pipeline**:
  - Distributed training across cluster nodes
  - Custom dataset management
  - Model evaluation and benchmarking
