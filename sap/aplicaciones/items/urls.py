from django.conf.urls import patterns, url
from .views import adm_items
#, crear_fase, consultar_fase, eliminar_fase, modificar_fase, importar_fase, importarf

urlpatterns = patterns('',
                       url(r'^adm_proyectos/gestionar/(?P<id_proyecto>\d+)/adm_items/(?P<id_fase>\d+)/$', adm_items),
                       )