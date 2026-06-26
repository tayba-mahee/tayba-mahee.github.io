---
layout: page
icon: fas fa-laptop-code
order: 5
---

<link rel="stylesheet" href="/assets/css/project-tiles.css">

<div class="page-title-projects">Featured Projects</div>
<div class="page-subtitle-projects">Explore my work in UX research, web development, machine learning, and educational technology.</div>

<div class="project-grid">
  {% for project in site.data.projects %}
    {% include project-card.html 
      title=project.title
      subtitle=project.subtitle
      description=project.description
      image=project.image
      tags=project.tags
      link=project.link
      button_text=project.button_text
    %}
  {% endfor %}
</div>

