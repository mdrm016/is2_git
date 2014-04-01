from django.conf.urls import patterns, url
from .views import Autenticacion

urlpatterns = patterns('',
    
    url(r'^$', 'django.contrib.auth.views.login', 
        {'template_name' : 'autenticacion/autenticacion.html'}, name = 'login'),
                       
    url(r'^cerrar/$', 'django.contrib.auth.views.logout_then_login', 
        name = 'logout'),
    
     url(r'^inicio/$', Autenticacion.as_view(), name='inicio'),
)
