from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
	url(r'^fahanda/', include('fahanda.urls')),
	url(r'^admin/', include(admin.site.urls)),
)
