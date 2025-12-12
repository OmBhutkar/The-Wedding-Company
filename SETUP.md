# Quick Setup Guide

## Step-by-Step Instructions

### 1. Install Python
Make sure you have Python 3.8 or higher installed.
Check by running:
```bash
python --version
```

### 2. Navigate to Project Directory
```bash
cd D:\wedding_company
```

### 3. Create Virtual Environment (Recommended)
```bash
python -m venv venv
```

### 4. Activate Virtual Environment
**Windows:**
```bash
venv\Scripts\activate
```

**Linux/Mac:**
```bash
source venv/bin/activate
```

### 5. Install Dependencies
```bash
pip install -r requirements.txt
```

### 6. Create Database Tables
```bash
python manage.py makemigrations
python manage.py migrate
```

### 7. Create Admin User
```bash
python manage.py createsuperuser
```
Enter username, email, and password when prompted.

### 8. Run the Server
```bash
python manage.py runserver
```

### 9. Access the Application
- Open browser: `http://127.0.0.1:8000/`
- Admin panel: `http://127.0.0.1:8000/admin/`

## First Steps After Setup

1. **Login to Admin Panel:**
   - Go to `http://127.0.0.1:8000/admin/`
   - Login with your superuser credentials

2. **Create Vendor Categories:**
   - Go to Vendors > Vendor Categories
   - Add categories like: Photography, Catering, Decoration, Music, etc.

3. **Create Vendors:**
   - Go to Vendors > Vendors
   - Add vendor details

4. **Create Packages:**
   - Go to Packages > Packages
   - Create wedding packages with pricing

5. **Create Test Users:**
   - Go to Accounts > Users
   - Create client users with role "Client"

6. **Start Using:**
   - Register/Login as a client
   - Create bookings
   - Manage payments and timeline

## Common Commands

```bash
# Create migrations after model changes
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Run server
python manage.py runserver

# Run server on different port
python manage.py runserver 8001

# Collect static files (for production)
python manage.py collectstatic
```

## Troubleshooting

**Issue: ModuleNotFoundError**
- Solution: Make sure virtual environment is activated and dependencies are installed

**Issue: Migration errors**
- Solution: Delete `db.sqlite3` and `migrations` folders (except `__init__.py`), then run migrations again

**Issue: Port already in use**
- Solution: Use a different port: `python manage.py runserver 8001`

**Issue: Static files not loading**
- Solution: Run `python manage.py collectstatic`


