from django.conf.urls import patterns, url
from aplicaciones.proyectos.views import crear_proyecto
#from aplicaciones.usuarios.views import modificarUsuario

urlpatterns = patterns('',
        #url(r'^adm_proyecto/eliminar/(?P<id_usuario>.*)/$', modificarUsuario),
        url(r'^adm_proyectos/crear/', crear_proyecto),

)