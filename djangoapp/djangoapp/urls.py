from django.conf.urls import patterns, include, url
	
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^appmanager/', include('appmanager.urls')),
    url(r'^userdb/'	   , include('userdb.urls')),
    # url(r'^djangoapp/', include('djangoapp.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admindocs:
    url(r'^admin/', include(admin.site.urls)),
)
