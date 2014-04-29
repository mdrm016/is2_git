from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect, HttpResponse
from django.template.context import RequestContext
from aplicaciones.proyectos.models import Proyectos
from datetime import datetime
from django.contrib.auth.decorators import login_required, permission_required
from django.db.models import Q

# Create your views here.

def adm_items(request, id_proyecto, id_fase):
    
    """ Recibe un request, se verifica cual es el usuario registrado y el proyecto del cual se solicita,
    se obtiene la lista de fases con las que estan relacionados el usuario y el proyecto 
    desplegandola en pantalla, ademas permite realizar busquedas avanzadas sobre
    las fases que puede mostrar.
    
    @type request: django.http.HttpRequest.
    @param request: Contiene informacion sobre la solicitud web actual que llamo a esta vista.
    
    @rtype: django.shortcuts.render_to_response.
    @return: fases.html, donde se listan las fases, ademas de las funcionalidades para cada fase.
    
    @author: Ysapy Ortiz.
    
    """
    lista_items=[]
    mensaje = 'Aun no hay items en la fase'
    ctx = {'lista_items': lista_items, 'mensaje': mensaje, 'id_proyecto':id_proyecto, 'id_fase': id_fase}
    template_name = './items/items.html'
    return render_to_response(template_name, ctx, context_instance=RequestContext(request))
