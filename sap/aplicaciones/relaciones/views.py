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
from .models import Relaciones, ListaRelaciones

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
        ctx = {'mensaje': mensaje, 'id_proyecto':id_proyecto, 'id_fase': id_fase}
        template_name = './items/itemalerta.html'
        return render_to_response(template_name, ctx, context_instance=RequestContext(request))
    rantecesor = Relaciones.objects.filter(proyecto=id_proyecto, faseprimera=id_fase, antecesor_id=id_item, is_active=True)
    rpadre = Relaciones.objects.filter(proyecto=id_proyecto, faseprimera=id_fase, padre_id=id_item, is_active=True)
    rsucesor = Relaciones.objects.filter(proyecto=id_proyecto, fasesegunda=id_fase, sucesor_id=id_item, is_active=True)
    rhijo = Relaciones.objects.filter(proyecto=id_proyecto, fasesegunda=id_fase, hijo_id=id_item, is_active=True)
    lista_relaciones = []
    
    for antecesor in rantecesor:
        valor = ListaRelaciones()
        valor.itemrelacionado = antecesor.sucesor_id
        valor.tiporelacion = 'Sucesor'
        itemrelacionado = Items.objects.get(id=valor.itemrelacionado)
        valor.nombreitemrelacionado = itemrelacionado.nombre
        valor.save()
        lista_relaciones.append(valor)
    for sucesor in rsucesor:
        valor = ListaRelaciones()
        valor.itemrelacionado = sucesor.antecesor_id
        valor.tiporelacion = 'Antecesor'
        itemrelacionado = Items.objects.get(id=valor.itemrelacionado)
        valor.nombreitemrelacionado = itemrelacionado.nombre
        valor.save()
        lista_relaciones.append(valor)
    for padre in rpadre:
        valor = ListaRelaciones()
        valor.itemrelacionado = padre.hijo_id
        valor.tiporelacion = 'Hijo'
        itemrelacionado = Items.objects.get(id=valor.itemrelacionado)
        valor.nombreitemrelacionado = itemrelacionado.nombre
        valor.save()
        lista_relaciones.append(valor)
    for hijo in rhijo:
        valor = ListaRelaciones()
        valor.itemrelacionado = hijo.padre_id
        valor.tiporelacion = 'Padre'
        itemrelacionado = Items.objects.get(id=valor.itemrelacionado)
        valor.nombreitemrelacionado = itemrelacionado.nombre
        valor.save()
        lista_relaciones.append(valor)

    ctx = {'lista_relaciones': lista_relaciones, 'id_proyecto':id_proyecto, 'id_fase': id_fase, 'id_item': id_item}
    template_name = './relaciones/relaciones.html'
    return render_to_response(template_name, ctx, context_instance=RequestContext(request))

def listar_items(request, id_proyecto, id_fase, id_item):
    proyecto = Proyectos.objects.get(id=id_proyecto)
    fase = Fases.objects.get(id=id_fase)
    item = Items.objects.get(id=id_item)

    itemstodos = Items.objects.filter(proyecto_id=id_proyecto, fase_id=id_fase, is_active=True)
    rantecesor = Relaciones.objects.filter(proyecto=id_proyecto, faseprimera=id_fase, antecesor_id=id_item, is_active=True)
    rpadre = Relaciones.objects.filter(proyecto=id_proyecto, faseprimera=id_fase, padre_id=id_item, is_active=True)
    rsucesor = Relaciones.objects.filter(proyecto=id_proyecto, fasesegunda=id_fase, sucesor_id=id_item, is_active=True)
    rhijo = Relaciones.objects.filter(proyecto=id_proyecto, fasesegunda=id_fase, hijo_id=id_item, is_active=True)
    lista_items = []

    for itemtodo in itemstodos:
        relacionado='Vacio'
        for antecesor in rantecesor:
            if antecesor.sucesor_id==itemtodo.id:
                relacionado = 'Si'
        for sucesor in rsucesor:
            if sucesor.antecesor_id==itemtodo.id:
                relacionado = 'Si'
        for padre in rpadre:
            if padre.hijo_id==itemtodo.id:
                relacionado = 'Si'
        for hijo in rhijo:
            if hijo.padre_id==itemtodo.id:
                relacionado = 'Si'
        
        if itemtodo.id==int(id_item):
            relacionado = 'No'
        if relacionado=='Vacio': 
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
        relacioncreada = Relaciones()
        if (request.POST.get('tiporelacion', ''))=='Padre':
            relacioncreada.padre_id = id_importar
            relacioncreada.faseprimera = itemrelacionado.fase_id
            relacioncreada.hijo_id = id_item
            relacioncreada.fasesegunda = item.fase_id
            relacioncreada.is_active = True
            relacioncreada.proyecto = id_proyecto
        if (request.POST.get('tiporelacion', ''))=='Hijo':
            relacioncreada.hijo_id = id_importar
            relacioncreada.fasesegunda = itemrelacionado.fase_id
            relacioncreada.padre_id = id_item
            relacioncreada.faseprimera = item.fase_id
            relacioncreada.is_active = True
            relacioncreada.proyecto = id_proyecto
        relacioncreada.save()
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
    