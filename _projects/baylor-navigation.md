---
layout: page
title: "GoBears: Baylor Campus Navigation System"
permalink: /projects/baylor-navigation/
---

## Overview

GoBears is a comprehensive campus navigation system designed to help Baylor University students, faculty, and visitors easily navigate the campus environment. The platform provides an interactive map-based interface with detailed information about buildings, rooms, and campus resources, making it simple to find locations and reserve spaces.

This full-stack web application addresses the common challenge of navigating large university campuses, where finding specific rooms, buildings, or resources can be time-consuming and confusing, especially for new students and visitors.

---

## Project Objectives

- **Simplify Campus Navigation**: Provide an intuitive interface for locating buildings and specific rooms across campus
- **Enable Indoor Navigation**: Offer detailed floor plans and internal building navigation
- **Facilitate Resource Management**: Allow authorized users to manage building and room information
- **Support Room Reservations**: Enable students and faculty to check room availability and make reservations
- **Improve Campus Accessibility**: Make campus information accessible to all users regardless of familiarity with the campus

---

## Key Features

### Interactive Campus Map
- Real-time map interface powered by LeafletJS
- Building locations marked with interactive markers
- Zoom and pan functionality for detailed exploration
- Search functionality to quickly find specific buildings

### Internal Building Navigation
- Detailed floor plans for campus buildings
- Room-by-room navigation
- Information about room types, capacity, and amenities
- Accessibility information for each location

### Resource Management System (Admin)
- Add, edit, and delete building information
- Manage room details and configurations
- Update building hours and contact information
- Validation system to ensure data integrity

### Room Reservation System
- View available time slots for bookable rooms
- Reserve rooms for specific time periods
- Check reservation status and availability
- Automatic validation of reservation conflicts

### User-Friendly Interface
- Clean, modern UI design
- Responsive layout for mobile and desktop
- Intuitive navigation flow
- Quick access to frequently needed information

---

## Technical Architecture

### Frontend Technologies
- **React.js**: Component-based UI framework for building interactive interfaces
- **LeafletJS**: Open-source JavaScript library for interactive maps
- **Responsive Design**: Mobile-first approach ensuring usability across devices

### Backend Technologies
- **Spring Boot**: Java-based framework for building RESTful APIs
- **PostgreSQL**: Relational database for storing building, room, and reservation data
- **RESTful API Architecture**: Clean API design for frontend-backend communication

### Key Technical Implementations

**Activity Diagram: Add Room**
- Admin authentication and authorization
- Room number validation to prevent duplicates
- Form validation for required fields
- Confirmation workflow before submission
- Data persistence to database

**Sequence Diagram: Building Management**
- Building name uniqueness validation
- Repository pattern for data access
- Service layer for business logic
- Controller layer for request handling
- Error handling for duplicate entries

**Sequence Diagram: Room Reservation**
- Real-time availability checking
- 30-day advance booking window
- Validation of bookable room status
- Conflict detection for overlapping reservations
- User notification system

---

## System Design Highlights

### Database Schema
- **Buildings Table**: Store building information including name, location, hours, and contact details
- **Rooms Table**: Room details including number, type, capacity, and bookable status
- **Reservations Table**: Booking records with user info, time slots, and status
- **Users Table**: Authentication and authorization management

### API Endpoints
- `GET /buildings`: Retrieve all buildings
- `POST /buildings`: Add new building (admin only)
- `GET /rooms/{buildingId}`: Get rooms in a building
- `POST /reservations`: Create room reservation
- `GET /reservations/available`: Check available time slots

### Security Features
- Role-based access control (Admin/User)
- Input validation and sanitization
- Secure authentication system
- Protection against common web vulnerabilities

---

## Development Team

This project was developed collaboratively by:
- **Mahee Tayba** - Full-stack development, system design
- **Nishan Karki** - Backend development, database design
- **Pranish Bhagat** - Frontend development, UI/UX design
- **Yudeep Rajbhandari** - Backend development, API design

---

## Technologies & Tools

- **Frontend**: React.js, JavaScript, HTML5, CSS3, LeafletJS
- **Backend**: Spring Boot, Java
- **Database**: PostgreSQL
- **Version Control**: Git, GitHub
- **Development Tools**: IntelliJ IDEA, Visual Studio Code
- **API Testing**: Postman
- **Design Tools**: Visual Paradigm (for UML diagrams)

---

## Impact & Learning Outcomes

### Project Impact
- Improved campus navigation experience for students and visitors
- Reduced time spent searching for buildings and rooms
- Streamlined room reservation process
- Provided administrators with efficient resource management tools

### Technical Skills Developed
- Full-stack web application development
- RESTful API design and implementation
- Database schema design and optimization
- Frontend-backend integration
- Team collaboration and version control
- UML diagram creation for system design
- Agile development methodology

---

## Related Repository

View the complete source code and technical documentation:

**Backend Repository**: [GoBears Backend on GitHub](https://github.com/yudeep-rajbhandari/goBearsBackEnd)

---

## Future Enhancements

Potential improvements for future iterations:
- Mobile application for iOS and Android
- Real-time occupancy tracking
- Integration with university course scheduling system
- AR-based navigation for indoor wayfinding
- Accessibility features for users with disabilities
- Multilingual support for international students
