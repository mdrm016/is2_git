from django.conf.urls import patterns, url
#from .views import rolNuevo, eliminarRol
from .views import administrarRoles#, modificarRol, consultarRol

urlpatterns = patterns('',
        url(r'^adm_roles/$', administrarRoles),
        #url(r'^adm_roles/nuevo/$', rolNuevo),
        #url(r'^adm_roles/modificar/(?P<id_usuario>\d+)/$', modificarRol),
        #url(r'^adm_roles/consultar/(?P<id_usuario>\d+)/$', consultarRol),
        #url(r'^adm_roles/eliminar/(?P<id_usuario>.*)/$', eliminarRol),

)