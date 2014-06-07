from django.conf.urls import patterns, url
from views import generarLineaBase, administrarLineaBase, consultar_lineabase, informe_lineabase, reactivarLineaBase

urlpatterns = patterns('',
                       url(r'^adm_proyectos/gestionar/(?P<id_proyecto>\d+)/adm_items/(?P<id_fase>\d+)/adm_lineas_base/$', administrarLineaBase),
                       url(r'^adm_proyectos/gestionar/(?P<id_proyecto>\d+)/adm_items/(?P<id_fase>\d+)/adm_lineas_base/nuevo/$', generarLineaBase),
                       url(r'^adm_proyectos/gestionar/(?P<id_proyecto>\d+)/adm_items/(?P<id_fase>\d+)/adm_lineas_base/consultar/(?P<id_lineabase>\d+)/$', consultar_lineabase),
                       url(r'^adm_proyectos/gestionar/(?P<id_proyecto>\d+)/adm_items/(?P<id_fase>\d+)/adm_lineas_base/informe_lineabase/(?P<id_lineabase>\d+)/$', informe_lineabase),
                       url(r'^adm_proyectos/gestionar/(?P<id_proyecto>\d+)/adm_items/(?P<id_fase>\d+)/adm_lineas_base/nuevo/reactivar_lineabase/(?P<id_lineabase>\d+)/$', reactivarLineaBase),
                       url(r'^adm_proyectos/gestionar/(?P<id_proyecto>\d+)/adm_items/(?P<id_fase>\d+)/adm_lineas_base/nuevo/consultar/(?P<id_lineabase>\d+)/$', consultar_lineabase),
                       )