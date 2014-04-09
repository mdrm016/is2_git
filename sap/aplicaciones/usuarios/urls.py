from django.conf.urls import patterns, url
from .views import usuario_nuevo
from .views import administrarUsuarios, modificarUsuario, consultarUsuario
from .views import usuarionuevo

urlpatterns = patterns('',
        url(r'^adm_usuarios/nuevo/$', usuario_nuevo),
        url(r'^adm_usuarios/$', administrarUsuarios),
        url(r'^adm_usuarios/nuevo/enviar/$', usuarionuevo),
        url(r'^adm_usuarios/modificar/(?P<id_usuario>.*)/$$', modificarUsuario),
        url(r'^adm_usuarios/consultar/(?P<id_usuario>.*)/$$', consultarUsuario),

)
