from django.conf.urls import patterns, url
from .views import adm_fases

urlpatterns = patterns('',
                       url(r'^adm_proyectos/gestionar/(?P<id_proyecto>\d+)/$', adm_fases),
                       
                       )