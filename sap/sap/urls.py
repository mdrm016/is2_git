
from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sap.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

     url(r'^admin/', include(admin.site.urls)),
    
    #""" Incluimos la urls.py de la aplicacion Autenticacion """
    url(r'^', include('aplicaciones.autenticacion.urls')),
    
    #""" Incluimos la urls.py de la aplicacion usuarios"""
    url(r'^', include('aplicaciones.usuarios.urls')),


)
