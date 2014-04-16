from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect, HttpResponse
from django.template.context import RequestContext
from forms import FaseNuevaForm
from .models import Fases

# Create your views here.

def adm_fases(request, id_proyecto):
    
    error = False
    if 'busqueda' in request.GET:
        busqueda = request.GET['busqueda']
        if not busqueda:
            error = True
            template_name = './Fases/fases.html'
            return render(request, template_name, {'error':error})
        else:
            fasenombre = Fases.objects.filter(nombre=busqueda, proyecto=id_proyecto)
            faseestado = Fases.objects.filter(estado=busqueda, proyecto=id_proyecto)
            
            if (not fasenombre) & (not faseestado):
                error = True
                template_name = './Fases/fases.html'
                return render(request, template_name, {'error':error})
            else:
                fases=[]
                if (fasenombre):
                    fases.extend(fasenombre)
                if (faseestado):
                    fases.extend(faseestado)
                listfases = set(fases)
                template_name='./Fases/fases.html'
                return render(request, template_name, {'lista_fases': listfases, 'error':error})
    listfases = Fases.objects.filter(proyecto=id_proyecto)
    template_name = './Fases/fases.html'
    return render(request, template_name, {'lista_fases': listfases})