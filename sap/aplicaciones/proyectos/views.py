from django.shortcuts import render_to_response, render
from django.template import RequestContext
from .forms import ProyectoNuevoForm
from .models import Proyectos
from django.contrib.auth.models import User

def crear_proyecto (request):
    if request.method == 'POST':
        form = ProyectoNuevoForm(request.POST)
        print form.errors
        if form.is_valid():
            form.clean()
            nombre = form.cleaned_data['Nombre_del_Proyecto'] 
            lider =  form.cleaned_data['Lider']
            fecha_inicio = form.cleaned_data['Fecha_de_Inicio']
            duracion =  form.cleaned_data['Duracion']
            
            user = User.objects.get(id=lider)
            
            proyecto = Proyectos()
            proyecto.nombre=nombre
            proyecto.lider=user
            proyecto.fecha_inicio=fecha_inicio
            proyecto.duracion=duracion
            proyecto.is_active='True'
            proyecto.save()
            
            mensaje="Proyecto creado exitosamente"
            ctx = {'mensaje':mensaje}
            return render_to_response('proyectos/proyectoalerta.html',ctx, context_instance=RequestContext(request))
    else:    
        form = ProyectoNuevoForm()
        
    ctx ={'form': form}      
    template_name='proyectos/crearproyecto.html'
    #return render_to_response(template_name, ctx, context_instance=RequestContext(request))
    return render(request, template_name, {'form': form})
