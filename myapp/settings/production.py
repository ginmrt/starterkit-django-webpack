from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
ALLOWED_HOSTS = ["myapp.com"]  # TODO

# TODO
SECRET_KEY = "Generate-Another-Something-Secret-And-Unique-For-This"
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

# TODO Choose some caching
# Example: using Memcached (add 'python-memcached' to requirements/prod.txt)
# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
#         'LOCATION': '127.0.0.1:11211',
#     }
# }


# -------------------- django-static-url --------------------
# The prefix of the static URL.
STATIC_ROOT_URL = "/static/"
IMPORTANT_FILE_PATH = "/srv/allmyapps/myapp/config/prod.uwsgi.ini"

# Cache Busting on a per-deployment basis
#
# Will change the URL for static files everytime the IMPORTANT_FILE_PATH is
# 'touched' (url generated based on access time).
#
# Users who previously had cached static files will be forced to download
# the 'new' version with each deployment.

from django_static_url_helper import url_helper
STATIC_URL = url_helper.get_static_url_file(
    STATIC_ROOT_URL, IMPORTANT_FILE_PATH, True, SECRET_KEY)
# ------------------------------------------------------------


# -------------------- django-webpack-loader -----------------
WEBPACK_LOADER = {
    'DEFAULT': {
        'CACHE': not DEBUG,
        'BUNDLE_DIR_NAME': 'bundles/',  # must end with slash
        'STATS_FILE': os.path.join(BASE_DIR, 'webpack-stats-prod.json'),
    }
}
# ------------------------------------------------------------

# ------------------------- Logging --------------------------
LOGGING["handlers"]["files"] = {
    "level": "WARNING",
    "class": "logging.handlers.RotatingFileHandler",
    "filename": "/var/log/python/django.myapp.log",
    "maxBytes": 5 * 1024 * 1024,
    "backupCount": 5,
    "formatter": "verbose"
}
LOGGING["handlers"]["mail_admins"] = {
    "level": "ERROR",
    "class": "django.utils.log.AdminEmailHandler",
    "include_html": True,
}
for name, logger in LOGGING["loggers"].items():
    logger["handlers"].remove("console")
    logger["handlers"].extend(["files", "mail_admins"])
# ------------------------------------------------------------


# ------------------------- Mailing --------------------------
# TODO: Configure this to receive error emails from Production
# and to send emails

# EMAIL_HOST = ""
# EMAIL_HOST_PASSWORD = ""
# EMAIL_HOST_USER = ""
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
# ------------------------------------------------------------
