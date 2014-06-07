from django.conf.urls import patterns, url
from views import crear_solicitud, cancelar_solicitud, consultar_solicitud, administrar_solicitud_realizadas, administrar_solicitud_recibidas, votar_solicitud, impacto, administrar_credenciales, consultarCredencial, cancelar_credencial

urlpatterns = patterns('',
                       url(r'^adm_proyectos/gestionar/(?P<id_proyecto>\d+)/adm_items/(?P<id_fase>\d+)/crear_solicitud/(?P<id_item>\d+)/$', crear_solicitud),
                       url(r'^adm_proyectos/gestionar/(?P<id_proyecto>\d+)/adm_items/(?P<id_fase>\d+)/crear_solicitud/(?P<id_item>\d+)/impacto/$', impacto),
                       url(r'^adm_proyectos/solicitudes_realizadas/$', administrar_solicitud_realizadas),
                       url(r'^adm_proyectos/solicitudes_recibidas/$', administrar_solicitud_recibidas),
                       url(r'^adm_proyectos/solicitudes_realizadas/cancelar_solicitud/(?P<id_solicitud>\d+)/$', cancelar_solicitud),
                       url(r'^adm_proyectos/solicitudes_realizadas/consultar_solicitud/(?P<id_solicitud>\d+)/$', consultar_solicitud),
                       url(r'^adm_proyectos/solicitudes_recibidas/votar_solicitud/(?P<id_solicitud>\d+)/$', votar_solicitud),
                       url(r'^adm_proyectos/admin_credenciales/$', administrar_credenciales),
                       url(r'^adm_proyectos/admin_credenciales/consultar_credencial/(?P<id_credencial>\d+)/$', consultarCredencial),
                       url(r'^adm_proyectos/admin_credenciales/cancelar_credencial/(?P<id_credencial>\d+)/$', cancelar_credencial),
                       )
