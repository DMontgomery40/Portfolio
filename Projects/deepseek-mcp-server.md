---
title: Deepseek MCP Server
layout: default
---

<div id="readme-content">
  <script>
    fetch('https://raw.githubusercontent.com/DMontgomery40/deepseek-mcp-server/main/README.md')
      .then(response => response.text())
      .then(data => {
        document.getElementById('readme-content').innerHTML = marked.parse(data);
      });
  </script>
</div>

<script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
