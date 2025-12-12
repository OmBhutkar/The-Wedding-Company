# The Wedding Company Management System - Project Summary

## Overview
A comprehensive Django web application for managing wedding company operations including client bookings, vendor management, package offerings, and payment tracking.

## Project Structure

### Django Apps

#### 1. **accounts** - User Management
- **Models:**
  - `User`: Custom user model with roles (Admin, Staff, Client)
  - `ClientProfile`: Extended profile for clients
- **Features:**
  - User registration and authentication
  - Role-based access control
  - User profiles

#### 2. **bookings** - Booking Management
- **Models:**
  - `Booking`: Main booking model with event details
  - `Payment`: Payment tracking for bookings
  - `EventTimeline`: Timeline/checklist items for events
- **Features:**
  - Create, update, and view bookings
  - Payment tracking and management
  - Event timeline management
  - Dashboard with statistics
  - Status management (Pending, Confirmed, In Progress, Completed, Cancelled)

#### 3. **vendors** - Vendor Management
- **Models:**
  - `VendorCategory`: Categories for vendors
  - `Vendor`: Vendor information and details
  - `VendorAssignment`: Assignment of vendors to bookings
- **Features:**
  - Vendor CRUD operations
  - Vendor categorization
  - Vendor assignment to bookings
  - Vendor rating system

#### 4. **packages** - Package Management
- **Models:**
  - `Package`: Wedding packages with pricing
  - `PackageService`: Services included in packages
- **Features:**
  - Package listing and details
  - Service management
  - Guest capacity management

## Key Features

### User Roles
- **Admin**: Full system access
- **Staff**: Can manage bookings, vendors, and packages
- **Client**: Can create and manage their own bookings

### Booking Management
- Event details (name, date, time, venue)
- Guest count tracking
- Financial tracking (total amount, advance paid, remaining)
- Status workflow
- Payment history
- Event timeline/checklist

### Vendor Management
- Vendor profiles with contact information
- Service descriptions and pricing
- Rating system
- Assignment to specific bookings
- Category organization

### Package Management
- Predefined wedding packages
- Feature listings
- Service inclusions
- Guest capacity ranges

## Technology Stack

- **Backend**: Django 4.2+
- **Database**: SQLite (default, can be changed to PostgreSQL/MySQL)
- **Frontend**: Bootstrap 5.3, HTML5, CSS3
- **Icons**: Bootstrap Icons

## File Structure

```
wedding_company/
├── accounts/              # User management app
│   ├── models.py         # User and ClientProfile models
│   ├── views.py          # Authentication views
│   ├── forms.py          # Registration and login forms
│   └── urls.py           # URL routing
│
├── bookings/              # Booking management app
│   ├── models.py         # Booking, Payment, EventTimeline models
│   ├── views.py          # Booking CRUD and dashboard
│   ├── forms.py          # Booking forms
│   └── urls.py           # URL routing
│
├── vendors/               # Vendor management app
│   ├── models.py         # Vendor models
│   ├── views.py          # Vendor CRUD views
│   ├── forms.py          # Vendor forms
│   └── urls.py           # URL routing
│
├── packages/              # Package management app
│   ├── models.py         # Package models
│   ├── views.py          # Package views
│   └── urls.py           # URL routing
│
├── templates/             # HTML templates
│   ├── base.html         # Base template
│   ├── accounts/         # Account templates
│   ├── bookings/         # Booking templates
│   ├── vendors/          # Vendor templates
│   └── packages/         # Package templates
│
├── static/                # Static files (CSS, JS, images)
├── media/                 # User uploaded files
│
├── wedding_company/       # Project settings
│   ├── settings.py       # Django settings
│   ├── urls.py           # Main URL configuration
│   ├── wsgi.py           # WSGI configuration
│   └── asgi.py           # ASGI configuration
│
├── manage.py              # Django management script
├── requirements.txt       # Python dependencies
├── README.md              # Main documentation
├── SETUP.md               # Setup instructions
└── .gitignore            # Git ignore file
```

## Database Schema

### Key Relationships
- User → Booking (One-to-Many)
- Booking → Payment (One-to-Many)
- Booking → EventTimeline (One-to-Many)
- Booking → VendorAssignment (One-to-Many)
- Vendor → VendorAssignment (One-to-Many)
- VendorCategory → Vendor (One-to-Many)
- Package → PackageService (One-to-Many)

## URLs Structure

- `/` - Redirects to dashboard
- `/admin/` - Django admin panel
- `/accounts/` - Authentication (login, register, profile)
- `/bookings/` - Booking management
  - `/bookings/` - Dashboard
  - `/bookings/list/` - Booking list
  - `/bookings/create/` - Create booking
  - `/bookings/<id>/` - Booking detail
  - `/bookings/<id>/update/` - Update booking
- `/vendors/` - Vendor management
- `/packages/` - Package listing

## Security Features

- CSRF protection
- Password validation
- Role-based access control
- User authentication required for most views
- Admin-only features protected

## Future Enhancements (Optional)

- Email notifications
- Calendar integration
- File uploads for contracts/documents
- Advanced reporting and analytics
- Invoice generation
- Multi-language support
- Mobile app API

## Development Notes

- Uses Django's built-in authentication system
- Custom user model extends AbstractUser
- Bootstrap for responsive UI
- SQLite for easy development (changeable for production)
- Media files stored in `media/` directory
- Static files in `static/` directory

## Running the Project

See `SETUP.md` for detailed setup instructions.

Quick start:
```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```


