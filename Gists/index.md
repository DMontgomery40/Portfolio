---
layout: default
title: Gists
---

# Gists

Public gists -- reusable skills, utilities, and writeups for agentic coding workflows. These are platform-agnostic: they work with any agentic coding tool that supports skill/agent directories (Claude Code, Codex, Cursor, etc.).

## Skill Bundles

Multi-file skill packages with agent configs, verification references, and supporting scripts.

<div class="project-grid" markdown="0">

  <a href="https://gist.github.com/DMontgomery40/59f94f0f06da40b7acbd52faa029e6b9" class="project-card" target="_blank" rel="noopener">
    <div class="project-card__body">
      <h3 class="project-card__title">Frontend Review Loop Skill Bundle</h3>
      <p class="project-card__description">Multi-file skill bundle for automated frontend code review. Runs a structured review loop focused on rendering bugs, state issues, async flows, accessibility, and visual behavior. Includes browser-proof verification references and test expansion patterns.</p>
      <div class="project-card__tags">
        <span class="tag">SKILL.md</span>
        <span class="tag">Agents Config</span>
        <span class="tag">Review Probe Script</span>
        <span class="tag">Sync Script</span>
      </div>
    </div>
  </a>

  <a href="https://gist.github.com/DMontgomery40/c8ac6352741a5668aadb58b6a39634f2" class="project-card" target="_blank" rel="noopener">
    <div class="project-card__body">
      <h3 class="project-card__title">Thorough Code Review Loop Skill Bundle</h3>
      <p class="project-card__description">Deep, bug-focused code review skill that goes beyond surface-level linting. Targets correctness, regressions, missing tests, fake/gamed tests, security, portability, cleanup, and operational risk. Same multi-file structure for maximum coverage.</p>
      <div class="project-card__tags">
        <span class="tag">SKILL.md</span>
        <span class="tag">Agents Config</span>
        <span class="tag">Review Probe Script</span>
        <span class="tag">Sync Script</span>
      </div>
    </div>
  </a>

  <a href="https://gist.github.com/DMontgomery40/e47f410b8b6a2536b3313eb4212f1d0b" class="project-card" target="_blank" rel="noopener">
    <div class="project-card__body">
      <h3 class="project-card__title">PR Loop Skill Bundle</h3>
      <p class="project-card__description">Automated PR review cycle skill. Watches for open PRs, runs structured review, and provides actionable feedback. Lightweight bundle with agent config and prompt shim.</p>
      <div class="project-card__tags">
        <span class="tag">SKILL.md</span>
        <span class="tag">Agents Config</span>
        <span class="tag">Prompt Shim</span>
      </div>
    </div>
  </a>

</div>

## Standalone Skills

Single-file portable versions -- drop into any agentic tool's skill or agent directory.

<div class="project-grid" markdown="0">

  <a href="https://gist.github.com/DMontgomery40/0ee2f40f5931de06320f239e74b86c18" class="project-card" target="_blank" rel="noopener">
    <div class="project-card__body">
      <h3 class="project-card__title">Frontend Review Loop</h3>
      <p class="project-card__description">Single-file portable frontend review skill. Drop-in ready for any agentic coding tool.</p>
      <div class="project-card__tags">
        <span class="tag">frontend-review-loop.md</span>
      </div>
    </div>
  </a>

  <a href="https://gist.github.com/DMontgomery40/35c16613aef2a210e828b4738479f8b4" class="project-card" target="_blank" rel="noopener">
    <div class="project-card__body">
      <h3 class="project-card__title">Thorough Code Review Loop</h3>
      <p class="project-card__description">Single-file portable version of the thorough review skill. Drop into any agentic tool's skill/agent directory and it works.</p>
      <div class="project-card__tags">
        <span class="tag">thorough-code-review-loop.md</span>
      </div>
    </div>
  </a>

  <a href="https://gist.github.com/DMontgomery40/01eb7e435569e5768b6a1a10a913b855" class="project-card" target="_blank" rel="noopener">
    <div class="project-card__body">
      <h3 class="project-card__title">PR Loop Skill</h3>
      <p class="project-card__description">Single-file portable PR review skill. Same capabilities as the bundle, packaged as one file for easy adoption.</p>
      <div class="project-card__tags">
        <span class="tag">pr-loop.md</span>
      </div>
    </div>
  </a>

</div>

## Tools and Utilities

Standalone scripts and workflows for agentic coding infrastructure.

<div class="project-grid" markdown="0">

  <a href="https://gist.github.com/DMontgomery40/a26fe25cd217e184c4d2c39cbe93e57c" class="project-card" target="_blank" rel="noopener">
    <div class="project-card__body">
      <h3 class="project-card__title">Local-First Agentic RAG Index</h3>
      <p class="project-card__description">Hybrid RAG index for agentic coding tool session history. Bootstraps a local vector store from session transcripts for searchable context across conversations. Works with any tool that stores session history locally -- swap one path variable to target Claude Code, Codex, or Cursor history.</p>
      <div class="project-card__tags">
        <span class="tag">bootstrap_and_ingest.sh</span>
        <span class="tag">codex_rag.py</span>
        <span class="tag">requirements.txt</span>
      </div>
    </div>
  </a>

  <a href="https://gist.github.com/DMontgomery40/dc6fad2fe552f2654b518c25bac16a5f" class="project-card" target="_blank" rel="noopener">
    <div class="project-card__body">
      <h3 class="project-card__title">Step 0: Before Fixing Your Vibe Slop</h3>
      <p class="project-card__description">Practical starter guide for configuring agentic coding tools before diving into code generation. Includes a macOS batch setup script and visual operator hint diagrams. The thesis: get your configuration right first, or everything downstream is slop.</p>
      <div class="project-card__tags">
        <span class="tag">codex-batch-macos.sh</span>
        <span class="tag">Operator Hint SVGs</span>
      </div>
    </div>
  </a>

  <a href="https://gist.github.com/DMontgomery40/08c1bdede08ca1cee8800db7da1cda25" class="project-card" target="_blank" rel="noopener">
    <div class="project-card__body">
      <h3 class="project-card__title">Ralph Audit Loop</h3>
      <p class="project-card__description">Read-only code audit runner for CLI-based agentic tools. Runs structured security and quality audits without making changes. Includes PRD for the audit scope, progress tracking, and a shell runner script.</p>
      <div class="project-card__tags">
        <span class="tag">ralph.sh</span>
        <span class="tag">prd.json</span>
        <span class="tag">progress.txt</span>
      </div>
    </div>
  </a>

  <a href="https://gist.github.com/DMontgomery40/ec5300e88b1866401e5d1efa1db5ffc0" class="project-card" target="_blank" rel="noopener">
    <div class="project-card__body">
      <h3 class="project-card__title">DOCX-PDF Round-Trip Normalization</h3>
      <p class="project-card__description">Python utility for normalizing document formats during DOCX/PDF conversion round-trips. Handles formatting loss, font substitution, and layout drift that occurs when converting between formats.</p>
      <div class="project-card__tags">
        <span class="tag">normalize_docx.py</span>
        <span class="tag">PROMPT.md</span>
      </div>
    </div>
  </a>

  <a href="https://gist.github.com/DMontgomery40/deddc0ab562f923e7e0da68413d6990a" class="project-card" target="_blank" rel="noopener">
    <div class="project-card__body">
      <h3 class="project-card__title">Toggle Scrypted Extensions</h3>
      <p class="project-card__description">TypeScript utility for toggling Scrypted NVR extensions on and off. Useful for debugging camera detection issues or temporarily disabling resource-heavy plugins.</p>
      <div class="project-card__tags">
        <span class="tag">extension_toggler.ts</span>
      </div>
    </div>
  </a>

</div>

## Writeups

<div class="project-grid" markdown="0">

  <a href="https://gist.github.com/DMontgomery40/f11535bb6e458d8a25018e996504f10e" class="project-card" target="_blank" rel="noopener">
    <div class="project-card__body">
      <h3 class="project-card__title">Automation Hardening Incident Report</h3>
      <p class="project-card__description">Post-incident writeup from March 2026 documenting lessons learned from hardening automated coding workflows. Covers failure modes, guardrails implemented, and patterns to avoid when running agentic tools at scale.</p>
      <div class="project-card__tags">
        <span class="tag">codex-automation-hardening-2026-03-10.md</span>
      </div>
    </div>
  </a>

</div>
