
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings

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
    
    #""" Incluimos la urls.py de la aplicacion roles"""
    url(r'^', include('aplicaciones.roles.urls')),

    #""" Incluimos la urls.py de la aplicacion Proyectos"""
    url(r'^', include('aplicaciones.proyectos.urls')),
    
    #""" Incluimos la urls.py de la aplicacion Fases"""
    url(r'^', include('aplicaciones.fases.urls')),
    
    #""" Incluimos la urls.py de la aplicacion Items"""
    url(r'^', include('aplicaciones.items.urls')),
    
    #""" Incluimos la urls.py de la aplicacion tipoAtributo"""
    url(r'^', include('aplicaciones.tipoatributo.urls')),
    
     #""" Incluimos la urls.py de la aplicacion tipoitem"""
    url(r'^', include('aplicaciones.tipoitem.urls')),
    
     #""" Incluimos la urls.py de la aplicacion relaciones"""
    url(r'^', include('aplicaciones.relaciones.urls')),
    
    #""" Incluimos la urls.py de la aplicacion lineabase"""
    url(r'^', include('aplicaciones.lineabase.urls')),
    
    #""" Incluimos la urls.py de la aplicacion solicitudes"""
    url(r'^', include('aplicaciones.solicitudes.urls')),
    
    #""" Incluimos la urls.py de la aplicacion comite"""
    url(r'^', include('aplicaciones.comite.urls')),
    
    #""" Incluimos la urls.py de la aplicacion informes"""
    url(r'^', include('aplicaciones.informes.urls')),

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
