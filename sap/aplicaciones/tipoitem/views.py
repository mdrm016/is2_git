from django.shortcuts import render_to_response, render, HttpResponseRedirect
from django.template import RequestContext
from .models import TipoItem, ListaAtributo
from .forms import TipoItemNuevoForm, TipoItemModificadoForm
from django.db.models import Q
from aplicaciones.tipoatributo.models import TipoAtributo
from aplicaciones.proyectos.models import Proyectos
from django.contrib.auth.decorators import login_required, permission_required
from aplicaciones.items.models import Items

@login_required(login_url='/login/')
@permission_required('tipoitem.administrar_tipoitem',raise_exception=True)
def adm_tipoitem (request, id_proyecto):
    
    """ Recibe un request y un id de proyecto, se obtiene todos los tipos de item disponibles para ese proyecto
    y luego son enviados al template para desplegarlos al usuario solicitante, ademas de realizar busquedas
    avanzadas de los tipos de items desplegados.
    
    @type request: django.http.HttpRequest.
    @param request: Contiene informacion sobre la solicitud web actual que llamo a esta vista adm_tipoitem.
    
    @type id_proyecto: string.
    @param id_proyecto: Contiene el id del proyecto cuyos tipos de items seran desplegados.
    
    @rtype: django.shortcuts.render_to_response.
    @return: tipoitem.html, donde se listan los tipos de items, ademas de las funcionalidades para cada tipo de item.
    
    @author: Marcelo Denis.
    
    """
    
    tipoitem = TipoItem.objects.filter(id_proyecto=id_proyecto, is_active=True)
    
    busqueda = ''
    error=False
    if 'busqueda' in request.GET:
        busqueda = request.GET.get('busqueda', '')
        if busqueda:
            qset = (
                Q(nombre__icontains=busqueda) |
                Q(descripcion__icontains=busqueda) 
            )
            tipoitem = tipoitem.filter(qset).distinct()
            if not tipoitem:
                error = True
                
    lista_tipoitem=[]            
    for TA in tipoitem:
        items = Items.objects.filter(is_active=True, tipo_item=TA.id)
        if items:
            usado= True
        else:
            usado= False
        tupla=(TA, usado)
        lista_tipoitem.append(tupla)
        
                
    ctx = {'lista_tipoitem':lista_tipoitem, 'query':busqueda, 'error':error, 'id_proyecto':id_proyecto}   
    template_name = 'tipoitem/tipoitem.html'
    return render_to_response(template_name, ctx, context_instance=RequestContext(request))

@login_required(login_url='/login/')
@permission_required('tipoitem.crear_tipoitem',raise_exception=True)
def crear_tipoitem (request, id_proyecto):
    
    """ Recibe un request y un id de proyecto, se verifica si el usuario tiene permisos para crear un tipo de item
    y se lo redirige a una pagina para que rellene el formulario de creacion de un tipo de item, una vez completado 
    correctamente dicho formulario, el tipo de item puede ser creado.
    
    @type request: django.http.HttpRequest.
    @param request: Contiene informacion sobre la solicitud web actual que llamo a esta vista crear_tipoitem.
    
    @type id_proyecto: string.
    @param id_proyecto: Contiene el id del proyecto al cual pertenecera el tipo de item a crear.
    
    @rtype: django.shortcuts.render_to_response.
    @return: creartipoitem.html, donde se encuentra el formulario de creacion de tipo de item y luego a 
    tipoitemalerta.html donde se notifica la creacion correcta de un tipo de item.
    
    @author: Marcelo Denis.
    
    """
    
    if request.method == 'POST':
        form = TipoItemNuevoForm(request.POST)
        if form.is_valid():
            form.clean()
            nombre = form.cleaned_data['Nombre_Tipo_de_Item'] 
            descripcion =  form.cleaned_data['Descripcion']
            #tipoatributos= form.cleaned_data['Tipo_Atributo']
            
            tipoitem = TipoItem()
            tipoitem.nombre=nombre
            tipoitem.descripcion=descripcion
            tipoitem.id_proyecto=id_proyecto
            tipoitem.is_active='True'
            tipoitem.save()

            mensaje="Tipo Item creado exitosamente"
            ctx = {'mensaje':mensaje, 'id_proyecto':id_proyecto}
            return render_to_response('tipoitem/tipoitemalerta.html',ctx, context_instance=RequestContext(request))
    else:
        form = TipoItemNuevoForm()
        
    ctx ={'form': form, 'id_proyecto':id_proyecto}      
    template_name='tipoitem/creartipoitem.html'
    return render_to_response(template_name, ctx, context_instance=RequestContext(request))

@login_required(login_url='/login/')
@permission_required('tipoitem.modificar_tipoitem',raise_exception=True)
def modificar_tipoitem (request, id_tipoitem, id_proyecto):
    
    """ Recibe un request, el id de proyecto y el id del tipo de item  a ser modificado, se verifica si
     el usuario tiene permisos para modificar un tipo de item existente y se lo redirige a una pagina para
    que modifique el formulario existente de un tipo de item, una vez modificado de forma correcta dicho 
    formulario el tipo de item puede ser modificado.
    
    @type request: django.http.HttpRequest.
    @param request: Contiene informacion sobre la solicitud web actual que llamo a esta vista modificar_tipoitem.
    
    @type id_proyecto: string.
    @param id_proyecto: Contiene el id del proyecto al cual pertenece el tipo de item a modificar.
    
    @type id_tipoitem: string.
    @param id_tipoitem: Contiene el id del tipo de item a modificar.
    
    @rtype: django.shortcuts.render_to_response.
    @return: modificartipoitem.html, donde se encuentra el formulario de modificacion de tipo de item y luego a 
    tipoitemalerta.html donde se notifica la modificacion correcta de un tipo de item.
    
    @author: Marcelo Denis.
    
    """
    
    tipoitem = TipoItem.objects.get(id=id_tipoitem)
    mensaje=''
    if request.method == 'POST':
        form = TipoItemModificadoForm(request.POST)
        if form.is_valid():
            form.clean()
            nombre = form.cleaned_data['Nombre_Tipo_de_Item'] 
            descripcion =  form.cleaned_data['Descripcion']
            #tipoatributos= form.cleaned_data['Tipo_Atributo']
            
            
            # Comprobar cantidad miembros de comite para pasar a un estado en construccion con un elif
            #si exite ya un proyecto con el nombre suministrado y el nombre suminitrado es distinto al del proyecto que esta siendo modificado
            if TipoItem.objects.filter(nombre=nombre, is_active=True) and nombre != tipoitem.nombre:
                data ={'Nombre_Tipo_de_Item':tipoitem.nombre, 'Descripcion':tipoitem.descripcion}  
                form = TipoItemModificadoForm(data)
                mensaje = 'El nombre del Tipo de Item ya existe y no puede haber duplicados'
            
            else:
                if nombre == tipoitem.nombre and  descripcion == tipoitem.descripcion:
                      mensaje="Tipo de Item guardado sin modificaciones"
                      
                else:
                    tipoitem.nombre=nombre
                    tipoitem.descripcion=descripcion
                    tipoitem.save()
                        
                    mensaje="Tipo de Item modificado exitosamente"
                    
                ctx = {'mensaje':mensaje, 'id_proyecto':id_proyecto}
                template_name='tipoitem/tipoitemalerta.html'
                return render_to_response(template_name, ctx, context_instance=RequestContext(request))
    else:
        data ={'Nombre_Tipo_de_Item':tipoitem.nombre, 'Descripcion':tipoitem.descripcion}
        form = TipoItemModificadoForm(data)
        
    ctx ={'form': form, 'mensaje':mensaje, 'tipoitem':tipoitem, 'id_proyecto':id_proyecto}      
    template_name='tipoitem/modificartipoitem.html'
    return render_to_response(template_name, ctx, context_instance=RequestContext(request))

@login_required(login_url='/login/')
@permission_required('tipoitem.eliminar_tipoitem',raise_exception=True)
def eliminar_tipoitem (request, id_tipoitem, id_proyecto):
    
    """ Recibe un request, el id de proyecto y el id del tipo de item a ser eliminado, se verifica 
    que el usuario tenga permisos para eliminar un tipo de item y si el tipo de item no esta
    siendo usado por un item, luego le brinda la opcion de eliminar el tipo de item.
    
    @type request: django.http.HttpRequest.
    @param request: Contiene informacion sobre la solicitud web actual que llamo a esta vista eliminar_tipoitem.
    
    @type id_proyecto: string.
    @param id_proyecto: Contiene el id del proyecto al cual pertenece el tipo de item a eliminar.
    
    @type id_tipoitem: string.
    @param id_tipoitem: Contiene el id del tipo de item a eliminar.
    
    @rtype: django.shortcuts.render_to_response.
    @return: tipoitem.html, donde se redirige al usuario con la actualizacion de la lista de tipos de item o a
    tipoitemalerta.html donde se notifica al usuario la razon por la cual no se puede eliminar el tipo de item.
    
    @author: Marcelo Denis.
    
    """
    
    items = Items.objects.filter(is_active=True, tipo_item=id_tipoitem)
    if items:
        msj=''
        for item in items:
            if msj=='':
                msj='%s'% item.nombre
            else:
                msj='%s, %s' % (msj, item.nombre)
        if len(items)==1:
            mensaje='Imposible eliminar el Tipo de Item, es usado por el item: %s' % msj
        else:
            mensaje='Imposible eliminar el Tipo de Item, es usado por los items: %s' % msj
        ctx = {'mensaje':mensaje, 'id_proyecto':id_proyecto}
        template_name='tipoitem/tipoitemalerta.html'
        return render_to_response(template_name, ctx, context_instance=RequestContext(request))
    else:
        tipoitem = TipoItem.objects.get(id=id_tipoitem)
        
        elementos_existentes = ordenar_mantener (id_tipoitem)
        for elemento in elementos_existentes:
            elemento.is_active = False
            elemento.orden = 0
            elemento.save()
            
        tipoitem.is_active = False
        tipoitem.save()
        return HttpResponseRedirect('/adm_proyectos/gestionar/%s/adm_tipos_item/' % id_proyecto)

@login_required(login_url='/login/')
@permission_required('tipoitem.consultar_tipoitem',raise_exception=True)
def consultar_tipoitem (request, id_tipoitem, id_proyecto):
    
    """ Recibe un request, el id de proyecto y el id del tipo de item a ser consultado, se verifica
    si el usuario tiene permisos para consultar un tipo de item y se lo redirige a una pagina que 
    despliega los datos del tipo de item solicitado.
    
    @type request: django.http.HttpRequest.
    @param request: Contiene informacion sobre la solicitud web actual que llamo a esta vista consultar_tipoitem.
    
    @type id_proyecto: string.
    @param id_proyecto: Contiene el id del proyecto al cual pertenece el tipo de item a consultar.
    
    @type id_tipoitem: string.
    @param id_tipoitem: Contiene el id del tipo de item a consultar.
    
    @rtype: django.shortcuts.render_to_response.
    @return: consultartipoitem.html, donde se encuentra la pagina de consulta de tipo item.
    
    @author: Marcelo Denis.
    
    """
    
    tipoitem = TipoItem.objects.get(id=id_tipoitem)
    
    elementos_existentes = ordenar_mantener (id_tipoitem)
    consulta = []
    for elemento in elementos_existentes:
        tupla = (elemento.nombre, TipoAtributo.objects.get(id=elemento.id_atributo).descripcion)
        consulta.append(tupla)
        
    ctx = {'tipoitem':tipoitem, 'atributos':consulta, 'id_proyecto':id_proyecto}
    template_name = 'tipoitem/consultartipoitem.html'
    return render_to_response(template_name, ctx, context_instance=RequestContext(request))

@login_required(login_url='/login/')
@permission_required('tipoitem.gestionar_tipoitem',raise_exception=True)
def gestionar_tipoitem (request, id_tipoitem, id_proyecto):
    
    """ Recibe un request, el id de proyecto y el id del tipo de item a gestionar, se verifica
    si el usuario tiene permisos para gestionar un tipo de item y se lo redirige a una pagina que 
    le permite al usuario agregar, quitar o modificar los tipos de atributos de los cuales se compondra
    el tipo de item.
    
    @type request: django.http.HttpRequest.
    @param request: Contiene informacion sobre la solicitud web actual que llamo a esta vista gestionar_tipoitem.
    
    @type id_proyecto: string.
    @param id_proyecto: Contiene el id del proyecto al cual pertenece el tipo de item a gestionar.
    
    @type id_tipoitem: string.
    @param id_tipoitem: Contiene el id del tipo de item a gestionar.
    
    @rtype: django.shortcuts.render_to_response.
    @return: gestionartipoitem.html, donde se encuentra la pagina de gestion de tipo item.
    
    @author: Marcelo Denis.
    
    """
    
    tipoitem = TipoItem.objects.get(id=id_tipoitem)
    tablaTipoAtributo = TipoAtributo.objects.filter(is_active=True, proyecto=id_proyecto)
    lista_atributos = tipoitem.listaAtributo.all().filter(is_active=True).order_by('orden')
                
    ctx = {'tipoatributos_dispon':tablaTipoAtributo, 'tipoatributo_selec':lista_atributos, 'id_proyecto':id_proyecto, 'tipoitem':tipoitem}
    template_name = 'tipoitem/gestionartipoitem.html'
    return render_to_response(template_name, ctx, context_instance=RequestContext(request))


def agregar_tipo_atributo (request, id_tipoitem, id_proyecto, id_tipoatributo):
    
    """ Recibe un request, el id de proyecto, el id del tipo de item y el id del tipo de atributo agregar al 
    tipo de item, luego se agrega el tipo de atributo especificado al tipo de item.
    
    @type request: django.http.HttpRequest.
    @param request: Contiene informacion sobre la solicitud web actual que llamo a esta vista agregar_tipo_atributo.
    
    @type id_proyecto: string.
    @param id_proyecto: Contiene el id del proyecto al cual pertenece el tipo de item a gestionar.
    
    @type id_tipoitem: string.
    @param id_tipoitem: Contiene el id del tipo de item a gestionar.
    
    @rtype: django.shortcuts.render_to_response.
    @return: gestionartipoitem.html, donde se encuentra la pagina de gestion de tipo item.
    
    @author: Marcelo Denis.
    
    """
    
    tipoAtributo = TipoAtributo.objects.get(id=id_tipoatributo)
    
    lista_atributo = ListaAtributo()
    lista_atributo.id_atributo = tipoAtributo.id
    lista_atributo.id_tipoitem = id_tipoitem
    lista_atributo.nombre = tipoAtributo.nombre
    lista_atributo.is_active = True
    
    elementos_existentes = ordenar_mantener(id_tipoitem)
    if elementos_existentes:
        lista_atributo.orden = len(elementos_existentes) + 1
    else:
        lista_atributo.orden = 1
    lista_atributo.save()
    
    tipoitem = TipoItem.objects.get(id=id_tipoitem)
    tipoitem.listaAtributo.add(lista_atributo)
    
    return HttpResponseRedirect('/adm_proyectos/gestionar/%s/adm_tipos_item/gestionar_tipoitem/%s/' % (id_proyecto, id_tipoitem))


def quitar_tipo_atributo (request, id_tipoitem, id_proyecto, id_tipoatributo):
    
    """ Recibe un request, el id de proyecto, el id del tipo de item y el id del tipo de atributo quitar del 
    tipo de item, luego se quita el tipo de atributo especificado del tipo de item.
    
    @type request: django.http.HttpRequest.
    @param request: Contiene informacion sobre la solicitud web actual que llamo a esta vista quitar_tipo_atributo.
    
    @type id_proyecto: string.
    @param id_proyecto: Contiene el id del proyecto al cual pertenece el tipo de item a gestionar.
    
    @type id_tipoitem: string.
    @param id_tipoitem: Contiene el id del tipo de item a gestionar.
    
    @rtype: django.shortcuts.render_to_response.
    @return: gestionartipoitem.html, donde se encuentra la pagina de gestion de tipo item.
    
    @author: Marcelo Denis.
    
    """
    
    tipo_atributo = ListaAtributo.objects.get(id=id_tipoatributo)
    tipo_atributo.is_active = False
    tipo_atributo.orden = 0
    tipo_atributo.save()
    elementos_existentes = ordenar_mantener(id_tipoitem)
    return HttpResponseRedirect('/adm_proyectos/gestionar/%s/adm_tipos_item/gestionar_tipoitem/%s/' % (id_proyecto, id_tipoitem))


def ordenar_mantener (id_tipoitem):
    
    """ Recibe un id de tipo de item para conseguir los tipos de atributos de ese tipo de item, ordenarlos y reparar
    el orden si este fue modificado para luego enviarselas a la funcion solicitante.
    
    @type id_tipoitem: string.
    @param id_tipoitem: Contiene el id del tipo de item a del cual se conseguiran los tipos de atributos.
    
    @rtype: lista.
    @return: lista de objetos de tipo listaAtributo
    
    @author: Marcelo Denis.
    
    """
    
    elementos_existentes = ListaAtributo.objects.filter(id_tipoitem=id_tipoitem, is_active=True).exclude(orden='0').order_by('orden')
    control = 1
    for elemento in elementos_existentes:
        if elemento.orden != control:
            elemento.orden = control
            elemento.save()
        control = control + 1
    return elementos_existentes


def subir_tipo_atributo (request, id_tipoitem, id_proyecto, id_tipoatributo):
    
    """ Recibe un request, el id de proyecto, el id del tipo de item y el id del tipo de atributo a subir un nivel
    en el orden del tipo de item, luego se mueve el tipo de atributo especificado en el tipo de item.
    
    @type request: django.http.HttpRequest.
    @param request: Contiene informacion sobre la solicitud web actual que llamo a esta vista subir_tipo_atributo.
    
    @type id_proyecto: string.
    @param id_proyecto: Contiene el id del proyecto al cual pertenece el tipo de item a gestionar.
    
    @type id_tipoitem: string.
    @param id_tipoitem: Contiene el id del tipo de item a gestionar.
    
    @rtype: django.shortcuts.render_to_response.
    @return: gestionartipoitem.html, donde se encuentra la pagina de gestion de tipo item.
    
    @author: Marcelo Denis.
    
    """
    
    atributo_a_subir=ListaAtributo.objects.get(id=id_tipoatributo)
    if atributo_a_subir.orden-1 > 0:
        atributo_a_bajar=ListaAtributo.objects.get(orden=(atributo_a_subir.orden-1), is_active=True, id_tipoitem=id_tipoitem)
        orden = atributo_a_bajar.orden
        atributo_a_bajar.orden = atributo_a_subir.orden
        atributo_a_subir.orden = orden
        atributo_a_bajar.save()
        atributo_a_subir.save()
        
    return HttpResponseRedirect('/adm_proyectos/gestionar/%s/adm_tipos_item/gestionar_tipoitem/%s/' % (id_proyecto, id_tipoitem))

  
def bajar_tipo_atributo (request, id_tipoitem, id_proyecto, id_tipoatributo):
    
    """ Recibe un request, el id de proyecto, el id del tipo de item y el id del tipo de atributo a bajar un nivel
    en el orden del tipo de item, luego se mueve el tipo de atributo especificado en el tipo de item.
    
    @type request: django.http.HttpRequest.
    @param request: Contiene informacion sobre la solicitud web actual que llamo a esta vista bajar_tipo_atributo.
    
    @type id_proyecto: string.
    @param id_proyecto: Contiene el id del proyecto al cual pertenece el tipo de item a gestionar.
    
    @type id_tipoitem: string.
    @param id_tipoitem: Contiene el id del tipo de item a gestionar.
    
    @rtype: django.shortcuts.render_to_response.
    @return: gestionartipoitem.html, donde se encuentra la pagina de gestion de tipo item.
    
    @author: Marcelo Denis.
    
    """
    
    atributo_a_bajar=ListaAtributo.objects.get(id=id_tipoatributo)
    cantidad = len(ordenar_mantener (id_tipoitem))
    if atributo_a_bajar.orden+1 <= cantidad:
        atributo_a_subir=ListaAtributo.objects.get(orden=(atributo_a_bajar.orden+1), is_active=True, id_tipoitem=id_tipoitem)
        orden = atributo_a_subir.orden
        atributo_a_subir.orden = atributo_a_bajar.orden
        atributo_a_bajar.orden = orden
        atributo_a_subir.save()
        atributo_a_bajar.save()
        
    return HttpResponseRedirect('/adm_proyectos/gestionar/%s/adm_tipos_item/gestionar_tipoitem/%s/' % (id_proyecto, id_tipoitem))

@login_required(login_url='/login/')
@permission_required('tipoitem.importar_tipoitem',raise_exception=True)
def listar_proyectos (request, id_proyecto):
    
    """ Recibe un request y un id de proyecto, se obtiene todos los proyectos activos en el sistema
     y son despelgados al usuario para que seleccione uno que contiene el tipo de item a importar.
    
    @type request: django.http.HttpRequest.
    @param request: Contiene informacion sobre la solicitud web actual que llamo a esta vista listar_proyectos.
    
    @type id_proyecto: string.
    @param id_proyecto: Contiene el id del proyecto al cual se agregara el item a importar.
    
    @rtype: django.shortcuts.render_to_response.
    @return: listarproyectos.html, donde se listan los proyectos, y se otorga la posbilidad de seleccionar uno.
    
    @author: Marcelo Denis.
    
    """
    
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
    
    ctx = {'id_proyecto':id_proyecto, 'lista_proyectos':proyectos, 'query':busqueda, 'error':error}
    template_name = 'tipoitem/listarproyectos.html'
    return render_to_response(template_name, ctx, context_instance=RequestContext(request))

@login_required(login_url='/login/')    
def listar_tipoitem(request, id_proyecto, proyecto_select):
    
    """ Recibe un request y un id de proyecto y un id del proyecto seleccionado, se obtiene todos tipos
    de item del proyecto seleccionado y son desplegados al usuario para que este seleccione el que desea importar.
    
    @type request: django.http.HttpRequest.
    @param request: Contiene informacion sobre la solicitud web actual que llamo a esta vista listar_tipoitem.
    
    @type id_proyecto: string.
    @param id_proyecto: Contiene el id del proyecto al cual se agregara el item a importar.
    
    @rtype: django.shortcuts.render_to_response.
    @return: listartipoitem.html, donde se listan los tipos de item, y se otorga la posbilidad de importar uno.
    
    @author: Marcelo Denis.
    
    """
    
    tipoitem = TipoItem.objects.filter(id_proyecto=proyecto_select, is_active=True)
    proyecto = Proyectos.objects.get(id=id_proyecto)
    
    busqueda = ''
    error=False
    if 'busqueda' in request.GET:
        busqueda = request.GET.get('busqueda', '')
        if busqueda:
            qset = (
                Q(nombre__icontains=busqueda) |
                Q(descripcion__icontains=busqueda) 
            )
            tipoitem = tipoitem.filter(qset).distinct()
            if not tipoitem:
                error = True
                
    ctx = {'proyecto':proyecto, 'lista_tipoitem':tipoitem, 'query':busqueda, 'error':error}
    template_name = 'tipoitem/listartipoitem.html'
    return render_to_response(template_name, ctx, context_instance=RequestContext(request))

@login_required(login_url='/login/')
def importar_tipoitem(request, id_proyecto, proyecto_select, id_tipoitem):
    
    """ Recibe un request, el id de proyecto y el id proyecto seleccionado y el id del tipo de item a ser
    importado del proyecto seleccionado, se verifica si el usuario tiene permisos para importar un tipo de 
    item existente, luego se lo redirige a la pagina para completar los datos del formulario del tipo de item 
    a importar, una vez completado correctamente el formulario el sistema crea un nuevo tipo de item con tipos 
    de atributos que tenia el tipo de item importado.
    
    @type request: django.http.HttpRequest.
    @param request: Contiene informacion sobre la solicitud web actual que llamo a esta vista importar_tipoitem.
    
    @type id_proyecto: string.
    @param id_proyecto: Contiene el id del proyecto al cual pertenecera el nuevo tipo de item a importar.
    
    @type proyecto_select: string.
    @param proyecto_select: Contiene el id del proyecto al cual pertenece el tipo de item que sera importado.
    
    @type id_tipoitem: string.
    @param id_tipoitem: Contiene el id del tipo de item a importar.
    
    @rtype: django.shortcuts.render_to_response.
    @return: creartipoitemimportado.html, donde se redirige al usuario para completar los datos del nuevo
    tipo de item a importar y luego a proyectoalerta.html donde se notifica que el proyecto fue importado
    correctamente.
    
    @author: Marcelo Denis.
    
    """
    
    tipoI = TipoItem.objects.get(id=id_tipoitem)
    if request.method == 'POST':
        form = TipoItemNuevoForm(request.POST)
        if form.is_valid():
            form.clean()
            nombre = form.cleaned_data['Nombre_Tipo_de_Item'] 
            descripcion =  form.cleaned_data['Descripcion']
            
            tipoitem = TipoItem()
            tipoitem.nombre=nombre
            tipoitem.descripcion=descripcion
            tipoitem.id_proyecto=id_proyecto
            tipoitem.is_active='True'
            tipoitem.save()
            
            elementos_existentes = ordenar_mantener(id_tipoitem)
            for elemento in elementos_existentes:
                lista_atributo = ListaAtributo()
                lista_atributo.id_atributo = elemento.id
                lista_atributo.id_tipoitem = tipoitem.id
                lista_atributo.nombre = elemento.nombre
                lista_atributo.is_active = True
                
                elementos = ordenar_mantener(tipoitem.id)
                if elementos:
                    lista_atributo.orden = len(elementos_existentes) + 1
                else:
                    lista_atributo.orden = 1
                lista_atributo.save()
                
                tipoitem.listaAtributo.add(lista_atributo)
            
            
            mensaje="Tipo Item Importado exitosamente"
            ctx = {'mensaje':mensaje, 'id_proyecto':id_proyecto}
            return render_to_response('tipoitem/tipoitemalerta.html',ctx, context_instance=RequestContext(request))
    else:
        form = TipoItemNuevoForm()
        
    ctx ={'form': form, 'tipoitem':tipoI, 'id_proyecto':id_proyecto}      
    template_name='tipoitem/creartipoitemimportado.html'
    return render_to_response(template_name, ctx, context_instance=RequestContext(request))
