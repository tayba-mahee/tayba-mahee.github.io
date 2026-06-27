---
title: "AR Fishing: Designing an Augmented Reality Decision Support System for Sustainable Fishing"
date: 2026-06-26 19:30:00 -0600
categories: [Projects, UX Research]
tags: [augmented reality, sustainability, product design, ux research, hci, environmental technology]
image:
  path: /assets/img/arfishing/ar-fishing-hero.svg
  alt: AR Fishing Decision Support System
---

## Overview

Overfishing is one of the leading contributors to marine ecosystem decline worldwide. While existing monitoring technologies track fishing vessel activity and catch volumes, few solutions provide **real-time decision support** directly to individual fishermen at the moment of catch.

**AR Fishing** is a speculative Human-Computer Interaction (HCI) concept that explores how augmented reality and computer vision can support sustainable fishing practices. The system combines underwater imaging, machine learning-based species recognition, and contextual environmental information to help recreational and commercial fishermen make more informed decisions while reducing overfishing and accidental bycatch.

Rather than replacing traditional fishing practices, the system augments the fishing experience by embedding intelligent decision support directly into the user's workflow.

## Why This Matters

Healthy marine ecosystems depend on informed fishing practices. While governments and conservation organizations provide regulations and monitoring systems, individual fishermen rarely receive actionable guidance at the moment decisions are made. This project explores how human-centered design can bridge that gap through contextual augmented reality experiences.

## Project Details

**Role:** UX Researcher · Product Designer · Interaction Designer  
**Duration:** Human-Computer Interaction Concept Project  
**Methods:** Literature Review, Market Research, User-Centered Design, Task Flow Design, Interface Design, Usability Evaluation

## Project Timeline

| Research | Define | Ideate | Design | Evaluate |
|:---------|:-------|:--------|:--------|:----------|
| Literature Review | Problem Definition | User Journey | Wireframes | User Studies |
| Market Research | User Needs | Information Architecture | AR Interface | Findings |
| Competitive Analysis | Design Goals | Product Concept | Prototype | Iteration |



## The Challenge

> How might we help fishermen identify fish species and make sustainable fishing decisions without interrupting the natural fishing experience?

Current sustainable fishing solutions include:
- Fishing vessel monitoring systems
- Smart fishing nets with sensors
- Electronic catch monitoring
- Ocean data collection platforms

However, these solutions often require:
- Post-processing and manual review
- Specialized equipment that interrupts workflow
- Delayed feedback rather than real-time guidance
- No direct connection to the individual fisher's decision-making moment

The opportunity was to provide contextual environmental information precisely when fishermen need it most.

## My Role

As part of a three-person Human-Computer Interaction research team, I contributed to UX research, interaction design, interface concepts, user flows, literature review, and usability evaluation.

## Design Process

Throughout the project, I iteratively moved between research, ideation, prototyping, and evaluation to ensure that design decisions remained grounded in user needs and environmental sustainability.

![Design Thinking Process](/assets/img/arfishing/06-design-thinking-process.svg)
_Five-stage Design Thinking methodology guiding the project_

## Discovery & Research


### Research Objectives

The research was guided by four primary objectives:

- Understand the environmental and practical challenges associated with sustainable fishing.
- Investigate how fishermen currently identify fish species and comply with fishing regulations.
- Explore how augmented reality and computer vision have been applied in similar outdoor environments.
- Identify opportunities where real-time contextual information could support better decision-making without disrupting the fishing experience.

These objectives established the foundation for defining user needs and shaping the overall product direction.

### Research Questions

To guide the research process, I developed a set of questions that would help identify user needs, technological opportunities, and design constraints.

##### User Behavior

* How do fishermen currently identify fish species?
* What information do fishermen rely on when deciding whether to keep or release a catch?
* What challenges do recreational and commercial fishermen encounter during fishing?

##### Technology

* How have augmented reality and computer vision been applied in outdoor environments?
* How can contextual information be presented without distracting users from the fishing experience?

##### Sustainability

* What are the primary causes of accidental bycatch and overfishing?
* How can real-time decision support encourage more sustainable fishing practices?

##### Experience Design

* What information is most valuable at the moment a fish is detected?
* How can an interface remain glanceable, readable, and usable in bright outdoor environments?
* How can the system support decision-making while preserving user autonomy?


### Literature Review

I reviewed academic publications, Human-Computer Interaction (HCI) research, and environmental studies to understand both the ecological problem of overfishing and the technological landscape surrounding augmented reality applications.

The review focused on:

- Sustainable fishing practices and conservation efforts
- Illegal, unreported, and unregulated (IUU) fishing
- Fish species identification methods
- Human-Computer Interaction principles for outdoor and augmented reality systems
- Computer vision techniques for object recognition
- Environmental decision-support systems

The literature highlighted a recurring challenge: although governments and conservation organizations provide extensive regulations and monitoring systems, these resources rarely assist fishermen during the actual moment of decision-making.

### Market Research

To better understand the existing ecosystem, I examined technologies currently used within commercial and recreational fishing.

The research included:

- Smart fishing equipment
- Electronic catch monitoring systems
- Vessel tracking platforms
- Ocean environmental monitoring tools
- Mobile fishing companion applications

While these technologies provide valuable environmental data, most operate after fish have been caught or require specialized equipment that interrupts the natural fishing workflow.

This revealed an opportunity to design a lightweight decision-support tool that integrates directly into the fishing experience rather than functioning as a separate monitoring system.

### Competitive Analysis

The analysis revealed that although existing technologies collect environmental data, none integrated underwater visualization, real-time species recognition, and contextual sustainability guidance into a single user-centered experience.

The comparison focused on:

- Fish identification capabilities
- Real-time feedback
- Environmental guidance
- Hands-free interaction
- Ease of use in outdoor environments

### Key Findings

Existing solutions primarily focus on data collection rather than real-time user assistance. Most products require manual interpretation of regulations or post-processing of collected data. Few systems integrate environmental information directly into the user's field of view. None combined underwater visualization, computer vision, and contextual sustainability guidance into a single user-centered experience.


![Research Findings](/assets/img/arfishing/05-research-insights.svg)
_Key insights from literature review and market analysis_

## Defining the Problem

Research synthesis led to the central design question:

> How can augmented reality provide contextual environmental information without disrupting the natural fishing experience?

The solution needed to balance:
- **Environmental responsibility** with practical fishing needs
- **Real-time information** without cognitive overload
- **Hands-free interaction** in challenging outdoor conditions
- **Actionable guidance** while preserving human decision-making


## Product Concept


AR Fishing is a speculative decision-support system that augments the traditional fishing experience through real-time contextual information. Rather than replacing existing fishing practices, the concept combines computer vision, machine learning, and augmented reality to help fishermen make informed decisions while preserving their natural workflow.

The system consists of three primary components:

- **An underwater camera** mounted near the fishing line captures a continuous live video stream beneath the water's surface.
- **A mobile device or rod-mounted display** presents contextual information directly within the fisherman's field of view.
- **A machine learning pipeline** analyzes the video stream in real time, classifies fish species, and returns sustainability guidance to the interface.

Instead of simply identifying fish, the interface provides information that directly supports environmentally responsible decision-making, including:

- Fish species and family
- Estimated size and maturity
- Conservation status
- Fishing season restrictions
- Protected or prohibited species alerts
- Recommended keep-or-release actions
- Current fishing location
- Environmental context

The interface was intentionally designed around **glanceable interactions**, allowing fishermen to receive essential information without interrupting the fishing experience or diverting attention away from their surroundings.

By presenting contextual recommendations **before** a catch is made, the system shifts decision-making from reactive regulation checking to proactive environmental awareness while preserving user autonomy.



## System Architecture  

The concept was designed as an integrated hardware and software ecosystem that delivers contextual information in real time while remaining unobtrusive during fishing activities.

The interaction flow consists of five stages:

- **Capture:** An underwater camera attached near the fishing line continuously captures live video beneath the water's surface.

- **Transmit:**  The video stream is transmitted wirelessly to a mobile device or rod-mounted display.

- **Analyze:**  A machine learning model processes the incoming frames, detects fish, classifies species, and extracts contextual information including estimated size, maturity, fishing season, and conservation status.

- **Augment:**  The analyzed information is returned to the interface and presented as augmented overlays directly on top of the live camera feed.

- **Support Decision-Making:**  Rather than making decisions automatically, the system provides contextual recommendations that help fishermen determine whether a fish should be caught or released while preserving human judgment.


![System Architecture ](/assets/img/arfishing/07-system-architecture.svg)
_Real-time environmental information flows seamlessly from underwater sensing to user decision-making._

This architecture allows sustainability information to become part of the user's natural workflow instead of requiring manual searches or external reference materials.


### Information Provided

When a fish appears in view, the interface displays:
- Species name, family, size
- Conservation status (endangered, protected, sustainable)
- Estimated size with legal catch limits
- Catch/release recommendations
- Sustainability guidance
- Current fishing season, location and conditions

Rather than simply identifying fish, the interface supports environmentally responsible decision-making through contextual feedback.

![AR Interface Concept](/assets/img/arfishing/03-ar-interface-wireframes.svg)
_Interface showing real-time fish identification with sustainability indicators_

## User Journey

### Traditional Fishing Experience

**Prepare equipment → Travel to location → Cast line → Wait for catch → Catch fish → Identify the Species (uncertain) → Search Regulations or Reference Materials (interrupts workflow) → Decide to Keep or Release**

**Challenges:**
- Post-catch identification
- Uncertainty about regulations
- Manual research interrupts experience
- Risk of unintentional illegal catch

### AR-Enhanced Experience

**Prepare equipment → Travel to location → Cast line → View underwater feed → Fish Detected & Species Identified → Receive Real-Time Sustainability Guidance → Make an Informed Catch-or-Release Decision → Log Catch (Optional)**

**Opportunities**

- Reduce regulation lookup

- Increase decision confidence

- Prevent accidental bycatch

- Minimize interruption

![User Journey Comparison](/assets/img/arfishing/01-fishing-experience-comparison.svg)
_Comparison showing how AR provides decision support before the catch_



## Information Architecture

The experience was designed around a streamlined workflow:

**Home → Fishing Session → Live Camera Feed → Species Detection → Fish Details → Decision Support → Log Catch**

The information hierarchy prioritizes critical sustainability information while allowing users to access additional details when needed.

![Information Architecture](/assets/img/arfishing/02-information-architecture.svg)
_System structure showing navigation flow and content hierarchy_

## UX Principles

The interface was designed around several HCI principles:

#### Minimal Cognitive Load
Present only essential information to avoid distracting users during fishing activities.

#### Context-Aware Information
Display relevant sustainability guidance based on species, location, season, and regulations.

#### Hands-Free Interaction
Design for glanceable information that requires minimal physical interaction.

#### Outdoor Readability
Optimize contrast, typography, and layout for visibility in bright sunlight and water reflections.

#### Progressive Disclosure
Show critical information immediately while allowing deeper exploration when needed.

#### Real-Time Decision Support
Provide actionable guidance at the exact moment fishermen need it.

![Design Principles](/assets/img/arfishing/04-user-context-empathy.svg)
_Core UX principles guiding the interface design_


## Design Constraints

Designing for outdoor environments introduced several practical constraints that influenced both the interaction design and hardware configuration.

- **Outdoor Visibility** — Interfaces needed sufficient contrast and typography for use in bright sunlight and reflective water conditions.

- **Hands-Free Interaction** — Fishing requires continuous physical engagement, so interactions had to remain glanceable with minimal manual input.

- **Hardware Ergonomics** — Attaching a monitor directly to the fishing rod could affect comfort and casting performance. The concept therefore supported both rod-mounted and freestanding display configurations.

- **Connectivity** — Reliable wireless communication between the underwater camera, processing pipeline, and display device was necessary for delivering timely feedback.

## Prototype

The final prototype explored how contextual information could be integrated into the fishing workflow while minimizing cognitive load.

The concept included:

- Live underwater camera feed
- Real-time fish detection
- Species recognition
- Sustainability indicators
- Catch recommendations
- Fishing session tracking
- Catch history

The prototype prioritized glanceable interactions and progressive disclosure, allowing fishermen to access critical information without disrupting their natural workflow.

## Evaluation

### Success Criteria

The concept was evaluated to determine whether augmented reality could improve sustainable fishing decisions without disrupting the traditional fishing experience.

The primary success criteria were:

- Improve confidence in fish species identification.
- Help users interpret sustainability recommendations at a glance.
- Support informed keep-or-release decisions with minimal interruption.
- Integrate naturally into the existing fishing workflow.

### Study Design

To investigate the concept, our team conducted two comparative studies involving **30 participants** with varying levels of fishing experience, alongside a small control group responsible for validating fishing decisions throughout the study.

Participants included both experienced fishermen and recreational fishing practitioners. Both studies were conducted under consistent environmental conditions using the same fishing location and schedule to reduce external variability.

#### Study 1 — Traditional Fishing

Participants completed fishing activities using their normal workflow. This established a baseline for observing how users identified fish species, interpreted regulations, and decided whether to keep or release a catch without technological assistance.

Observations revealed that users frequently relied on prior experience or external reference materials when identifying fish and checking regulations, introducing uncertainty into the decision-making process.

#### Study 2 — AR-Assisted Fishing

Participants repeated the same fishing tasks using the AR Fishing concept. Before beginning, they explored the interface and became familiar with the interaction model.

During the fishing session, the system provided:

- Real-time species identification
- Conservation status
- Estimated fish size
- Sustainability guidance
- Catch recommendations

This allowed participants to make decisions using contextual information delivered at the moment of interaction rather than after the catch.

### Result

This project fundamentally changed how I think about designing emerging technologies.

Rather than viewing augmented reality as the product itself, I learned to treat AR as a medium for delivering contextual information that supports human decision-making without disrupting existing behaviors.

The comparative study demonstrated that contextual augmented reality guidance improved sustainable fishing decisions across both participant groups.

**Professional fishermen** reduced inadvertent overfishing from **30% to 15%.** and **Recreational fishermen** reduced inadvertent overfishing from **65% to 20%.**

The greatest improvement was observed among less experienced fishermen, suggesting that real-time decision support has the greatest impact when users have limited domain knowledge.

![Result ](/assets/img/arfishing/08-Reduction%20in%20inadvertent%20overfishing.png)
_Reduction in inadvertent overfishing_

### Key Findings

The evaluation revealed several important design insights:

Contextual guidance is most effective when delivered **before** a fishing decision rather than afterward.
Participants preferred concise visual recommendations over lengthy textual explanations.
Color-coded conservation indicators improved decision-making speed.
Real-time environmental information increased user confidence without reducing user autonomy.
Emerging technologies are most valuable when they complement existing workflows instead of replacing them.

Although exploratory in nature, the findings demonstrate the potential for augmented reality to encourage environmentally responsible fishing practices while maintaining the authenticity of the fishing experience.


## Reflection

This project fundamentally changed how I think about designing emerging technologies.

Rather than viewing augmented reality as the product itself, I learned to treat AR as a medium for delivering contextual information that supports human decision-making without disrupting existing behaviors.

Working on this concept also reinforced the importance of balancing technological capability with user needs. While machine learning can automate species recognition, the final decision should always remain with the fisherman. Designing technology that supports—not replaces—human expertise became one of the project's most valuable lessons.

The project also deepened my understanding of designing for outdoor environments, where visibility, cognitive load, and hands-free interaction become essential usability considerations.


## Future Directions

This project demonstrates the potential of augmented reality as a decision-support tool rather than a replacement for traditional fishing practices. Several opportunities remain for future exploration.

Future work could include:

- Conducting longitudinal field studies with recreational and commercial fishermen.
- Deploying the prototype in real marine environments under varying weather and lighting conditions.
- Integrating production-ready computer vision models for automatic fish recognition.
- Exploring voice interaction and audio feedback to further reduce manual interaction.
- Personalizing recommendations based on local fishing regulations and seasonal restrictions.
- Collaborating with marine conservation organizations to validate ecological data and sustainability recommendations.
- Expanding the system to support additional environmental metrics such as water quality, temperature, and habitat monitoring.

These improvements would help transform the concept into a deployable decision-support platform for sustainable fishing.



## Project Impact

This project demonstrates how **Human-Computer Interaction, Augmented Reality, and Machine Learning** can be combined to create meaningful environmental technology.

Rather than automating fishing decisions, AR Fishing **empowers users** with contextual information that supports sustainable practices while preserving the traditional fishing experience.

By providing real-time decision support at the moment of catch, the system has the potential to reduce overfishing, prevent bycatch, and encourage environmentally responsible fishing practices.



## Skills Applied

- UX Research & Literature Review
- Product Concept Design
- Design Thinking Methodology
- Augmented Reality Interface Design
- Spatial Computing & 3D Interaction Design
- Environmental Technology Design
- Information Architecture
- Task Flow Design
- Visual Design & Prototyping
- Usability Evaluation
- Human-Computer Interaction

---

*This project was done by three-person HCI research team, exploring how emerging technologies can support environmental sustainability through user-centered design.*
