from .config import *
from .base import *

# DEPLOY SETTINGS
# ------------------------------------------------------------------------------
DEBUG = True
ROOT_URLCONF = get_secret("ROOT_URLCONF")
SECRET_KEY = get_secret("SECRET_KEY")
ALLOWED_HOSTS = []
DATABASES = get_secret('DATABASES')