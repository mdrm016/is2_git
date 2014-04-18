from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect, HttpResponse
from django.template.context import RequestContext
from forms import FaseNuevaForm
from .models import Fases
from datetime import datetime

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
            fasenombre = Fases.objects.filter(nombre=busqueda, proyecto=id_proyecto, is_active='True')
            faseestado = Fases.objects.filter(estado=busqueda, proyecto=id_proyecto, is_active='True')
           # fasefechainicio = Fases.objects.filter(fechainicio=busqueda, proyecto=id_proyecto, is_active='True')
           # faseduracion = Fases.objects.filter(duracion=busqueda, proyecto=id_proyecto, is_active='True')
            
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
    listfases = Fases.objects.filter(proyecto=id_proyecto, is_active='True')
    template_name = './Fases/fases.html'
    return render(request, template_name, {'lista_fases': listfases})

def crear_fase(request, id_proyecto):
    """ Recibe un request, obtiene el formulario con los datos del usuario a crear
    o la solicitud de envio de dicho formulario. Luego verifica los datos recibidos
    y registra al nuevo usuario.  
    
    @type request: django.http.HttpRequest
    @param request: Contiene informacion sobre la solic. web actual que llamo a esta vista
    
    @rtype: django.http.HttpResponse
    @return: usuariocreado.html, mensaje de exito
    
    @author: Ysapy Ortiz
    
    """
    if request.method == 'POST':
        form = FaseNuevaForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['Nombre_de_Fase']
            descripcion = form.cleaned_data['Descripcion']
            duracion = form.cleaned_data['Duracion_semanas']
            
            fase = Fases()
            fase.nombre=nombre
            fase.descripcion=descripcion
            fase.estado='DF'
            fase.fechainicio= datetime.now()
            fase.duracion = duracion
            fase.proyecto_id = id_proyecto
            fase.is_active = 'True'
            fase.save()
      
            template_name='./Fases/fasecreada.html'
            return render(request, template_name, {'id_proyecto': id_proyecto})
    else: 
        form = FaseNuevaForm()    
        
    template_name='./Fases/fasenueva.html'
    return render(request, template_name, {'form': form})