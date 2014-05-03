from django.shortcuts import render_to_response, render, HttpResponseRedirect
from django.template import RequestContext
from .forms import ProyectoNuevoForm, ProyectoModificadoForm
from .models import Proyectos
from django.contrib.auth.models import User
from django.db.models import Q
from aplicaciones.usuarios.models import Usuarios
from aplicaciones.fases.models import Fases
from django.contrib.auth.decorators import login_required, permission_required
from aplicaciones.roles.models import Roles
from aplicaciones.tipoitem.models import TipoItem, ListaAtributo
from aplicaciones.tipoitem.views import ordenar_mantener


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
    
    if request.user.id != 1:
        id_p=[]
        usuario = User.objects.get(id=request.user.id)
        rolesUsuario=usuario.groups.all()
        roles = Roles.objects.all()
        for rls in roles:
            for ru in rolesUsuario:
                if rls.name == ru.name and rls.proyecto:
                    id_p.append(rls.proyecto)
        proyectos = Proyectos.objects.filter(pk__in=id_p, is_active=True)

    else:
        proyectos = Proyectos.objects.filter(is_active=True)
        
    qset=(Q(estado__icontains='Inactivo') | Q(estado__icontains='En Construccion') )
    proyectos= proyectos.filter(qset).distinct()
        
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
@permission_required('proyectos.consultar_proyectosfinalizados',raise_exception=True)
def proyecto_finalizado (request):
    
    """ Recibe un request, se verifica cual es el usuario registrado y se obtiene la lista de proyectos finalizados
    con los que esta relacionado desplegandolo en pantalla, ademas permite realizar busquedas avanzadas sobre
    los los proyectos que puede mostrar. Si el usuario es el administrador despliega todos los proyectos.
    
    @type request: django.http.HttpRequest.
    @param request: Contiene informacion sobre la solicitud web actual que llamo a esta vista adm_proyectos.
    
    @rtype: django.shortcuts.render_to_response.
    @return: index.html, donde se listan los proyectos, ademas de las funcionalidades para cada proyecto.
    
    @author: Marcelo Denis.
    
    """
    if request.user.id != 1:
        id_p=[]
        usuario = User.objects.get(id=request.user.id)
        rolesUsuario=usuario.groups.all()
        roles = Roles.objects.all()
        for rls in roles:
            for ru in rolesUsuario:
                if rls.name == ru.name:
                    id_p.append(rls.proyecto)
        proyectos = Proyectos.objects.filter(pk__in=id_p, is_active=True, estado='Finalizado')

    else:
        proyectos = Proyectos.objects.filter(is_active=True, estado='Finalizado')
        
    proyectos= proyectos.distinct()
    
    busqueda = ''
    error=False
    if 'busqueda' in request.GET:
        busqueda = request.GET.get('busqueda', '')
        if busqueda:
            qset = (
                Q(nombre__icontains=busqueda) |
                Q(lider__username__icontains=busqueda) |
                Q(fecha_inicio__icontains=busqueda) |
                Q(duracion__icontains=busqueda) 
            )
            proyectos= proyectos.filter(qset).distinct()
            if not proyectos:
                error = True
    
    ctx = {'lista_proyectos':proyectos, 'query':busqueda, 'error':error}
    template_name = 'proyectos/proyectofinalizado.html'
    return render_to_response(template_name, ctx, context_instance=RequestContext(request))

@login_required(login_url='/login/')
@permission_required('proyectos.crear_proyectos',raise_exception=True)
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
            #lider =  form.cleaned_data['Lider']
            fecha_inicio = form.cleaned_data['Fecha_de_Inicio']
            duracion =  form.cleaned_data['Duracion']
            
            #user = User.objects.get(id=lider)
            
            proyecto = Proyectos()
            proyecto.nombre=nombre
            #proyecto.lider=request.user
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

@login_required(login_url='/login/')
@permission_required('proyectos.modificar_proyectos',raise_exception=True)
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
    mensaje=''
    lista=[]      
    roles = Roles.objects.filter(proyecto=id_proyecto)
    users = User.objects.filter(is_active=True).exclude(id=1)
    for rol in roles:
        for user in users:
            roles_usuario=user.groups.all()
            for ru in roles_usuario:
                if ru.name == rol.name:
                    tupla=(user.id, user.username)
                    lista.append(tupla)
    choices_lider=[]
    if not lista:
        mensaje='No existen opciones de lider para este proyecto'
    for eleccion in lista:
        if eleccion not in choices_lider:
            choices_lider.append(eleccion)
     
    ESTADOS_PROYECTO = (
        ('Inactivo', 'Inactivo'),
        ('En Construccion', 'En Construccion'),
        ('Finalizado', 'Finalizado'),
    )
     
    proyecto = Proyectos.objects.get(id=id_proyecto)
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
                if proyecto.lider:
                    lideruser = User.objects.get(username=proyecto.lider)
                else:
                    lideruser = None
            else:
                lideruser = User.objects.get(id=lider)
            #lideruser = User.objects.get(id=lider)
            
            #Si no se ha suministrado un nuevo estado, el proyecto se queda con el estado actual
            if not estado:
                estado = proyecto.estado
            
            # Comprobar cantidad miembros de comite para pasar a un estado en construccion con un elif
            #si exite ya un proyecto con el nombre suministrado y el nombre suminitrado es distinto al del proyecto que esta siendo modificado
            if Proyectos.objects.filter(nombre=nombreNuevo) and nombreNuevo != proyecto.nombre:  
                form = ProyectoModificadoForm()
                mensaje = 'El nombre del proyecto ya existe y no puede haber duplicados'
            
            else:
                if nombreNuevo == proyecto.nombre and  lideruser == proyecto.lider and estado == proyecto.estado and duracion == proyecto.duracion:
                      mensaje="Proyecto guardado sin modificaciones"
                      
                elif estado == 'En Construccion' and not Fases.objects.filter(proyecto = id_proyecto):
                    mensaje="El proyecto no puede pasar a un estado En Construccion si aun no tiene fases"
                    
                elif not lider and proyecto.lider == None:
                    mensaje="El proyecto no puede pasar a un estado En Construccion si aun no tiene un lider"
                    
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
        form = ProyectoModificadoForm()
        
    ctx ={'form': form, 'mensaje':mensaje, 'proyecto':proyecto, 'choices_lider':choices_lider, 'ESTADOS_PROYECTO':ESTADOS_PROYECTO}      
    template_name='proyectos/modificarproyecto.html'
    return render_to_response(template_name, ctx, context_instance=RequestContext(request))

@login_required(login_url='/login/')
@permission_required('proyectos.consultar_proyectos',raise_exception=True)
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
@permission_required('proyectos.eliminar_proyectos',raise_exception=True)
def eliminar_proyecto (request, id_proyecto):
    
    """ Recibe un request y el id del proyecto a ser eliminado, se verifica si el usuario tiene
    permisos para eliminar un proyecto existente y le brinda la opcion de eliminar el proyecto.
    
    @type request: django.http.HttpRequest.
    @param request: Contiene informacion sobre la solicitud web actual que llamo a esta vista eliminar_proyecto.
     
    @rtype: django.shortcuts.render_to_response.
    @return: index.html, donde se redirige al usuario con la actualizacion de la lista de proyectos o a
    proyectoalerta.html donde se notifica al usuario la razon por la cual no se puede eliminar un proyecto.
    
    @type id_usuario : string.
    @param id_usuario : Contiene el id del proyecto a ser eliminado.
    
    @author: Marcelo Denis.
    
    """
    
    proyecto = Proyectos.objects.get(id=id_proyecto)
    if proyecto.estado != 'Inactivo':
        if proyecto.estado == 'En Construccion':
            mensaje = 'Imposible eliminar un proyecto Inicializado.'
        else:
            mensaje = 'Imposible eliminar un proyecto con estado finalizado.'
            
        ctx = {'mensaje':mensaje}
        template_name = 'proyectos/proyectoalerta.html'
        return render_to_response(template_name, ctx, context_instance=RequestContext(request))
    
    else:
        proyecto.is_active = False
        proyecto.save()
        return HttpResponseRedirect('/')

@login_required(login_url='/login/')      
@permission_required('proyectos.listar_miembros',raise_exception=True)
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
    
    """proyecto = Proyectos.objects.get(id=id_proyecto)
    miembros = Proyectos.objects.get(id=id_proyecto).miembros.all()
    user_rol={}
    for miembro in miembros:
        usuario = User.objects.get(username=miembro)
        rolesmiembro = usuario.groups.all()
        lista = []
        for rol in rolesmiembro:
            lista.append(rol)
        user_rol[usuario.id]= lista"""
    
    
    users = User.objects.all()
    proyecto = Proyectos.objects.get(id=id_proyecto)
    rolesProyecto = Roles.objects.filter(proyecto=id_proyecto)
    
    #conseguimos la lista de usuarios que tienen un rol en el proyecto
    lista = []
    roluser=[]
    for user in users:
        if user.is_active:
            rols = user.groups.all()
            for rol in rols:
                for roluser in rolesProyecto:
                    if rol.name == roluser.name:
                        lista.append(user)
                        
    #eliminamos los usuarios duplicados si existen
    listamiembro = []                    
    for lis in lista:
        if lis not in listamiembro:
            listamiembro.append(lis)
            
    #Armamos una lista de tuplas de usuario con sus roles en el proyecto
    lista=[]
    for miembro in listamiembro:
        rls=[]
        roles = miembro.groups.all()
        for r in roles:
            for rp in rolesProyecto:
                if r.name == rp.name:
                    rls.append(rp)
        tupla = (miembro, rls)
        lista.append(tupla)                       
        
    ctx ={'miembros':lista, 'proyecto':proyecto}
    template_name = 'proyectos/listarmiembrosproyecto.html'
    return render_to_response(template_name, ctx, context_instance=RequestContext(request))

@login_required(login_url='/login/')
@permission_required('proyectos.importar_proyectos',raise_exception=True)
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
            fecha_inicio = form.cleaned_data['Fecha_de_Inicio']
            duracion =  form.cleaned_data['Duracion']
            
            proyecto = Proyectos()
            proyecto.nombre=nombre
            proyecto.lider=None
            proyecto.fecha_inicio=fecha_inicio
            proyecto.duracion=duracion
            proyecto.is_active='True'
            proyecto.save()
                
            fasesImportadas = Fases.objects.filter(proyecto=id_proyecto, is_active=True)     
            for faseImport in fasesImportadas:
                fase = Fases()
                fase.nombre = faseImport.nombre
                fase.estado = 'DF'
                fase.proyecto = proyecto
                fase.save()
                
            tipoitems=TipoItem.objects.filter(id_proyecto=id_proyecto, is_active=True)
            for tipoitem in tipoitems:
                TI= TipoItem()
                TI.nombre=tipoitem.nombre
                TI.descripcion=tipoitem.descripcion
                TI.id_proyecto=proyecto.id
                TI.is_active='True'
                TI.save()
                    
                elementos_existentes = ordenar_mantener(tipoitem.id)
                for elemento in elementos_existentes:
                    lista_atributo = ListaAtributo()
                    lista_atributo.id_atributo = elemento.id
                    lista_atributo.id_tipoitem = TI.id
                    lista_atributo.nombre = elemento.nombre
                    lista_atributo.is_active = True
                    
                    elementos = ordenar_mantener(TI.id)
                    if elementos:
                        lista_atributo.orden = len(elementos_existentes) + 1
                    else:
                        lista_atributo.orden = 1
                    lista_atributo.save()
                        
                    TI.listaAtributo.add(lista_atributo)
            
            mensaje="Proyecto importado exitosamente"
            ctx = {'mensaje':mensaje}
            return render_to_response('proyectos/proyectoalerta.html',ctx, context_instance=RequestContext(request))
    else:   
        form = ProyectoNuevoForm()
        
    ctx ={'form': form, 'proyecto':proyectoImportado}      
    template_name='proyectos/crearproyectoimportado.html'
    return render_to_response(template_name, ctx, context_instance=RequestContext(request))
    
