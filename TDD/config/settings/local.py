from pathlib import Path
import os
from .base import *  # noqa
from .base import env
# GENERAL
# ------------------------------------------------------------------------------
DEBUG = True
SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
    default="SET DJANGO_SECRET_KEY",
)

ALLOWED_HOSTS = ["localhost", "0.0.0.0", "127.0.0.1"]
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': str(os.path.join(BASE_DIR, "db.sqlite3"))
    }
}
