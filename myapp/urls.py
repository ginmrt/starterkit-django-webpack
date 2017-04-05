from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin

from myblog.views import BlogView

urlpatterns = [
    # Django Admin
    url(r'^admin/', include(admin.site.urls)),
]

urlpatterns += i18n_patterns(
    # These URLs will have /<language_code>/ appended to the beginning

    # myblog
    url(r'^$', BlogView.as_view(), name='blog'),
)


# Development cache busting on every Django server reload
if settings.DEBUG:
    from django_static_url_helper.django_url_helper import (
        staticfiles_dynamicurlpatterns
    )

    # Serve static and media files from development server
    urlpatterns += staticfiles_dynamicurlpatterns(settings.STATIC_ROOT_URL)
