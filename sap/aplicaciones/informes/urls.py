from django.conf.urls import patterns, url
from .views import informes, informe_proyecto_pdf, informe_proyecto

urlpatterns = patterns('',
                      url(r'^informes/$', informes),
                      url(r'^informes/proyectos_pdf/$', informe_proyecto_pdf),
                      url(r'^informes/proyectos/$', informe_proyecto),
                       )
