from django.conf.urls import patterns, url
from .views import adm_items, listar_tipo_item, crear_item, cargar_valores, listar_versiones, consultar_version, revertir_version

urlpatterns = patterns('',
                       url(r'^adm_proyectos/gestionar/(?P<id_proyecto>\d+)/adm_items/(?P<id_fase>\d+)/$', adm_items),
                       url(r'^adm_proyectos/gestionar/(?P<id_proyecto>\d+)/adm_items/(?P<id_fase>\d+)/atributos/(?P<id_item>\d+)/$', cargar_valores),
                       url(r'^adm_proyectos/gestionar/(?P<id_proyecto>\d+)/adm_items/(?P<id_fase>\d+)/versiones/(?P<id_item>\d+)/$', listar_versiones),        
                       url(r'^adm_proyectos/gestionar/(?P<id_proyecto>\d+)/adm_items/(?P<id_fase>\d+)/versiones/(?P<id_item>\d+)/version/(?P<version>\d+)/$', consultar_version),
                       url(r'^adm_proyectos/gestionar/(?P<id_proyecto>\d+)/adm_items/(?P<id_fase>\d+)/versiones/(?P<id_item>\d+)/revertir/(?P<version>\d+)/$', revertir_version),
                       url(r'^adm_proyectos/gestionar/(?P<id_proyecto>\d+)/adm_items/(?P<id_fase>\d+)/nuevo/$', listar_tipo_item),
                       url(r'^adm_proyectos/gestionar/(?P<id_proyecto>\d+)/adm_items/(?P<id_fase>\d+)/nuevo/crear/(?P<id_tipoitem>\d+)/$', crear_item),
                       )