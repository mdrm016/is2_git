from django.conf.urls import patterns, url
from .views import usuario_nuevo, Administrar_usuarios, usuarionuevo, usuario_eliminar

urlpatterns = patterns('',
        url(r'^adm_usuarios/nuevo/$', usuario_nuevo),
        url(r'^adm_usuarios/$', Administrar_usuarios),
        url(r'^adm_usuarios/nuevo/enviar/$', usuarionuevo),
        url(r'^adm_usuarios/eliminar/(?P<id_usuario>.*)/$', usuario_eliminar),

)
