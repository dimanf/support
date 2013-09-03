# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^', include('tech_support.ticket.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
