from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect, HttpResponse
from django.template.context import RequestContext
from forms import FaseNuevaForm, FaseModificadaForm
from .models import Fases
from aplicaciones.proyectos.models import Proyectos
from datetime import datetime
from django.contrib.auth.decorators import login_required, permission_required
from django.db.models import Q

# Create your views here.
@login_required(login_url='/login/')
@permission_required('fases.administrar_fases',raise_exception=True)
def adm_fases(request, id_proyecto):
    
    fases = Fases.objects.filter(proyecto=id_proyecto, is_active=True)
    busqueda = ''
    error=False
    if 'busqueda' in request.GET:
        busqueda = request.GET.get('busqueda', '')
        if busqueda:
            qset = (
                Q(nombre__icontains=busqueda) |
                Q(estado__icontains=busqueda) |
                Q(fechainicio__icontains=busqueda) |
                Q(duracion__icontains=busqueda) 
            )
            fases= Fases.objects.filter(qset).distinct()
            if not fases:
                error = True
        
    ctx = {'lista_fases':fases, 'query':busqueda, 'error':error, 'id_proyecto':id_proyecto}
    template_name = './Fases/fases.html'
    return render_to_response(template_name, ctx, context_instance=RequestContext(request))
    """error = False
    if 'busqueda' in request.GET:
        busqueda = request.GET['busqueda']
        if not busqueda:
            error = True
            template_name = './Fases/fases.html'
            return render(request, template_name, {'error':error})
        else:
            fasenombre = Fases.objects.filter(nombre=busqueda, proyecto=id_proyecto, is_active=True)
            faseestado = Fases.objects.filter(estado=busqueda, proyecto=id_proyecto, is_active=True)
            
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
    listfases = Fases.objects.filter(proyecto=id_proyecto, is_active=True)
    template_name = './Fases/fases.html'
    return render(request, template_name, {'lista_fases': listfases})"""

@login_required(login_url='/login/')
@permission_required('fases.add_fases',raise_exception=True)
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
            fase.is_active = True
            fase.save()
      
            template_name='./Fases/fasecreada.html'
            return render(request, template_name, {'id_proyecto': id_proyecto})
    else: 
        form = FaseNuevaForm()    
        
    template_name='./Fases/fasenueva.html'
    return render(request, template_name, {'form': form, 'id_proyecto':id_proyecto})

@login_required(login_url='/login/')
def consultar_fase (request, id_fase, id_proyecto):
    fase = Fases.objects.get(id=id_fase, proyecto_id=id_proyecto)
    # conseguir el contexto de las fases y sus estados
    #fases = Fases.objects.filter(id_proyecto = id_proyecto)
    ctx = {'fase':fase}
    template_name = './Fases/consultarfase.html'
    return render(request, template_name, {'id_proyecto': id_proyecto, 'fase': fase, 'id_fase': id_fase})
    
@login_required(login_url='/login/')
@permission_required('fases.delete_fases',raise_exception=True)
def eliminar_fase (request, id_fase, id_proyecto):
    fase = Fases.objects.get(id=id_fase, proyecto_id=id_proyecto)
    if fase.estado != 'DF':
        mensaje = 'Imposible eliminar la fase, ya se esta trabajando en ella.'
        ctx = {'mensaje':mensaje, 'id_proyecto': id_proyecto}
        template_name = 'Fases/fasealerta.html'
        return render_to_response(template_name, ctx, context_instance=RequestContext(request))
    
    else:
        fase.is_active = False
        nom = fase.nombre
        fase.nombre_eliminado = fase.nombre
        fase.nombre = '/eliminado/'+fase.nombre_eliminado
        fase.save()
        template_name='./Fases/faseeliminada.html'
        return render(request, template_name, {'id_proyecto': id_proyecto})

@login_required(login_url='/login/')
@permission_required('fases.change_fases',raise_exception=True)
def modificar_fase (request, id_proyecto, id_fase):
    fase = Fases.objects.get(id=id_fase, proyecto_id=id_proyecto)
    mensaje=''
    if request.method == 'POST':
        form = FaseModificadaForm(request.POST)
        if form.is_valid():
            form.clean()
            nombreNuevo = form.cleaned_data['Nombre_de_Fase'] 
            descripcionNueva =  form.cleaned_data['Descripcion']
            estadoNuevo = form.cleaned_data['Estado']
            duracionNueva =  form.cleaned_data['Duracion']
            
            #Si no se ha suministrado un nuevo lider, el proyecto se queda con el lider actual
            if nombreNuevo:
                fase.nombre = nombreNuevo
            if descripcionNueva:
                fase.descripcion = descripcionNueva
            if duracionNueva:
                fase.duracion = duracionNueva
            if estadoNuevo:
                if (estadoNuevo=='DR') or (estadoNuevo=='FD'):
                    mensaje = 'No se puede modificar el estado sin items'
                    data ={'Nombre_de_Fase':fase.nombre, 'Descripcion':fase.descripcion, 'Estado':fase.estado, 'Duracion':fase.duracion}
                    form = FaseModificadaForm(data)
                    ctx ={'form': form, 'mensaje':mensaje, 'id_proyecto':id_proyecto, 'id_fase':id_fase}      
                    template_name='Fases/modificarfase.html'
                    return render_to_response(template_name, ctx, context_instance=RequestContext(request))
                else:
                    fase.estado = estadoNuevo
                    
            fase.save()
            mensaje="Proyecto modificado exitosamente"
                    
            ctx = {'mensaje':mensaje, 'id_proyecto': id_proyecto}
            template_name='Fases/fasealerta.html'
            return render_to_response(template_name, ctx, context_instance=RequestContext(request))
    else:
        data ={'Descripcion':fase.descripcion, 'Estado':fase.estado, 'Duracion':fase.duracion}   
        form = FaseModificadaForm(data)
        
    ctx ={'form': form, 'mensaje':mensaje, 'id_proyecto':id_proyecto, 'id_fase':id_fase}      
    template_name='Fases/modificarfase.html'
    return render_to_response(template_name, ctx, context_instance=RequestContext(request))

@login_required(login_url='/login/')
def abrir_proyectos (request, id_proyecto):
    
    """ Recibe un request, se verifica los permisos del usuario que desea importar un proyecto y luego se lo
redirige a la pagina donde se lista los proyectos del sistema que pueden ser importados.
@type request: django.http.HttpRequest.
@param request: Contiene informacion sobre la solicitud web actual que llamo a esta vista importar_proyecto.
@rtype: django.shortcuts.render_to_response.
@return: mportarproyecto.html, donde se encuentra la pagina que lista los proyectos a ser importados.
@author: Marcelo Denis
"""
    
    proyectos = Proyectos.objects.filter(is_active=True)
    ctx ={'lista_proyectos':proyectos, 'id_proyecto':id_proyecto}
    template_name = 'Fases/elegirproyecto.html'
    return render_to_response(template_name, ctx, context_instance=RequestContext(request))

@login_required(login_url='/login/')
def importar_fase (request, id_proyecto):
    
    """ Recibe un request, se verifica los permisos del usuario que desea importar un proyecto y luego se lo
redirige a la pagina donde se lista los proyectos del sistema que pueden ser importados.
@type request: django.http.HttpRequest.
@param request: Contiene informacion sobre la solicitud web actual que llamo a esta vista importar_proyecto.
@rtype: django.shortcuts.render_to_response.
@return: mportarproyecto.html, donde se encuentra la pagina que lista los proyectos a ser importados.
@author: Marcelo Denis
"""
   # id_import = int(id_importar)
    fases = Fases.objects.filter(is_active=True)
    ctx ={'lista_fases':fases}
    template_name = 'Fases/importarfase.html'
    return render_to_response(template_name, ctx, context_instance=RequestContext(request))


@login_required(login_url='/login/')
@permission_required('fases.importar_fases',raise_exception=True)
def importarf (request, id_proyecto, id_fase):
    
    """ Recibe un request y el id del proyecto a ser importado, se verifica si el usuario tiene
permisos para importar un proyecto existente, luego se lo redirige a la pagina para completar los
datos del formulario de nuevo proyecto importado, una vez completado correctamente el formulario el
sistema crea un nuevo proyecto con las caracteristicas del proyecto importado.
@type request: django.http.HttpRequest.
@param request: Contiene informacion sobre la solicitud web actual que llamo a esta vista importar.
@type id_usuario : string.
@param id_usuario : Contiene el id del proyecto a ser importado.
@rtype: django.shortcuts.render_to_response.
@return: crearproyectoimportado.html, donde se redirige al usuario para completar los datos del nuevo
proyecto importado o a proyectoalerta.html donde se notifica que el proyecto fue importado correctamente.
@author: Marcelo Denis.
"""
    
    faseImportada = Fases.objects.get(id=id_fase)
    if request.method == 'POST':
        form = FaseModificadaForm(request.POST)
        if form.is_valid():
            form.clean()
            nombre = form.cleaned_data['Nombre_de_Fase']
            descripcion = form.cleaned_data['Descripcion']
            duracion = form.cleaned_data['Duracion']
            
            fase = Fases()
            fase.nombre=nombre
            fase.descripcion=descripcion
            fase.estado='DF'
            fase.fechainicio= datetime.now()
            fase.duracion = duracion
            fase.proyecto_id = id_proyecto
            fase.is_active = True
            fase.save()
                
            mensaje="Fase importada exitosamente"
            ctx = {'mensaje':mensaje}
            return render_to_response('Fases/fasealerta.html',ctx, context_instance=RequestContext(request))
    else:
        data ={'Nombre_de_Fase':faseImportada.nombre, 'Descripcion':faseImportada.descripcion, 'Estado':faseImportada.estado, 'Duracion':faseImportada.duracion}   
        form = FaseModificadaForm(data)
        
    ctx ={'form': form, 'fase':faseImportada}
    template_name='Fases/crearfaseimportada.html'
    return render_to_response(template_name, ctx, context_instance=RequestContext(request))

