# Campus Connect - MVP Platform

## Overview
Campus Connect is a web-based platform designed to solve information chaos on campus by providing a centralized hub for announcements, events, and student feedback.

**Purpose**: Single source of truth for campus notices and events
**Status**: MVP Complete - Ready for deployment
**Last Updated**: October 25, 2025

## Core Features

### 1. Unified Hub (Event & Notice Board)
- **Student Feed**: Real-time feed of all campus posts
- **Filtering**: Toggle between All, Official Notices, and Club Events
- **Search**: Find specific announcements quickly
- **Post Types**: 
  - Notices (title + description)
  - Events (title + description + date/time/location)

### 2. Creator Dashboard
- **Secure Login**: Authentication for clubs and faculty
- **Post Creation**: Simple form to create notices or events
- **Post Management**: View and delete your own posts
- **Role-Based**: Admin posts are marked as "Official"

### 3. Suggestion Box
- **Anonymous Feedback**: Optional name field
- **Categorized**: Hostel, Academics, Campus, Suggestion, Other
- **Simple Submission**: Lightweight form for student feedback
- **Admin Dashboard**: Admin users can view and manage all feedback submissions
- **Status Tracking**: Mark feedback as Pending, Reviewed, or Resolved

## Project Architecture

### Technology Stack
- **Backend**: Flask (Python 3.11)
- **Database**: SQLite (file-based, perfect for MVP)
- **Authentication**: Flask-Login
- **Frontend**: Jinja2 templates + vanilla JavaScript
- **Styling**: Custom CSS with mobile-responsive design

### File Structure
```
/
├── app.py              # Main Flask application
├── models.py           # Database models (User, Post)
├── templates/          # HTML templates
│   ├── base.html       # Base template
│   ├── index.html      # Student feed
│   ├── login.html      # Login page
│   ├── register.html   # Registration page
│   ├── dashboard.html  # Creator dashboard
│   ├── create_post.html # Post creation form
│   └── feedback.html   # Feedback form
├── static/
│   └── css/
│       └── style.css   # Custom styles
├── campus_connect.db   # SQLite database (auto-created)
└── replit.md          # This file
```

### Database Schema

**User Model**:
- id, username, password_hash
- full_name, organization, role (club/admin)
- created_at

**Post Model**:
- id, title, body, post_type (notice/event)
- is_official, author_id
- event_date, event_time, event_location (for events)
- created_at

**Feedback Model**:
- id, name (optional), category, message
- status (pending/reviewed/resolved)
- created_at

## Getting Started

### Demo Credentials
- **Username**: admin
- **Password**: admin123

### Creating New Accounts
1. Click "Register" in navigation
2. Fill in your details
3. Choose account type (Club Organizer or Faculty/Admin)
4. Login and start posting!

### Creating Posts
1. Login to your account
2. Click "Create New Post" button
3. Select post type (Notice or Event)
4. Fill in required fields
5. Submit

### Submitting Feedback
1. Click "Feedback" in navigation
2. Choose a category
3. Write your message
4. Submit (optionally provide your name)

## Recent Changes
- October 25, 2025: Initial MVP implementation
  - Complete authentication system
  - Post creation and management
  - Student feed with search and filters
  - Feedback system with database persistence
  - Admin dashboard for viewing and managing feedback
  - Mobile-responsive design
  
## Security Notes (Important for Production)
- **Demo Admin Account**: The app creates a default admin account (username: admin, password: admin123) for testing purposes. This should be removed or secured before production deployment.
- **CSRF Protection**: Not implemented in MVP. Should be added using Flask-WTF for production.
- **Secret Key**: Using a development secret key. Should be changed to a secure random value in production.

## Not in MVP (Phase 2 Features)
- ❌ Complex complaint ticketing system
- ❌ Attendance/timetable tracking
- ❌ Club collaboration tools (chat, tasks, files)
- ❌ Email integration for feedback
- ❌ Advanced analytics and reporting

## Success Metrics
The MVP is designed to validate:
1. **Adoption**: Will students use a centralized platform?
2. **Engagement**: Will clubs/admin post regularly?
3. **Feedback Volume**: Is there demand for a formal complaint system?

Target metrics:
- 50% of students visit within first month
- 10+ new posts per week
- 20+ meaningful feedback submissions in first month

## Deployment Notes
- Application runs on port 5000
- SQLite database is file-based (no external DB needed)
- Environment runs on Python 3.11
- Uses Flask development server (adequate for MVP)

## User Preferences
- Clean, simple interface prioritized
- Mobile-first responsive design
- No unnecessary complexity
- Focus on core MVP features only
