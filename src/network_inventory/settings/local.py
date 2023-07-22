from socket import gethostname
from socket import gethostbyname
from socket import getfqdn

import os

from .base import *


ALLOWED_HOSTS = [
    "localhost",
    "127.0.0.1",
    "0.0.0.0",
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
        "NAME": "django",
        "USER": os.environ.get("USER"),
        "HOST": os.environ.get("PGHOST"),
        "PORT": os.environ.get("PGPORT"),
    }
}
