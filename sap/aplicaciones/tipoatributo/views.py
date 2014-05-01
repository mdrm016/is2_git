from django.shortcuts import render, render_to_response
from models import TipoAtributo
from  django.http import  HttpResponseRedirect
from django.template import RequestContext
from forms import TipoAtributoForm, TipoAtributoModificadoForm
from aplicaciones.proyectos.models import Proyectos
from aplicaciones.tipoitem.models import TipoItem
from django.contrib.auth.decorators import login_required, permission_required
from django.db.models import Q

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
    
    if request.user.has_perm('tipoAtributo.administrar_tipos_de_atributo'):
        atributos = TipoAtributo.objects.filter(is_active=True, proyecto=id_proyecto)
        busqueda = ''
        error=False
        if 'busqueda' in request.GET:
            busqueda = request.GET.get('busqueda', '')
            if busqueda:
                qset = (
                    Q(nombre__icontains=busqueda) |
                    Q(tipo__icontains=busqueda) |
                    Q(descripcion__icontains=busqueda) 
                )
                atributos = atributos.filter(qset).distinct()
                if not atributos:
                    error = True
                
    else:
        raise PermissionDenied
    
    template_name='./tipoAtributo/tipo_atributos.html'
    return render(request, template_name, {'tipos_de_atributo': atributos, 'id_proyecto':id_proyecto, 'query':busqueda, 'error':error})


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
                if not precision and precision != 0:
                    errors.append('Ha seleccionado como tipo de dato NUMERICO, por favor especifique la cantidad de decimales con el campo Precision')
                if not longitud and longitud > 0:
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
    
    @type id_tipo_atributo: Integer
    @param id_tipo_atributo: Es el id del Tipo de Atributo cuyos datos se quieren modificar
    
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

@login_required(login_url='/login/')
@permission_required('tipoAtributo.eliminar_tipo_de_atributo',raise_exception=True)
def eliminarTipoAtributo(request, id_proyecto, id_tipo_atributo):
    """ Eliminar de manera logica los registros del Tipo de atributo.Tambien elimina la relacion entre 
    los proyectos que poseen este Tipo de atributo.
        
    @type request: django.http.HttpRequest
    @param request: Contiene informacion sobre la solicitud web actual que llamo a esta vista
    
    @type id_proyecto: Integer
    @param id_proyecto: Es el id del proyecto actual en el que se esta trabajando
    
     @type id_tipo_atributo: Integer
    @param id_tipo_atributo: Es el id del Tipo de Atributo a eliminar
        
    @rtype: django.shortcuts.render_to_response
    @return: Se retorna al la administracion de Roles o se manda a la pagina de notificacion
        
    @author: Eduardo Gimenez"""
    
    tipo_atributo = TipoAtributo.objects.get(id=id_tipo_atributo)
    tipos_item = TipoItem.objects.filter(is_active=True, id_proyecto=id_proyecto)
    puede_eliminarse = True
    for tipo_item in tipos_item:
        atributos = tipo_item.listaAtributo.all()
        if atributos:
            for atributo in atributos:
                if tipo_atributo.id == atributo.id_atributo:
                    puede_eliminarse = False  
    if puede_eliminarse:
        if len(tipo_atributo.proyecto.all()) <= 1: 
            tipo_atributo.is_active = False
            tipo_atributo.save()
        else:
            tipo_atributo.proyecto.remove(id_proyecto)
    else:
        mensaje="No es posible eliminar Tipo de Atributo, actualmente esta siendo utilizado"
        ctx = {'mensaje':mensaje, 'id_proyecto':id_proyecto}
        return render_to_response('tipoAtributo/alerta_tipo_atributo.html',ctx, context_instance=RequestContext(request))

    return HttpResponseRedirect('/adm_proyectos/gestionar/%s/adm_tipos_atributo/' % id_proyecto)

@login_required(login_url='/login/')
def consultarTipoAtributo(request, id_proyecto, id_tipo_atributo):
    """ Busca en la base de datos al Tipo de atributo cuyos datos se quieren consultar, 
    los presenta en un html con la disponibilidad de regresar a la pagina anterior 
    @type request: django.http.HttpRequest
    @param request: Contiene informacion sobre la solic. web actual que llamo a esta vista
    
    @type id_proyecto: Integer
    @param id_proyecto: Es el id del proyecto actual en el que se esta trabajando
    
     @type id_tipo_atributo: Integer
    @param id_tipo_atributo: Es el id del Tipo de Atributo cuyos datos se quieren visualizar
    
    @rtype: django.HttpResponse
    @return: consultar_tipo_atributo.html, donde se le despliega al usuario los datos
        
    @author: Eduardo Gimenez
    """
    template_name='./tipoAtributo/consultar_tipo_atributo.html'
    tipo_atributo = TipoAtributo.objects.get(id = id_tipo_atributo)
    proyectos = tipo_atributo.proyecto.all()
    return render(request, template_name, {'tipo_atributo' : tipo_atributo, 'proyectos':proyectos}) 

@login_required(login_url='/login/')
@permission_required('tipoAtributo.importar_tipo_de_atributo',raise_exception=True)
def importarTipoAtributo(request, id_proyecto, proyecto_select, id_tipo_atributo):
    """ Busca en la base de datos los Tipos de atributo de todos los proyectos,
    con la disponibilidad de importar el tipo de atributo que el usuario desee.  
    @type request: django.http.HttpRequest
    @param request: Contiene informacion sobre la solic. web actual que llamo a esta vista
    
    @type id_proyecto: Integer
    @param id_proyecto: Es el id del proyecto actual en el que se esta trabajando

    @rtype: django.HttpResponse
    @return: importar_tipo_atributo.html, donde se le despliega al usuario los datos
        
    @author: Eduardo Gimenez
    """
    tipo_atributo = TipoAtributo.objects.get(id=id_tipo_atributo)
    proyectos_tipo_atributo = tipo_atributo.proyecto.all()
    proyectos = []
    for proyecto in proyectos_tipo_atributo: 
        proyectos.append(str(proyecto.id))
        
    if id_proyecto in proyectos:
        mensaje="El Tipo de Atributo ya existe actualmente en el proyecto"
    else:
        tipo_atributo.proyecto.add(id_proyecto)
        mensaje="Tipo de Atributo importado exitosamente"
        
    ctx = {'mensaje':mensaje, 'id_proyecto':id_proyecto}
    return render_to_response('tipoAtributo/alerta_tipo_atributo.html',ctx, context_instance=RequestContext(request))

    
@login_required(login_url='/login/')
@permission_required('tipoAtributo.importar_tipo_de_atributo',raise_exception=True)
def listar_proyectos (request, id_proyecto):
    
    proyectos = Proyectos.objects.filter(is_active=True)
    ctx = {'id_proyecto':id_proyecto, 'lista_proyectos':proyectos}
    template_name = 'tipoAtributo/listar_Proyectos.html'
    return render_to_response(template_name, ctx, context_instance=RequestContext(request))

@login_required(login_url='/login/')
@permission_required('tipoAtributo.importar_tipo_de_atributo',raise_exception=True)
def listar_tipoAtributo(request, id_proyecto, proyecto_select):
    
    tipo_atributo = TipoAtributo.objects.filter(proyecto=proyecto_select, is_active=True)
    proyecto = Proyectos.objects.get(id=id_proyecto)
    ctx = {'proyecto': proyecto, 'lista_tipo_atributo': tipo_atributo}
    template_name = 'tipoAtributo/importar_tipo_atributo.html'
    return render_to_response(template_name, ctx, context_instance=RequestContext(request))
   