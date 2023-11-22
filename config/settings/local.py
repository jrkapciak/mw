from .base import *

DEBUG = True

INTERNAL_IPS = [
    "127.0.0.1",
    "localhost",
]

INSTALLED_APPS += [
    "debug_toolbar",
    "drf_yasg",
]
ROOT_URLCONF = "config.urls_dev"
ALLOWED_HOSTS = ["127.0.0.1", "localhost"]

MIDDLEWARE += [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

DEBUG_TOOLBAR_CONFIG = {
    "SHOW_TOOLBAR_CALLBACK": True,
}