from django.conf.urls import patterns, url
from .views import usuario_nuevo
from .views import Administrar_usuarios

urlpatterns = patterns('',
        url(r'^adm_usuarios/nuevo/$', usuario_nuevo),
        url(r'^adm_usuarios/$', Administrar_usuarios),
)
