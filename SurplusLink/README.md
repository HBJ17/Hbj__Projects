# SurplusLink

A full-stack web application connecting surplus food donors (hotels, mess, caterers) with NGOs and orphanages using real-time location-based matching, delivery tracking, and rating system.

## Tech Stack

- **Frontend:** HTML, CSS (Bootstrap), Vanilla JavaScript, Leaflet.js (OpenStreetMap), Browser Geolocation API
- **Backend:** Python Flask, Flask-SQLAlchemy, Flask-Login
- **Database:** SQLite3
- **Email:** Local SMTP (no external API)

## Features

- **Authentication:** Role-based (Donor, NGO, Admin) with password hashing
- **Food Posting:** Donors create posts with food type, quantity, expiry, location
- **Location-Based Matching:** NGOs see nearby posts within configurable radius (Haversine formula)
- **Leaflet Map:** Donor/NGO markers, route polyline, delivery simulation, distance & ETA
- **Auto-Assignment:** NGO accepts → auto-assigned, delivery tracking
- **Delivery Completion:** Both donor and NGO notified; both can rate each other
- **Admin Dashboard:** Analytics, all posts with acceptor names/emails, CSV export
- **Expiry Intelligence:** Highlight posts expiring within 2 hours; auto-mark expired
- **Glassmorphism UI:** Green/light-green/white theme, frosted glass cards



## Project Structure

```
app/
  __init__.py          # Flask app factory
  models.py            # User, FoodPost, Rating
  routes/
    auth.py            # Register, login, logout
    donor.py           # Dashboard, create post, track, rate NGO
    ngo.py             # Nearby posts, accept, track delivery, confirm, rate donor
    admin.py           # Analytics, posts list, CSV export
  services/
    location_service.py   # Haversine, nearby posts, expiry
    rating_service.py     # Create rating, update average
    notification_service.py  # Local SMTP emails
  templates/
config.py
run.py
requirements.txt
```

## Database

SQLite database file: `surplus_link.db` (created on first run)

## Security

- Passwords hashed with Werkzeug
- Role-based access control
- Protected routes per role
