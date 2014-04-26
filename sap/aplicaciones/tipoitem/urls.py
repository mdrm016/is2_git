from django.conf.urls import patterns, url
from .views import adm_tipoitem, crear_tipoitem, eliminar_tipoitem, modificar_tipoitem, consultar_tipoitem

urlpatterns = patterns('',
                       
        url(r'^adm_tipoitem/$', adm_tipoitem),
        url(r'^adm_tipoitem/crear_tipoitem/$', crear_tipoitem),
        url(r'^adm_tipoitem/modificar/(?P<id_tipoitem>.*)/$', modificar_tipoitem),
        url(r'^adm_tipoitem/eliminar/(?P<id_tipoitem>.*)/$', eliminar_tipoitem),
        url(r'^adm_tipoitem/consultar/(?P<id_tipoitem>.*)/$', consultar_tipoitem),

)