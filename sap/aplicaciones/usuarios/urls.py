from django.conf.urls import patterns, url
from .views import UsuarioNuevo
from .views import Administrar_usuarios

urlpatterns = patterns('',
                       url(r'^nuevo/$', 'UsuarioNuevo', name='usuarionuevo'),
                       url(r'^adm_usuarios/$', 'Administrar_usuarios', name='admusuarios'),
)