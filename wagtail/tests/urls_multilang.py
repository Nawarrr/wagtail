from __future__ import absolute_import, unicode_literals

from django.conf.urls.i18n import i18n_patterns
from django.urls import include, path

from wagtail.core import urls as wagtail_urls

urlpatterns = i18n_patterns(path("", include(wagtail_urls)))
