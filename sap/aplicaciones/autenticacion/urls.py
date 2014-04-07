from django.conf.urls import patterns, url
from .views import Autenticacion, login_view, logout_view

urlpatterns = patterns('',
    
    url(r'^login/$', login_view, name='login'),
    url(r'^cerrar/$', logout_view, name='logout'),
    url(r'^$', Autenticacion.as_view(), name='inicio'),
)