from django.conf.urls import patterns, url
from .views import adm_tipoitem, crear_tipoitem, eliminar_tipoitem, modificar_tipoitem, consultar_tipoitem

urlpatterns = patterns('',
                       
        url(r'^adm_proyectos/gestionar/(?P<id_proyecto>\d+)/adm_tipos_item/$', adm_tipoitem),
        url(r'^adm_proyectos/gestionar/(?P<id_proyecto>\d+)/adm_tipos_item/crear_tipoitem/$', crear_tipoitem),
        url(r'^adm_proyectos/gestionar/(?P<id_proyecto>\d+)/adm_tipos_item/modificar/(?P<id_tipoitem>.*)/$', modificar_tipoitem),
        url(r'^adm_proyectos/gestionar/(?P<id_proyecto>\d+)/adm_tipos_item/eliminar/(?P<id_tipoitem>.*)/$', eliminar_tipoitem),
        url(r'^adm_proyectos/gestionar/(?P<id_proyecto>\d+)/adm_tipos_item/consultar/(?P<id_tipoitem>.*)/$', consultar_tipoitem),

)