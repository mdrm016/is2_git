from django.conf.urls import patterns, url
from .views import adm_tipoitem, crear_tipoitem, eliminar_tipoitem, modificar_tipoitem, consultar_tipoitem, gestionar_tipoitem, agregar_tipo_atributo, quitar_tipo_atributo, subir_tipo_atributo, bajar_tipo_atributo

urlpatterns = patterns('',
                       
        url(r'^adm_proyectos/gestionar/(?P<id_proyecto>\d+)/adm_tipos_item/$', adm_tipoitem),
        url(r'^adm_proyectos/gestionar/(?P<id_proyecto>\d+)/adm_tipos_item/crear_tipoitem/$', crear_tipoitem),
        url(r'^adm_proyectos/gestionar/(?P<id_proyecto>\d+)/adm_tipos_item/modificar/(?P<id_tipoitem>\d+)/$', modificar_tipoitem),
        url(r'^adm_proyectos/gestionar/(?P<id_proyecto>\d+)/adm_tipos_item/eliminar/(?P<id_tipoitem>\d+)/$', eliminar_tipoitem),
        url(r'^adm_proyectos/gestionar/(?P<id_proyecto>\d+)/adm_tipos_item/consultar/(?P<id_tipoitem>\d+)/$', consultar_tipoitem),
        url(r'^adm_proyectos/gestionar/(?P<id_proyecto>\d+)/adm_tipos_item/gestionar_tipoitem/(?P<id_tipoitem>\d+)/$', gestionar_tipoitem),
        url(r'^adm_proyectos/gestionar/(?P<id_proyecto>\d+)/adm_tipos_item/gestionar_tipoitem/(?P<id_tipoitem>\d+)/agregar_tipo_atributo/(?P<id_tipoatributo>\d+)/$', agregar_tipo_atributo),
        url(r'^adm_proyectos/gestionar/(?P<id_proyecto>\d+)/adm_tipos_item/gestionar_tipoitem/(?P<id_tipoitem>\d+)/quitar_tipo_atributo/(?P<id_tipoatributo>\d+)/$', quitar_tipo_atributo),
        url(r'^adm_proyectos/gestionar/(?P<id_proyecto>\d+)/adm_tipos_item/gestionar_tipoitem/(?P<id_tipoitem>\d+)/subir_tipo_atributo/(?P<id_tipoatributo>\d+)/$', subir_tipo_atributo),
        url(r'^adm_proyectos/gestionar/(?P<id_proyecto>\d+)/adm_tipos_item/gestionar_tipoitem/(?P<id_tipoitem>\d+)/bajar_tipo_atributo/(?P<id_tipoatributo>\d+)/$', bajar_tipo_atributo),

)