from .base import *


DEBUG = True
# Notice the 'ngrok' wildcard
ALLOWED_HOSTS = ["localhost", "127.0.0.1", "[::1]", ".ngrok.io"]

# TODO
SECRET_KEY = 'Generate-Something-Secret-And-Unique-For-This'

# No caching
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}

# Testing the cache while in development
# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
#         'LOCATION': 'unique-snowflake',
#     }
# }

# -------------------- django-static-url --------------------
# The prefix of the static URL.
STATIC_ROOT_URL = "/static/"

# Cache Busting for development for files under all the Django apps'
# /static/ directories.
#
# Will change the URL everytime the settings/server is reloaded.

from django_static_url_helper import url_helper
STATIC_URL = url_helper.get_static_url_now(STATIC_ROOT_URL, True, SECRET_KEY)
# ------------------------------------------------------------


# -------------------- django-webpack-loader -----------------
WEBPACK_LOADER = {
    'DEFAULT': {
        'CACHE': not DEBUG,
        'BUNDLE_DIR_NAME': 'bundles/',  # must end with slash
        'STATS_FILE': os.path.join(BASE_DIR, 'webpack-stats-dev.json'),
    }
}
# ------------------------------------------------------------

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


# Use local settings as needed
try:
    from .local import *
except ImportError:
    pass
