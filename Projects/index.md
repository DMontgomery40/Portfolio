---
layout: default
title: Projects Portfolio
description: AI/ML Infrastructure, RAG Systems, and Production-Grade Tools
---

<!-- Projects Filter Section -->
<div class="projects-filter">
    <div class="container">
        <div class="filter-tabs">
            <button class="filter-tab active" data-filter="all">All Projects</button>
            <button class="filter-tab" data-filter="rag">RAG/Search</button>
            <button class="filter-tab" data-filter="ai-ml">AI/ML</button>
            <button class="filter-tab" data-filter="infrastructure">Infrastructure</button>
            <button class="filter-tab" data-filter="security">Security</button>
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
        <p class="section-subtitle">Enterprise-grade AI infrastructure and RAG systems</p>
        <div class="projects-grid grid-3">

            <!-- agro-rag-engine -->
            <div class="project-card card" data-category="rag ai-ml" data-keywords="rag search vector embeddings reranker cross-encoder langgraph mcp fastapi qdrant">
                <div class="project-badge featured">Featured</div>
                <div class="project-icon">
                    <i class="fas fa-brain"></i>
                </div>
                <h3 class="project-title">agro-rag-engine</h3>
                <p class="project-description">
                    Enterprise-grade RAG workspace for codebases — 240K+ LOC production platform with self-learning
                    cross-encoder, hybrid search (BM25 + Qdrant), 28 API router modules, and MCP servers.
                </p>
                <div class="project-stats">
                    <span class="stat"><i class="fas fa-code"></i> 240K+ LOC</span>
                    <span class="stat"><i class="fas fa-graduation-cap"></i> Self-Learning</span>
                </div>
                <div class="project-tags">
                    <span class="tag">Python</span>
                    <span class="tag">TypeScript</span>
                    <span class="tag">RAG</span>
                    <span class="tag">ML Pipeline</span>
                    <span class="tag">FastAPI</span>
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

            <!-- SecondBrain + MemVid -->
            <div class="project-card card" data-category="rag ai-ml" data-keywords="memvid ocr vision rag search secondbrain deepseek chromadb embeddings">
                <div class="project-badge new">Cutting Edge</div>
                <div class="project-icon">
                    <i class="fas fa-eye"></i>
                </div>
                <h3 class="project-title">SecondBrain + MemVid</h3>
                <p class="project-description">
                    Local-first visual memory system with RAG-enabled video search. Continuous screen capture →
                    OCR → ChromaDB vectors → MemVid compression. DeepSeek-OCR for enhanced document extraction.
                </p>
                <div class="project-stats">
                    <span class="stat"><i class="fas fa-compress"></i> 99% Compression</span>
                    <span class="stat"><i class="fas fa-search"></i> Hybrid Search</span>
                </div>
                <div class="project-tags">
                    <span class="tag">Python</span>
                    <span class="tag">RAG</span>
                    <span class="tag">MemVid</span>
                    <span class="tag">Vision AI</span>
                    <span class="tag">ChromaDB</span>
                </div>
                <div class="project-links">
                    <a href="https://github.com/DMontgomery40/secondbrain" class="btn btn-primary btn-sm" target="_blank">
                        <i class="fab fa-github"></i> GitHub
                    </a>
                    <a href="{{ site.baseurl }}/projects/secondbrain-memvid/" class="btn btn-secondary btn-sm">
                        <i class="fas fa-info-circle"></i> Details
                    </a>
                </div>
            </div>

            <!-- qEEG Council -->
            <div class="project-card card" data-category="ai-ml" data-keywords="llm orchestration multi-model consensus medical vision pdf analysis">
                <div class="project-badge featured">Featured</div>
                <div class="project-icon">
                    <i class="fas fa-users"></i>
                </div>
                <h3 class="project-title">qEEG Council</h3>
                <p class="project-description">
                    6-stage multi-LLM deliberation workflow for medical report analysis. GPT-4o, Claude 3.5, and
                    Gemini analyze in parallel, then build consensus through structured comparison.
                </p>
                <div class="project-stats">
                    <span class="stat"><i class="fas fa-layer-group"></i> 6-Stage Pipeline</span>
                    <span class="stat"><i class="fas fa-brain"></i> Multi-LLM</span>
                </div>
                <div class="project-tags">
                    <span class="tag">Python</span>
                    <span class="tag">FastAPI</span>
                    <span class="tag">React</span>
                    <span class="tag">Vision AI</span>
                    <span class="tag">Medical</span>
                </div>
                <div class="project-links">
                    <a href="https://github.com/DMontgomery40/qEEG-analysis" class="btn btn-primary btn-sm" target="_blank">
                        <i class="fab fa-github"></i> GitHub
                    </a>
                    <a href="{{ site.baseurl }}/projects/qeeg-council/" class="btn btn-secondary btn-sm">
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

            <!-- local-explainer-video -->
            <div class="project-card card" data-category="ai-ml" data-keywords="video tts text-to-speech image generation multimodal document">
                <div class="project-icon">
                    <i class="fas fa-video"></i>
                </div>
                <h3 class="project-title">local-explainer-video</h3>
                <p class="project-description">
                    AI-powered document-to-video pipeline. LLM directs storyboarding, generates images,
                    synthesizes speech, and assembles narrated MP4 explanations.
                </p>
                <div class="project-tags">
                    <span class="tag">Python</span>
                    <span class="tag">Streamlit</span>
                    <span class="tag">TTS</span>
                    <span class="tag">Image Gen</span>
                </div>
                <div class="project-links">
                    <a href="https://github.com/DMontgomery40/local-explainer-video" class="btn btn-primary btn-sm" target="_blank">
                        <i class="fab fa-github"></i> GitHub
                    </a>
                    <a href="{{ site.baseurl }}/projects/local-explainer-video/" class="btn btn-secondary btn-sm">
                        <i class="fas fa-info-circle"></i> Details
                    </a>
                </div>
            </div>

            <!-- thrylen (VIVIFIED) -->
            <div class="project-card card" data-category="security infrastructure" data-keywords="encryption security aes messaging privacy domestic violence safety">
                <div class="project-icon">
                    <i class="fas fa-shield-alt"></i>
                </div>
                <h3 class="project-title">thrylen (VIVIFIED)</h3>
                <p class="project-description">
                    Encrypted messaging system with e-commerce cover. AES-256-GCM encryption, zero-footprint
                    design, multi-theme storefronts. Built for survivor safety.
                </p>
                <div class="project-tags">
                    <span class="tag">JavaScript</span>
                    <span class="tag">Netlify</span>
                    <span class="tag">AES-256</span>
                    <span class="tag">Security</span>
                </div>
                <div class="project-links">
                    <a href="https://github.com/DMontgomery40/thrylen" class="btn btn-primary btn-sm" target="_blank">
                        <i class="fab fa-github"></i> GitHub
                    </a>
                </div>
            </div>

            <!-- DeepSeek MCP Server -->
            <div class="project-card card" data-category="ai-ml infrastructure" data-keywords="mcp deepseek llm api server r1 reasoning">
                <div class="project-icon">
                    <i class="fas fa-server"></i>
                </div>
                <h3 class="project-title">DeepSeek MCP Server</h3>
                <p class="project-description">
                    Model Context Protocol server for DeepSeek models including R1 reasoning.
                    Multi-turn conversation support with automatic fallbacks.
                </p>
                <div class="project-tags">
                    <span class="tag">TypeScript</span>
                    <span class="tag">MCP</span>
                    <span class="tag">DeepSeek</span>
                    <span class="tag">npm</span>
                </div>
                <div class="project-links">
                    <a href="https://github.com/DMontgomery40/mcp_deepseek" class="btn btn-primary btn-sm" target="_blank">
                        <i class="fab fa-github"></i> GitHub
                    </a>
                    <a href="{{ site.baseurl }}/projects/deepseek-mcp-server/" class="btn btn-secondary btn-sm">
                        <i class="fas fa-info-circle"></i> Details
                    </a>
                </div>
            </div>

            <!-- SecurityLens -->
            <div class="project-card card" data-category="security" data-keywords="vulnerability scanning analysis pentesting web security">
                <div class="project-icon">
                    <i class="fas fa-search"></i>
                </div>
                <h3 class="project-title">SecurityLens</h3>
                <p class="project-description">
                    Open-source security analysis platform with 32+ vulnerability detection types.
                    Web-based scanning interface for penetration testing.
                </p>
                <div class="project-tags">
                    <span class="tag">Python</span>
                    <span class="tag">Flask</span>
                    <span class="tag">Vue.js</span>
                    <span class="tag">Security</span>
                </div>
                <div class="project-links">
                    <a href="https://securitylens.io" class="btn btn-primary btn-sm" target="_blank">
                        <i class="fas fa-external-link-alt"></i> Live Demo
                    </a>
                    <a href="{{ site.baseurl }}/projects/SecurityLens/" class="btn btn-secondary btn-sm">
                        <i class="fas fa-info-circle"></i> Details
                    </a>
                </div>
            </div>

            <!-- Pentest MCP -->
            <div class="project-card card" data-category="security infrastructure" data-keywords="pentesting nmap hashcat gpu security mcp">
                <div class="project-icon">
                    <i class="fas fa-bug"></i>
                </div>
                <h3 class="project-title">Pentest MCP</h3>
                <p class="project-description">
                    Professional penetration testing toolkit via MCP. Integrates Nmap, Gobuster,
                    Nikto, Hashcat with GPU acceleration through natural language.
                </p>
                <div class="project-tags">
                    <span class="tag">Node.js</span>
                    <span class="tag">MCP</span>
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

            <!-- Intel NPU Monitor -->
            <div class="project-card card" data-category="infrastructure" data-keywords="intel npu monitoring hardware ai accelerator">
                <div class="project-icon">
                    <i class="fas fa-microchip"></i>
                </div>
                <h3 class="project-title">Intel NPU Monitor</h3>
                <p class="project-description">
                    Lightweight monitoring tool for Intel Neural Processing Units.
                    52 lines of pure Python with zero dependencies.
                </p>
                <div class="project-tags">
                    <span class="tag">Python</span>
                    <span class="tag">Hardware</span>
                    <span class="tag">NPU</span>
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
            <div class="project-card card" data-category="infrastructure" data-keywords="3d printer mcp iot automation octoprint klipper">
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
                    <span class="tag">MCP</span>
                    <span class="tag">IoT</span>
                </div>
                <div class="project-links">
                    <a href="https://github.com/DMontgomery40/mcp-3D-printer-server" class="btn btn-primary btn-sm" target="_blank">
                        <i class="fab fa-github"></i> GitHub
                    </a>
                    <a href="{{ site.baseurl }}/projects/mcp-3D-printer-server/" class="btn btn-secondary btn-sm">
                        <i class="fas fa-info-circle"></i> Details
                    </a>
                </div>
            </div>
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
                <div class="stat-number">250K+</div>
                <div class="stat-label">Lines of Code</div>
                <div class="stat-description">agro-rag-engine alone is 240K+</div>
            </div>
            <div class="stat-card card">
                <div class="stat-icon">
                    <i class="fas fa-brain"></i>
                </div>
                <div class="stat-number">4</div>
                <div class="stat-label">RAG Systems</div>
                <div class="stat-description">Production-grade retrieval pipelines</div>
            </div>
            <div class="stat-card card">
                <div class="stat-icon">
                    <i class="fas fa-plug"></i>
                </div>
                <div class="stat-number">5</div>
                <div class="stat-label">MCP Servers</div>
                <div class="stat-description">Model Context Protocol integrations</div>
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

.section-subtitle {
    text-align: center;
    color: var(--text-secondary);
    font-size: 1.1rem;
    margin-bottom: 3rem;
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
    min-height: 4rem;
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
        position: static;
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

    .featured-projects-section,
    .all-projects-section,
    .project-stats-section {
        padding: 2.5rem 0;
    }

    .project-card {
        padding: 1.5rem;
        margin-bottom: 1.5rem;
    }

    .project-description {
        min-height: auto;
    }

    .project-links {
        flex-direction: column;
        gap: 0.75rem;
    }

    .project-links .btn {
        width: 100%;
        justify-content: center;
    }
}
</style>

<script>
document.addEventListener('DOMContentLoaded', function() {
    const filterTabs = document.querySelectorAll('.filter-tab');
    const projectCards = document.querySelectorAll('.project-card');
    const searchInput = document.getElementById('projectSearch');

    filterTabs.forEach(tab => {
        tab.addEventListener('click', function() {
            filterTabs.forEach(t => t.classList.remove('active'));
            this.classList.add('active');

            const filter = this.getAttribute('data-filter');
            filterProjects(filter, searchInput.value);
        });
    });

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
            } else {
                card.classList.add('hidden');
            }
        });
    }

    // Intersection Observer for animations
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    }, { threshold: 0.1 });

    projectCards.forEach((card, index) => {
        card.style.opacity = '0';
        card.style.transform = 'translateY(50px)';
        card.style.transition = `all 0.6s ease ${index * 0.1}s`;
        observer.observe(card);
    });
});
</script>
