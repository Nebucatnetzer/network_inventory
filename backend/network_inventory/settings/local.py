from .base import *

ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
]

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'development_key'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}
