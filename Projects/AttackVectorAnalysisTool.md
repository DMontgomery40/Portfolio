---
title: Attack Vector Analysis Tool
layout: page
nav_order: 3
parent: Projects
---
**# Attack Vector Analysis Tool**
An interactive security vulnerability assessment interface that maps relationships between common attack vectors, showing prerequisites, potential consequences, and risk levels for each attack type.
**## Overview**
This tool provides an interactive visualization of various attack vectors, helping security professionals and students understand:
- How different attack types relate to each other
- Which vulnerabilities can lead to other exploits
- Risk levels and severity of different attacks
- Common attack patterns and chains
**## Interactive Demo**

<div markdown="0">
  <iframe id="demo-iframe" 
    src="https://claude.site/artifacts/abcf42a2-194c-4593-afbd-9ba562b56d79" 
    width="100%" 
    height="600px" 
    style="border: 1px solid #ccc; border-radius: 4px;" 
    frameborder="0" 
    onload="this.style.display='block'" 
    onerror="handleIframeError()">
  </iframe>

  <style>
    .game {
      width: 100%;
      max-width: 600px;
      height: 150px;
      border: 1px solid var(--border-color);
      margin: 2rem auto;
      background: var(--background-color);
    }

    #dino {
      width: 50px;
      height: 50px;
      background-image: url("https://raw.githubusercontent.com/MysticReborn/t-rexGame/master/images/trex1.png");
      background-size: 50px 50px;
      position: relative;
      top: 98px;
    }

    #cactus {
      width: 20px;
      height: 40px;
      background-image: url("https://raw.githubusercontent.com/MysticReborn/t-rexGame/master/images/obstacle1.png");
      background-size: 20px 40px;
      position: relative;
      top: 58px;
      left: calc(100% - 20px);
      animation: block 1s infinite linear;
    }

    @keyframes block {
      0% {left: calc(100% - 20px);}
      100% {left: -20px;}
    }

    .jump {
      animation: jump 0.3s linear;
    }

    @keyframes jump {
      0% {top: 98px;}
      30% {top: 70px;}
      50% {top: 50px;}
      80% {top: 70px;}
      100% {top: 98px;}
    }
  </style>

  <div id="fallback" style="display:none">
    <div class="game">
      <div id="dino"></div>
      <div id="cactus"></div>
    </div>
  </div>

  <script>
    function handleIframeError() {
      document.getElementById('demo-iframe').style.display = 'none';
      document.getElementById('fallback').style.display = 'block';
    }

    document.addEventListener('DOMContentLoaded', function() {
      const dino = document.getElementById("dino");
      const cactus = document.getElementById("cactus");

      function jump() {
        if (!dino.classList.contains("jump")) {
          dino.classList.add("jump");
          setTimeout(function () {
            dino.classList.remove("jump");
          }, 300);
        }
      }

      let isAlive = setInterval(function () {
        let dinoTop = parseInt(window.getComputedStyle(dino).getPropertyValue("top"));
        let cactusLeft = parseInt(window.getComputedStyle(cactus).getPropertyValue("left"));
        
        if (cactusLeft < 50 && cactusLeft > 0 && dinoTop >= 140) {
          alert("Game Over!");
        }
      }, 10);

      document.addEventListener("keydown", function (event) {
        jump();
      });
    });
  </script>
</div>

[Click Here If Demo Is Blank Below](https://claude.site/artifacts/abcf42a2-194c-4593-afbd-9ba562b56d79){: .btn .btn-primary }
{: .text-center }
## Features

### Risk Assessment
{: .no_toc }

- Visual risk level indicators (Medium to Critical)
- Numerical risk scores (5/10 - 10/10)
- Terminal indicators for command-line based attacks
- Filterable view by risk level

### Attack Vector Mapping
{: .no_toc }

- Target information (e.g., Login Form, Database, User Sessions)
- Common aliases and related techniques
- Risk level and severity score
- Prerequisites ("Caused By")
- Potential consequences ("Can Lead To")

### Interactive Navigation
{: .no_toc }

- Click-through relationship exploration
- Follow attack chains from initial breach to potential escalations
- Filter by risk level or attack type
- Detailed view for each attack vector

### Attack Types Covered
{: .no_toc }

- Authentication attacks (Brute Force, Password Spraying)
- Data extraction (SQL Injection)
- Social attacks (Phishing, Social Engineering)
- Session attacks (Hijacking, Cookie Theft)
- System attacks (Zero-Day Exploits)
- Network attacks (Man-in-the-Middle, DNS Cache Poisoning)
- Client-side attacks (XSS, Keylogging)
- Physical security (Physical Security Breach)
- Cryptographic attacks (Rainbow Table Attack)

## Technical Implementation

Built using React with:

- Interactive relationship mapping
- Risk level visualization
- Dynamic content loading
- Responsive design for various screen sizes

## Educational Purpose

This tool is designed for:

- Security education and training
- Threat modeling and analysis
- Understanding attack relationships
- Security assessment visualization
