# The Wedding Company Management System

Modern Django app to run a wedding company end-to-end: bookings, vendors, packages, payments, timelines, and role-based access.

## ✨ Highlights
- Role-based auth (Admin, Staff, Client)
- Booking lifecycle with status, payments, and timelines
- Vendor catalog + assignments
- Packages with feature lists and pricing
- Dashboard with stats and upcoming events
- Polished UI with light/dark toggle

## 🧭 Quick Start (dev)
```bash
cd D:\wedding_company
python -m venv venv
venv\Scripts\activate           # on Windows (or source venv/bin/activate on macOS/Linux)
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver 8001 # or 8000
```
Open: http://127.0.0.1:8001/ (admin: /admin/)

## 🏗️ Project Structure
```
wedding_company/
├── accounts/        # users, roles, auth
├── bookings/        # bookings, payments, timelines
├── vendors/         # vendor catalog + assignments
├── packages/        # wedding packages + features
├── templates/       # Django templates
├── static/          # CSS/JS/assets
├── media/           # uploaded files
├── wedding_company/ # settings/urls/wsgi
└── manage.py
```

## 🔐 Roles
- **Admin**: full control (users, bookings, vendors, packages, payments)
- **Staff**: manage operational data (bookings, vendors, packages)
- **Client**: manage their own bookings

## 🚀 Deploy to Render (blueprint)
Already included:
- `render.yaml` (service + free Postgres)
- `Procfile` (gunicorn)
- `whitenoise` + `dj-database-url` in `settings.py`

Render env vars to set (auto in render.yaml):
- `SECRET_KEY`
- `DEBUG=False`
- `ALLOWED_HOSTS` = your Render URL
- `CSRF_TRUSTED_ORIGINS` = https://yourapp.onrender.com
- `DATABASE_URL` (from Render Postgres)

### Manual deploy steps
1) Push to GitHub.  
2) In Render: New → Blueprint → select repo.  
3) First deploy runs `collectstatic` and `migrate`.  
4) Open Render shell: `python manage.py createsuperuser`.  
5) Visit your Render URL.

## ⚙️ Common commands
```bash
# migrations
python manage.py makemigrations
python manage.py migrate

# static
python manage.py collectstatic --noinput

# tests
python manage.py test
```

## 🔧 Troubleshooting
- Port busy: `python manage.py runserver 8001`
- Static 404 in prod: ensure `collectstatic` ran and `STATIC_ROOT` is served (WhiteNoise enabled)
- DB issues: check `DATABASE_URL`, rerun `migrate`

## 📄 License
Open source for learning and adaptation. Add your preferred license if needed.
