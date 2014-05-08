from django.conf.urls import patterns, url
from .views import adm_fases, crear_fase, consultar_fase, eliminar_fase, modificar_fase, importar_fase, importarf, ordenar_fases, subir_fase, bajar_fase

urlpatterns = patterns('',
                       url(r'^adm_proyectos/gestionar/(?P<id_proyecto>\d+)/$', adm_fases),
                       url(r'^adm_proyectos/gestionar/(?P<id_proyecto>\d+)/nuevo/$', crear_fase),
                       url(r'^adm_proyectos/gestionar/(?P<id_proyecto>\d+)/ordenar_fases/$', ordenar_fases),
                       url(r'^adm_proyectos/gestionar/(?P<id_proyecto>\d+)/ordenar_fases/subir_fase/(?P<id_fase>\d+)/$', subir_fase),
                       url(r'^adm_proyectos/gestionar/(?P<id_proyecto>\d+)/ordenar_fases/bajar_fase/(?P<id_fase>\d+)/$', bajar_fase),
                       url(r'^adm_proyectos/gestionar/(?P<id_proyecto>\d+)/importar_fase/importarf/(?P<id_fase>\d+)/$', importarf),
                       url(r'^adm_proyectos/gestionar/(?P<id_proyecto>\d+)/importar_fase/$', importar_fase),
                       url(r'^adm_proyectos/gestionar/(?P<id_proyecto>\d+)/consultar/(?P<id_fase>\d+)/$', consultar_fase),
                       url(r'^adm_proyectos/gestionar/(?P<id_proyecto>\d+)/eliminar/(?P<id_fase>\d+)/$', eliminar_fase),
                       url(r'^adm_proyectos/gestionar/(?P<id_proyecto>\d+)/modificar/(?P<id_fase>\d+)/$', modificar_fase),


                       )
