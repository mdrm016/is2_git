from django.conf.urls import patterns, url
from .views import adm_items, listar_tipo_item, crear_item, cargar_valores, listar_versiones, consultar_version, revertir_version, modificar_item, consultar_item, consultar_atributos, eliminar_item, listar_eliminados, revivir_eliminado, consultar_eliminado, consultar_version_eliminado, consultar_relaciones
from .views import costo_impacto, consultar_enrevision, finrevision 

urlpatterns = patterns('',
                       url(r'^adm_proyectos/gestionar/(?P<id_proyecto>\d+)/adm_items/(?P<id_fase>\d+)/$', adm_items),
                       url(r'^adm_proyectos/gestionar/(?P<id_proyecto>\d+)/adm_items/(?P<id_fase>\d+)/atributos/(?P<id_item>\d+)/$', cargar_valores),
                       url(r'^adm_proyectos/gestionar/(?P<id_proyecto>\d+)/adm_items/(?P<id_fase>\d+)/versiones/(?P<id_item>\d+)/$', listar_versiones),
                       url(r'^adm_proyectos/gestionar/(?P<id_proyecto>\d+)/adm_items/(?P<id_fase>\d+)/modificar/(?P<id_item>\d+)/$', modificar_item),
                       url(r'^adm_proyectos/gestionar/(?P<id_proyecto>\d+)/adm_items/(?P<id_fase>\d+)/eliminar/(?P<id_item>\d+)/$', eliminar_item),
                       url(r'^adm_proyectos/gestionar/(?P<id_proyecto>\d+)/adm_items/(?P<id_fase>\d+)/consultar/(?P<id_item>\d+)/$', consultar_item),
                       url(r'^adm_proyectos/gestionar/(?P<id_proyecto>\d+)/adm_items/(?P<id_fase>\d+)/consul_eliminado/(?P<id_item>\d+)/$', consultar_eliminado),
                       url(r'^adm_proyectos/gestionar/(?P<id_proyecto>\d+)/adm_items/(?P<id_fase>\d+)/consul_atrib/(?P<id_item>\d+)/$', consultar_atributos),
                       url(r'^adm_proyectos/gestionar/(?P<id_proyecto>\d+)/adm_items/(?P<id_fase>\d+)/consul_relac/(?P<id_item>\d+)/$', consultar_relaciones),        
                       url(r'^adm_proyectos/gestionar/(?P<id_proyecto>\d+)/adm_items/(?P<id_fase>\d+)/versiones/(?P<id_item>\d+)/version/(?P<version>\d+)/$', consultar_version),
                       url(r'^adm_proyectos/gestionar/(?P<id_proyecto>\d+)/adm_items/(?P<id_fase>\d+)/consul_eliminado/(?P<id_item>\d+)/eliminadoversion/(?P<version>\d+)/$', consultar_version_eliminado),
                       url(r'^adm_proyectos/gestionar/(?P<id_proyecto>\d+)/adm_items/(?P<id_fase>\d+)/consul_eliminado/(?P<id_item>\d+)/revivir/(?P<version>\d+)/$', revivir_eliminado),
                       url(r'^adm_proyectos/gestionar/(?P<id_proyecto>\d+)/adm_items/(?P<id_fase>\d+)/versiones/(?P<id_item>\d+)/revertir/(?P<version>\d+)/$', revertir_version),
                       url(r'^adm_proyectos/gestionar/(?P<id_proyecto>\d+)/adm_items/(?P<id_fase>\d+)/nuevo/$', listar_tipo_item),
                       url(r'^adm_proyectos/gestionar/(?P<id_proyecto>\d+)/adm_items/(?P<id_fase>\d+)/eliminados/$', listar_eliminados), 
                       url(r'^adm_proyectos/gestionar/(?P<id_proyecto>\d+)/adm_items/(?P<id_fase>\d+)/nuevo/crear/(?P<id_tipoitem>\d+)/$', crear_item),
                       url(r'^adm_proyectos/gestionar/(?P<id_proyecto>\d+)/adm_items/(?P<id_fase>\d+)/impacto/(?P<id_item>\d+)/$', costo_impacto),
                       url(r'^adm_proyectos/gestionar/(?P<id_proyecto>\d+)/adm_items/(?P<id_fase>\d+)/consultar_enrevision/(?P<id_item>\d+)/$', consultar_enrevision),
                       url(r'^adm_proyectos/gestionar/(?P<id_proyecto>\d+)/adm_items/(?P<id_fase>\d+)/finrevision/(?P<id_item>\d+)/$', finrevision),
                       )
