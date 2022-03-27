from socket import gethostname
from socket import gethostbyname
from socket import getfqdn

from .base import *


ALLOWED_HOSTS = [
    "localhost",
    "127.0.0.1",
    getfqdn(),
    gethostname(),
    gethostbyname(gethostname()),
]

CSRF_TRUSTED_ORIGINS = [
    "http://localhost:8000",
]

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "foo"

DEBUG = True
CRISPY_FAIL_SILENTLY = not DEBUG

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "postgres",
        "USER": "postgres",
        "HOST": "localhost",
        "PORT": 5432,
        "PASSWORD": "password",
    }
}
