from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required
from models import Roles
from aplicaciones.proyectos.models import Proyectos
from django.contrib.auth.models import Group, Permission, User
from forms import RolForm, RolModificadoForm
from django.http import HttpResponseRedirect
# Create your views here.

@login_required(login_url='/login/')
def administrarRoles(request):
    """ Recibe un request, obtiene la lista de todos los Roles del sistema y 
    luego retorna el html renderizado con la lista de usuarios 
    @type request: django.http.HttpRequest
    @param request: Contiene informacion sobre la solic. web actual que llamo a esta vista
    
    @rtype: django.http.HttpResponse
    @return: usuarios.html, donde se listan los Roles, ademas de las funcionalidades para un Rol
    
    @author: eduardo gimenez
    
    """
    error = False
    usuario_logueado = User.objects.get(username=request.user.username)
    mis_roles = usuario_logueado.groups.all()
    if 'busqueda' in request.GET:
        busqueda = request.GET['busqueda']
        if not busqueda:
            error = True
            template_name= './Roles/roles.html'
            return render(request, template_name, {'error': error})
        else:
            rolname =   Roles.objects.filter(name=busqueda)
            if not rolname:
                error = True
                template_name= './Roles/roles.html'
                return render(request, template_name, {'error': error})
            else:
                rol=[]
                if rolname:
                    rol.extend(rolname)
                roles = set(rol)
                template_name='./Roles/roles.html'
                return render(request, template_name, {'lista_roles': roles, 'mis_roles':mis_roles, 'error': error})
    
    roles = []
    if request.user.has_perm('roles.administrar_roles'):
        roles = Roles.objects.filter(is_active=True)
    
    template_name='./Roles/roles.html'
    return render(request, template_name, {'lista_roles': roles, 'mis_roles': mis_roles})
    
@login_required(login_url='/login/')
@permission_required('roles.add_roles',raise_exception=True)
def rolNuevo(request):
    """ Recibe un request, obtiene el formulario con los datos del rol a crear
    o la solicitud de envio de dicho formulario. Luego verifica los datos recibidos
    y registra el nuevo rol.  
    
    @type request: django.http.HttpRequest
    @param request: Contiene informacion sobre la solic. web actual que llamo a esta vista
    
    @rtype: django.http.HttpResponse
    @return: rolcreado.html, mensaje de exito
    
    @author: Eduardo Gimenez
    
    """
    if request.method == 'POST':
        form = RolForm(request.POST)
        if form.is_valid():
            form.clean()
            nombreRol = form.cleaned_data['Nombre_de_Rol']
            permisos = form.cleaned_data['Permisos']
            proyecto = form.cleaned_data['Proyecto']
            descripcion = form.cleaned_data['Descripcion']
            
            rol = Roles.objects.create(name = nombreRol)
            for permiso in permisos:
                rol.permissions.add(Permission.objects.get(codename=permiso))
            
            p = proyecto
            if proyecto:
                try:
                    p = Proyectos.objects.get(id=proyecto)
                except Roles.DoesNotExist:
                   p = ''
                 
            rol.proyecto = p
            rol.descripcion = descripcion
            rol.save()
                    
            template_name='./Roles/rolcreado.html'
            return render(request, template_name)
    else:
        form = RolForm()
        
    template_name='./Roles/rolnuevo.html'
    return render(request, template_name, {'form': form})

@login_required(login_url='/login/')
@permission_required('roles.change_roles',raise_exception=True)
def modificarRol(request, id_rol):
    """ Busca en la base de datos el Rol cuyos datos se quieren modificar.
    Presenta esos datos en un formulario y luego se guardan los cambios realizados.
    Con la posibilidad de que el usuario cancele la operacion
     
    @type request: django.http.HttpRequest
    @param request: Contiene informacion sobre la solic. web actual que llamo a esta vista
    
    @type id_rol: integer
    @param id_rol: es el id del rol cuyos datos se quieren modificar
    
    @rtype: django.HttpResponse
    @return: modificar_rol.html,un formulario donde se despliegan los datos que el usuario puede modificar ,usuario_modificado.html, donde se notifica al usuario el exito de la operacion 
    
    @author: eduardo gimenez"""
    rol = Roles.objects.get(id=id_rol)
    if request.method == 'POST':
        form = RolModificadoForm(request.POST)
        if form.is_valid():
            form.clean()
            nombreRol = form.cleaned_data['Nombre_de_Rol']
            permisos = form.cleaned_data['Permisos']
            descripcion = form.cleaned_data['Descripcion']
            
            rol.name = nombreRol
            if permisos:
                for permiso in permisos:
                    rol.permissions.add(Permission.objects.get(codename=permiso))
            
            rol.descripcion = descripcion
            rol.save()
                    
            template_name='./Roles/rol_modificado.html'
            return render(request, template_name)
    else:
        data = {'Nombre_de_Rol': rol.name, 'Descripcion': rol.descripcion}
        form = RolModificadoForm(data)
        
    template_name='./Roles/modificar_rol.html'
    return render(request, template_name, {'form': form})

@login_required(login_url='/login/')
@permission_required('roles.delete_roles',raise_exception=True)
def eliminarRol(request, id_rol):
    """ Eliminar de manera logica los registros del rol.Tambien elimina la relacion entre 
    los usuarios que posees este rol.
        
    @type request: django.http.HttpRequest
    @param request: Contiene informacion sobre la solicitud web actual que llamo a esta vista
        
    @type id_usuario : string
    @param id_usuario : Contiene el id del rol a ser eliminado.
        
    @rtype: django.shortcuts.render_to_response
    @return: Se retorna al la administracion de Roles o se manda a la pagina de notificacion
        
    @author: Eduardo Gimenez"""
    
    rol = Roles.objects.get(id=id_rol)
    rol.is_active = False
    rol.save()
    grupos = Group.objects.filter(name=rol.name)
    if grupos:
        for grupo in grupos:
            grupo.delete()
    
    return HttpResponseRedirect('/adm_roles/')

@login_required(login_url='/login/')
def consultarRol(request, id_rol):
    """ Busca en la base de datos al Rol cuyos datos se quieren consultar, 
    los presenta en un html con la disponibilidad de regresar a la pagina anterior 
    @type request: django.http.HttpRequest
    @param request: Contiene informacion sobre la solic. web actual que llamo a esta vista
    
    @type id_rol: integer
    @param id_rol: es el id del Rol cuyos datos se quieren consultar
    
    @rtype: django.HttpResponse
    @return: consultar_rol.html, donde se le despliega al usuario los datos
    
    @author: eduardo gimenez"""
    template_name='./Roles/consultar_rol.html'
    rol = Roles.objects.get(id = id_rol)
    este_rol = rol
    permisos = rol.permissions.all()
    usuarios_con_rol = []
    usuarios_activos = User.objects.filter(is_active=True)
    for usuario in usuarios_activos:
        roles = usuario.groups.all()
        if roles:
            for rol in roles:
                if rol.name == este_rol.name:
                    usuarios_con_rol.append(usuario)
    return render(request, template_name, {'rol' : rol, 'permisos':permisos, 'usuarios': usuarios_con_rol}) 

@login_required(login_url='/login/')
@permission_required('roles.asignar_rol',raise_exception=True)
def asignarRol(request, id_rol):
    """ Asigna un Rol a un usuario, desplegando los usuarios que no posean este Rol
    
    @type request: django.http.HttpRequest
    @param request: Contiene informacion sobre la solic. web actual que llamo a esta vista
    
    @type id_rol: integer
    @param id_rol: es el id del Rol el cual se quiera asignar a un usuario
    
    @rtype: django.HttpResponse
    @return: asignar_rol.html, donde se despliega un formulario con los usuarios que aun no poseen el rol
    
    @author: Eduardo Gimenez"""
    errors = []
    if request.method == 'POST':
        eleccion = request.POST.get('Usuario', '')
        if not eleccion:
            errors.append('Debe seleccionar un usuario')
        elif not User.objects.filter(username=eleccion):
            errors.append('El usuario no existe, por favor escoja un usuario de la lista')
        if not errors:
            eleccion_rol = Roles.objects.get(id=id_rol)
            usuario_elegido  = User.objects.get(username=eleccion)
            usuario_elegido.groups.add(eleccion_rol)
            
            return render(request, './Roles/rol_asignado.html')
    
    usuarios_sin_rol = []
    este_rol = Roles.objects.get(id = id_rol)
    usuarios_activos = User.objects.filter(is_active=True)
    for usuario in usuarios_activos:
        roles = usuario.groups.all()
        if roles:
            for rol in roles:
                if rol.name != este_rol.name:
                    usuarios_sin_rol.append(usuario)
        else:
            usuarios_sin_rol.append(usuario)
    
    template_name='./Roles/asignar_rol.html'
    return render(request, template_name, {'usuarios':usuarios_sin_rol})

@login_required(login_url='/login/')
@permission_required('roles.desasignar_rol',raise_exception=True)
def desasignarRol(request, id_rol):
    """ Libera a un usuario de un Rol, desplegando los usuarios que posean este Rol
    
    @type request: django.http.HttpRequest
    @param request: Contiene informacion sobre la solic. web actual que llamo a esta vista
    
    @type id_rol: integer
    @param id_rol: es el id del Rol el cual se quiera desligar de un usuario
    
    @rtype: django.HttpResponse
    @return: desasignar_rol.html, donde se despliega un formulario con los usuarios que poseen el rol
    
    @author: Eduardo Gimenez"""
    errors = []
    if request.method == 'POST':
        eleccion = request.POST.get('Usuario', '')
        if not eleccion:
            errors.append('Debe seleccionar un usuario')
        elif not User.objects.filter(username=eleccion):
            errors.append('El usuario no existe, por favor escoja un usuario de la lista')
        if not errors:
            eleccion_rol = Roles.objects.get(id=id_rol)
            usuario_elegido  = User.objects.get(username=eleccion)
            usuario_elegido.groups.remove(eleccion_rol)
            
            return render(request, './Roles/rol_desasignado.html')
    
    usuarios_con_rol = []
    este_rol = Roles.objects.get(id = id_rol)
    usuarios_activos = User.objects.filter(is_active=True)
    for usuario in usuarios_activos:
        roles = usuario.groups.all()
        if roles:
            for rol in roles:
                if rol.name == este_rol.name:
                    usuarios_con_rol.append(usuario)
    template_name='./Roles/desasignar_rol.html'
    return render(request, template_name, {'usuarios':usuarios_con_rol})

