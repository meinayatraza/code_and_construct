from .base import *

DEBUG = False
ALLOWED_HOSTS = ['yourdomain.com']  # Update with your domain

# Configure production database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'aluminum_material',
        'USER': 'dbuser',
        'PASSWORD': '**********',  # Use environment variables in real setup
        'HOST': 'localhost',
        'PORT': '',
    }
}

# Security settings
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True