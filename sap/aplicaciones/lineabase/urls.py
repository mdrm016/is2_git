from django.conf.urls import patterns, url
from views import generarLineaBase, administrarLineaBase

urlpatterns = patterns('',
                       url(r'^adm_proyectos/gestionar/(?P<id_proyecto>\d+)/adm_items/(?P<id_fase>\d+)/adm_lineas_base/$', administrarLineaBase),
                       url(r'^adm_proyectos/gestionar/(?P<id_proyecto>\d+)/adm_items/(?P<id_fase>\d+)/adm_lineas_base/nuevo/$', generarLineaBase),
                       )