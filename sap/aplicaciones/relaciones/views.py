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
    rantecesor = Relaciones.objects.filter(proyecto=id_proyecto, faseprimera=id_fase, antecesor_id=id_item, is_active=True, versionprimero=item.version)
    rpadre = Relaciones.objects.filter(proyecto=id_proyecto, faseprimera=id_fase, padre_id=id_item, is_active=True, versionprimero=item.version)
    rsucesor = Relaciones.objects.filter(proyecto=id_proyecto, fasesegunda=id_fase, sucesor_id=id_item, is_active=True, versionsegundo=item.version)
    rhijo = Relaciones.objects.filter(proyecto=id_proyecto, fasesegunda=id_fase, hijo_id=id_item, is_active=True, versionsegundo=item.version)
    lista_relaciones = []
    
    for antecesor in rantecesor:
        valor = ListaRelaciones()
        valor.itemrelacionado = antecesor.sucesor_id
        valor.tiporelacion = 'Sucesor'
        itemrelacionado = Items.objects.get(id=valor.itemrelacionado)
        valor.nombreitemrelacionado = itemrelacionado.nombre
        valor.relacionid = antecesor.id
        valor.save()
        antecesor_sucesor = Items.objects.get(id=antecesor.sucesor_id)
        if antecesor.versionsegundo==antecesor_sucesor.version:
            lista_relaciones.append(valor)
    for sucesor in rsucesor:
        valor = ListaRelaciones()
        valor.itemrelacionado = sucesor.antecesor_id
        valor.tiporelacion = 'Antecesor'
        itemrelacionado = Items.objects.get(id=valor.itemrelacionado)
        valor.nombreitemrelacionado = itemrelacionado.nombre
        valor.relacionid = sucesor.id
        valor.save()
        sucesor_antecesor = Items.objects.get(id=sucesor.antecesor_id)
        if sucesor.versionprimero==sucesor_antecesor.version:
            lista_relaciones.append(valor)
    for padre in rpadre:
        valor = ListaRelaciones()
        valor.itemrelacionado = padre.hijo_id
        valor.tiporelacion = 'Hijo'
        itemrelacionado = Items.objects.get(id=valor.itemrelacionado)
        valor.nombreitemrelacionado = itemrelacionado.nombre
        valor.relacionid = padre.id
        valor.save()
        padre_hijo = Items.objects.get(id=padre.hijo_id)
        if padre.versionsegundo==padre_hijo.version:
            lista_relaciones.append(valor)
    for hijo in rhijo:
        valor = ListaRelaciones()
        valor.itemrelacionado = hijo.padre_id
        valor.tiporelacion = 'Padre'
        itemrelacionado = Items.objects.get(id=valor.itemrelacionado)
        valor.nombreitemrelacionado = itemrelacionado.nombre
        valor.relacionid = hijo.id
        valor.save()
        hijo_padre = Items.objects.get(id=hijo.padre_id)
        if hijo.versionprimero==hijo_padre.version:
            lista_relaciones.append(valor)

    ctx = {'lista_relaciones': lista_relaciones, 'id_proyecto':id_proyecto, 'id_fase': id_fase, 'id_item': id_item}
    template_name = './relaciones/relaciones.html'
    return render_to_response(template_name, ctx, context_instance=RequestContext(request))

def listar_items(request, id_proyecto, id_fase, id_item):
    proyecto = Proyectos.objects.get(id=id_proyecto)
    fase = Fases.objects.get(id=id_fase)
    item = Items.objects.get(id=id_item)

    itemstodos = Items.objects.filter(proyecto_id=id_proyecto, fase_id=id_fase, is_active=True)
    rantecesor = Relaciones.objects.filter(proyecto=id_proyecto, faseprimera=id_fase, antecesor_id=id_item, is_active=True, versionprimero=item.version)
    rpadre = Relaciones.objects.filter(proyecto=id_proyecto, faseprimera=id_fase, padre_id=id_item, is_active=True, versionprimero=item.version)
    rsucesor = Relaciones.objects.filter(proyecto=id_proyecto, fasesegunda=id_fase, sucesor_id=id_item, is_active=True, versionsegundo=item.version)
    rhijo = Relaciones.objects.filter(proyecto=id_proyecto, fasesegunda=id_fase, hijo_id=id_item, is_active=True, versionsegundo=item.version)
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
    versionnueva = item.version+1
    versionnueva2 = itemrelacionado.version+1
    
    if request.method=='POST':
            
        item1 = ValorItem.objects.filter(item_id=id_item, fase_id=id_fase, proyecto_id=id_proyecto, version=item.version).order_by('orden')
        item2 = ValorItem.objects.filter(item_id=id_importar, fase_id=id_fase, proyecto_id=id_proyecto, version=itemrelacionado.version).order_by('orden')
        
        rpadre1 = Relaciones.objects.filter(padre_id=id_item, versionprimero=item.version, is_active=True)
        rpadre2 = Relaciones.objects.filter(padre_id=id_importar, versionprimero=itemrelacionado.version, is_active=True)
        rantecesor1 = Relaciones.objects.filter(antecesor_id=id_item, versionprimero=item.version, is_active=True)
        rantecesor2 = Relaciones.objects.filter(antecesor_id=id_importar, versionprimero=itemrelacionado.version, is_active=True)
        rhijo1 = Relaciones.objects.filter(hijo_id=id_item, versionsegundo=item.version, is_active=True)
        rhijo2 = Relaciones.objects.filter(hijo_id=id_importar, versionsegundo=itemrelacionado.version, is_active=True)
        rsucesor1 = Relaciones.objects.filter(sucesor_id=id_item, versionsegundo=item.version, is_active=True)
        rsucesor2 = Relaciones.objects.filter(sucesor_id=id_importar, versionsegundo=itemrelacionado.version, is_active=True)
        
        listap1 = []
        listap1.extend(rpadre1)
        listap1.extend(rantecesor1)
        listap2 = []
        listap2.extend(rpadre2)
        listap2.extend(rantecesor2)
        listas1 = []
        listas1.extend(rhijo1)
        listas1.extend(rsucesor1)
        listas2 = []
        listas2.extend(rhijo2)
        listas2.extend(rsucesor2)
        
        for itemvalor in item1:
            if not (cargar_atributos(itemvalor.valor_id, itemvalor.nombre_atributo, itemvalor.orden, itemvalor.tabla_valor_nombre, id_proyecto, id_fase, id_item)):
                estamosenproblemas.append(gkcmt)
        for p1 in listap1:
            if not (version_relacion(p1, int(id_item))):
                estamosenproblemas.append(gkcmt)
        for s1 in listas1:
            if not (version_relacion(s1, int(id_item))):
                estamosenproblemas.append(gkcmt)
        
        for itemvalor in item2:
            if not (cargar_atributos(itemvalor.valor_id, itemvalor.nombre_atributo, itemvalor.orden, itemvalor.tabla_valor_nombre, id_proyecto, id_fase, id_importar)):
                estamosenproblemas2.append(gkcmt)
        for p2 in listap2:
            if not (version_relacion(p2, int(id_importar))):
                estamosenproblemas.append(gkcmt)
        for s2 in listas2:
            if not (version_relacion(s2, int(id_importar))):
                estamosenproblemas.append(gkcmt)
                
        relacioncreada = Relaciones()
        if (request.POST.get('tiporelacion', ''))=='Padre':
            relacioncreada.padre_id = id_importar
            relacioncreada.faseprimera = itemrelacionado.fase_id
            relacioncreada.hijo_id = id_item
            relacioncreada.fasesegunda = item.fase_id
            relacioncreada.is_active = True
            relacioncreada.proyecto = id_proyecto
            relacioncreada.versionsegundo = versionnueva
            relacioncreada.versionprimero = versionnueva2
            relacioncreada.save()
        if (request.POST.get('tiporelacion', ''))=='Hijo':
            relacioncreada.hijo_id = id_importar
            relacioncreada.fasesegunda = itemrelacionado.fase_id
            relacioncreada.padre_id = id_item
            relacioncreada.faseprimera = item.fase_id
            relacioncreada.is_active = True
            relacioncreada.proyecto = id_proyecto
            relacioncreada.versionprimero = versionnueva
            relacioncreada.versionsegundo = versionnueva2
            relacioncreada.save()        
        
        item.version = versionnueva
        item.save()
        itemrelacionado.version = versionnueva2
        itemrelacionado.save()
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
    itemaca = Items.objects.get(id=id_item)
    relacion = Relaciones.objects.get(id=id_relacion)
    if relacion.padre_id==id_item:
        itemotro = Items.objects.get(id=relacion.hijo_id)
    else:
        itemotro = Items.objects.get(id=relacion.padre_id)
    
    #if proyecto.estado=='Inactivo' or proyecto.estado=='Finalizado' or fase.estado=='FD' or itempadre.estado=='En Revision' or itempadre.estado=='Bloqueado' or itempadre.estado=='Validado' or itemhijo.estado=='En Revision' or itemhijo.estado=='Bloqueado' or itemhijo.estado=='Validado':
     #   mensaje = 'No se puede eliminar la relacion. Dirijase a consultar item.'
      #  ctx = {'mensaje': mensaje, 'id_proyecto': id_proyecto, 'id_fase': id_fase, 'id_item': id_item, 'id_relacion': id_relacion}
       # template_name = './relaciones/relacionalerta.html'
        #return render_to_response(template_name, ctx, context_instance=RequestContext(request))
    
    item1 = ValorItem.objects.filter(item_id=id_item, fase_id=id_fase, proyecto_id=id_proyecto, version=itemaca.version).order_by('orden')
    item2 = ValorItem.objects.filter(item_id=itemotro.id, fase_id=id_fase, proyecto_id=id_proyecto, version=itemotro.version).order_by('orden')
    
    rpadre1 = Relaciones.objects.filter(padre_id=itemaca.id, versionprimero=itemaca.version, is_active=True).exclude(id=id_relacion)
    rpadre2 = Relaciones.objects.filter(padre_id=itemotro.id, versionprimero=itemotro.version, is_active=True).exclude(id=id_relacion)
    rantecesor1 = Relaciones.objects.filter(antecesor_id=itemaca.id, versionprimero=itemaca.version, is_active=True).exclude(id=id_relacion)
    rantecesor2 = Relaciones.objects.filter(padre_id=itemotro.id, versionprimero=itemotro.version, is_active=True).exclude(id=id_relacion)
    rhijo1 = Relaciones.objects.filter(hijo_id=itemaca.id, versionsegundo=itemaca.version, is_active=True).exclude(id=id_relacion)
    rhijo2 = Relaciones.objects.filter(hijo_id=itemotro.id, versionsegundo=itemotro.version, is_active=True).exclude(id=id_relacion)
    rsucesor1 = Relaciones.objects.filter(sucesor_id=itemaca.id, versionsegundo=itemaca.version, is_active=True).exclude(id=id_relacion)
    rsucesor2 = Relaciones.objects.filter(sucesor_id=itemotro.id, versionsegundo=itemotro.version, is_active=True).exclude(id=id_relacion)
        
    listap1 = []
    listap1.extend(rpadre1)
    listap1.extend(rantecesor1)
    listap2 = []
    listap2.extend(rpadre2)
    listap2.extend(rantecesor2)
    listas1 = []
    listas1.extend(rhijo1)
    listas1.extend(rsucesor1)
    listas2 = []
    listas2.extend(rhijo2)
    listas2.extend(rsucesor2)
    
    for itemvalor in item1:
        if not (cargar_atributos(itemvalor.valor_id, itemvalor.nombre_atributo, itemvalor.orden, itemvalor.tabla_valor_nombre, id_proyecto, id_fase, int(id_item))):
            estamosenproblemas.append(gkcmt)
    for p1 in listap1:
        if not (version_relacion(p1, int(itemaca.id))):
            estamosenproblemas.append(gkcmt)

    for s1 in listas1:
        if not (version_relacion(s1, int(itemaca.id))):
            estamosenproblemas.append(gkcmt)
    
    for itemvalor in item2:
        if not (cargar_atributos(itemvalor.valor_id, itemvalor.nombre_atributo, itemvalor.orden, itemvalor.tabla_valor_nombre, id_proyecto, id_fase, int(itemotro.id))):
            estamosenproblemas2.append(gkcmt)
            
    for p2 in listap2:
        if not (version_relacion(p2, int(itemotro.id))):
            estamosenproblemas.append(gkcmt)
            
    for s2 in listas2:
        if not (version_relacion(s2, int(itemotro.id))):
            estamosenproblemas.append(gkcmt)
        
    if itemaca.estado=='Terminado':
        itemaca.estado='En Construccion'
    if itemotro.estado=='Terminado':
        itemotro.estado = 'En Construccion'

    itemaca.version = itemaca.version + 1
    itemotro.version = itemotro.version + 1
    eliminada = Relaciones()
    eliminada.padre_id = relacion.padre_id
    eliminada.antecesor_id = relacion.antecesor_id
    eliminada.sucesor_id = relacion.sucesor_id
    eliminada.hijo_id = relacion.hijo_id
    eliminada.faseprimera = relacion.faseprimera
    eliminada.fasesegunda = relacion.fasesegunda
    eliminada.is_active=True
    eliminada.proyecto = relacion.proyecto
    eliminada.versionprimero = relacion.versionprimero
    eliminada.versionsegundo = relacion.versionsegundo
    
    eliminada.save()
    relacion.is_active=False
    relacion.save()
    itemaca.save()
    itemotro.save()
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

def version_relacion(relacion, item):
    
    if relacion.antecesor_id==item:
        sucesor = Items.objects.get(id=relacion.sucesor_id)
        if relacion.versionsegundo==sucesor.version:
            relacionnueva = Relaciones()
            relacionnueva.padre_id = relacion.padre_id
            relacionnueva.hijo_id = relacion.hijo_id
            relacionnueva.antecesor_id = relacion.antecesor_id
            relacionnueva.sucesor_id = relacion.sucesor_id
            relacionnueva.is_active = True
            relacionnueva.proyecto = relacion.proyecto
            relacionnueva.faseprimera = relacion.faseprimera
            relacionnueva.fasesegunda = relacion.fasesegunda
            relacionnueva.versionprimero = relacion.versionprimero +1
            relacionnueva.versionsegundo = relacion.versionsegundo
            relacionnueva.save()
    elif  relacion.padre_id==item:
        hijo = Items.objects.get(id=relacion.hijo_id)
        if relacion.versionsegundo==hijo.version:
            relacionnueva = Relaciones()
            relacionnueva.padre_id = relacion.padre_id
            relacionnueva.hijo_id = relacion.hijo_id
            relacionnueva.antecesor_id = relacion.antecesor_id
            relacionnueva.sucesor_id = relacion.sucesor_id
            relacionnueva.is_active = True
            relacionnueva.proyecto = relacion.proyecto
            relacionnueva.faseprimera = relacion.faseprimera
            relacionnueva.fasesegunda = relacion.fasesegunda
            relacionnueva.versionprimero = relacion.versionprimero +1
            relacionnueva.versionsegundo = relacion.versionsegundo
            relacionnueva.save()
    elif relacion.sucesor_id==item:
        antecesor = Items.objects.get(id=relacion.antecesor_id)
        if relacion.versionprimero==antecesor.version:
            relacionnueva = Relaciones()
            relacionnueva.padre_id = relacion.padre_id
            relacionnueva.hijo_id = relacion.hijo_id
            relacionnueva.antecesor_id = relacion.antecesor_id
            relacionnueva.sucesor_id = relacion.sucesor_id
            relacionnueva.is_active = True
            relacionnueva.proyecto = relacion.proyecto
            relacionnueva.faseprimera = relacion.faseprimera
            relacionnueva.fasesegunda = relacion.fasesegunda
            relacionnueva.versionprimero = relacion.versionprimero
            relacionnueva.versionsegundo = relacion.versionsegundo + 1
            relacionnueva.save()
    elif relacion.hijo_id==item:
        padre = Items.objects.get(id=relacion.padre_id)
        if relacion.versionprimero==padre.version:
            relacionnueva = Relaciones()
            relacionnueva.padre_id = relacion.padre_id
            relacionnueva.hijo_id = relacion.hijo_id
            relacionnueva.antecesor_id = relacion.antecesor_id
            relacionnueva.sucesor_id = relacion.sucesor_id
            relacionnueva.is_active = True
            relacionnueva.proyecto = relacion.proyecto
            relacionnueva.faseprimera = relacion.faseprimera
            relacionnueva.fasesegunda = relacion.fasesegunda
            relacionnueva.versionprimero = relacion.versionprimero
            relacionnueva.versionsegundo = relacion.versionsegundo + 1
            relacionnueva.save()
    return (True)

def relacion_nueva_version(relacion, primero, segundo):
    nuevo = Relaciones()
    if (segundo):
        if (relacion.padre_id==primero.id):
            nuevo.padre_id = primero.id
            nuevo.hijo_id = segundo.id
            nuevo.antecesor_id = relacion.antecesor_id
            nuevo.sucesor_id = relacion.sucesor_id
            nuevo.faseprimera = relacion.faseprimera
            nuevo.fasesegunda = relacion.fasesegunda
            nuevo.proyecto = relacion.proyecto
            nuevo.is_active = True
            nuevo.versionprimero = primero.version + 1
            nuevo.versionsegundo = segundo.version + 1
        elif (relacion.hijo_id==primero.id):
            nuevo.padre_id = segundo.id
            nuevo.hijo_id = primero.id
            nuevo.antecesor_id = relacion.antecesor_id
            nuevo.sucesor_id = relacion.sucesor_id
            nuevo.faseprimera = relacion.faseprimera
            nuevo.fasesegunda = relacion.fasesegunda
            nuevo.proyecto = relacion.proyecto
            nuevo.is_active = True
            nuevo.versionprimero = segundo.version + 1
            nuevo.versionsegundo = primero.version + 1
        elif (relacion.antecesor_id==primero_id):
            nuevo.antecesor_id = primero.id
            nuevo.sucesor_id = segundo.id
            nuevo.hijo_id = relacion.hijo_id
            nuevo.padre_id = relacion.padre_id
            nuevo.faseprimera = relacion.faseprimera
            nuevo.fasesegunda = relacion.fasesegunda
            nuevo.proyecto = relacion.proyecto
            nuevo.is_active = True
            nuevo.versionprimero = primero.version + 1
            nuevo.versionsegundo = segundo.version + 1
        elif (relacion.sucesor_id==primero):
            nuevo.antecesor_id = segundo.id
            nuevo.sucesor_id = primero.id
            nuevo.hijo_id = relacion.hijo_id
            nuevo.padre_id = relacion.padre_id
            nuevo.faseprimera = relacion.faseprimera
            nuevo.fasesegunda = relacion.fasesegunda
            nuevo.proyecto = relacion.proyecto
            nuevo.is_active = True
            nuevo.versionprimero = segundo.version + 1
            nuevo.versionsegundo = primero.version + 1
    else:
        if relacion.padre_id==primero.id:
            nuevo.versionprimero = primero.version + 1
            nuevo.versionsegundo = relacion.versionsegundo
        elif relacion.hijo_id==primero.id:
            nuevo.versionsegundo = primero.version + 1
            nuevo.versionprimero = relacion.versionsegundo
        elif relacion.antecesor_id==primero.id:
            nuevo.versionprimero = primero.version + 1
            nuevo.versionsegundo = relacion.versionsegundo
        elif relacion.sucesor_id==primero.id:
            nuevo.versionsegundo = primero.version + 1
            nuevo.versionprimero = relacion.versionsegundo
        nuevo.padre_id = relacion.padre_id
        nuevo.hijo_id = relacion.hijo_id
        nuevo.sucesor_id = relacion.sucesor_id
        nuevo.antecesor_id = relacion.antecesor_id
        nuevo.is_active = True
        nuevo.proyecto = relacion.proyecto
        nuevo.faseprimera = relacion.faseprimera
        nuevo.fasesegunda = relacion.fasesegunda
    nuevo.save()
    return (True)