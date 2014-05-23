from django.conf.urls import patterns, url
from .views import consultar_comite, agregar_miembro

urlpatterns = patterns('',
                       url(r'^adm_proyectos/gestionar/(?P<id_proyecto>\d+)/comite/$', consultar_comite),
                       url(r'^adm_proyectos/gestionar/(?P<id_proyecto>\d+)/comite/nuevo/$', agregar_miembro),
                       )
