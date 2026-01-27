---
layout: home
title: Home
description: AI/RAG Engineer specializing in retrieval systems, ML pipelines, and production AI infrastructure
hero: true
breadcrumb: false
---

<!-- Hero Section -->
<div class="hero-section">
    <div class="hero-background"></div>
    <div class="hero-particles"></div>
    <div class="hero-content">
        <h1 class="hero-title">David Montgomery</h1>
        <h2 class="hero-subtitle">AI/RAG Engineer & <span class="typing-text" id="typing-text">ML Infrastructure</span></h2>
        <p class="hero-description">
            Building production-grade RAG systems, ML pipelines, and AI infrastructure.
            Specializing in retrieval systems, cross-encoder training, and multimodal AI.
        </p>
        <div class="cta-buttons">
            <a href="#projects" class="btn btn-primary">
                <i class="fas fa-code"></i> View Projects
            </a>
            <a href="{{ site.baseurl }}/assets/davidMontgomery.pdf" class="btn btn-secondary" target="_blank">
                <i class="fas fa-download"></i> Download Resume
            </a>
            <button class="btn btn-secondary" onclick="startTour()">
                <i class="fas fa-route"></i> Take a Tour
            </button>
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
        <p class="section-subtitle">Enterprise-grade RAG systems and production AI infrastructure</p>
        
        <div class="projects-grid grid-3">
            <div class="project-card card featured">
                <div class="project-icon">
                    <i class="fas fa-brain"></i>
                </div>
                <h3 class="project-title">agro-rag-engine</h3>
                <p class="project-description">
                    Enterprise-grade local-first RAG workspace for codebases — 240K+ LOC production platform with self-learning
                    transformer, hybrid search (BM25 + Qdrant vectors), trainable cross-encoder reranker with hot-reload,
                    28 API router modules, MCP servers (4 transport types), and full observability stack.
                </p>
                <div class="project-tags">
                    <span class="tag">Python</span>
                    <span class="tag">TypeScript</span>
                    <span class="tag">RAG</span>
                    <span class="tag">ML Pipeline</span>
                    <span class="tag">FastAPI</span>
                    <span class="tag">React</span>
                    <span class="tag">Qdrant</span>
                </div>
                <div class="project-links">
                    <a href="https://github.com/DMontgomery40/agro-rag-engine" class="btn btn-primary btn-sm" target="_blank">
                        <i class="fab fa-github"></i> GitHub
                    </a>
                    <a href="{{ site.baseurl }}/projects/agro-rag-engine/" class="btn btn-secondary btn-sm">
                        <i class="fas fa-info-circle"></i> Learn More
                    </a>
                </div>
            </div>

            <div class="project-card card">
                <div class="project-icon">
                    <i class="fas fa-eye"></i>
                </div>
                <h3 class="project-title">SecondBrain + MemVid</h3>
                <p class="project-description">
                    Local-first visual memory system with RAG-enabled video search. Continuous screen capture →
                    OCR → ChromaDB vectors → MemVid compression. DeepSeek-OCR for enhanced document extraction.
                </p>
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
                        <i class="fas fa-info-circle"></i> Learn More
                    </a>
                </div>
            </div>

            <div class="project-card card">
                <div class="project-icon">
                    <i class="fas fa-users"></i>
                </div>
                <h3 class="project-title">qEEG Council</h3>
                <p class="project-description">
                    6-stage multi-LLM deliberation workflow for medical report analysis. GPT-4o, Claude 3.5, and
                    Gemini analyze in parallel, then build consensus through structured comparison.
                </p>
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
                        <i class="fas fa-info-circle"></i> Learn More
                    </a>
                </div>
            </div>

            <div class="project-card card">
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
                    <span class="tag">Multimodal</span>
                </div>
                <div class="project-links">
                    <a href="https://github.com/DMontgomery40/local-explainer-video" class="btn btn-primary btn-sm" target="_blank">
                        <i class="fab fa-github"></i> GitHub
                    </a>
                    <a href="{{ site.baseurl }}/projects/local-explainer-video/" class="btn btn-secondary btn-sm">
                        <i class="fas fa-info-circle"></i> Learn More
                    </a>
                </div>
            </div>
        </div>

        <div class="text-center" style="margin-top: 3rem;">
            <a href="{{ site.baseurl }}/projects/" class="btn btn-primary">
                <i class="fas fa-grid-3x3"></i> View All Projects
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
            <a href="{{ site.baseurl }}/homelab/" class="quick-link-card card">
                <div class="quick-link-icon">
                    <i class="fas fa-home"></i>
                </div>
                <h3>HomeLab</h3>
                <p>Enterprise-grade infrastructure for development and AI research</p>
                <span class="quick-link-arrow"><i class="fas fa-arrow-right"></i></span>
            </a>
            
            <a href="{{ site.baseurl }}/storytime/" class="quick-link-card card">
                <div class="quick-link-icon">
                    <i class="fas fa-book-open"></i>
                </div>
                <h3>Story Time</h3>
                <p>My journey from phone phreaking to modern AI development</p>
                <span class="quick-link-arrow"><i class="fas fa-arrow-right"></i></span>
            </a>
            
            <a href="{{ site.baseurl }}/resume/" class="quick-link-card card">
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

<style>
/* Home-specific styles */
.hero-section {
    min-height: 100vh;
    display: flex;
    align-items: center;
    position: relative;
    overflow: hidden;
    background: radial-gradient(circle at 20% 80%, rgba(0, 245, 255, 0.1) 0%, transparent 50%),
                radial-gradient(circle at 80% 20%, rgba(78, 205, 196, 0.1) 0%, transparent 50%);
}

.hero-background {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: radial-gradient(circle at 20% 80%, rgba(0, 245, 255, 0.1) 0%, transparent 50%),
                radial-gradient(circle at 80% 20%, rgba(78, 205, 196, 0.1) 0%, transparent 50%);
}

.hero-particles {
    position: absolute;
    width: 100%;
    height: 100%;
    background-image: 
        radial-gradient(2px 2px at 20px 30px, var(--primary), transparent),
        radial-gradient(2px 2px at 40px 70px, var(--accent), transparent),
        radial-gradient(1px 1px at 90px 40px, var(--secondary), transparent);
    background-repeat: repeat;
    background-size: 150px 150px;
    animation: float 10s infinite linear;
    opacity: 0.3;
}

@keyframes float {
    0% { transform: translateY(0px) rotate(0deg); }
    100% { transform: translateY(-20px) rotate(360deg); }
}

.hero-content {
    position: relative;
    z-index: 2;
    text-align: center;
}

.hero-title {
    font-size: clamp(2.5rem, 8vw, 5rem);
    font-weight: 700;
    margin-bottom: 1rem;
    background: var(--gradient);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    animation: slideInUp 1s ease-out;
}

.hero-subtitle {
    font-size: clamp(1.2rem, 4vw, 2rem);
    color: var(--text-secondary);
    margin-bottom: 2rem;
    animation: slideInUp 1s ease-out 0.2s both;
}

.hero-description {
    font-size: 1.2rem;
    color: var(--text-muted);
    max-width: 600px;
    margin: 0 auto 3rem;
    animation: slideInUp 1s ease-out 0.4s both;
}

.cta-buttons {
    display: flex;
    gap: 1rem;
    justify-content: center;
    flex-wrap: wrap;
    animation: slideInUp 1s ease-out 0.6s both;
}

.typing-text {
    border-right: 2px solid var(--primary);
    animation: blink 1s infinite;
}

@keyframes blink {
    0%, 50% { border-color: var(--primary); }
    51%, 100% { border-color: transparent; }
}

.stats-section {
    padding: 4rem 0;
    background: var(--bg-card);
}

.stats-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 2rem;
}

.stat-card {
    text-align: center;
    padding: 2rem;
    background: var(--bg-hover);
    border-radius: 15px;
    border: 1px solid var(--border);
    transition: all 0.3s ease;
}

.stat-card:hover {
    transform: translateY(-5px);
    box-shadow: var(--shadow);
    border-color: var(--primary);
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

.section-title {
    text-align: center;
    font-size: 3rem;
    font-weight: 700;
    margin-bottom: 1rem;
    background: var(--gradient);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

.section-subtitle {
    text-align: center;
    color: var(--text-secondary);
    font-size: 1.2rem;
    margin-bottom: 4rem;
    max-width: 600px;
    margin-left: auto;
    margin-right: auto;
}

.featured-projects,
.latest-articles,
.skills-overview,
.quick-links {
    padding: 6rem 0;
}

.latest-articles {
    background: var(--bg-card);
}

.project-icon,
.article-icon,
.skill-icon,
.quick-link-icon {
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

.project-title,
.article-title {
    font-size: 1.5rem;
    font-weight: 600;
    margin-bottom: 1rem;
    color: var(--text-primary);
}

.project-description,
.article-excerpt {
    color: var(--text-secondary);
    margin-bottom: 1.5rem;
    line-height: 1.6;
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

.article-meta {
    display: flex;
    gap: 1rem;
    margin-bottom: 1rem;
    font-size: 0.9rem;
    color: var(--text-muted);
}

.skill-category ul {
    list-style: none;
    padding: 0;
}

.skill-category li {
    color: var(--text-secondary);
    margin-bottom: 0.5rem;
    position: relative;
    padding-left: 1.5rem;
}

.skill-category li::before {
    content: '▸';
    position: absolute;
    left: 0;
    color: var(--primary);
}

.quick-link-card {
    text-decoration: none;
    color: inherit;
    position: relative;
    transition: all 0.3s ease;
}

.quick-link-card:hover {
    color: inherit;
    text-decoration: none;
}

.quick-link-arrow {
    position: absolute;
    top: 1rem;
    right: 1rem;
    color: var(--primary);
    transition: transform 0.3s ease;
}

.quick-link-card:hover .quick-link-arrow {
    transform: translateX(5px);
}

.text-center {
    text-align: center;
}

@media (max-width: 768px) {
    .hero-title {
        font-size: 2.5rem;
    }
    
    .cta-buttons {
        flex-direction: column;
        align-items: center;
    }
    
    .stats-grid {
        grid-template-columns: repeat(2, 1fr);
    }
    
    .section-title {
        font-size: 2rem;
    }
}
</style>

<script>
// Typing effect
const typingText = document.getElementById('typing-text');
const texts = ['ML Infrastructure', 'RAG Systems', 'Cross-Encoder Training', 'Multimodal AI'];
let textIndex = 0;
let charIndex = 0;
let isDeleting = false;

function typeText() {
    const currentText = texts[textIndex];
    
    if (isDeleting) {
        typingText.textContent = currentText.substring(0, charIndex - 1);
        charIndex--;
    } else {
        typingText.textContent = currentText.substring(0, charIndex + 1);
        charIndex++;
    }

    let typeSpeed = isDeleting ? 50 : 100;

    if (!isDeleting && charIndex === currentText.length) {
        typeSpeed = 2000;
        isDeleting = true;
    } else if (isDeleting && charIndex === 0) {
        isDeleting = false;
        textIndex = (textIndex + 1) % texts.length;
        typeSpeed = 500;
    }

    setTimeout(typeText, typeSpeed);
}

// Counter animation
function animateCounters() {
    const counters = document.querySelectorAll('.stat-number');
    
    counters.forEach(counter => {
        const target = parseInt(counter.getAttribute('data-count'));
        const duration = 2000;
        const increment = target / (duration / 16);
        let current = 0;
        
        const updateCounter = () => {
            if (current < target) {
                current += increment;
                counter.textContent = Math.floor(current);
                requestAnimationFrame(updateCounter);
            } else {
                counter.textContent = target;
            }
        };
        
        updateCounter();
    });
}

// Interactive tour
function startTour() {
    alert('Interactive tour coming soon! For now, feel free to explore the projects and articles sections.');
}

// Initialize animations
document.addEventListener('DOMContentLoaded', function() {
    typeText();
    
    // Intersection observer for stats animation
    const statsObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                animateCounters();
                statsObserver.unobserve(entry.target);
            }
        });
    });
    
    const statsSection = document.querySelector('.stats-section');
    if (statsSection) {
        statsObserver.observe(statsSection);
    }
});
</script>