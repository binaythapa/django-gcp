import os
from pathlib import Path

# Base directory
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'dummy-secret-key'

DEBUG = True

ALLOWED_HOSTS = ['*']


# ✅ Installed apps
INSTALLED_APPS = [
    'django.contrib.contenttypes',
    'django.contrib.staticfiles',
    'core',
]


# ✅ Middleware (minimal but required)
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
]


ROOT_URLCONF = 'hello_project.urls'


# ✅ FIXED TEMPLATES (IMPORTANT)
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [],
        },
    },
]

WSGI_APPLICATION = 'hello_project.wsgi.application'


# ✅ Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# ✅ Static files
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')