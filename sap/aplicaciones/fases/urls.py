from django.conf.urls import patterns, url
from .views import adm_fases, crear_fase, consultar_fase, eliminar_fase, modificar_fase, importar_fase, importarf

urlpatterns = patterns('',
                       url(r'^adm_proyectos/gestionar/(?P<id_proyecto>\d+)/$', adm_fases),
                       url(r'^adm_proyectos/gestionar/(?P<id_proyecto>\d+)/nuevo/$', crear_fase),
                      # url(r'^adm_proyectos/gestionar/(?P<id_proyecto>\d+)/abrir_proyecto/$', abrir_proyectos),
                       #url(r'^adm_proyectos/gestionar/(?P<id_proyecto>\d+)/abrir_proyecto/importar_fase/importarf/(?P<id_fase>.*)/$', importarf),
                       url(r'^adm_proyectos/gestionar/(?P<id_proyecto>\d+)/importar_fase/importarf/(?P<id_fase>.*)/$', importarf),
                       #url(r'^adm_proyectos/gestionar/(?P<id_proyecto>\d+)/abrir_proyecto/importar_fase/(?P<id_proyectoimportado>.*)/$', importar_fase),
                       url(r'^adm_proyectos/gestionar/(?P<id_proyecto>\d+)/importar_fase/$', importar_fase),
                       url(r'^adm_proyectos/gestionar/(?P<id_proyecto>\d+)/consultar/(?P<id_fase>\d+)/$', consultar_fase),
                       url(r'^adm_proyectos/gestionar/(?P<id_proyecto>.*)/eliminar/(?P<id_fase>.*)/$', eliminar_fase),
                       url(r'^adm_proyectos/gestionar/(?P<id_proyecto>.*)/modificar/(?P<id_fase>.*)/$', modificar_fase),
                       
                       )