from .base import *

DEBUG = True

INTERNAL_IPS = [
    "127.0.0.1",
    "localhost",
]

INSTALLED_APPS += [
    "debug_toolbar",
]

ALLOWED_HOSTS = ["127.0.0.1", "localhost"]

MIDDLEWARE += [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]
