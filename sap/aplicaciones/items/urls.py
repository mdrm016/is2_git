from django.conf.urls import patterns, url
from .views import adm_items, listar_tipo_item, crear_item
#, crear_fase, consultar_fase, eliminar_fase, modificar_fase, importar_fase, importarf

urlpatterns = patterns('',
                       url(r'^adm_proyectos/gestionar/(?P<id_proyecto>\d+)/adm_items/(?P<id_fase>\d+)/$', adm_items),
                       url(r'^adm_proyectos/gestionar/(?P<id_proyecto>\d+)/adm_items/(?P<id_fase>\d+)/nuevo/$', listar_tipo_item),
                       url(r'^adm_proyectos/gestionar/(?P<id_proyecto>\d+)/adm_items/(?P<id_fase>\d+)/nuevo/crear/(?P<id_tipoitem>\d+)/$', crear_item),
                       )