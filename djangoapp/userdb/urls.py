from django.conf.urls import patterns, url

from userdb import views

urlpatterns = patterns('',
    url(r'^sync/', views.sync, name='sync')
)