---
title: Projects
layout: default
nav_order: 2
has_children: true
has_toc: true
parent: Projects
projects: 
  exclude: true
---

# Projects

This section contains a collection of software development projects focused on backend systems, security tools, bird-related applications, and educational technology. Each project demonstrates different aspects of software development, from security analysis to data processing.


{% comment %}
  The following snippet dynamically lists all pages that have "parent: Projects"
{% endcomment %}
{% assign projects = site.pages | where: "parent", "Projects" %}
{% if projects %}
## List of Projects
<ul>
  {% for project in projects %}
  <li><a href="{{ project.url | prepend: site.baseurl }}">{{ project.title }}</a></li>
  {% endfor %}
</ul>
{% else %}
<p>No projects found.</p>
{% endif %}

## Projects Table of Contents

- [AttackVectorAnalysisTool]({{ site.baseurl }}/Projects/AttackVectorAnalysisTool.md)
- [SecurityLens]({{ site.baseurl }}/Projects/SecurityLens.md)
- [birdstatsgpt]({{ site.baseurl }}/Projects/birdstatsgpt.md)
- [deepseek-mcp-server]({{ site.baseurl }}/Projects/deepseek-mcp-server.md)
- [intel-npu-top]({{ site.baseurl }}/Projects/intel-npu-top.md)
- [mcp-server-birdstats]({{ site.baseurl }}/Projects/mcp-server-birdstats.md)
- [mcp-server-canvas]({{ site.baseurl }}/Projects/mcp-server-canvas.md)
