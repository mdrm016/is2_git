from django.conf.urls import patterns, url
from .views import tipoAtributoNuevo , eliminarTipoAtributo#, asignarRol, desasignarRol
from .views import administrarTipoAtributo, modificarTipoAtributo #, consultarRol

urlpatterns = patterns('',
        url(r'^adm_proyectos/gestionar/(?P<id_proyecto>\d+)/adm_tipos_atributo/$', administrarTipoAtributo),
        url(r'^adm_proyectos/gestionar/(?P<id_proyecto>\d+)/adm_tipos_atributo/nuevo/$', tipoAtributoNuevo),
        url(r'^adm_proyectos/gestionar/(?P<id_proyecto>\d+)/adm_tipos_atributo/modificar/(?P<id_tipo_atributo>\d+)/$', modificarTipoAtributo),
        #url(r'^adm_roles/consultar/(?P<id_rol>\d+)/$', consultarRol),
        #url(r'^adm_roles/asignar/(?P<id_rol>\d+)/$', asignarRol),
        #url(r'^adm_roles/desasignar/(?P<id_rol>\d+)/$', desasignarRol),
        url(r'^adm_proyectos/gestionar/(?P<id_proyecto>\d+)/adm_tipos_atributo/eliminar/(?P<id_tipo_atributo>\d+)/$', eliminarTipoAtributo),

)