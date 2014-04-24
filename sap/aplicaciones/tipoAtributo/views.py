from django.shortcuts import render
from models import TipoAtributo
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.
@login_required(login_url='/login/')
def administrarTipoAtributo(request):
    """ Recibe un request, obtiene la lista de todos los Tipos de Atributo de un Proyecto y 
    luego retorna el html renderizado con la lista de Tipos de atributo 
    @type request: django.http.HttpRequest
    @param request: Contiene informacion sobre la solic. web actual que llamo a esta vista
    
    @rtype: django.http.HttpResponse
    @return: tipo_atributos.html, donde se listan los Tipos de atributos, ademas de las funcionalidades para un Tipo de Atributo
    
    @author: Eduardo Gimenez
    
    """
    """error = False
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
    """
    roles = []
    if request.user.has_perm('tipoAtributo.administrar_tipos_de_atributo'):
        atributos = TipoAtributo.objects.filter(is_active=True)
    else:
        raise PermissionDenied
    
    template_name='./tipoAtributo/tipo_atributos.html'
    return render(request, template_name, {'tipos_de_atributo': atributos})


@login_required(login_url='/login/')
@permission_required('tipoAtributo.crear_tipo_de_atributo',raise_exception=True)
def tipoAtributoNuevo(request):
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
        form = UsuarioNuevoForm(request.POST)
        if form.is_valid():
            form.clean()
            username = form.cleaned_data['Nombre_de_Usuario']
            password = form.cleaned_data['Contrasenha']
            password2 = form.cleaned_data['Confirmar_contrasenha']
            email = form.cleaned_data['Email']
            first_name = form.cleaned_data['Nombre']
            last_name = form.cleaned_data['Apellido']
            telefono = form.cleaned_data['Telefono']
            direccion = form.cleaned_data['Direccion']
            especialidad = form.cleaned_data['Especialidad']
            observaciones = form.cleaned_data['Observaciones']
            
            if (password != password2):
                template_name='./Usuarios/usuarionuevo.html'
                #mensaje='contrasenhas no coinciden'
                return render(request, template_name, {'form': form, 'mensaje': 'el password no coincide'})

            useri = User.objects.create_user(username, email, password)
            useri.first_name = first_name
            useri.last_name = last_name
            useri.save()
            
            profile = useri.get_profile()
            profile.telefono=telefono
            profile.direccion=direccion
            profile.especialidad=especialidad
            profile.observaciones=observaciones
            
            profile.save()
                    
            template_name='./Usuarios/usuariocreado.html'
            return render(request, template_name)
    else: 
        form = UsuarioNuevoForm()    
        
    template_name='./Usuarios/usuarionuevo.html'
    return render(request, template_name, {'form': form})
