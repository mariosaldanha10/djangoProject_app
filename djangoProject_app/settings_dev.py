import os

import djangoProject_app
from djangoProject_app.settings import BASE_DIR

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoProject_app.settings_dev')

DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'pollsdjango',
        'USER': 'root',
        'PASSWORD': 'admin100190',
        'HOST': 'localhost',
    }
}

INSTALLED_APPS = [
    'polls.apps.PollsConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'accounts'
]
SECRET_KEY = 'django-insecure-z#+ik2l+drzf-ma!*db8w#mr+^wix9%*)^n!(q15xk8#xcto4+'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'djangoProject_app.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
STATIC_URL = 'static/'
# django_project/settings_base.py
LOGIN_REDIRECT_URL = "home"
LOGOUT_REDIRECT_URL = "home"
