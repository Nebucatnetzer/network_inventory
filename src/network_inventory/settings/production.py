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
    os.getenv("DOMAIN"),
]

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
CRISPY_FAIL_SILENTLY = not DEBUG

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "postgres",
        "USER": "postgres",
        "HOST": "db",
        "PORT": 5432,
    }
}
