from .base import *

ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
]

CSRF_TRUSTED_ORIGINS = [
    'http://localhost:8000',
]

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "foo"

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'HOST': 'localhost',
        'PORT': 5432,
        'PASSWORD': 'password',
    }
}
