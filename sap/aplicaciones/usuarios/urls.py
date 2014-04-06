from django.conf.urls import patterns, url
from .views import UsuarioNuevo
from .views import Administrar_usuarios

urlpatterns = patterns('',
        url(r'^adm_usuarios/nuevo/$', UsuarioNuevo),
        url(r'^adm_usuarios/$', Administrar_usuarios),
)

