from django.shortcuts import render_to_response, render, HttpResponseRedirect
from django.template import RequestContext
from .forms import ProyectoNuevoForm, ProyectoModificadoForm
from .models import Proyectos
from django.contrib.auth.models import User
from django.db.models import Q
from aplicaciones.usuarios.models import Usuarios

def adm_proyectos (request):
    
    busqueda = ''
    error=False
    if 'busqueda' in request.GET:
        busqueda = request.GET.get('busqueda', '')
        if busqueda:
            qset = (
                Q(nombre__icontains=busqueda) |
                Q(lider__username__icontains=busqueda) |
                Q(estado__icontains=busqueda) |
                Q(fecha_inicio__icontains=busqueda) |
                Q(duracion__icontains=busqueda) 
            )
            proyectos = Proyectos.objects.filter(qset).distinct()
            if not proyectos:
                error = True
        else:
            proyectos = Proyectos.objects.all()
    else:
        proyectos = Proyectos.objects.all()
        
    ctx = {'lista_proyectos':proyectos, 'query':busqueda, 'error':error}   
    template_name = 'index.html'
    return render_to_response(template_name, ctx, context_instance=RequestContext(request))

def crear_proyecto (request):
    if request.method == 'POST':
        form = ProyectoNuevoForm(request.POST)
        if form.is_valid():
            form.clean()
            nombre = form.cleaned_data['Nombre_del_Proyecto'] 
            lider =  form.cleaned_data['Lider']
            fecha_inicio = form.cleaned_data['Fecha_de_Inicio']
            duracion =  form.cleaned_data['Duracion']
            miembros = form.cleaned_data['Miembros']
            
            user = User.objects.get(id=lider)
            
            proyecto = Proyectos()
            proyecto.nombre=nombre
            proyecto.lider=user
            proyecto.fecha_inicio=fecha_inicio
            proyecto.duracion=duracion
            proyecto.is_active='True'
            proyecto.save()
            
            for miembro_id in miembros:
                miembro = Usuarios.objects.get(user_id=miembro_id)
                proyecto.miembros.add(miembro)
            
            mensaje="Proyecto creado exitosamente"
            ctx = {'mensaje':mensaje}
            return render_to_response('proyectos/proyectoalerta.html',ctx, context_instance=RequestContext(request))
    else:    
        form = ProyectoNuevoForm()
        
    ctx ={'form': form}      
    template_name='proyectos/crearproyecto.html'
    return render_to_response(template_name, ctx, context_instance=RequestContext(request))

def modificar_proyecto (request, id_proyecto):
    proyecto = Proyectos.objects.get(id=id_proyecto)
    mensaje=''
    if request.method == 'POST':
        form = ProyectoModificadoForm(request.POST)
        if form.is_valid():
            form.clean()
            nombreNuevo = form.cleaned_data['Nombre_del_Proyecto'] 
            lider =  form.cleaned_data['Nuevo_Lider']
            estado = form.cleaned_data['Nuevo_Estado']
            duracion =  form.cleaned_data['Duracion']
            miembros = form.cleaned_data['Cambio_de_Miembros']
            
            #Si no se ha suministrado un nuevo lider, el proyecto se queda con el lider actual
            if not lider:
                lider = User.objects.get(username=proyecto.lider)
                lider = lider.id
            lideruser = User.objects.get(id=lider)
            
            if not estado:
                estado = proyecto.estado
            
            print miembros
            print proyecto.miembros
            #si exite ya un proyecto con el nombre suministrado y el nombre suminitrado es distinto al del proyecto que esta siendo modificado
            # Comprobar con fases y miembros de comite para pasar a un estado en construccion con un elif
            if Proyectos.objects.filter(nombre=nombreNuevo) and nombreNuevo != proyecto.nombre:
                data ={'Nombre_del_Proyecto':nombreNuevo, 'Lider_Actual':lider, 'Duracion':duracion}  
                form = ProyectoModificadoForm(data)
                mensaje = 'El nombre del proyecto ya existe y no puede haber duplicados'
            
            else:
                if nombreNuevo == proyecto.nombre and  lideruser == proyecto.lider and estado == proyecto.estado and duracion == proyecto.duracion and not miembros:
                      mensaje="Proyecto Guardado sin modificaciones"
                else:
                    proyecto.nombre=nombreNuevo
                    proyecto.lider=lideruser
                    proyecto.estado = estado
                    proyecto.duracion=duracion
                    proyecto.save()
                    
                    proyecto.miembros.clear()
                    for miembro_id in miembros:
                        miembro = Usuarios.objects.get(user_id=miembro_id)
                        proyecto.miembros.add(miembro)
                        
                    mensaje="Proyecto modificado exitosamente"
                    
                ctx = {'mensaje':mensaje}
                template_name='proyectos/proyectoalerta.html'
                return render_to_response(template_name, ctx, context_instance=RequestContext(request))
    else:
        data ={'Nombre_del_Proyecto':proyecto.nombre, 'Lider_Actual':proyecto.lider, 'Estado_Actual':proyecto.estado, 'Duracion':proyecto.duracion, 'Miembros_Actuales': proyecto.miembros.all()}   
        form = ProyectoModificadoForm(data)
        
    ctx ={'form': form, 'mensaje':mensaje, 'proyecto':proyecto}      
    template_name='proyectos/modificarproyecto.html'
    return render_to_response(template_name, ctx, context_instance=RequestContext(request))

def consultar_proyecto (request, id_proyecto):
    proyecto = Proyectos.objects.get(id=id_proyecto)
    # conseguir el contexto de las fases y sus estados
    #fases = Fases.objects.filter(id_proyecto = id_proyecto)
    ctx = {'proyecto':proyecto}
    template_name = 'proyectos/consultarproyecto.html'
    return render_to_response(template_name, ctx, context_instance=RequestContext(request))

def eliminar_proyecto (request, id_proyecto):
    proyecto = Proyectos.objects.get(id=id_proyecto)
    if proyecto.estado == 'Finalizado':
        mensaje = 'Imposible eliminar un proyecto con estado finalizado.'
        ctx = {'mensaje':mensaje}
        template_name = 'proyectos/proyectoalerta.html'
        return render_to_response(template_name, ctx, context_instance=RequestContext(request))
    
    else:
        proyecto.is_active = False
        proyecto.save()
        return HttpResponseRedirect('/')
        
def listar_miembros (request, id_proyecto):
    #obtener Roles.
    proyecto = Proyectos.objects.get(id=id_proyecto)
    miembros = Proyectos.objects.get(id=id_proyecto).miembros.all()
    print miembros
    ctx ={'miembros':miembros, 'proyecto':proyecto}
    template_name = 'proyectos/listarmiembrosproyecto.html'
    return render_to_response(template_name, ctx, context_instance=RequestContext(request))
    