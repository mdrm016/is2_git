from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect, HttpResponse
from django.template.context import RequestContext
from aplicaciones.proyectos.models import Proyectos
from aplicaciones.fases.models import Fases
from aplicaciones.tipoitem.models import TipoItem
from aplicaciones.tipoatributo.models import TipoAtributo, Numerico, Fecha, Texto, ArchivoExterno, Logico
from aplicaciones.items.models import Items, ListaValores, ValorItem
from datetime import datetime
from django.contrib.auth.decorators import login_required, permission_required
from django.db.models import Q
from aplicaciones.tipoitem.views import ordenar_mantener
from .models import Relaciones
from aplicaciones.solicitudes.models import Credenciales
import logging

logger = logging.getLogger(__name__)

# Create your views here.
def adm_relaciones(request, id_proyecto, id_fase, id_item):
    
    """ Recibe un request, se verifica cual es el usuario registrado y el proyecto del cual se solicita,
    se obtiene la lista de fases con las que estan relacionados el usuario y el proyecto 
    desplegandola en pantalla, ademas permite realizar busquedas avanzadas sobre
    las fases que puede mostrar.
    
    @type request: django.http.HttpRequest.
    @param request: Contiene informacion sobre la solicitud web actual que llamo a esta vista.
    
    @rtype: django.shortcuts.render_to_response.
    @return: fases.html, donde se listan las fases, ademas de las funcionalidades para cada fase.
    
    @author: Ysapy Ortiz.
    
    """
    proyecto = Proyectos.objects.get(id=id_proyecto)
    fase = Fases.objects.get(id=id_fase)
    item = Items.objects.get(id=id_item)
    if proyecto.estado=='Inactivo' or fase.estado=='FD' or item.estado=='En revision' or item.estado=='Validado' or item.estado=='Bloqueado':
        mensaje = 'No se pueden gestionar relaciones. Dirijase a consultar item.'
        ctx = {'mensaje': mensaje, 'id_proyecto':id_proyecto, 'id_fase': id_fase, 'proyecto':proyecto, 'fase':fase}
        template_name = './items/itemalerta.html'
        return render_to_response(template_name, ctx, context_instance=RequestContext(request))
    if item.estado=='Habilitado':
        credencial = Credenciales.objects.get(item_id=item.id, estado='Habilitado')
        if credencial.usuario.user.id!=request.user.id:
            mensaje = 'No posee credencial sobre este item.'
            ctx = {'mensaje':mensaje, 'id_proyecto': id_proyecto}
            template_name = './relaciones/relacionalerta.html'
            return render_to_response(template_name, ctx, context_instance=RequestContext(request))
    
    try:
        padre = Items.objects.get(id=item.padre)
    except Items.DoesNotExist:
        padre = False
    logger.info('Administracion de Relaciones del item %s, hecho por %s' % (item.nombre, request.user.username))
    ctx = {'id_proyecto':id_proyecto, 'id_fase': id_fase, 'id_item': id_item, 'padre': padre, 'proyecto':proyecto, 'fase':fase}
    template_name = './relaciones/relaciones.html'
    return render_to_response(template_name, ctx, context_instance=RequestContext(request))

def listar_items(request, id_proyecto, id_fase, id_item):
    """ Recibe un request, se verifica cual es el usuario registrado y el proyecto del cual se solicita,
    se obtiene la lista de fases con las que estan relacionados el usuario y el proyecto 
    desplegandola en pantalla, ademas permite realizar busquedas avanzadas sobre
    las fases que puede mostrar.
    
    @type request: django.http.HttpRequest.
    @param request: Contiene informacion sobre la solicitud web actual que llamo a esta vista.
    
    @rtype: django.shortcuts.render_to_response.
    @return: fases.html, donde se listan las fases, ademas de las funcionalidades para cada fase.
    
    @author: Ysapy Ortiz.
    
    """
    proyecto = Proyectos.objects.get(id=id_proyecto)
    fase = Fases.objects.get(id=id_fase)
    item = Items.objects.get(id=id_item)
    
    if item.estado=='Validado' or item.estado=='En Revision' or item.estado=='Bloqueado':
        mensaje = 'No se puede crear relacion. Dirijase a consultar item.'
        ctx = {'mensaje': mensaje, 'id_proyecto':id_proyecto, 'id_fase': id_fase, 'proyecto':proyecto, 'fase':fase}
        template_name = './items/itemalerta.html'
        return render_to_response(template_name, ctx, context_instance=RequestContext(request))
    if item.padre!=0:
        mensaje = 'El item ya posee un padre/antecesor. Elimine la relacion actual y verifique.'
        ctx = {'mensaje': mensaje, 'id_proyecto':id_proyecto, 'id_fase': id_fase, 'proyecto':proyecto, 'fase':fase}
        template_name = './items/itemalerta.html'
        return render_to_response(template_name, ctx, context_instance=RequestContext(request))

    itemsmismafase = Items.objects.filter(proyecto_id=id_proyecto, fase_id=id_fase, is_active=True).exclude(id=id_item)
    lista_items = []
    for itemhijo in itemsmismafase:
        if itemhijo.padre!=item.id:
            lista_items.append(itemhijo)
    
    if fase.orden!=1:
        faseanterior = Fases.objects.get(orden=fase.orden-1, is_active=True, proyecto_id=id_proyecto)
        lista_items_ant = Items.objects.filter(proyecto_id=id_proyecto, fase_id=faseanterior.id, is_active=True, estado='Bloqueado')
    else:
        lista_items_ant = False
    logger.info('Lista de items relacionados con el item %s, hecho por %s' % (item.nombre, request.user.username))
    ctx = {'lista_items_ant': lista_items_ant, 'lista_items': lista_items, 'id_proyecto': id_proyecto, 'id_fase': id_fase, 'id_item': id_item}
    template_name = './relaciones/relacionnueva.html'
    return render_to_response(template_name, ctx, context_instance=RequestContext(request))

def crear_relacion(request, id_proyecto, id_fase, id_item, id_importar):
    """ Recibe un request, se verifica cual es el usuario registrado y el proyecto del cual se solicita,
    se obtiene la lista de fases con las que estan relacionados el usuario y el proyecto 
    desplegandola en pantalla, ademas permite realizar busquedas avanzadas sobre
    las fases que puede mostrar.
    
    @type request: django.http.HttpRequest.
    @param request: Contiene informacion sobre la solicitud web actual que llamo a esta vista.
    
    @rtype: django.shortcuts.render_to_response.
    @return: fases.html, donde se listan las fases, ademas de las funcionalidades para cada fase.
    
    @author: Ysapy Ortiz.
    
    """
    proyecto = Proyectos.objects.get(id=id_proyecto)    
    fase = Fases.objects.get(id=id_fase)
    item = Items.objects.get(id=id_item)
    itemrelacionado = Items.objects.get(id=id_importar)
    ciclo = control_ciclo(id_proyecto, id_fase, id_item, id_importar)

    if ciclo==True:
        mensaje = 'No se puede crear la relacion, se formaria un ciclo. Verifiquelo'
        ctx = {'mensaje': mensaje, 'id_proyecto': id_proyecto, 'id_fase': id_fase, 'id_item': id_item}
        template_name = './relaciones/relacionalerta.html'
        return render_to_response(template_name, ctx, context_instance=RequestContext(request))
    
    nuevo = Relaciones()
    nuevo.padre_id = id_importar
    nuevo.item = item.id
    nuevo.version = item.version + 1
    nuevo.save()
    item.padre = id_importar

    item1 = ValorItem.objects.filter(item_id=id_item, fase_id=id_fase, proyecto_id=id_proyecto, version=item.version).order_by('orden')
    for itemvalor in item1:
        if not (cargar_atributos(itemvalor.valor_id, itemvalor.nombre_atributo, itemvalor.orden, itemvalor.tabla_valor_nombre, id_proyecto, id_fase, id_item)):
            estamosenproblemas.append(gkcmt)
                
    item.version = item.version + 1
    item.save()
    mensaje = 'La relacion ha sido creada con exito.'
    logger.info('Crear relacion de item %s con el item %s, hecho por %s' % (item.nombre, itemrelacionado.nombre, request.user.username))
        
    ctx = {'mensaje': mensaje, 'id_proyecto': id_proyecto, 'id_fase': id_fase, 'id_item': id_item}
    template_name = './relaciones/relacionalerta.html'
    return render_to_response(template_name, ctx, context_instance=RequestContext(request))
    
def eliminar_relacion(request, id_proyecto, id_fase, id_item, id_padre):
    """ Recibe un request, se verifica cual es el usuario registrado y el proyecto del cual se solicita,
    se obtiene la lista de fases con las que estan relacionados el usuario y el proyecto 
    desplegandola en pantalla, ademas permite realizar busquedas avanzadas sobre
    las fases que puede mostrar.
    
    @type request: django.http.HttpRequest.
    @param request: Contiene informacion sobre la solicitud web actual que llamo a esta vista.
    
    @rtype: django.shortcuts.render_to_response.
    @return: fases.html, donde se listan las fases, ademas de las funcionalidades para cada fase.
    
    @author: Ysapy Ortiz.
    
    """
    proyecto = Proyectos.objects.get(id=id_proyecto)
    fase = Fases.objects.get(id=id_fase)
    item1 = Items.objects.get(id=id_item)
    
    if proyecto.estado=='Inactivo' or proyecto.estado=='Finalizado' or fase.estado=='FD' or item1.estado=='En Revision' or item1.estado=='Bloqueado' or item1.estado=='Validado':
        mensaje = 'No se puede eliminar la relacion. Dirijase a consultar item.'
        ctx = {'mensaje': mensaje, 'id_proyecto': id_proyecto, 'id_fase': id_fase, 'id_item': id_item, 'id_relacion': id_relacion}
        template_name = './relaciones/relacionalerta.html'
        return render_to_response(template_name, ctx, context_instance=RequestContext(request))
    
    itemvalor1 = ValorItem.objects.filter(item_id=item1.id, fase_id=id_fase, proyecto_id=id_proyecto, version=item1.version).order_by('orden')
    
    for itemvalor in itemvalor1:
        if not (cargar_atributos(itemvalor.valor_id, itemvalor.nombre_atributo, itemvalor.orden, itemvalor.tabla_valor_nombre, id_proyecto, id_fase, int(item1.id))):
            estamosenproblemas.append(gkcmt)

    if item1.estado!='Habilitado':            
        pasar_construccion(id_item)
    
    item1.padre = 0
    item1.version = item1.version + 1
    item1.save()

    logger.info('Eliminacion de la relacion entre el item %s y el item %s, hecho por %s' % (item1.nombre, item1.padre, request.user.username))
    mensaje = 'Relacion eliminada con exito.'
    ctx = {'mensaje': mensaje, 'id_proyecto': id_proyecto, 'id_fase': id_fase, 'id_item': id_item}
    template_name = './relaciones/relacionalerta.html'
    return render_to_response(template_name, ctx, context_instance=RequestContext(request))

def cargar_atributos(valor_id, nombreatributo, orden, nombretabla, id_proyecto, id_fase, id_item):
    """ Recibe un request, se verifica cual es el usuario registrado y el proyecto del cual se solicita,
    se obtiene la lista de fases con las que estan relacionados el usuario y el proyecto 
    desplegandola en pantalla, ademas permite realizar busquedas avanzadas sobre
    las fases que puede mostrar.
    
    @type request: django.http.HttpRequest.
    @param request: Contiene informacion sobre la solicitud web actual que llamo a esta vista.
    
    @rtype: django.shortcuts.render_to_response.
    @return: fases.html, donde se listan las fases, ademas de las funcionalidades para cada fase.
    
    @author: Ysapy Ortiz.
    
    """
    proyecto = Proyectos.objects.get(id=id_proyecto)
    fase = Fases.objects.get(id=id_fase)
    itemactual = Items.objects.get(id=id_item)
    if fase.estado == 'FD' or proyecto.estado=='Inactivo' or itemactual.estado=='En Revision' or itemactual.estado=='Bloqueado' or itemactual.estado=='Validado':
        mensaje = 'No se pueden modificar atributos. Dirijase a consultar item.'
        ctx = {'mensaje':mensaje, 'id_proyecto': id_proyecto}
        template_name = './items/itemalerta.html'
        return render_to_response(template_name, ctx, context_instance=RequestContext(request))
     
    versionitem = itemactual.version + 1
     
    valoritems = ValorItem()
    if nombretabla=='tipoatributo_archivoexterno':
        archivo = ArchivoExterno()
        viejo = ArchivoExterno.objects.get(id=valor_id)
        archivo.valor = viejo.valor
        archivo.id_item = id_item
        archivo.nombre_atributo = nombreatributo
        archivo.save()
        valoritems.item_id = id_item
        valoritems.valor_id = archivo.id
        valoritems.tabla_valor_nombre = 'tipoatributo_archivoexterno'
        valoritems.nombre_atributo = nombreatributo
        valoritems.tipo_dato = 'Archivo Externo'
        valoritems.version = versionitem
        valoritems.orden = orden
        valoritems.proyecto_id = id_proyecto
        valoritems.fase_id = id_fase
        valoritems.save()
    elif nombretabla=='tipoatributo_texto':
        archivo = Texto()
        viejo = Texto.objects.get(id=valor_id)
        archivo.valor = viejo.valor
        archivo.id_item = id_item
        archivo.nombre_atributo = nombreatributo
        archivo.longitud = viejo.longitud
        archivo.save()
        valoritems.item_id = id_item
        valoritems.valor_id = archivo.id
        valoritems.tabla_valor_nombre = 'tipoatributo_texto'
        valoritems.nombre_atributo = nombreatributo
        valoritems.tipo_dato = 'Texto'
        valoritems.version = versionitem
        valoritems.orden = orden
        valoritems.proyecto_id = id_proyecto
        valoritems.fase_id = id_fase
        valoritems.save()
    elif nombretabla=='tipoatributo_numerico':
        archivo = Numerico()
        viejo = Numerico.objects.get(id=valor_id)
        archivo.valor = viejo.valor
        archivo.id_item = id_item
        archivo.nombre_atributo = nombreatributo
        archivo.longitud = viejo.longitud
        archivo.precision = viejo.precision
        archivo.save()
        valoritems.item_id = id_item
        valoritems.valor_id = archivo.id
        valoritems.tabla_valor_nombre = 'tipoatributo_numerico'
        valoritems.nombre_atributo = nombreatributo
        valoritems.tipo_dato = 'Numerico'
        valoritems.version = versionitem
        valoritems.orden = orden
        valoritems.proyecto_id = id_proyecto
        valoritems.fase_id = id_fase
        valoritems.save()
    elif nombretabla=='tipoatributo_fecha':
        archivo = Fecha()
        viejo = Fecha.objects.get(id=valor_id)
        archivo.valor = viejo.valor
        archivo.id_item = id_item
        archivo.nombre_atributo = nombreatributo
        archivo.save()
        valoritems.item_id = id_item
        valoritems.valor_id = archivo.id
        valoritems.tabla_valor_nombre = 'tipoatributo_fecha'
        valoritems.nombre_atributo = nombreatributo
        valoritems.tipo_dato = 'Fecha'
        valoritems.version = versionitem
        valoritems.orden = orden
        valoritems.proyecto_id = id_proyecto
        valoritems.fase_id = id_fase
        valoritems.save()
    elif nombretabla=='tipoatributo_logico':
        archivo = Logico()
        viejo = Logico.objects.get(id=valor_id)
        archivo.valor = viejo.valor
        archivo.id_item = id_item
        archivo.nombre_atributo = nombreatributo
        archivo.save()
        valoritems.item_id = id_item
        valoritems.valor_id = archivo.id
        valoritems.tabla_valor_nombre = 'tipoatributo_logico'
        valoritems.nombre_atributo = nombreatributo
        valoritems.tipo_dato = 'Logico'
        valoritems.version = versionitem
        valoritems.orden = orden
        valoritems.proyecto_id = id_proyecto
        valoritems.fase_id = id_fase
        valoritems.save()
    return (True)

def control_ciclo(id_proyecto, id_fase, id_item, id_padre):
    """ Recibe un request, se verifica cual es el usuario registrado y el proyecto del cual se solicita,
    se obtiene la lista de fases con las que estan relacionados el usuario y el proyecto 
    desplegandola en pantalla, ademas permite realizar busquedas avanzadas sobre
    las fases que puede mostrar.
    
    @type request: django.http.HttpRequest.
    @param request: Contiene informacion sobre la solicitud web actual que llamo a esta vista.
    
    @rtype: django.shortcuts.render_to_response.
    @return: fases.html, donde se listan las fases, ademas de las funcionalidades para cada fase.
    
    @author: Ysapy Ortiz.
    
    """
    item = Items.objects.get(id=id_item)
    padre = Items.objects.get(id=id_padre)
    try:
        padre_padre = Items.objects.get(id=padre.padre)
    except Items.DoesNotExist:
        padre_padre = False
    if padre_padre:
            if int(padre.padre)==int(id_item):
                return True
            else:
                if control_ciclo(id_proyecto, id_fase, id_item, padre.padre):
                    return True
    return False

def recorrer_hijos(id_proyecto, id_fase, id_raiz, id_item, is_ciclo):
    """ Recibe un request, se verifica cual es el usuario registrado y el proyecto del cual se solicita,
    se obtiene la lista de fases con las que estan relacionados el usuario y el proyecto 
    desplegandola en pantalla, ademas permite realizar busquedas avanzadas sobre
    las fases que puede mostrar.
    
    @type request: django.http.HttpRequest.
    @param request: Contiene informacion sobre la solicitud web actual que llamo a esta vista.
    
    @rtype: django.shortcuts.render_to_response.
    @return: fases.html, donde se listan las fases, ademas de las funcionalidades para cada fase.
    
    @author: Ysapy Ortiz.
    
    """
    item = Items.objects.get(id=id_item)
    raiz = Items.objects.get(id=id_raiz)
    hijos = []
    try:
        relacioneshijas = Relaciones.objects.filter(padre_id=item.id)
    except Relaciones.DoesNotExists:
        relacioneshijas = False
    if relacioneshijas:
        for relacionhija in relacioneshijas:
            try:
                hijo = Items.objects.get(id=relacionhija.item, is_active=True, version=relacionhija.version, fase_id=item.fase_id)
            except Items.DoesNotExist:
                hijos.append(hijo)
        for hijo in hijos:
            if is_ciclo==False:
                if hijo.id==id_raiz:
                    is_ciclo = True
                    return is_ciclo
                else:
                    is_ciclo = recorrer_hijos(id_proyecto, id_fase, id_raiz, hijo.id, is_ciclo)
    return is_ciclo

def pasar_construccion(id_item):
    """ Recibe un request, se verifica cual es el usuario registrado y el proyecto del cual se solicita,
    se obtiene la lista de fases con las que estan relacionados el usuario y el proyecto 
    desplegandola en pantalla, ademas permite realizar busquedas avanzadas sobre
    las fases que puede mostrar.
    
    @type request: django.http.HttpRequest.
    @param request: Contiene informacion sobre la solicitud web actual que llamo a esta vista.
    
    @rtype: django.shortcuts.render_to_response.
    @return: fases.html, donde se listan las fases, ademas de las funcionalidades para cada fase.
    
    @author: Ysapy Ortiz.
    
    """
    item = Items.objects.get(id=id_item)
    hijos = Items.objects.filter(padre=id_item)
    for hijo in hijos:
        hijo.estado = 'En Construccion'
        hijo.save()
        pasar_construccion(hijo.id)
