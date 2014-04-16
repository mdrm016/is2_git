from django.shortcuts import render_to_response, render
from django.template import RequestContext
from .forms import ProyectoNuevoForm, ProyectoModificadoForm
from .models import Proyectos
from django.contrib.auth.models import User

def crear_proyecto (request):
    if request.method == 'POST':
        form = ProyectoNuevoForm(request.POST)
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
    return render_to_response(template_name, ctx, context_instance=RequestContext(request))

def modificar_proyecto (request, id_usuario):
    proyecto = Proyectos.objects.get(id=id_usuario)
    mensaje=''
    if request.method == 'POST':
        form = ProyectoModificadoForm(request.POST)
        if form.is_valid():
            form.clean()
            nombreNuevo = form.cleaned_data['Nombre_del_Proyecto'] 
            lider =  form.cleaned_data['Nuevo_Lider']
            estado = form.cleaned_data['Nuevo_Estado']
            duracion =  form.cleaned_data['Duracion']
            
            #Si no se ha suministrado un nuevo lider, el proyecto se queda con el lider actual
            if not lider:
                lider = User.objects.get(username=proyecto.lider)
                lider = lider.id
            lideruser = User.objects.get(id=lider)
            
            if not estado:
                estado = proyecto.estado
            
            #si exite ya un proyecto con el nombre suministrado y el nombre suminitrado es distinto al del proyecto que esta siendo modificado
            # Comprobar con fases y miembros de comite para pasar a un estado en construccion con un elif
            if Proyectos.objects.filter(nombre=nombreNuevo) and nombreNuevo != proyecto.nombre:
                data ={'Nombre_del_Proyecto':nombreNuevo, 'Lider_Actual':lider, 'Duracion':duracion}  
                form = ProyectoModificadoForm(data)
                mensaje = 'El nombre del proyecto ya existe y no puede haber duplicados'
                
            else:
                if nombreNuevo == proyecto.nombre and  lideruser == proyecto.lider and estado == proyecto.estado and duracion == proyecto.duracion:
                      mensaje="Proyecto Guardado sin modificaciones"
                else:
                    proyecto.nombre=nombreNuevo
                    proyecto.lider=lideruser
                    proyecto.estado = estado
                    proyecto.duracion=duracion
                    proyecto.save()
                    mensaje="Proyecto modificado exitosamente"
                    
                ctx = {'mensaje':mensaje}
                template_name='proyectos/proyectoalerta.html'
                return render_to_response(template_name, ctx, context_instance=RequestContext(request))
    else:
        data ={'Nombre_del_Proyecto':proyecto.nombre, 'Lider_Actual':proyecto.lider, 'Estado_Actual':proyecto.estado, 'Duracion':proyecto.duracion}   
        form = ProyectoModificadoForm(data)
        
    ctx ={'form': form, 'mensaje':mensaje}      
    template_name='proyectos/modificarproyecto.html'
    return render_to_response(template_name, ctx, context_instance=RequestContext(request))

