# User Portal

This is a simple Django application that allows two types of users — Patients and Doctors — to sign up, log in, and view their respective dashboards.

## Features

- Custom user model with profile picture and address fields
- User signup with password confirmation check
- Separate dashboards for Doctors and Patients
- Login and logout functionality
- Media handling for profile picture uploads
- Blog app with creation and viewing of blog posts (Doctors can create and view, Patients can only view)
- Role-based navigation and access control for Patients and Doctors

## User Types

- Patient
- Doctor

## Signup Fields

- First Name
- Last Name
- Profile Picture
- Username
- Email
- Password
- Confirm Password
- Address: Line 1, City, State, Pincode
- User Type (Patient or Doctor)

## Blog Features

- Doctors can create blog posts and view their own posts
- Patients can view blog posts but cannot create them
- Blog posts include title, content, and author information
- Separate pages for creating blogs, viewing individual blog posts, and listing user's blog posts
- Navigation buttons to switch between blog views and profile dashboards

## Setup Instructions

Follow the steps below to set up and run the project locally.

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/user-portal.git
cd user-portal
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate        # On Linux/Mac
venv\Scripts\activate           # On Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

If you don't have a `requirements.txt` yet, install manually:

```bash
pip install django pillow
```

### 4. Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create Superuser (Optional)

```bash
python manage.py createsuperuser
```

### 6. Run the Development Server

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/signup/` to register a new user or `http://127.0.0.1:8000/login/` to log in.

### 7. Media File Support

Ensure the following is present in `settings.py` to serve uploaded profile pictures during development:

```python
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
```

And in `urls.py`:

```python
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # ... your urls ...
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

## Project Structure

```
user_portal/
├── accounts/
│   ├── migrations/
│   │   └── __init__.py
│   ├── templates/
│   │   ├── doctor_dashboard.html
│   │   ├── login.html
│   │   ├── patient_dashboard.html
│   │   └── signup.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── blog/
│   ├── migrations/
│   │   └── __init__.py
│   ├── templates/
│   │   ├── create_post.html
│   │   ├── my_posts.html
│   │   └── view_post.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── media/
├── user_portal/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── db.sqlite3
├── manage.py
├── requirements.txt

```

## Notes

- This project uses Django’s built-in authentication system with a custom user model.
- The root URL (`/`) redirects to the signup page.
