from django.shortcuts import render_to_response, render, HttpResponseRedirect
from django.template import RequestContext
from .forms import ProyectoNuevoForm, ProyectoModificadoForm
from .models import Proyectos
from django.contrib.auth.models import User
from django.db.models import Q
from aplicaciones.usuarios.models import Usuarios
from aplicaciones.fases.models import Fases
from django.contrib.auth.decorators import login_required


@login_required(login_url='/login/')
def adm_proyectos (request):
    
    """ Recibe un request, se verifica cual es el usuario registrado y se obtiene la lista de proyectos
    con los que esta relacionado desplegandolo en pantalla, ademas permite realizar busquedas avanzadas sobre
    los los proyectos que puede mostrar. Si el usuario es el administrador despliega todos los proyectos.
    
    @type request: django.http.HttpRequest.
    @param request: Contiene informacion sobre la solicitud web actual que llamo a esta vista adm_proyectos.
    
    @rtype: django.shortcuts.render_to_response.
    @return: index.html, donde se listan los proyectos, ademas de las funcionalidades para cada proyecto.
    
    @author: Marcelo Denis.
    
    """
    
    usuario = Usuarios.objects.get(user_id=request.user.id)
    if request.user.id != 1:
        proyectos = usuario.proyectos_set.all()
        lider = Proyectos.objects.filter(lider_id=request.user.id)
        miembros = proyectos | lider
        proyectos = miembros.distinct()

    else:
        proyectos = Proyectos.objects.filter(is_active=True)
        
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
            proyectos= proyectos.filter(qset).distinct()
            if not proyectos:
                error = True
        
    ctx = {'lista_proyectos':proyectos, 'query':busqueda, 'error':error}   
    template_name = 'index.html'
    return render_to_response(template_name, ctx, context_instance=RequestContext(request))

@login_required(login_url='/login/')
def crear_proyecto (request):
    
    """ Recibe un request, se verifica si el usuario tiene permisos para crear un proyecto 
    y se lo redirige a una pagina para que rellene el formulario de creacion de un proyecto,
    una vez completado de forma correcta dicho formulario el proyecto puede ser creado.
    
    @type request: django.http.HttpRequest.
    @param request: Contiene informacion sobre la solicitud web actual que llamo a esta vista crear_proyecto.
    
    @rtype: django.shortcuts.render_to_response.
    @return: crearproyecto.html, donde se encuentra el formulario de creacion de proyecto y luego a proyectoalerta.html
    donde se notifica la creacion correcta de un proyecto.
    
    @author: Marcelo Denis.
    
    """
    
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

@login_required(login_url='/login/')
def modificar_proyecto (request, id_proyecto):
    
    """ Recibe un request y el id del proyecto a ser modificado, se verifica si el usuario tiene
    permisos para modificar un proyecto existente y se lo redirige a una pagina para que modifique el 
    formulario existente de un proyecto, una vez modificado de forma correcta dicho formulario el proyecto
    puede ser modificado.
    
    @type request: django.http.HttpRequest.
    @param request: Contiene informacion sobre la solicitud web actual que llamo a esta vista crear_proyecto.
     
    @rtype: django.shortcuts.render_to_response.
    @return: modificarproyecto.html, donde se encuentra el formulario de modificacion de proyecto y luego a 
    proyectoalerta.html donde se notifica la modificacion correcta de un proyecto.
    
    @type id_usuario : string.
    @param id_usuario : Contiene el id del proyecto a ser modificado.
    
    @author: Marcelo Denis.
    
    """
    
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
            
            #Si no se ha suministrado un nuevo estado, el proyecto se queda con el estado actual
            if not estado:
                estado = proyecto.estado
            
            # Comprobar cantidad miembros de comite para pasar a un estado en construccion con un elif
            #si exite ya un proyecto con el nombre suministrado y el nombre suminitrado es distinto al del proyecto que esta siendo modificado
            if Proyectos.objects.filter(nombre=nombreNuevo) and nombreNuevo != proyecto.nombre:
                data ={'Nombre_del_Proyecto':nombreNuevo, 'Lider_Actual':lider, 'Duracion':duracion}  
                form = ProyectoModificadoForm(data)
                mensaje = 'El nombre del proyecto ya existe y no puede haber duplicados'
            
            else:
                if nombreNuevo == proyecto.nombre and  lideruser == proyecto.lider and estado == proyecto.estado and duracion == proyecto.duracion and not miembros:
                      mensaje="Proyecto guardado sin modificaciones"
                      
                elif estado == 'En Construccion' and not Fases.objects.filter(proyecto = id_proyecto):
                    mensaje="El proyecto no puede pasar a un estado En Construccion si aun no tiene fases"
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
        print proyecto.miembros.all()
        data ={'Nombre_del_Proyecto':proyecto.nombre, 'Lider_Actual':proyecto.lider, 'Estado_Actual':proyecto.estado, 'Duracion':proyecto.duracion}   
        form = ProyectoModificadoForm(data)
        
    ctx ={'form': form, 'mensaje':mensaje, 'proyecto':proyecto}      
    template_name='proyectos/modificarproyecto.html'
    return render_to_response(template_name, ctx, context_instance=RequestContext(request))

@login_required(login_url='/login/')
def consultar_proyecto (request, id_proyecto):
    
    """ Recibe un request y el id del proyecto a ser consultado, se verifica si el usuario tiene
    permisos para consultar un proyecto y se lo redirige a una pagina que despliega los datos del
    proyecto solicitado.
    
    @type request: django.http.HttpRequest.
    @param request: Contiene informacion sobre la solicitud web actual que llamo a esta vista consultar_proyecto.
     
    @rtype: django.shortcuts.render_to_response.
    @return: consultarproyecto.html, donde se encuentra la pagina de consulta de proyecto.
    
    @type id_usuario : string.
    @param id_usuario : Contiene el id del proyecto a ser consultado.
    
    @author: Marcelo Denis.
    
    """
    
    proyecto = Proyectos.objects.get(id=id_proyecto)
    fases = Fases.objects.filter(proyecto = id_proyecto)
    ctx = {'proyecto':proyecto, 'fases':fases}
    template_name = 'proyectos/consultarproyecto.html'
    return render_to_response(template_name, ctx, context_instance=RequestContext(request))

@login_required(login_url='/login/')
def eliminar_proyecto (request, id_proyecto):
    
    """ Recibe un request y el id del proyecto a ser eliminado, se verifica si el usuario tiene
    permisos para eliminar un proyecto existente y le brinda la opcion de eliminar elm proyecto.
    
    @type request: django.http.HttpRequest.
    @param request: Contiene informacion sobre la solicitud web actual que llamo a esta vista eliminar_proyecto.
     
    @rtype: django.shortcuts.render_to_response.
    @return: index.html, donde se redirige al usuario con actualizacion de la lista de proyectos o a
    proyectoalerta.html donde se notifica al usuario la razon por la cual no se puede eliminar un proyecto.
    
    @type id_usuario : string.
    @param id_usuario : Contiene el id del proyecto a ser eliminado.
    
    @author: Marcelo Denis.
    
    """
    
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

@login_required(login_url='/login/')      
def listar_miembros (request, id_proyecto):
    
    """ Recibe un request y el id del proyecto cuyos miembros se desea que se liste, se verifica
    los permisos del usuario solicitante y de procede a listar los miembros del proyecto en cuestion.
    
    @type request: django.http.HttpRequest.
    @param request: Contiene informacion sobre la solicitud web actual que llamo a esta vista listar_miembros
     
    @rtype: django.shortcuts.render_to_response.
    @return: listarmiembrosproyecto.html, donde se encuentra la pagina que lista los miembros de un proyecto.
    
    @type id_usuario : string.
    @param id_usuario : Contiene el id del proyecto cuyos miembros seran listados.
    
    @author: Marcelo Denis
    
    """
    
    proyecto = Proyectos.objects.get(id=id_proyecto)
    miembros = Proyectos.objects.get(id=id_proyecto).miembros.all()
    #obtener Roles.
    ctx ={'miembros':miembros, 'proyecto':proyecto}
    template_name = 'proyectos/listarmiembrosproyecto.html'
    return render_to_response(template_name, ctx, context_instance=RequestContext(request))

@login_required(login_url='/login/')
def importar_proyecto (request):
    
    """ Recibe un request, se verifica los permisos del usuario que desea importar un proyecto y luego se lo 
    redirige a la pagina donde se lista los proyectos del sistema que pueden ser importados.
    
    @type request: django.http.HttpRequest.
    @param request: Contiene informacion sobre la solicitud web actual que llamo a esta vista importar_proyecto.
     
    @rtype: django.shortcuts.render_to_response.
    @return: mportarproyecto.html, donde se encuentra la pagina que lista los proyectos a ser importados.
    
    @author: Marcelo Denis
    
    """
    
    proyectos = Proyectos.objects.filter(is_active=True)
    ctx ={'lista_proyectos':proyectos}
    template_name = 'proyectos/importarproyecto.html'
    return render_to_response(template_name, ctx, context_instance=RequestContext(request))

@login_required(login_url='/login/')
def importar (request, id_proyecto):
    
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
    
    proyectoImportado = Proyectos.objects.get(id=id_proyecto)
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
                
            fasesImportadas = Fases.objects.filter(proyecto=id_proyecto, is_active=True)     
            for faseImport in fasesImportadas:
                fase = Fases()
                fase.nombre = faseImport.nombre
                fase.estado = 'DF'
                fase.proyecto = proyecto
                fase.save()
                
            mensaje="Proyecto importado exitosamente"
            ctx = {'mensaje':mensaje}
            return render_to_response('proyectos/proyectoalerta.html',ctx, context_instance=RequestContext(request))
    else:    
        form = ProyectoNuevoForm()
        
    ctx ={'form': form, 'proyecto':proyectoImportado}      
    template_name='proyectos/crearproyectoimportado.html'
    return render_to_response(template_name, ctx, context_instance=RequestContext(request))
    