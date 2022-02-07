from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'development_key'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
CRISPY_FAIL_SILENTLY = not DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}
