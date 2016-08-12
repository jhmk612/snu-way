from .common import *

DEBUG = False
ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
    'ENGINE': 'django.db.backends.portgresql',
    'NAME': 'ubuntu',
    'USER': 'ubuntu',
    'PASSWORD': 'withaskdjango!',
    'HOST': '127.0.0.1',
    },
}