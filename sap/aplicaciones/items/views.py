from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect, HttpResponse
from django.template.context import RequestContext
from aplicaciones.proyectos.models import Proyectos
from aplicaciones.fases.models import Fases
from aplicaciones.tipoitem.models import TipoItem
from .models import Items
from datetime import datetime
from django.contrib.auth.decorators import login_required, permission_required
from django.db.models import Q
from forms import ItemNuevoForm

# Create your views here.

def adm_items(request, id_proyecto, id_fase):
    
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

    #lista_items=Items.objects.get(proyecto=id_proyecto, fase=id_fase, is_active=True)
    lista_items = Items.objects.filter(is_active=True)
    mensaje = ''
    ctx = {'lista_items': lista_items, 'mensaje': mensaje, 'id_proyecto':id_proyecto, 'id_fase': id_fase}
    template_name = './items/items.html'
    return render_to_response(template_name, ctx, context_instance=RequestContext(request))

def listar_tipo_item(request, id_proyecto, id_fase):
    fase = Fases.objects.get(id=id_fase)
    if fase.estado =='FD':
        mensaje ='No se pueden agregar items a la fase.'
        ctx = {'mensaje':mensaje, 'id_proyecto': id_proyecto, 'id_fase': id_fase}
        template_name = './items/itemalerta.html'
        return render_to_response(template_name, ctx, context_instance=RequestContext(request))
    else:
        lista_tipo_item = TipoItem.objects.filter(id_proyecto=id_proyecto, is_active=True)
    ctx={'lista_tipo_item':lista_tipo_item, 'id_proyecto':id_proyecto, 'id_fase':id_fase}
    template_name = './items/listartipos.html'
    return render_to_response(template_name, ctx, context_instance=RequestContext(request))

"""def elegir_tipo_item (request, id_proyecto, id_fase, id_tipoitem):
    cantidad = len(ordenar_mantener (id_tipoitem))
    lista_atributos = ordenar_mantener(id_tipoitem)
    if request.method == 'POST':
        for lista in lista_atributos:
            atributo = TipoAtributo.objects.get(id=lista.id_atributo)
            tipodato = atributo.tipo
            if (tipodato=='Numerico'):
                form = AtributoNumericoForm(request.POST)
                if form.is_valid():
"""
def crear_item(request, id_proyecto, id_fase, id_tipoitem):
    proyecto = Proyectos.objects.get(id=id_proyecto)
    fase = Fases.objects.get(id=id_fase)
    if fase.estado == 'FD':
        mensaje = 'No se pueden agregar items a la fase.'
        ctx = {'mensaje':mensaje, 'id_proyecto': id_proyecto}
        template_name = './items/itemalerta.html'
        return render_to_response(template_name, ctx, context_instance=RequestContext(request))
    if request.method == 'POST':
        form = ItemNuevoForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['Nombre_de_Item']
            prioridad = form.cleaned_data['Prioridad']
            descripcion = form.cleaned_data['Descripcion']
            observaciones = form.cleaned_data['Observaciones']
            costo_temporal = form.cleaned_data['Costo_Temporal']
            costo_monetario = form.cleaned_data['Costo_Monetario']
            complejidad = form.cleaned_data['Complejidad']
            
            item = Items()
            item.nombre = nombre
            item.version = '1'
            item.prioridad = prioridad
            item.estado = 'En Construccion'
            item.descripcion = descripcion
            item.observaciones = observaciones
            item.costoMonetario = costo_monetario
            item.costoTemporal = costo_temporal
            item.complejidad = complejidad
            item.proyecto_id = id_proyecto
            item.fase_id = id_fase
            item.is_active = True
            item.tipo_item_id = id_tipoitem
            
            item.save()
            id_item = item.id
            template_name='./items/cargaratributos.html'
            lista_atributos = ordenar_mantener(id_tipoitem)
            return render(request, template_name, {'id_proyecto': id_proyecto, 'id_fase': id_fase, 'id_item': id_item, 'id_tipoitem': id_tipoitem, 'lista_atributos': lista_atributos})
    else: 
        form = ItemNuevoForm()    
        
    template_name='./items/itemnuevo.html'
    return render(request, template_name, {'form': form, 'id_proyecto':id_proyecto, 'id_fase': id_fase, 'id_tipoitem': id_tipoitem})