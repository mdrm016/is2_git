from django.conf.urls import patterns, url
from .views import crear_solicitud, cancelar_solicitud, consultar_solicitud, administrar_solicitud_realizadas, listar_proyectos, listar_fases, listar_items, administrar_solicitud_recibida

urlpatterns = patterns('',
                       url(r'^adm_proyectos/gestionar/(?P<id_proyecto>\d+)/adm_items/(?P<id_fase>\d+)/crear_solicitud/(?P<id_item>\d+)/$', crear_solicitud),

                       url(r'^adm_proyectos/solicitudes_realizadas/$', administrar_solicitud_realizadas),
                       url(r'^adm_proyectos/solicitudes_realizadas/listar_proyectos/$', listar_proyectos),
                       url(r'^adm_proyectos/solicitudes_realizadas/listar_proyectos/(?P<id_proyecto>\d+)/listar_fases/$', listar_fases),
                       url(r'^adm_proyectos/solicitudes_realizadas/listar_proyectos/(?P<id_proyecto>\d+)/listar_fases/(?P<id_fase>\d+)/listar_items/$', listar_items),
                       url(r'^adm_proyectos/solicitudes_realizadas/cancelar_solicitud/(?P<id_solicitud>\d+)/$', cancelar_solicitud),
                       url(r'^adm_proyectos/solicitudes_realizadas/consultar_solicitud/(?P<id_solicitud>\d+)/$', consultar_solicitud),
                       )
