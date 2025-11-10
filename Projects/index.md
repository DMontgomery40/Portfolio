---
layout: default
title: Projects Portfolio
description: A collection of software development projects demonstrating expertise in backend systems, security tools, AI/ML infrastructure, and educational technology
---

<!-- Projects Filter Section -->
<div class="projects-filter">
    <div class="container">
        <div class="filter-tabs">
            <button class="filter-tab active" data-filter="all">All Projects</button>
            <button class="filter-tab" data-filter="security">Security</button>
            <button class="filter-tab" data-filter="ai-ml">AI/ML</button>
            <button class="filter-tab" data-filter="infrastructure">Infrastructure</button>
            <button class="filter-tab" data-filter="tools">Tools</button>
        </div>
        <div class="filter-search">
            <input type="text" id="projectSearch" placeholder="Search projects..." class="search-input">
            <i class="fas fa-search search-icon"></i>
        </div>
    </div>
</div>

<!-- Featured Projects -->
<section class="featured-projects-section">
    <div class="container">
        <h2 class="section-title">Featured Projects</h2>
        <div class="projects-grid grid-3">
            
            <!-- SecurityLens -->
            <div class="project-card card" data-category="security" data-keywords="security vulnerability scanning analysis">
                <div class="project-badge featured">Featured</div>
                <div class="project-icon">
                    <i class="fas fa-shield-alt"></i>
                </div>
                <h3 class="project-title">SecurityLens</h3>
                <p class="project-description">
                    Open-source security analysis platform for vulnerability discovery and education. 
                    Features web-based scanning interface with support for 32+ vulnerability types.
                </p>
                <div class="project-stats">
                    <span class="stat"><i class="fas fa-star"></i> Production Ready</span>
                    <span class="stat"><i class="fas fa-users"></i> Active Users</span>
                </div>
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
                    <a href="{{ site.baseurl }}/projects/securitylens/" class="btn btn-secondary btn-sm">
                        <i class="fas fa-info-circle"></i> Details
                    </a>
                </div>
            </div>

            <!-- Pentest MCP -->
            <div class="project-card card" data-category="security" data-keywords="pentesting security hacking mcp ai professional">
                <div class="project-badge featured">Featured</div>
                <div class="project-icon">
                    <i class="fas fa-bug"></i>
                </div>
                <h3 class="project-title">Pentest MCP</h3>
                <p class="project-description">
                    Professional penetration testing toolkit with STDIO/HTTP/SSE support. 
                    Integrates Nmap, Gobuster, Nikto, John the Ripper, and Hashcat with GPU acceleration through natural language commands.
                </p>
                <div class="project-stats">
                    <span class="stat"><i class="fas fa-layer-group"></i> Multi-Transport</span>
                    <span class="stat"><i class="fas fa-microchip"></i> GPU Accelerated</span>
                </div>
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
                    <a href="{{ site.baseurl }}/projects/pentest-mcp/" class="btn btn-secondary btn-sm">
                        <i class="fas fa-info-circle"></i> Details
                    </a>
                </div>
            </div>

            <!-- Deepseek MCP Server -->
            <div class="project-card card" data-category="ai-ml" data-keywords="ai ml llm mcp server deepseek">
                <div class="project-badge new">New</div>
                <div class="project-icon">
                    <i class="fas fa-brain"></i>
                </div>
                <h3 class="project-title">Deepseek MCP Server</h3>
                <p class="project-description">
                    Model Context Protocol server for running large language models locally. 
                    Bypass rate limits while keeping your data private.
                </p>
                <div class="project-stats">
                    <span class="stat"><i class="fab fa-github"></i> 50+ Stars</span>
                    <span class="stat"><i class="fas fa-download"></i> 1K+ Downloads</span>
                </div>
                <div class="project-tags">
                    <span class="tag">Python</span>
                    <span class="tag">AI/ML</span>
                    <span class="tag">FastAPI</span>
                    <span class="tag">MCP</span>
                </div>
                <div class="project-links">
                    <a href="https://github.com/DMontgomery40/deepseek-mcp-server" class="btn btn-primary btn-sm" target="_blank">
                        <i class="fab fa-github"></i> GitHub
                    </a>
                    <a href="{{ site.baseurl }}/projects/deepseek-mcp-server/" class="btn btn-secondary btn-sm">
                        <i class="fas fa-info-circle"></i> Details
                    </a>
                </div>
            </div>

            <!-- Faxbot -->
            <div class="project-card card" data-category="tools" data-keywords="fax communications hipaa compliance mcp api">
                <div class="project-badge featured">Featured</div>
                <div class="project-icon">
                    <i class="fas fa-fax"></i>
                </div>
                <h3 class="project-title">Faxbot</h3>
                <p class="project-description">
                    The only known open‑source, self‑hosted fax server and API — and the only fax server (as far as known) that supports distinct inbound vs. outbound provider routing for cost, reliability, and compliance flexibility. HIPAA‑aligned design, Docker deploy, a clean REST surface, and MCP integration so AI assistants can send/receive faxes via auditable actions.
                </p>
                <div class="project-stats">
                    <span class="stat"><i class="fas fa-shield-alt"></i> HIPAA-Aligned</span>
                    <span class="stat"><i class="fas fa-server"></i> Self-Hosted</span>
                </div>
                <div class="project-tags">
                    <span class="tag">TypeScript</span>
                    <span class="tag">Python</span>
                    <span class="tag">Docker</span>
                    <span class="tag">REST</span>
                    <span class="tag">MCP</span>
                    <span class="tag">HIPAA</span>
                </div>
                <div class="project-links">
                    <a href="https://faxbot.net" class="btn btn-primary btn-sm" target="_blank">
                        <i class="fas fa-external-link-alt"></i> Live Site
                    </a>
                    <a href="https://github.com/DMontgomery40/Faxbot" class="btn btn-primary btn-sm" target="_blank">
                        <i class="fab fa-github"></i> GitHub
                    </a>
                    <a href="{{ site.baseurl }}/projects/faxbot/" class="btn btn-secondary btn-sm">
                        <i class="fas fa-info-circle"></i> Details
                    </a>
                </div>
            </div>
        </div>
    </div>
</section>

<!-- All Projects -->
<section class="all-projects-section">
    <div class="container">
        <h2 class="section-title">All Projects</h2>
        <div class="projects-grid grid-3" id="projectsContainer">
            
            <!-- vivified -->
            <div class="project-card card" data-category="security" data-keywords="zero-trust security kernel policy isolation">
                <div class="project-icon">
                    <i class="fas fa-lock"></i>
                </div>
                <h3 class="project-title">vivified</h3>
                <p class="project-description">
                    Zero‑Trust Enterprise Application Kernel enforcing capability‑gated interfaces, policy‑as‑code isolation, and least‑privilege boundaries. Hardens multi‑component architectures with auditable flows and minimized attack surface.
                </p>
                <div class="project-tags">
                    <span class="tag">TypeScript</span>
                    <span class="tag">Python</span>
                    <span class="tag">Zero‑Trust</span>
                    <span class="tag">Policy‑as‑Code</span>
                </div>
                <div class="project-links">
                    <a href="https://github.com/DMontgomery40/vivified" class="btn btn-primary btn-sm" target="_blank">
                        <i class="fab fa-github"></i> GitHub
                    </a>
                    <a href="{{ site.baseurl }}/projects/vivified/" class="btn btn-secondary btn-sm">
                        <i class="fas fa-info-circle"></i> Details
                    </a>
                </div>
            </div>

            <!-- agro-rag-engine -->
            <div class="project-card card" data-category="ai-ml" data-keywords="rag retrieval vector ai ml agriculture">
                <div class="project-icon">
                    <i class="fas fa-seedling"></i>
                </div>
                <h3 class="project-title">agro‑rag‑engine</h3>
                <p class="project-description">
                    Domain‑focused RAG engine for agricultural content: ingestion → structured chunking &amp; embedding → vector indexing → high‑signal retrieval → prompt orchestration grounding outputs in authoritative sources. Includes a demo UI for rapid iteration.
                </p>
                <div class="project-tags">
                    <span class="tag">Python</span>
                    <span class="tag">TypeScript</span>
                    <span class="tag">RAG</span>
                    <span class="tag">Vector</span>
                    <span class="tag">AI/ML</span>
                </div>
                <div class="project-links">
                    <a href="https://github.com/DMontgomery40/agro-rag-engine" class="btn btn-primary btn-sm" target="_blank">
                        <i class="fab fa-github"></i> GitHub
                    </a>
                    <a href="{{ site.baseurl }}/projects/agro-rag-engine/" class="btn btn-secondary btn-sm">
                        <i class="fas fa-info-circle"></i> Details
                    </a>
                </div>
            </div>

            <!-- agentspec -->
            <div class="project-card card" data-category="tools" data-keywords="python tooling ci spec ai documentation">
                <div class="project-icon">
                    <i class="fas fa-file-code"></i>
                </div>
                <h3 class="project-title">agentspec</h3>
                <p class="project-description">
                    Schema‑enforced, machine‑readable docstrings for Python codebases enabling reliable AI/LLM tooling and CI validation. Contracts become parseable and enforceable to reduce ambiguity for tooling and model integrations.
                </p>
                <div class="project-tags">
                    <span class="tag">Python</span>
                    <span class="tag">Tooling</span>
                    <span class="tag">CI</span>
                    <span class="tag">Spec</span>
                </div>
                <div class="project-links">
                    <a href="https://github.com/DMontgomery40/agentspec" class="btn btn-primary btn-sm" target="_blank">
                        <i class="fab fa-github"></i> GitHub
                    </a>
                    <a href="{{ site.baseurl }}/projects/agentspec/" class="btn btn-secondary btn-sm">
                        <i class="fas fa-info-circle"></i> Details
                    </a>
                </div>
            </div>
            
            <!-- Intel NPU Monitor -->
            <div class="project-card card" data-category="tools infrastructure" data-keywords="intel npu monitoring hardware">
                <div class="project-icon">
                    <i class="fas fa-microchip"></i>
                </div>
                <h3 class="project-title">Intel NPU Monitor</h3>
                <p class="project-description">
                    Lightweight monitoring tool for Intel Neural Processing Units. 
                    Just 52 lines of pure Python with zero dependencies.
                </p>
                <div class="project-tags">
                    <span class="tag">Python</span>
                    <span class="tag">Hardware</span>
                    <span class="tag">NPU</span>
                    <span class="tag">Monitoring</span>
                </div>
                <div class="project-links">
                    <a href="https://github.com/DMontgomery40/intel-npu-top" class="btn btn-primary btn-sm" target="_blank">
                        <i class="fab fa-github"></i> GitHub
                    </a>
                    <a href="{{ site.baseurl }}/projects/intel-npu-top/" class="btn btn-secondary btn-sm">
                        <i class="fas fa-info-circle"></i> Details
                    </a>
                </div>
            </div>
            
            <!-- MCP 3D Printer Server -->
            <div class="project-card card" data-category="tools infrastructure" data-keywords="3d printer mcp iot automation">
                <div class="project-icon">
                    <i class="fas fa-cube"></i>
                </div>
                <h3 class="project-title">MCP 3D Printer Server</h3>
                <p class="project-description">
                    AI-powered 3D printer control through Model Context Protocol. 
                    Universal support for OctoPrint, Klipper, Duet, and more.
                </p>
                <div class="project-tags">
                    <span class="tag">Node.js</span>
                    <span class="tag">IoT</span>
                    <span class="tag">3D Printing</span>
                    <span class="tag">MCP</span>
                </div>
                <div class="project-links">
                    <a href="https://github.com/DMontgomery40/mcp-3D-printer-server" class="btn btn-primary btn-sm" target="_blank">
                        <i class="fab fa-github"></i> GitHub
                    </a>
                    <a href="{{ site.baseurl }}/projects/mcp-3d-printer-server/" class="btn btn-secondary btn-sm">
                        <i class="fas fa-info-circle"></i> Details
                    </a>
                </div>
            </div>

            <!-- BirdStats GPT -->
            <div class="project-card card" data-category="ai-ml" data-keywords="birds ai gpt data analysis ornithology">
                <div class="project-icon">
                    <i class="fas fa-dove"></i>
                </div>
                <h3 class="project-title">BirdStats GPT</h3>
                <p class="project-description">
                    AI-powered bird observation analysis connecting BirdNET-Pi data with eBird. 
                    Natural language interface for birding statistics.
                </p>
                <div class="project-tags">
                    <span class="tag">AI/ML</span>
                    <span class="tag">Data Analysis</span>
                    <span class="tag">APIs</span>
                    <span class="tag">OpenAI</span>
                </div>
                <div class="project-links">
                    <a href="https://chat.openai.com/g/g-G8R6D6ufP-birdstats-gpt" class="btn btn-primary btn-sm" target="_blank">
                        <i class="fas fa-external-link-alt"></i> Try It
                    </a>
                    <a href="{{ site.baseurl }}/projects/birdstatsgpt/" class="btn btn-secondary btn-sm">
                        <i class="fas fa-info-circle"></i> Details
                    </a>
                </div>
            </div>

            <!-- MCP Server BirdStats -->
            <div class="project-card card" data-category="ai-ml tools" data-keywords="mcp birds api server data">
                <div class="project-icon">
                    <i class="fas fa-server"></i>
                </div>
                <h3 class="project-title">MCP Server BirdStats</h3>
                <p class="project-description">
                    Model Context Protocol server for bird observation data. 
                    Cross-reference BirdNET-Pi with eBird observations.
                </p>
                <div class="project-tags">
                    <span class="tag">Node.js</span>
                    <span class="tag">MCP</span>
                    <span class="tag">APIs</span>
                    <span class="tag">Data</span>
                </div>
                <div class="project-links">
                    <a href="https://github.com/DMontgomery40/mcp-server-birdstats" class="btn btn-primary btn-sm" target="_blank">
                        <i class="fab fa-github"></i> GitHub
                    </a>
                    <a href="{{ site.baseurl }}/projects/mcp-server-birdstats/" class="btn btn-secondary btn-sm">
                        <i class="fas fa-info-circle"></i> Details
                    </a>
                </div>
            </div>

            <!-- MCP Canvas Server -->
            <div class="project-card card" data-category="tools" data-keywords="canvas lms education mcp server">
                <div class="project-icon">
                    <i class="fas fa-graduation-cap"></i>
                </div>
                <h3 class="project-title">MCP Canvas Server</h3>
                <p class="project-description">
                    Canvas LMS integration via Model Context Protocol. 
                    Automated course management and grade analysis.
                </p>
                <div class="project-tags">
                    <span class="tag">Node.js</span>
                    <span class="tag">Education</span>
                    <span class="tag">LMS</span>
                    <span class="tag">MCP</span>
                </div>
                <div class="project-links">
                    <a href="https://github.com/DMontgomery40/mcp-server-canvas" class="btn btn-primary btn-sm" target="_blank">
                        <i class="fab fa-github"></i> GitHub
                    </a>
                    <a href="{{ site.baseurl }}/projects/mcp-server-canvas/" class="btn btn-secondary btn-sm">
                        <i class="fas fa-info-circle"></i> Details
                    </a>
                </div>
            </div>

            <!-- Attack Vector Analysis Tool -->
            <div class="project-card card" data-category="security" data-keywords="attack vector analysis security vulnerability">
                <div class="project-icon">
                    <i class="fas fa-network-wired"></i>
                </div>
                <h3 class="project-title">Attack Vector Analysis</h3>
                <p class="project-description">
                    Interactive security vulnerability assessment interface. 
                    Maps relationships between attack vectors and risk levels.
                </p>
                <div class="project-tags">
                    <span class="tag">React</span>
                    <span class="tag">Security</span>
                    <span class="tag">Visualization</span>
                    <span class="tag">Education</span>
                </div>
                <div class="project-links">
                    <a href="https://claude.site/artifacts/abcf42a2-194c-4593-afbd-9ba562b56d79" class="btn btn-primary btn-sm" target="_blank">
                        <i class="fas fa-external-link-alt"></i> Demo
                    </a>
                    <a href="{{ site.baseurl }}/projects/attackvectoranalysistool/" class="btn btn-secondary btn-sm">
                        <i class="fas fa-info-circle"></i> Details
                    </a>
                </div>
            </div>

            <!-- Secure Anonymous Messaging System -->
            <div class="project-card card" data-category="security" data-keywords="steganography security privacy messaging encryption">
                <div class="project-icon">
                    <i class="fas fa-user-secret"></i>
                </div>
                <h3 class="project-title">Secure Anonymous Messaging System | Open Source Contribution</h3>
                <p class="project-description">
                    Steganographic communications disguised as an e‑commerce returns workflow; time‑limited per‑message unlock (10s), encrypted storage with decoy text, zero‑footprint UX. Deployed to prevent harm in a domestic violence case.
                </p>
                <div class="project-tags">
                    <span class="tag">Security</span>
                    <span class="tag">Steganography</span>
                    <span class="tag">Crypto</span>
                    <span class="tag">Privacy</span>
                    <span class="tag">Zero‑Footprint</span>
                </div>
                <div class="project-links">
                    <a href="{{ site.baseurl }}/projects/secure-anonymous-messaging/" class="btn btn-secondary btn-sm">
                        <i class="fas fa-info-circle"></i> Details
                    </a>
                </div>
            </div>
        </div>

        <!-- Load More Button -->
        <div class="text-center" style="margin-top: 3rem;">
            <button class="btn btn-secondary" id="loadMoreBtn" style="display: none;">
                <i class="fas fa-plus"></i> Load More Projects
            </button>
        </div>
    </div>
</section>

<!-- Project Statistics -->
<section class="project-stats-section">
    <div class="container">
        <h2 class="section-title">Portfolio Statistics</h2>
        <div class="stats-grid grid-4">
            <div class="stat-card card">
                <div class="stat-icon">
                    <i class="fas fa-code"></i>
                </div>
                <div class="stat-number">15</div>
                <div class="stat-label">Total Projects</div>
                <div class="stat-description">Across multiple domains</div>
            </div>
            <div class="stat-card card">
                <div class="stat-icon">
                    <i class="fas fa-language"></i>
                </div>
                <div class="stat-number">7</div>
                <div class="stat-label">Languages Used</div>
                <div class="stat-description">Python, Node.js, Go, and more</div>
            </div>
            <div class="stat-card card">
                <div class="stat-icon">
                    <i class="fas fa-star"></i>
                </div>
                <div class="stat-number">200+</div>
                <div class="stat-label">GitHub Stars</div>
                <div class="stat-description">Community appreciation</div>
            </div>
            <div class="stat-card card">
                <div class="stat-icon">
                    <i class="fas fa-download"></i>
                </div>
                <div class="stat-number">5K+</div>
                <div class="stat-label">Downloads</div>
                <div class="stat-description">NPM and PyPI packages</div>
            </div>
        </div>
    </div>
</section>

<style>
/* Projects Filter */
.projects-filter {
    background: var(--bg-card);
    padding: 2rem 0;
    border-bottom: 1px solid var(--border);
    position: sticky;
    top: 80px;
    z-index: 100;
}

.filter-tabs {
    display: flex;
    gap: 1rem;
    justify-content: center;
    flex-wrap: wrap;
    margin-bottom: 2rem;
}

.filter-tab {
    background: var(--bg-hover);
    border: 1px solid var(--border);
    color: var(--text-secondary);
    padding: 0.75rem 1.5rem;
    border-radius: 25px;
    cursor: pointer;
    transition: all 0.3s ease;
    font-weight: 500;
}

.filter-tab:hover,
.filter-tab.active {
    background: var(--primary);
    color: var(--bg-dark);
    border-color: var(--primary);
}

.filter-search {
    position: relative;
    max-width: 400px;
    margin: 0 auto;
}

.search-input {
    width: 100%;
    padding: 0.75rem 1rem 0.75rem 3rem;
    background: var(--bg-hover);
    border: 1px solid var(--border);
    border-radius: 25px;
    color: var(--text-primary);
    font-size: 1rem;
    transition: all 0.3s ease;
}

.search-input:focus {
    outline: none;
    border-color: var(--primary);
    box-shadow: 0 0 0 3px rgba(0, 245, 255, 0.1);
}

.search-icon {
    position: absolute;
    left: 1rem;
    top: 50%;
    transform: translateY(-50%);
    color: var(--text-muted);
}

/* Project Cards */
.featured-projects-section,
.all-projects-section,
.project-stats-section {
    padding: 4rem 0;
}

.all-projects-section {
    background: var(--bg-card);
}

.project-card {
    position: relative;
    transition: all 0.3s ease;
    opacity: 1;
    transform: scale(1);
}

.project-card.hidden {
    opacity: 0;
    transform: scale(0.8);
    pointer-events: none;
}

.project-badge {
    position: absolute;
    top: 1rem;
    right: 1rem;
    padding: 0.25rem 0.75rem;
    border-radius: 15px;
    font-size: 0.8rem;
    font-weight: 600;
    text-transform: uppercase;
    z-index: 2;
}

.project-badge.featured {
    background: rgba(255, 193, 7, 0.2);
    color: #ffc107;
}

.project-badge.new {
    background: rgba(76, 175, 80, 0.2);
    color: #4caf50;
}

.project-icon {
    width: 60px;
    height: 60px;
    background: var(--gradient);
    border-radius: 15px;
    display: flex;
    align-items: center;
    justify-content: center;
    margin-bottom: 1.5rem;
    font-size: 1.5rem;
    color: var(--bg-dark);
}

.project-title {
    font-size: 1.5rem;
    font-weight: 600;
    margin-bottom: 1rem;
    color: var(--text-primary);
}

.project-description {
    color: var(--text-secondary);
    margin-bottom: 1.5rem;
    line-height: 1.6;
    min-height: 4rem; /* Ensure consistent card heights */
}

.project-stats {
    display: flex;
    gap: 1rem;
    margin-bottom: 1.5rem;
    flex-wrap: wrap;
}

.stat {
    display: flex;
    align-items: center;
    gap: 0.25rem;
    font-size: 0.85rem;
    color: var(--text-muted);
}

.project-tags {
    display: flex;
    flex-wrap: wrap;
    gap: 0.5rem;
    margin-bottom: 1.5rem;
}

.tag {
    background: rgba(0, 245, 255, 0.1);
    color: var(--primary);
    padding: 0.3rem 0.8rem;
    border-radius: 20px;
    font-size: 0.8rem;
    border: 1px solid rgba(0, 245, 255, 0.2);
}

.project-links {
    display: flex;
    gap: 1rem;
}

.btn-sm {
    padding: 0.6rem 1.2rem;
    font-size: 0.85rem;
}

/* Statistics Section */
.project-stats-section {
    background: var(--bg-dark);
}

.stat-card {
    text-align: center;
    padding: 2rem;
    transition: all 0.3s ease;
}

.stat-card:hover {
    transform: translateY(-5px);
    box-shadow: var(--shadow);
}

.stat-icon {
    width: 60px;
    height: 60px;
    background: var(--gradient);
    border-radius: 15px;
    display: flex;
    align-items: center;
    justify-content: center;
    margin: 0 auto 1rem;
    font-size: 1.5rem;
    color: var(--bg-dark);
}

.stat-number {
    font-size: 2.5rem;
    font-weight: 700;
    background: var(--gradient);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin-bottom: 0.5rem;
}

.stat-label {
    color: var(--text-primary);
    font-weight: 600;
    margin-bottom: 0.5rem;
}

.stat-description {
    color: var(--text-muted);
    font-size: 0.9rem;
}

/* Responsive Design */
@media (max-width: 768px) {
    .projects-filter {
        padding: 1.5rem 0;
        position: static; /* Remove sticky on mobile */
    }

    .filter-tabs {
        flex-direction: column;
        align-items: center;
        gap: 0.75rem;
        margin-bottom: 1.5rem;
    }
    
    .filter-tab {
        width: 200px;
        text-align: center;
        padding: 0.75rem 1rem;
        font-size: 0.9rem;
    }
    
    .filter-search {
        max-width: 100%;
        padding: 0 1rem;
    }

    .search-input {
        font-size: 1rem; /* Prevent zoom on iOS */
        padding: 0.9rem 1rem 0.9rem 3rem;
    }
    
    .featured-projects-section,
    .all-projects-section,
    .project-stats-section {
        padding: 2.5rem 0;
    }

    .section-title {
        font-size: 2.2rem;
        margin-bottom: 0.8rem;
    }

    .section-subtitle {
        font-size: 1rem;
        margin-bottom: 2rem;
        padding: 0 1rem;
    }

    .project-card {
        padding: 1.5rem;
        margin-bottom: 1.5rem;
    }

    .project-badge {
        top: 0.8rem;
        right: 0.8rem;
        padding: 0.2rem 0.6rem;
        font-size: 0.7rem;
    }

    .project-icon {
        width: 50px;
        height: 50px;
        font-size: 1.3rem;
        margin-bottom: 1.2rem;
    }

    .project-title {
        font-size: 1.3rem;
        margin-bottom: 0.8rem;
    }

    .project-description {
        font-size: 0.95rem;
        margin-bottom: 1.2rem;
        min-height: auto;
    }

    .project-stats {
        justify-content: center;
        margin-bottom: 1.2rem;
        flex-wrap: wrap;
    }

    .stat {
        font-size: 0.8rem;
    }

    .project-tags {
        justify-content: center;
        margin-bottom: 1.2rem;
    }

    .tag {
        font-size: 0.75rem;
        padding: 0.25rem 0.6rem;
    }

    .project-links {
        flex-direction: column;
        gap: 0.75rem;
    }

    .project-links .btn {
        width: 100%;
        justify-content: center;
        padding: 0.8rem 1rem;
    }

    .project-stats-section .stat-card {
        padding: 1.5rem 1rem;
    }

    .stat-icon {
        width: 50px;
        height: 50px;
        font-size: 1.3rem;
    }

    .stat-number {
        font-size: 2rem;
    }

    .stat-label {
        font-size: 0.9rem;
    }

    .stat-description {
        font-size: 0.8rem;
    }
}

/* Small mobile phones - Projects specific */
@media (max-width: 480px) {
    .projects-filter {
        padding: 1rem 0;
    }

    .filter-tab {
        width: 180px;
        padding: 0.6rem 0.8rem;
        font-size: 0.85rem;
    }

    .featured-projects-section,
    .all-projects-section,
    .project-stats-section {
        padding: 2rem 0;
    }

    .section-title {
        font-size: 1.8rem;
    }

    .section-subtitle {
        font-size: 0.9rem;
        margin-bottom: 1.5rem;
    }

    .project-card {
        padding: 1.2rem;
    }

    .project-icon {
        width: 45px;
        height: 45px;
        font-size: 1.2rem;
        margin-bottom: 1rem;
    }

    .project-title {
        font-size: 1.2rem;
    }

    .project-description {
        font-size: 0.9rem;
        margin-bottom: 1rem;
    }

    .project-stats {
        margin-bottom: 1rem;
    }

    .project-tags {
        margin-bottom: 1rem;
        gap: 0.4rem;
    }

    .tag {
        font-size: 0.7rem;
        padding: 0.2rem 0.5rem;
    }
}

/* Animation for filtering */
.project-card {
    transition: all 0.5s ease;
}

.project-card.filtering-out {
    opacity: 0;
    transform: scale(0.8);
}

.project-card.filtering-in {
    opacity: 1;
    transform: scale(1);
}
</style>

<script>
document.addEventListener('DOMContentLoaded', function() {
    const filterTabs = document.querySelectorAll('.filter-tab');
    const projectCards = document.querySelectorAll('.project-card');
    const searchInput = document.getElementById('projectSearch');

    // Filter functionality
    filterTabs.forEach(tab => {
        tab.addEventListener('click', function() {
            // Update active tab
            filterTabs.forEach(t => t.classList.remove('active'));
            this.classList.add('active');
            
            const filter = this.getAttribute('data-filter');
            filterProjects(filter, searchInput.value);
        });
    });

    // Search functionality
    searchInput.addEventListener('input', function() {
        const activeFilter = document.querySelector('.filter-tab.active').getAttribute('data-filter');
        filterProjects(activeFilter, this.value);
    });

    function filterProjects(category, searchTerm) {
        projectCards.forEach(card => {
            const cardCategory = card.getAttribute('data-category');
            const cardKeywords = card.getAttribute('data-keywords') || '';
            const cardTitle = card.querySelector('.project-title').textContent.toLowerCase();
            const cardDescription = card.querySelector('.project-description').textContent.toLowerCase();
            
            const matchesCategory = category === 'all' || cardCategory.includes(category);
            const matchesSearch = searchTerm === '' || 
                cardTitle.includes(searchTerm.toLowerCase()) ||
                cardDescription.includes(searchTerm.toLowerCase()) ||
                cardKeywords.includes(searchTerm.toLowerCase());
            
            if (matchesCategory && matchesSearch) {
                card.classList.remove('hidden');
                card.classList.add('filtering-in');
                card.classList.remove('filtering-out');
            } else {
                card.classList.add('hidden');
                card.classList.add('filtering-out');
                card.classList.remove('filtering-in');
            }
        });
    }

    // Intersection Observer for animations
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    }, observerOptions);

    // Observe project cards for animation
    projectCards.forEach((card, index) => {
        card.style.opacity = '0';
        card.style.transform = 'translateY(50px)';
        card.style.transition = `all 0.6s ease ${index * 0.1}s`;
        observer.observe(card);
    });
});
</script>