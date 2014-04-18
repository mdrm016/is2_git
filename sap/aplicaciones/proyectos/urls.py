from django.conf.urls import patterns, url
from .views import crear_proyecto, modificar_proyecto, consultar_proyecto, eliminar_proyecto, listar_miembros
#from aplicaciones.usuarios.views import modificarUsuario

urlpatterns = patterns('',
                       
        url(r'^adm_proyectos/crear/$', crear_proyecto),
        url(r'^adm_proyectos/modificar/(?P<id_proyecto>.*)/$', modificar_proyecto),
        url(r'^adm_proyectos/consultar/(?P<id_proyecto>.*)/$', consultar_proyecto),
        url(r'^adm_proyectos/eliminar/(?P<id_proyecto>.*)/$', eliminar_proyecto),
        url(r'^adm_proyectos/listar_miembros/(?P<id_proyecto>.*)/$', listar_miembros),

)