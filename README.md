# Campus Connect - MVP Platform

A web-based platform designed to solve information chaos on campus by providing a centralized hub for announcements, events, and student feedback.

## 🎯 Features

### 1. Unified Hub (Event & Notice Board)
- **Student Feed**: Real-time feed of all campus posts sorted by date
- **Smart Filters**: Toggle between All, Official Notices, and Club Events
- **Search**: Find specific announcements quickly by title or content
- **Post Types**: 
  - **Notices**: Important announcements from faculty/admin or clubs
  - **Events**: Campus events with date, time, and location details

### 2. Creator Dashboard
- **Secure Login**: Authentication system for clubs and faculty
- **Post Creation**: Simple form to create notices or events
- **Post Management**: View and delete your own posts
- **Role-Based Access**: Admin posts are automatically marked as "Official"

### 3. Suggestion Box
- **Anonymous Feedback**: Optional name field for student submissions
- **Categorized**: Choose from Hostel, Academics, Campus, Suggestion, or Other
- **Simple Submission**: Lightweight form for student feedback
- **Admin Dashboard**: Admin users can view all feedback and track status
- **Status Tracking**: Mark feedback as Pending, Reviewed, or Resolved

## 🚀 Getting Started

### Demo Credentials
To test the platform, use these credentials:

**Admin Account:**
- Username: `admin`
- Password: `admin123`

**Club Accounts:**
- Drama Club: `dramaclub` / `password123`
- Tech Club: `techclub` / `password123`
- Sports: `sportsclub` / `password123`

### For Students
1. Visit the home page to see all campus announcements and events
2. Use the search bar to find specific posts
3. Filter by "Official Notices" or "Club Events"
4. Click "Feedback" to submit suggestions or complaints

### For Clubs & Faculty
1. Click "Register" to create a new account
2. Fill in your details and choose account type (Club Organizer or Faculty/Admin)
3. Login to access your dashboard
4. Click "Create New Post" to share announcements or events
5. Manage your posts from the dashboard

### For Admins
1. Login with admin credentials
2. Access your dashboard to see all posts
3. Scroll down to view and manage student feedback
4. Update feedback status using the dropdown menu

## 📁 Project Structure

```
/
├── app.py              # Main Flask application
├── models.py           # Database models (User, Post, Feedback)
├── seed_data.py        # Sample data for demonstration
├── templates/          # HTML templates
│   ├── base.html       # Base template with navigation
│   ├── index.html      # Student feed (home page)
│   ├── login.html      # Login page
│   ├── register.html   # Registration page
│   ├── dashboard.html  # Creator dashboard
│   ├── create_post.html # Post creation form
│   └── feedback.html   # Feedback submission form
├── static/
│   └── css/
│       └── style.css   # Custom responsive styles
└── replit.md          # Technical documentation
```

## 🛠️ Technology Stack

- **Backend**: Flask (Python 3.11)
- **Database**: SQLite (file-based, perfect for MVP)
- **Authentication**: Flask-Login with password hashing
- **Frontend**: Jinja2 templates + vanilla JavaScript
- **Styling**: Custom CSS with mobile-responsive design

## 📊 Success Metrics

The MVP is designed to validate:

1. **Adoption**: Will students use a centralized platform?
   - Target: 50% of students visit within first month

2. **Engagement**: Will clubs/admin post regularly?
   - Target: 10+ new posts per week

3. **Feedback Volume**: Is there demand for a formal complaint system?
   - Target: 20+ meaningful feedback submissions in first month

## ⚠️ Important Notes

### Security (For Production Deployment)
- **Demo Admin Account**: Remove or change the hardcoded admin credentials before production
- **CSRF Protection**: Not implemented in MVP. Add Flask-WTF for production
- **Secret Key**: Change the development secret key to a secure random value
- **HTTPS**: Use HTTPS in production to protect login credentials

### Not in MVP (Phase 2 Features)
The following features are intentionally excluded from the MVP:
- ❌ Complex complaint ticketing system with routing
- ❌ Email notifications for feedback
- ❌ Attendance or timetable tracking
- ❌ Club collaboration tools (chat, tasks, file sharing)
- ❌ Advanced analytics and reporting

These will be evaluated for Phase 2 based on MVP success metrics.

## 🎨 Design Philosophy

Campus Connect prioritizes:
- **Simplicity**: Clean interface focused on core features
- **Mobile-First**: Responsive design that works on all devices
- **Speed**: Fast loading with minimal dependencies
- **Accessibility**: Clear navigation and readable content

## 📝 License

This is an MVP demonstration project for campus management.

## 🤝 Support

For questions or issues, please submit feedback through the platform's Feedback form.

---

**Built with ❤️ for campus communities**
