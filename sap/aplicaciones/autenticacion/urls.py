from django.conf.urls import patterns, url
from .views import Autenticacion, login_view, logout_view

urlpatterns = patterns('',
    
    url(r'^login/$', login_view, name='login'), #""" Esta url redirecciona a la pagina del login """
    url(r'^cerrar/$', logout_view, name='logout'),  #""" Esta url activa la funcion de cierre de  sesion """
    url(r'^$', Autenticacion.as_view(), name='inicio'), #""" Esta url despliega la pagina de inicio """
)