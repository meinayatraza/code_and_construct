# aluminum_material/settings/production.py
from .base import *

DEBUG = False
ALLOWED_HOSTS = ['yourdomain.com']  # Replace with your actual domain

# Database (example for PostgreSQL)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'aluminum_material',
        'USER': 'dbuser',
        'PASSWORD': 'your_password',  # Use environment variables in production
        'HOST': 'localhost',
        'PORT': '',
    }
}

# Security settings
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True