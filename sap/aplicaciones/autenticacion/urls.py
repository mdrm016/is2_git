from django.conf.urls import patterns, url
from .views import Autenticacion, login_view, logout_view
from aplicaciones.proyectos.views import adm_proyectos

"""   
    La url "login/" redirecciona a la pagina del login
    La url "cerrar/" activa la funcion de cierre de  sesion
    La url "/" despliega la pagina de inicio

"""
urlpatterns = patterns('',
                       
    url(r'^$', Autenticacion.as_view(), name='inicio'),
    url(r'^login/$', login_view, name='login'),
    url(r'^cerrar/$', logout_view, name='logout'),
    url(r'^adm_proyectos/$', adm_proyectos),
)