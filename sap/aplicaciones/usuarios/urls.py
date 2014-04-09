from django.conf.urls import patterns, url
from .views import usuario_nuevo
from .views import Administrar_usuarios
from .views import usuarionuevo

urlpatterns = patterns('',
        url(r'^adm_usuarios/nuevo/$', usuarionuevo),
        url(r'^adm_usuarios/$', Administrar_usuarios),
        url(r'^adm_usuarios/nuevo/enviar/$', usuario_nuevo),

)
