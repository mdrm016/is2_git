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
from .models import Relaciones, ListaRelacion, VersionRelacion

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
    
    try:
        padre = Items.objects.get(id=item.padre)
    except Items.DoesNotExist:
        padre = Items()

    ctx = {'id_proyecto':id_proyecto, 'id_fase': id_fase, 'id_item': id_item, 'padre': padre, 'proyecto':proyecto, 'fase':fase}
    template_name = './relaciones/relaciones.html'
    return render_to_response(template_name, ctx, context_instance=RequestContext(request))

def listar_items(request, id_proyecto, id_fase, id_item):
    proyecto = Proyectos.objects.get(id=id_proyecto)
    fase = Fases.objects.get(id=id_fase)
    item = Items.objects.get(id=id_item)

    itemstodos = Items.objects.filter(proyecto_id=id_proyecto, fase_id=id_fase, is_active=True).exclude(id=id_item)
    relacionesactuales = VersionRelacion.objects.filter(item_id=id_item, version=item.version)
    lista_items=[]
    for itemtodo in itemstodos:
        relacionado=False
        for relaciones in relacionesactuales:
            relacion = Relacion.objects.get(id=itemtodo.relacion_id)
            if relacion.hijo==itemtodo.id and relacion.hijo!=int(id_item):
                relacionado=True
            elif relacion.padre==itemtodo.id and relacion.padre!=int(id_item):
                relacionado=True
        if not relacionado:
            lista_items.append(itemtodo)
    
    ctx = {'lista_items': lista_items, 'id_proyecto': id_proyecto, 'id_fase': id_fase, 'id_item': id_item}
    template_name = './relaciones/relacionnueva.html'
    return render_to_response(template_name, ctx, context_instance=RequestContext(request))

def crear_relacion(request, id_proyecto, id_fase, id_item, id_importar):
    proyecto = Proyectos.objects.get(id=id_proyecto)    
    fase = Fases.objects.get(id=id_fase)
    item = Items.objects.get(id=id_item)
    itemrelacionado = Items.objects.get(id=id_importar)
    
    if request.method=='POST':
        nuevo = Relaciones()
        if request.POST.get('tiporelacion', '')=='Padre' or request.POST.get('tiporelacion', '')=='Antecesor':
            if item.padre!=0:
                mensaje ='El item ya posee un padre/antecesor. No se pudo crear la relacion.'
                ctx = {'mensaje': mensaje, 'id_proyecto': id_proyecto, 'id_fase': id_fase, 'id_item': id_item}
                template_name = './relaciones/relacionalerta.html'
                return render_to_response(template_name, ctx, context_instance=RequestContext(request))
            nuevo.padre = id_importar
            nuevo.hijo = id_item
            item.padre = id_importar
        nuevo.is_active=True
        nuevo.save()
        relacion_version = VersionRelacion()
        relacion_version.item_id = id_item
        relacion_version.relacion_id = nuevo.id
        relacion_version.version = item.version + 1
        relacion_version.save()
        relacion_version = VersionRelacion()
        relacion_version.item_id = id_importar
        relacion_version.relacion_id = nuevo.id
        relacion_version.version = itemrelacionado.version
        relacion_version.save()
        
        item1 = ValorItem.objects.filter(item_id=id_item, fase_id=id_fase, proyecto_id=id_proyecto, version=item.version).order_by('orden')
        
        for itemvalor in item1:
            if not (cargar_atributos(itemvalor.valor_id, itemvalor.nombre_atributo, itemvalor.orden, itemvalor.tabla_valor_nombre, id_proyecto, id_fase, id_item)):
                estamosenproblemas.append(gkcmt)
                
        item.version = item.version + 1
        item.save()
        mensaje = 'La relacion ha sido creada con exito.'
        id_item = int(id_item)
        
        ctx = {'mensaje': mensaje, 'id_proyecto': id_proyecto, 'id_fase': id_fase, 'id_item': id_item}
        template_name = './relaciones/relacionalerta.html'
        return render_to_response(template_name, ctx, context_instance=RequestContext(request))
    else:
        mensaje = 'El item seleccionado sera (seleccione opcion) del item actual: '
        ctx = {'mensaje': mensaje, 'id_proyecto': id_proyecto, 'id_fase': id_fase, 'id_item': id_item, 'id_importar': id_importar}
    template_name = './relaciones/tiporelacion.html'
    return render_to_response(template_name, ctx, context_instance=RequestContext(request))
    
def eliminar_relacion(request, id_proyecto, id_fase, id_item, id_relacion):
    proyecto = Proyectos.objects.get(id=id_proyecto)
    fase = Fases.objects.get(id=id_fase)
    item1 = Items.objects.get(id=id_item)
    relacion = Relaciones.objects.get(id=id_relacion)
    item2 = Items.objects.get(id=relacion.padre)
    
    if proyecto.estado=='Inactivo' or proyecto.estado=='Finalizado' or fase.estado=='FD' or item1.estado=='En Revision' or item1.estado=='Bloqueado' or item1.estado=='Validado' or item2.estado=='En Revision' or item2.estado=='Bloqueado' or item2.estado=='Validado':
        mensaje = 'No se puede eliminar la relacion. Dirijase a consultar item.'
        ctx = {'mensaje': mensaje, 'id_proyecto': id_proyecto, 'id_fase': id_fase, 'id_item': id_item, 'id_relacion': id_relacion}
        template_name = './relaciones/relacionalerta.html'
        return render_to_response(template_name, ctx, context_instance=RequestContext(request))
    
    itemvalor1 = ValorItem.objects.filter(item_id=item1.id, fase_id=id_fase, proyecto_id=id_proyecto, version=item1.version).order_by('orden')
    
    for itemvalor in itemvalor1:
        if not (cargar_atributos(itemvalor.valor_id, itemvalor.nombre_atributo, itemvalor.orden, itemvalor.tabla_valor_nombre, id_proyecto, id_fase, int(item1.id))):
            estamosenproblemas.append(gkcmt)
            
    if item1.estado=='Terminado':
        item1.estado='En Construccion'

    item1.version = item1.version + 1
    item1.save()
    
    mensaje = 'Relacion eliminada con exito.'
    ctx = {'mensaje': mensaje, 'id_proyecto': id_proyecto, 'id_fase': id_fase, 'id_item': id_item, 'id_relacion': id_relacion}
    template_name = './relaciones/relacionalerta.html'
    return render_to_response(template_name, ctx, context_instance=RequestContext(request))

def cargar_atributos(valor_id, nombreatributo, orden, nombretabla, id_proyecto, id_fase, id_item):
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

def aumentar_version(lista_relaciones, item):
    for relacion in lista_relaciones:
        nuevo = VersionRelacion()
        nuevo.relacion_id = relacion.relacion
        nuevo.item_id = relacion.item_id
        nuevo.version = item.version + 1
        nuevo.save()
    return ()