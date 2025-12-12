# The Wedding Company Management System

A comprehensive Django-based web application for managing wedding company operations including bookings, vendors, packages, and payments.

## Features

- **User Management**: Role-based authentication (Admin, Staff, Client)
- **Booking Management**: Create, update, and track wedding bookings
- **Payment Tracking**: Record and manage payments for bookings
- **Vendor Management**: Manage vendors and assign them to bookings
- **Package Management**: Create and manage wedding packages
- **Event Timeline**: Track event timeline and checklist items
- **Dashboard**: Overview of bookings, statistics, and upcoming events

## Project Structure

```
wedding_company/
├── accounts/          # User authentication and profiles
├── bookings/          # Booking management
├── vendors/           # Vendor management
├── packages/          # Package management
├── templates/         # HTML templates
├── static/            # Static files (CSS, JS, images)
├── media/             # User uploaded files
├── wedding_company/   # Project settings
└── manage.py          # Django management script
```

## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Steps

1. **Clone or navigate to the project directory:**
   ```bash
   cd D:\wedding_company
   ```

2. **Create a virtual environment (recommended):**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment:**
   
   On Windows:
   ```bash
   venv\Scripts\activate
   ```
   
   On Linux/Mac:
   ```bash
   source venv/bin/activate
   ```

4. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

5. **Run migrations:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create a superuser (admin account):**
   ```bash
   python manage.py createsuperuser
   ```
   Follow the prompts to create an admin account.

7. **Load sample data (optional):**
   You can create sample data through the Django admin panel or by running:
   ```bash
   python manage.py shell
   ```

8. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

9. **Access the application:**
   - Open your browser and go to: `http://127.0.0.1:8000/`
   - Admin panel: `http://127.0.0.1:8000/admin/`

## Usage

### Creating Users

1. Register a new account at `/register/`
2. Or create users through the admin panel at `/admin/`

### User Roles

- **Admin**: Full access to all features
- **Staff**: Can manage bookings, vendors, and packages
- **Client**: Can view and create their own bookings

### Managing Bookings

1. Navigate to "Bookings" from the main menu
2. Click "New Booking" to create a booking
3. Fill in event details, date, venue, and guest count
4. Set the total amount and advance paid
5. Add payments, timeline items, and assign vendors as needed

### Managing Vendors

1. Navigate to "Vendors" from the main menu
2. Click "New Vendor" (Admin/Staff only)
3. Fill in vendor details, contact information, and pricing
4. Assign vendors to bookings from the booking detail page

### Managing Packages

1. Navigate to "Packages" from the main menu
2. View available packages
3. Create packages through the admin panel

## Admin Panel

Access the Django admin panel at `/admin/` to:
- Manage all models
- Create vendor categories
- Manage packages and services
- View all bookings and payments
- Manage users and permissions

## Database

The project uses SQLite by default (for development). For production, consider using PostgreSQL or MySQL.

To change the database, update `DATABASES` in `wedding_company/settings.py`.

## Static Files

Static files are served from the `static/` directory. In production, configure your web server to serve static files or use:
```bash
python manage.py collectstatic
```

## Media Files

User-uploaded files are stored in the `media/` directory. Make sure this directory exists and is writable.

## Security Notes

- Change the `SECRET_KEY` in `wedding_company/settings.py` before deploying to production
- Set `DEBUG = False` in production
- Configure `ALLOWED_HOSTS` for your domain
- Use environment variables for sensitive settings
- Enable HTTPS in production

## Troubleshooting

### Migration Issues
If you encounter migration issues:
```bash
python manage.py makemigrations
python manage.py migrate
```

### Static Files Not Loading
```bash
python manage.py collectstatic
```

### Port Already in Use
If port 8000 is in use, specify a different port:
```bash
python manage.py runserver 8001
```

## Development

### Running Tests
```bash
python manage.py test
```

### Creating Migrations
After modifying models:
```bash
python manage.py makemigrations
python manage.py migrate
```

## License

This project is open source and available for educational purposes.

## Support

For issues or questions, please check the Django documentation or create an issue in the project repository.


