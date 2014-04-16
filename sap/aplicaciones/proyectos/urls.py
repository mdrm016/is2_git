from django.conf.urls import patterns, url
from aplicaciones.proyectos.views import crear_proyecto, modificar_proyecto
#from aplicaciones.usuarios.views import modificarUsuario

urlpatterns = patterns('',
                       
        url(r'^adm_proyectos/crear/$', crear_proyecto),
        url(r'^adm_proyectos/modificar/(?P<id_usuario>.*)/$', modificar_proyecto),

)