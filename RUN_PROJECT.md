# How to Run The Wedding Company Project

## ✅ Already Completed:
- ✅ Python 3.11.1 is installed
- ✅ Dependencies installed (Django, Pillow)
- ✅ Database migrations created and applied
- ✅ Database tables created

## Next Steps:

### Step 1: Create Admin User (Superuser)
Open a new terminal/command prompt and run:
```bash
cd D:\wedding_company
python manage.py createsuperuser
```

**When prompted, enter:**
- Username: (choose a username, e.g., "admin")
- Email: (your email address)
- Password: (choose a strong password)
- Password (again): (confirm password)

### Step 2: Start the Development Server
After creating the superuser, run:
```bash
python manage.py runserver
```

You should see output like:
```
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

### Step 3: Access the Application

**Open your web browser and go to:**

1. **Main Application:** 
   - URL: `http://127.0.0.1:8000/`
   - This will redirect to the dashboard

2. **Admin Panel:**
   - URL: `http://127.0.0.1:8000/admin/`
   - Login with the superuser credentials you created

### Step 4: First Steps After Login

1. **In Admin Panel (`/admin/`):**
   - Go to **Vendors > Vendor Categories** → Add categories (Photography, Catering, Decoration, etc.)
   - Go to **Vendors > Vendors** → Add some vendors
   - Go to **Packages > Packages** → Create wedding packages
   - Go to **Accounts > Users** → Create test client users (set role to "Client")

2. **In Main Application (`/`):**
   - Register a new client account at `/accounts/register/`
   - Or login with a client account
   - Create bookings, manage payments, assign vendors

## Quick Commands Reference:

```bash
# Start server
python manage.py runserver

# Start server on different port (if 8000 is busy)
python manage.py runserver 8001

# Create superuser
python manage.py createsuperuser

# Stop server
Press CTRL+C or CTRL+BREAK in the terminal
```

## Troubleshooting:

**Port 8000 already in use?**
```bash
python manage.py runserver 8001
```
Then access at: `http://127.0.0.1:8001/`

**Need to reset database?**
Delete `db.sqlite3` file and run:
```bash
python manage.py migrate
python manage.py createsuperuser
```

## That's it! Your project is ready to run! 🎉

