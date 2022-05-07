from .config import *
from .base import *

# GENERAL
# ------------------------------------------------------------------------------
DEBUG = True

SECRET_KEY = get_secret("SECRET_KEY")
ALLOWED_HOSTS = ["localhost", "0.0.0.0", "127.0.0.1"]
DATABASES = get_secret('DATABASES')