from .base import *

ALLOWED_HOSTS = [
    'inventory.2li.local',
]

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'kzx(i9^@*g^cgp(_3052%*1d%zyu^2z_@pgso5!_q@jb-j%4m='

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'HOST': 'db',
        'PORT': 5432,
    }
}

