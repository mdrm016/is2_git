from django.conf.urls import patterns, url
from .views import logHoy, logAyer, logSemana1, logSemana2, logMas

urlpatterns = patterns('',
                      url(r'^logs/hoy/$', logHoy),
                      url(r'^logs/ayer/$', logAyer),
                      url(r'^logs/semana1/$', logSemana1),
                      url(r'^logs/semana2/$', logSemana2),
                      url(r'^logs/mas/$', logMas),
                       )
