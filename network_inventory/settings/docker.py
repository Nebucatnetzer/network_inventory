from .base import *

ALLOWED_HOSTS = ["localhost", "127.0.0.1", "10.7.89.104"]

CSRF_TRUSTED_ORIGINS = [
    "http://localhost:8080",
]

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY")

DEBUG = os.environ.get("DJANGO_DEBUG")
CRISPY_FAIL_SILENTLY = not DEBUG

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "postgres",
        "USER": "postgres",
        "HOST": "db",
        "PORT": 5432,
        "PASSWORD": "password",
    }
}
