from django.shortcuts import render
from models import TipoAtributo
from  django.http import  HttpResponseRedirect
from forms import TipoAtributoForm, TipoAtributoModificadoForm
from aplicaciones.proyectos.models import Proyectos
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.
@login_required(login_url='/login/')
def administrarTipoAtributo(request, id_proyecto):
    """ Recibe un request, obtiene la lista de todos los Tipos de Atributo de un Proyecto y 
    luego retorna el html renderizado con la lista de Tipos de atributo 
    
    @type request: django.http.HttpRequest
    @param request: Contiene informacion sobre la solic. web actual que llamo a esta vista
    
    @type id_proyecto: Integer
    @param id_proyecto: Es el id del proyecto actual en el que se esta trabajando
    
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
    return render(request, template_name, {'tipos_de_atributo': atributos, 'id_proyecto':id_proyecto})


@login_required(login_url='/login/')
@permission_required('tipoAtributo.crear_tipo_de_atributo',raise_exception=True)
def tipoAtributoNuevo(request, id_proyecto):
    """ Recibe un request, obtiene el formulario con los datos del Tipo de Atributo a crear
    o la solicitud de envio de dicho formulario. Luego verifica los datos recibidos
    y registra el nuevo Tipo de atributo.  
    
    @type request: django.http.HttpRequest
    @param request: Contiene informacion sobre la solic. web actual que llamo a esta vista
    
    @type id_proyecto: Integer
    @param id_proyecto: Es el id del proyecto actual en el que se esta trabajando
    
    @rtype: django.http.HttpResponse
    @return: tipo_atributo_creado.html, mensaje de exito
    
    @author: Eduardo Gimenez
    
    """
    errors = []
    if request.method == 'POST':
        form = TipoAtributoForm(request.POST)
        if form.is_valid():
            form.clean()
            nombre = form.cleaned_data['Nombre_tipo_atributo']
            tipo = form.cleaned_data['Tipo_de_dato']
            precision = form.cleaned_data['Precision']
            longitud = form.cleaned_data['Longitud']
            obligatorio = form.cleaned_data['Obligatorio']
            descripcion = form.cleaned_data['Descripcion']
            
            if tipo == 'Numerico':
                if not precision:
                    errors.append('Ha seleccionado como tipo de dato NUMERICO, por favor especifique la cantidad de decimales con el campo Precision')
                if not longitud:
                    errors.append('Ha seleccionado como tipo de dato NUMERICO, por favor especifique la longitud (enteros mas decimales) con el campo Longitud')
            elif tipo == 'Texto':
                precision = 0
                if not longitud:
                    errors.append('Ha seleccionado como tipo de dato TEXTO, por favor especifique la cantidad de caracteres con el campo Longitud')
            else: 
                precision = 0
                longitud = 0
            
            if not errors:
                tipo_atributo = TipoAtributo()
                tipo_atributo.nombre = nombre
                tipo_atributo.tipo = tipo
                tipo_atributo.precision = precision
                tipo_atributo.longitud = longitud
                if obligatorio == 'N':
                    tipo_atributo.obligatorio = False
                else:
                    tipo_atributo.obligatorio = True 
                tipo_atributo.descripcion = descripcion
                tipo_atributo.save()
                tipo_atributo.proyecto.add(id_proyecto)
                
                
                        
                template_name='./tipoAtributo/tipo_atributo_creado.html'
                return render(request, template_name, {'id_proyecto': id_proyecto})
    else: 
        form = TipoAtributoForm()    
        
    template_name='./tipoAtributo/tipo_atributo_nuevo.html'
    return render(request, template_name, {'form': form, 'errors': errors, 'id_proyecto': id_proyecto})

@login_required(login_url='/login/')
@permission_required('tipoAtributo.modificar_tipo_de_atributo',raise_exception=True)
def modificarTipoAtributo(request, id_proyecto, id_tipo_atributo):
    """ Recibe un request, obtiene el formulario con los datos del Tipo de Atributo a modificar
    o la solicitud de envio de dicho formulario. Luego verifica los datos recibidos
    y registra los cambios hechos en el Tipo de atributo.  
    
    @type request: django.http.HttpRequest
    @param request: Contiene informacion sobre la solic. web actual que llamo a esta vista
    
    @type id_proyecto: Integer
    @param id_proyecto: Es el id del proyecto actual en el que se esta trabajando
    
    @rtype: django.http.HttpResponse
    @return: tipo_atributo_mmodificado.html, mensaje de exito
    
    @author: Eduardo Gimenez
    
    """
    errors = []
    tipo_atributo = TipoAtributo.objects.get(id=id_tipo_atributo)
    if request.method == 'POST':
        form = TipoAtributoModificadoForm(request.POST)
        if form.is_valid():
            form.clean()
            nombre = form.cleaned_data['Nombre_tipo_atributo']
            tipo = form.cleaned_data['Tipo_de_dato']
            precision = form.cleaned_data['Precision']
            longitud = form.cleaned_data['Longitud']
            obligatorio = form.cleaned_data['Obligatorio']
            descripcion = form.cleaned_data['Descripcion']
            
            if tipo == 'Numerico':
                if not precision:
                    errors.append('Ha seleccionado como tipo de dato NUMERICO, por favor especifique la cantidad de decimales con el campo Precision')
                if not longitud:
                    errors.append('Ha seleccionado como tipo de dato NUMERICO, por favor especifique la longitud (enteros mas decimales) con el campo Longitud')
            elif tipo == 'Texto':
                precision = 0
                if not longitud:
                    errors.append('Ha seleccionado como tipo de dato TEXTO, por favor especifique la cantidad de caracteres con el campo Longitud')
            else: 
                precision = 0
                longitud = 0
            
            if not errors:
                
                tipo_atributo.nombre = nombre
                tipo_atributo.tipo = tipo
                tipo_atributo.precision = precision
                tipo_atributo.longitud = longitud
                if obligatorio == 'N':
                    tipo_atributo.obligatorio = False
                else:
                    tipo_atributo.obligatorio = True 
                tipo_atributo.descripcion = descripcion
                tipo_atributo.save()
                
                
                        
                template_name='./tipoAtributo/tipo_atributo_modificado.html'
                return render(request, template_name, {'id_proyecto': id_proyecto})
    else: 
        if tipo_atributo.obligatorio:
            obligatorio = 'S'
        else:
            obligatorio = 'N'
        initial = {'Nombre_tipo_atributo': tipo_atributo.nombre, 'Tipo_de_dato': tipo_atributo.tipo, 'Precision': tipo_atributo.precision, 'Longitud': tipo_atributo.longitud, 'Obligatorio': obligatorio, 'Descripcion': tipo_atributo.descripcion}
        form = TipoAtributoModificadoForm(initial)    
        
    template_name='./tipoAtributo/modificar_tipo_atributo.html'
    return render(request, template_name, {'form': form, 'errors': errors, 'id_proyecto': id_proyecto})

def eliminarTipoAtributo(request, id_proyecto, id_tipo_atributo):
    """ Eliminar de manera logica los registros del Tipo de atributo.Tambien elimina la relacion entre 
    los proyectos que poseen este Tipo de atributo.
        
    @type request: django.http.HttpRequest
    @param request: Contiene informacion sobre la solicitud web actual que llamo a esta vista
    
    @type id_proyecto: Integer
    @param id_proyecto: Es el id del proyecto actual en el que se esta trabajando
        
    @rtype: django.shortcuts.render_to_response
    @return: Se retorna al la administracion de Roles o se manda a la pagina de notificacion
        
    @author: Eduardo Gimenez"""
    
    tipo_atributo = TipoAtributo.objects.get(id=id_tipo_atributo)
    tipo_atributo.is_active = False
    tipo_atributo.save()
    
    return HttpResponseRedirect('/adm_proyectos/gestionar/%s/adm_tipos_atributo/' % id_proyecto)

