from django.conf.urls import patterns, url
from .views import crear_proyecto, modificar_proyecto, consultar_proyecto, eliminar_proyecto, listar_miembros, importar_proyecto, importar, proyecto_finalizado

urlpatterns = patterns('',
                       
        url(r'^adm_proyectos/crear/$', crear_proyecto),
        url(r'^adm_proyectos/modificar/(?P<id_proyecto>.*)/$', modificar_proyecto),
        url(r'^adm_proyectos/consultar/(?P<id_proyecto>.*)/$', consultar_proyecto),
        url(r'^adm_proyectos/eliminar/(?P<id_proyecto>.*)/$', eliminar_proyecto),
        url(r'^adm_proyectos/listar_miembros/(?P<id_proyecto>.*)/$', listar_miembros),
        url(r'^adm_proyectos/importar_proyecto/$', importar_proyecto),
        url(r'^adm_proyectos/importar_proyecto/importar/(?P<id_proyecto>.*)/$', importar),
        url(r'^adm_proyectos/proyecto_finalizado/$', proyecto_finalizado),

)