from django.conf.urls import patterns, url
from .views import informes, acercaDe, informe_proyecto_pdf, informe_proyecto, informe_solicitudes_pdf, informe_solicitudes, informe_items_pdf, informe_items, seleccionar_proyecto

urlpatterns = patterns('',
                      url(r'^informes/$', informes),
                      url(r'^informes/acercade/$', acercaDe),
                      url(r'^informes/proyectos_pdf/$', informe_proyecto_pdf),
                      url(r'^informes/proyectos/$', informe_proyecto),
                      url(r'^informes/seleccionar_proyecto/$', seleccionar_proyecto),
                      url(r'^informes/seleccionar_proyecto/solicitudes/(?P<id_proyecto>\d+)/$', informe_solicitudes),
                      url(r'^informes/seleccionar_proyecto/solicitudes/(?P<id_proyecto>\d+)/solicitudes_pdf/$', informe_solicitudes_pdf), 
                      url(r'^informes/seleccionar_proyecto/items/(?P<id_proyecto>\d+)/$', informe_items),
                      url(r'^informes/seleccionar_proyecto/items/(?P<id_proyecto>\d+)/items_pdf/$', informe_items_pdf),
                       )
