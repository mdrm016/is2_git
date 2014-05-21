from django.conf.urls import patterns, url
from .views import crear_solicitud, cancelar_solicitud, consultar_solicitud

urlpatterns = patterns('',
                       url(r'^adm_proyectos/gestionar/(?P<id_proyecto>\d+)/adm_items/(?P<id_fase>\d+)/crear_solicitud/(?P<id_item>\d+)/$', crear_solicitud),
                       url(r'^adm_proyectos/gestionar/(?P<id_proyecto>\d+)/adm_items/(?P<id_fase>\d+)/cancelar_solicitud/(?P<id_solicitud>\d+)/$', cancelar_solicitud),
                       url(r'^adm_proyectos/gestionar/(?P<id_proyecto>\d+)/adm_items/(?P<id_fase>\d+)/consultar_solicitud/(?P<id_solicitud>\d+)/$', consultar_solicitud),
                       )
