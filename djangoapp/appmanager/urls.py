from django.conf.urls import patterns, url

from appmanager import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^login/', views.auth, name='auth')
)