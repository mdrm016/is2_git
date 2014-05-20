from django.conf.urls import patterns, url
from .views import crear_solicitud

urlpatterns = patterns('',
                       url(r'^adm_proyectos/gestionar/(?P<id_proyecto>\d+)/adm_items/(?P<id_fase>\d+)/solicitud/(?P<id_item>\d+)/$', crear_solicitud),
                       )
