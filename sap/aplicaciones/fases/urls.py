from django.conf.urls import patterns, url
from .views import adm_fases, crear_fase

urlpatterns = patterns('',
                       url(r'^gestionar/(?P<id_proyecto>\d+)/$', adm_fases),
                       url(r'^gestionar/(?P<id_proyecto>\d+)/nuevo/$', crear_fase),
                       
                       )