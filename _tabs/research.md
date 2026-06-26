---
layout: page
icon: fas fa-microscope
order: 3
---

<link rel="stylesheet" href="/assets/css/project-tiles.css">

<div class="page-title-projects">Research Experience</div>
<div class="page-subtitle-projects">Graduate research at the intersection of machine learning, computer vision, and human-computer interaction.</div>

<div class="project-grid">
  {% for research in site.data.research %}
    {% include project-card.html 
      title=research.title
      subtitle=research.subtitle
      description=research.description
      image=research.image
      tags=research.tags
      link=research.link
      button_text=research.button_text
    %}
  {% endfor %}
</div>

