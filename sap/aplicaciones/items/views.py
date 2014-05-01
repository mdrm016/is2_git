from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect, HttpResponse
from django.template.context import RequestContext
from aplicaciones.proyectos.models import Proyectos
from aplicaciones.fases.models import Fases
from aplicaciones.tipoitem.models import TipoItem
from aplicaciones.tipoatributo.models import TipoAtributo, Numerico, Fecha, Texto, Imagen
from .models import Items, ListaValores, ValorItem
from datetime import datetime
from django.contrib.auth.decorators import login_required, permission_required
from django.db.models import Q
from forms import ItemNuevoForm
from aplicaciones.tipoitem.views import ordenar_mantener

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
    lista_items = Items.objects.filter(proyecto_id=id_proyecto, fase_id=id_fase, is_active=True)
    mensaje = ''
    ctx = {'lista_items': lista_items, 'mensaje': mensaje, 'id_proyecto':id_proyecto, 'id_fase': id_fase}
    template_name = './items/items.html'
    return render_to_response(template_name, ctx, context_instance=RequestContext(request))

def listar_tipo_item(request, id_proyecto, id_fase):
    fase = Fases.objects.get(id=id_fase)
    proyecto = Proyectos.objects.get(id=id_proyecto)
    if fase.estado =='FD' or proyecto.estado=='Inactivo':
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
            repetido = 'Vacio'
            rep= Items.objects.filter(proyecto_id=id_proyecto, fase_id=id_fase, is_active=True, nombre=nombre)
            if rep:
                mensaje = 'El nombre de item ya existe para esta fase'
                data = {'Nombre_de_Item': nombre, 'Prioridad': prioridad, 'Descripcion': descripcion, 'Observaciones': observaciones, 'Costo_Temporal': costo_temporal, 'Costo_Monetario': costo_monetario, 'Complejidad': complejidad}
                form = ItemNuevoForm(data)
                ctx = {'form': form, 'mensaje':mensaje, 'id_proyecto': id_proyecto, 'id_fase': id_fase, 'id_tipoitem': id_tipoitem}
                template_name = 'items/itemnuevo.html'
                return render_to_response(template_name, ctx, context_instance=RequestContext(request))
            
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
            

            mensaje = 'Item creado con exito.'
            template_name='./items/itemalerta.html'
            ctx = {'mensaje': mensaje, 'id_proyecto':id_proyecto, 'id_fase': id_fase}
            return render_to_response(template_name, ctx, context_instance=RequestContext(request))
                
            #return render(request, template_name, {'id_proyecto': id_proyecto, 'id_fase': id_fase, 'id_item': id_item, 'id_tipoitem': id_tipoitem, 'lista_valores': lista_valores, 'lista_atributos': lista_atributos})
    else: 
        form = ItemNuevoForm()  
        
    template_name='./items/itemnuevo.html'
    return render(request, template_name, {'form': form, 'id_proyecto':id_proyecto, 'id_fase': id_fase, 'id_tipoitem': id_tipoitem})

def cargar_valores(request, id_proyecto, id_fase, id_item):
    proyecto = Proyectos.objects.get(id=id_proyecto)
    fase = Fases.objects.get(id=id_fase)
    itemactual = Items.objects.filter(id=id_item)
    if fase.estado == 'FD' or proyecto.estado=='Inactivo':
        mensaje = 'No se pueden modificar atributos. Dirijase a consultar item.'
        ctx = {'mensaje':mensaje, 'id_proyecto': id_proyecto}
        template_name = './items/itemalerta.html'
        return render_to_response(template_name, ctx, context_instance=RequestContext(request))
    if request.method=='POST':
        for j in itemactual:
            idtipoitem = j.tipo_item_id
            versionitem = j.version
        lista_atributos = ordenar_mantener(idtipoitem)
        i = 1
        posicion = 1
        for listaatributo in lista_atributos:
            nombreatributo = listaatributo.nombre
            idatributo = listaatributo.id_atributo
            iditematributo = listaatributo.id_tipoitem 
            tipoatributoobjetos = TipoAtributo.objects.filter(id=listaatributo.id_atributo)
            valoritems = ValorItem()
            for tipoatributoobjeto in tipoatributoobjetos:
                tipodatoatributo= tipoatributoobjeto.tipo
            if tipodatoatributo=='Archivo Externo':
                archivo = ArchivoExterno()
                archivo.valor = request.FILE[str(i)]
                archivo.id_item = id_item
                archivo.nombre_atributo = nombreatributo
                archivo.save()
                valoritems.item_id = id_item
                valoritems.valor_id = archivo.id
                valoritems.tabla_valor_nombre = 'tipoatributo_archivoexterno'
                valoritems.version = versionitem
                valoritems.orden = posicion
                valoritems.proyecto_id = id_proyecto
                valoritems.fase_id = id_fase
                valoritems.save()
            elif tipodatoatributo=='Texto':
                archivo = Texto()
                archivo.valor = request.POST.get(str(i), '')
                archivo.id_item = id_item
                archivo.nombre_atributo = nombreatributo
                for tipoatributoobjeto in tipoatributoobjetos:
                    archivo.longitud = tipoatributoobjeto.longitud
                archivo.save()
                valoritems.item_id = id_item
                valoritems.valor_id = archivo.id
                valoritems.tabla_valor_nombre = 'tipoatributo_texto'
                valoritems.version = versionitem
                valoritems.orden = posicion
                valoritems.proyecto_id = id_proyecto
                valoritems.fase_id = id_fase
                valoritems.save()
            elif tipodatoatributo=='Numerico':
                archivo = Numerico()
                archivo.valor = request.POST.get(str(i), '')
                archivo.id_item = id_item
                archivo.nombre_atributo = nombreatributo
                for tipoatributoobjeto in tipoatributoobjetos:
                    archivo.longitud = tipoatributoobjeto.longitud
                    archivo.precision = tipoatributoobjeto.precision
                archivo.save()
                valoritems.item_id = id_item
                valoritems.valor_id = archivo.id
                valoritems.tabla_valor_nombre = 'tipoatributo_numerico'
                valoritems.version = versionitem
                valoritems.orden = posicion
                valoritems.proyecto_id = id_proyecto
                valoritems.fase_id = id_fase
                valoritems.save()
            elif tipodatoatributo=='Fecha':
                archivo = Fecha()
                archivo.valor = request.POST.get(str(i), '')
                archivo.id_item = id_item
                archivo.nombre_atributo = nombreatributo
                archivo.save()
                valoritems.item_id = id_item
                valoritems.valor_id = archivo.id
                valoritems.tabla_valor_nombre = 'tipoatributo_fecha'
                valoritems.version = versionitem
                valoritems.orden = posicion
                valoritems.proyecto_id = id_proyecto
                valoritems.fase_id = id_fase
                valoritems.save()
            elif tipodatoatributo=='Logico':
                archivo = Logico()
                archivo.valor = request.POST.get(str(i), '')
                archivo.id_item = id_item
                archivo.nombre_atributo = nombreatributo
                archivo.save()
                valoritems.item_id = id_item
                valoritems.valor_id = archivo.id
                valoritems.tabla_valor_nombre = 'tipoatributo_logico'
                valoritems.version = versionitem
                valoritems.orden = posicion
                valoritems.proyecto_id = id_proyecto
                valoritems.fase_id = id_fase
                valoritems.save()
            i = i+1
            posicion = posicion+1

        mensaje = 'Item creado con exito.'
        template_name='./items/itemalerta.html'
        ctx = {'mensaje': mensaje, 'id_proyecto':id_proyecto, 'id_fase': id_fase,}
        return render_to_response(template_name, ctx, context_instance=RequestContext(request))
        
    for j in itemahora:
        idtipo = j.tipo_item_id
       
    lista_atributos = ordenar_mantener(idtipo)
    lista_valores = []
    orden = 0
    for i in lista_atributos:
        tipoat = TipoAtributo.objects.filter(id=i.id_atributo)
        for tipoatrib in tipoat:
            tipo = tipoatrib.tipo
        orden = orden + 1
        valorfuturo = ListaValores()
        valorfuturo.nombre_atributo = i.nombre
        valorfuturo.tipo_dato = tipo
        valorfuturo.valor = ""
        valorfuturo.orden = orden
        valorfuturo.save()
        lista_valores.append(valorfuturo)
        
    template_name='./items/cargaratributos.html'
    return render(request, template_name, {'id_proyecto':id_proyecto, 'id_fase': id_fase, 'id_tipoitem': idtipo, 'lista_valores': lista_valores, 'id_item': id_item})        