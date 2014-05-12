from django.conf.urls import patterns, url
from .views import tipoAtributoNuevo , eliminarTipoAtributo, importarTipoAtributo, listar_proyectos, listar_tipoAtributo
from .views import administrarTipoAtributo, modificarTipoAtributo , consultarTipoAtributo

urlpatterns = patterns('',
        url(r'^adm_proyectos/gestionar/(?P<id_proyecto>\d+)/adm_tipos_atributo/$', administrarTipoAtributo),
        url(r'^adm_proyectos/gestionar/(?P<id_proyecto>\d+)/adm_tipos_atributo/nuevo/$', tipoAtributoNuevo),
        url(r'^adm_proyectos/gestionar/(?P<id_proyecto>\d+)/adm_tipos_atributo/modificar/(?P<id_tipo_atributo>\d+)/$', modificarTipoAtributo),
        url(r'^adm_proyectos/gestionar/(?P<id_proyecto>\d+)/adm_tipos_atributo/consultar/(?P<id_tipo_atributo>\d+)/$', consultarTipoAtributo),
        url(r'^adm_proyectos/gestionar/(?P<id_proyecto>\d+)/adm_tipos_atributo/listar_proyectos/$', listar_proyectos),
        url(r'^adm_proyectos/gestionar/(?P<id_proyecto>\d+)/adm_tipos_atributo/listar_proyectos/listar_tipo_atributo/(?P<proyecto_select>\d+)/$', listar_tipoAtributo),
        url(r'^adm_proyectos/gestionar/(?P<id_proyecto>\d+)/adm_tipos_atributo/listar_proyectos/listar_tipo_atributo/(?P<proyecto_select>\d+)/importar_tipo_atributo/(?P<id_tipo_atributo>\d+)/$', importarTipoAtributo),
        url(r'^adm_proyectos/gestionar/(?P<id_proyecto>\d+)/adm_tipos_atributo/eliminar/(?P<id_tipo_atributo>\d+)/$', eliminarTipoAtributo),

)