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

---

## Research Responsibilities

Throughout my graduate research experience, I:

- **Designed Independent Studies**: Formulated research questions and experimental designs
- **Presented Research**: Shared findings and discussed papers in weekly research lab meetings
- **Collaborated Across Disciplines**: Worked with researchers from biology, environmental science, and computer science
- **Published Findings**: Co-authored peer-reviewed publications in conferences and journals
- **Mentored Peers**: Assisted fellow graduate students with research methodology and technical challenges

---

## Research Skills & Methodologies

**Machine Learning:**
- Deep learning architectures (CNNs, RNNs, GANs, Autoencoders)
- Ensemble methods and model selection
- Hyperparameter tuning and optimization
- Cross-validation and performance evaluation

**Computer Vision:**
- Image preprocessing and augmentation
- Feature extraction and representation learning
- Object detection and classification
- Super-resolution techniques

**Data Science:**
- Statistical analysis and hypothesis testing
- Data visualization and exploratory analysis
- Dimensionality reduction (PCA, autoencoders)
- Feature engineering and selection

**Tools & Frameworks:**
- Python (NumPy, Pandas, Scikit-learn)
- Deep Learning (TensorFlow, PyTorch, Keras)
- Data Visualization (Matplotlib, Seaborn)
- Version Control (Git, GitHub)

---

## Publications

For a complete list of my research publications, please visit the [Publications](/publications/) page.

## Current Research Interests

My ongoing research interests include:

- **Human-Computer Interaction**: Cultural factors in user experience and information seeking
- **Machine Learning**: Healthcare applications, environmental monitoring, and fair AI
- **Computer Vision**: Medical image analysis and satellite imagery processing
- **User Research**: Behavioral analysis and adaptive system design
- **Quantum Computing**: Quantum-classical hybrid models for practical applications

---

## Collaboration Opportunities

I'm always interested in collaborative research opportunities, particularly at the intersection of:
- Machine learning and healthcare
- Cultural computing and HCI
- AI ethics and fairness
- Educational technology and learning analytics

If you're working in these areas or have research collaboration ideas, please [contact me](/#contact).

