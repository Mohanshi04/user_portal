# User Portal

This is a simple Django application that allows two types of users — Patients and Doctors — to sign up, log in, and view their respective dashboards.

## Features

- Custom user model with profile picture and address fields
- User signup with password confirmation check
- Separate dashboards for Doctors and Patients
- Login and logout functionality
- Media handling for profile picture uploads

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
│   ├── templates/
│   │   ├── signup.html
│   │   ├── login.html
│   │   ├── doctor_dashboard.html
│   │   └── patient_dashboard.html
│   ├── models.py
│   ├── forms.py
│   ├── views.py
│   └── urls.py
├── user_portal/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── media/
├── manage.py
```

## Notes

- This project uses Django’s built-in authentication system with a custom user model.
- The root URL (`/`) redirects to the signup page.
