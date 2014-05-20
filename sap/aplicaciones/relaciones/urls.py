from django.conf.urls import patterns, url
from .views import adm_relaciones, crear_relacion, listar_items, eliminar_relacion

urlpatterns = patterns('',
                       url(r'^adm_proyectos/gestionar/(?P<id_proyecto>\d+)/adm_items/(?P<id_fase>\d+)/relaciones/(?P<id_item>\d+)/$', adm_relaciones),
                       url(r'^adm_proyectos/gestionar/(?P<id_proyecto>\d+)/adm_items/(?P<id_fase>\d+)/relaciones/(?P<id_item>\d+)/nuevo/$', listar_items),
                       url(r'^adm_proyectos/gestionar/(?P<id_proyecto>\d+)/adm_items/(?P<id_fase>\d+)/relaciones/(?P<id_item>\d+)/nuevo/relacionnueva/(?P<id_importar>\d+)/$', crear_relacion),
                       url(r'^adm_proyectos/gestionar/(?P<id_proyecto>\d+)/adm_items/(?P<id_fase>\d+)/relaciones/(?P<id_item>\d+)/eliminar/(?P<id_padre>\d+)/$', eliminar_relacion),
                       )
