from django.conf.urls import patterns, url
from .views import Administrar_usuarios

urlpatterns = patterns('', 
    url(r'^adm_usuarios/$', Administrar_usuarios),
)
