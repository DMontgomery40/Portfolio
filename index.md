---
layout: home
title: Home
description: Full Stack Developer & Security Researcher specializing in backend systems, AI infrastructure, and cybersecurity tools
---

<!-- Hero Section -->
<div class="hero-section">
    <div class="hero-background"></div>
    <div class="hero-particles"></div>
    <div class="hero-content">
        <div class="container">
            <h1 class="hero-title">David Montgomery</h1>
            <h2 class="hero-subtitle">Full Stack Developer & <span class="typing-text" id="typing-text">Security Researcher</span></h2>
            <p class="hero-description">
                Building the backend, securing the stack, and making AI accessible to everyone. 
                Specializing in security tools, AI infrastructure, and system utilities.
            </p>
            <div class="cta-buttons">
                <a href="#projects" class="btn btn-primary">
                    <i class="fas fa-code"></i> View Projects
                </a>
                <a href="{{ site.baseurl }}/assets/David_Montgomery_Resume_Developer_Focused.pdf" class="btn btn-secondary" target="_blank">
                    <i class="fas fa-download"></i> Download Resume
                </a>
            </div>
        </div>
    </div>
</div>

<!-- Live Stats Section -->
<section class="stats-section">
    <div class="container">
        <div class="stats-grid">
            <div class="stat-card">
                <div class="stat-number" id="total-downloads" data-count="0">0</div>
                <div class="stat-label">Package Downloads</div>
                <div class="stat-description">NPM + PyPI combined</div>
            </div>
            <div class="stat-card">
                <div class="stat-number" id="github-stars" data-count="0">0</div>
                <div class="stat-label">GitHub Stars</div>
                <div class="stat-description">Community recognition</div>
            </div>
            <div class="stat-card">
                <div class="stat-number" id="total-packages" data-count="0">0</div>
                <div class="stat-label">Packages & Repos</div>
                <div class="stat-description">Open source contributions</div>
            </div>
            <div class="stat-card">
                <div class="stat-number" id="github-forks" data-count="0">0</div>
                <div class="stat-label">Repository Forks</div>
                <div class="stat-description">Community collaboration</div>
            </div>
        </div>
        <div class="stats-update-note" style="text-align: center; margin-top: 1rem; color: var(--text-muted); font-size: 0.85rem;">
            <span id="stats-update-time">Loading live stats...</span>
        </div>
    </div>
</section>

<!-- Featured Projects -->
<section class="featured-projects" id="projects">
    <div class="container">
        <h2 class="section-title">Featured Projects</h2>
        <p class="section-subtitle">A showcase of my latest work in security, AI, and system utilities</p>
        
        <div class="projects-grid grid-3">
            <div class="project-card card">
                <div class="project-icon">
                    <i class="fas fa-shield-alt"></i>
                </div>
                <h3 class="project-title">SecurityLens</h3>
                <p class="project-description">
                    Open-source security analysis platform for vulnerability discovery and education. 
                    Features web-based scanning interface and binary analysis capabilities.
                </p>
                <div class="project-tags">
                    <span class="tag">Python</span>
                    <span class="tag">Security</span>
                    <span class="tag">Flask</span>
                    <span class="tag">Vue.js</span>
                </div>
                <div class="project-links">
                    <a href="https://securitylens.io" class="btn btn-primary btn-sm" target="_blank">
                        <i class="fas fa-external-link-alt"></i> Live Demo
                    </a>
                    <a href="{{ site.baseurl }}/Projects/SecurityLens/" class="btn btn-secondary btn-sm">
                        <i class="fas fa-info-circle"></i> Learn More
                    </a>
                </div>
            </div>

            <div class="project-card card">
                <div class="project-icon">
                    <i class="fas fa-bug"></i>
                </div>
                <h3 class="project-title">Pentest MCP</h3>
                <p class="project-description">
                    Professional penetration testing toolkit with STDIO/HTTP/SSE support. 
                    Integrates Nmap, Gobuster, Nikto, John the Ripper, and Hashcat with GPU acceleration through natural language commands.
                </p>
                <div class="project-tags">
                    <span class="tag">Node.js</span>
                    <span class="tag">Security</span>
                    <span class="tag">Docker</span>
                    <span class="tag">GPU</span>
                </div>
                <div class="project-links">
                    <a href="https://github.com/DMontgomery40/pentest-mcp" class="btn btn-primary btn-sm" target="_blank">
                        <i class="fab fa-github"></i> GitHub
                    </a>
                    <a href="{{ site.baseurl }}/Projects/pentest-mcp/" class="btn btn-secondary btn-sm">
                        <i class="fas fa-info-circle"></i> Learn More
                    </a>
                </div>
            </div>

            <div class="project-card card">
                <div class="project-icon">
                    <i class="fas fa-brain"></i>
                </div>
                <h3 class="project-title">Deepseek MCP Server</h3>
                <p class="project-description">
                    Model Context Protocol server for running large language models locally. 
                    Provides REST API for text generation and embeddings with privacy focus.
                </p>
                <div class="project-tags">
                    <span class="tag">Python</span>
                    <span class="tag">AI/ML</span>
                    <span class="tag">FastAPI</span>
                    <span class="tag">Docker</span>
                </div>
                <div class="project-links">
                    <a href="https://github.com/DMontgomery40/deepseek-mcp-server" class="btn btn-primary btn-sm" target="_blank">
                        <i class="fab fa-github"></i> GitHub
                    </a>
                    <a href="{{ site.baseurl }}/Projects/deepseek-mcp-server/" class="btn btn-secondary btn-sm">
                        <i class="fas fa-info-circle"></i> Learn More
                    </a>
                </div>
            </div>
        </div>

        <div class="text-center" style="margin-top: 3rem;">
            <a href="{{ site.baseurl }}/Projects/" class="btn btn-primary">
                <i class="fas fa-th"></i> View All Projects
            </a>
        </div>
    </div>
</section>

<!-- Latest Articles -->
<section class="latest-articles">
    <div class="container">
        <h2 class="section-title">Latest Articles</h2>
        <p class="section-subtitle">Technical writing on security, AI, and modern development</p>
        
        <div class="articles-grid grid-2">
            <article class="article-card card">
                <div class="article-icon">
                    <i class="fas fa-wifi"></i>
                </div>
                <div class="article-content">
                    <h3 class="article-title">Wireless Network Security in 2025</h3>
                    <p class="article-excerpt">
                        Exploring the evolving landscape of wireless security, emerging threats, 
                        and future-proof protection strategies.
                    </p>
                    <div class="article-meta">
                        <span class="article-date">January 2025</span>
                        <span class="article-read-time">8 min read</span>
                    </div>
                    <a href="https://medium.com/@dmontg/wireless-network-security-in-2025-and-beyond-71f7c13f9889" class="btn btn-primary btn-sm" target="_blank">
                        <i class="fab fa-medium"></i> Read on Medium
                    </a>
                </div>
            </article>

            <article class="article-card card">
                <div class="article-icon">
                    <i class="fas fa-key"></i>
                </div>
                <div class="article-content">
                    <h3 class="article-title">Fundamentals of Cryptography</h3>
                    <p class="article-excerpt">
                        A comprehensive exploration of cryptographic hashing, from basic principles 
                        to quantum-resistant algorithms.
                    </p>
                    <div class="article-meta">
                        <span class="article-date">December 2024</span>
                        <span class="article-read-time">12 min read</span>
                    </div>
                    <a href="https://medium.com/@dmontg/deep-dive-fundamentals-and-the-future-of-hashing-and-cryptography-94ad3e458a7e" class="btn btn-primary btn-sm" target="_blank">
                        <i class="fab fa-medium"></i> Read on Medium
                    </a>
                </div>
            </article>
        </div>

        <div class="text-center" style="margin-top: 2rem;">
            <a href="{{ site.baseurl }}/articles/" class="btn btn-secondary">
                <i class="fas fa-newspaper"></i> View All Articles
            </a>
        </div>
    </div>
</section>

<!-- Skills Overview -->
<section class="skills-overview">
    <div class="container">
        <h2 class="section-title">Technical Expertise</h2>
        <p class="section-subtitle">A comprehensive toolkit for modern development and security</p>
        
        <div class="skills-grid grid-4">
            <div class="skill-category card">
                <div class="skill-icon">
                    <i class="fas fa-code"></i>
                </div>
                <h3>Backend Development</h3>
                <ul>
                    <li>Python (FastAPI, Flask)</li>
                    <li>Node.js (Express, NestJS)</li>
                    <li>Go & Rust</li>
                    <li>API Design</li>
                </ul>
            </div>
            
            <div class="skill-category card">
                <div class="skill-icon">
                    <i class="fas fa-shield-alt"></i>
                </div>
                <h3>Security & Pentesting</h3>
                <ul>
                    <li>Vulnerability Assessment</li>
                    <li>Binary Analysis</li>
                    <li>Network Security</li>
                    <li>Cryptography</li>
                </ul>
            </div>
            
            <div class="skill-category card">
                <div class="skill-icon">
                    <i class="fas fa-brain"></i>
                </div>
                <h3>AI/ML & Data</h3>
                <ul>
                    <li>PyTorch & TensorFlow</li>
                    <li>Local LLM Deployment</li>
                    <li>Computer Vision</li>
                    <li>Model Optimization</li>
                </ul>
            </div>
            
            <div class="skill-category card">
                <div class="skill-icon">
                    <i class="fas fa-server"></i>
                </div>
                <h3>Infrastructure</h3>
                <ul>
                    <li>Docker & Kubernetes</li>
                    <li>AWS & Cloud Services</li>
                    <li>Linux Administration</li>
                    <li>CI/CD Pipelines</li>
                </ul>
            </div>
        </div>
    </div>
</section>

<!-- Quick Links -->
<section class="quick-links">
    <div class="container">
        <h2 class="section-title">Explore More</h2>
        <div class="quick-links-grid grid-3">
            <a href="{{ site.baseurl }}/Homelab/" class="quick-link-card card">
                <div class="quick-link-icon">
                    <i class="fas fa-home"></i>
                </div>
                <h3>HomeLab</h3>
                <p>Enterprise-grade infrastructure for development and AI research</p>
                <span class="quick-link-arrow"><i class="fas fa-arrow-right"></i></span>
            </a>
            
            <a href="{{ site.baseurl }}/Storytime/" class="quick-link-card card">
                <div class="quick-link-icon">
                    <i class="fas fa-book-open"></i>
                </div>
                <h3>Story Time</h3>
                <p>My journey from phone phreaking to modern AI development</p>
                <span class="quick-link-arrow"><i class="fas fa-arrow-right"></i></span>
            </a>
            
            <a href="{{ site.baseurl }}/Resume/" class="quick-link-card card">
                <div class="quick-link-icon">
                    <i class="fas fa-file-user"></i>
                </div>
                <h3>Resume</h3>
                <p>Professional experience and qualifications</p>
                <span class="quick-link-arrow"><i class="fas fa-arrow-right"></i></span>
            </a>
        </div>
    </div>
</section>