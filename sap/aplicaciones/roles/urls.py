from django.conf.urls import patterns, url
from .views import rolNuevo, eliminarRol, asignarRol, desasignarRol
from .views import administrarRoles, modificarRol, consultarRol, asignarFaseRol, desasignarFaseRol

urlpatterns = patterns('',
        url(r'^adm_roles/$', administrarRoles),
        url(r'^adm_roles/nuevo/$', rolNuevo),
        url(r'^adm_roles/modificar/(?P<id_rol>\d+)/$', modificarRol),
        url(r'^adm_roles/asignar_fases/(?P<id_rol>\d+)/$', asignarFaseRol),
        url(r'^adm_roles/desasignar_fases/(?P<id_rol>\d+)/$', desasignarFaseRol),
        url(r'^adm_roles/consultar/(?P<id_rol>\d+)/$', consultarRol),
        url(r'^adm_roles/asignar/(?P<id_rol>\d+)/$', asignarRol),
        url(r'^adm_roles/desasignar/(?P<id_rol>\d+)/$', desasignarRol),
        url(r'^adm_roles/eliminar/(?P<id_rol>.*)/$', eliminarRol),

)