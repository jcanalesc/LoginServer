from django.conf.urls import patterns, url
from django.conf import settings
from django.conf.urls.static import static

from userdb import views

urlpatterns = patterns('',
    url(r'^sync/', views.sync, name='sync'),
    url(r'^getExcel/$', views.getExcel)
)