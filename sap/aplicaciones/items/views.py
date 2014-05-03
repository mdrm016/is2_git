from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect, HttpResponse
from django.template.context import RequestContext
from aplicaciones.proyectos.models import Proyectos
from aplicaciones.fases.models import Fases
from aplicaciones.tipoitem.models import TipoItem
from aplicaciones.tipoatributo.models import TipoAtributo, Numerico, Fecha, Texto, ArchivoExterno, Logico, Imagen
from aplicaciones.relaciones.models import Relaciones, ListaRelaciones
from .models import Items, ListaValores, ValorItem
from datetime import datetime
from django.contrib.auth.decorators import login_required, permission_required
from django.db.models import Q
from forms import ItemNuevoForm, ItemModificadoForm
from aplicaciones.tipoitem.views import ordenar_mantener
from aplicaciones.relaciones.views import cargar_atributos

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
    proyecto = Proyectos.objects.get(id=id_proyecto)
    lista_items = Items.objects.filter(proyecto_id=id_proyecto, fase_id=id_fase, is_active=True)
    mensaje = ''
    ctx = {'lista_items': lista_items, 'mensaje': mensaje, 'id_proyecto':id_proyecto, 'id_fase': id_fase, 'proyecto':proyecto}
    template_name = './items/items.html'
    return render_to_response(template_name, ctx, context_instance=RequestContext(request))

def listar_tipo_item(request, id_proyecto, id_fase):
    fase = Fases.objects.get(id=id_fase)
    proyecto = Proyectos.objects.get(id=id_proyecto)
    if fase.estado =='FD' or proyecto.estado=='Inactivo':
        mensaje ='No se pueden agregar items a la fase, el proyecto o la fase del item no esta inicializado.'
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
    itemactual = Items.objects.get(id=id_item)
    lista_error = []
    if fase.estado == 'FD' or proyecto.estado=='Inactivo' or itemactual.estado=='En Revision' or itemactual.estado=='Bloqueado' or itemactual.estado=='Validado':
        mensaje = 'No se pueden modificar atributos. Dirijase a consultar item.'
        ctx = {'mensaje':mensaje, 'id_proyecto': id_proyecto}
        template_name = './items/itemalerta.html'
        return render_to_response(template_name, ctx, context_instance=RequestContext(request))
    if request.method=='POST': 
        idtipoitem = itemactual.tipo_item_id
        versionitem = itemactual.version + 1
        lista_atributos = ordenar_mantener(idtipoitem)
        i = 1
        posicion = 1
        # variables para deshacer las acciones del post si error es verdadero
        error = False
        lista_desh=[]
        for listaatributo in lista_atributos:
            nombreatributo = listaatributo.nombre
            idatributo = listaatributo.id_atributo
            iditematributo = listaatributo.id_tipoitem
            obligatoriedad = TipoAtributo.objects.get(id=idatributo).obligatorio
            tipoatributoobjetos = TipoAtributo.objects.filter(id=listaatributo.id_atributo)
            valoritems = ValorItem()
            
            for tipoatributoobjeto in tipoatributoobjetos:
                tipodatoatributo= tipoatributoobjeto.tipo
 #               
            if tipodatoatributo=='Archivo Externo':
                if obligatoriedad and request.FILES.has_key(str(i)):
                    error = True
                    nomb=nombreatributo
                    mensaje = 'El campo %s es obligatorio' % nombreatributo
                    tupla=(nomb, mensaje)
                    lista_error.append(tupla)
                else:
                    if request.FILES.has_key(str(i)):
                        archivo = ArchivoExterno()
                        archivo.valor = request.FILES[str(i)]
                        archivo.id_item = id_item
                        archivo.nombre_atributo = nombreatributo
                        archivo.save()
                        valoritems.item_id = id_item
                        valoritems.valor_id = archivo.id
                        valoritems.tabla_valor_nombre = 'tipoatributo_archivoexterno'
                        valoritems.nombre_atributo = nombreatributo
                        valoritems.tipo_dato = tipodatoatributo
                        valoritems.version = versionitem
                        valoritems.orden = posicion
                        valoritems.proyecto_id = id_proyecto
                        valoritems.fase_id = id_fase
                        valoritems.save()
                        lista_desh.append(valoritems.id)
                    else:
                        existe=True
                        try: 
                            valoritems_guardado = ValorItem.objects.get(item_id = id_item, nombre_atributo = nombreatributo, tipo_dato = tipodatoatributo, version = versionitem-1, orden = posicion)
                        except ValorItem.DoesNotExist:
                            existe = False
                        if existe: 
                            valoritems.item_id = valoritems_guardado.item_id
                            valoritems.valor_id = valoritems_guardado.valor_id
                            valoritems.tabla_valor_nombre = 'tipoatributo_archivoexterno'
                            valoritems.nombre_atributo = valoritems_guardado.nombre_atributo
                            valoritems.tipo_dato = valoritems_guardado.tipo_dato
                            valoritems.version = versionitem
                            valoritems.orden = valoritems_guardado.orden
                            valoritems.proyecto_id = valoritems_guardado.proyecto_id
                            valoritems.fase_id = valoritems_guardado.fase_id
                            valoritems.save()
                            lista_desh.append(valoritems.id)
                    
            elif tipodatoatributo=='Imagen':
                if obligatoriedad and request.FILES.has_key(str(i)):
                    error = True
                    nomb=nombreatributo
                    mensaje = 'El campo %s es obligatorio' % nombreatributo
                    tupla=(nomb, mensaje)
                    lista_error.append(tupla)
                else:
                    if request.FILES.has_key(str(i)):
                        imagen = Imagen()
                        imagen.valor = request.FILES[str(i)]
                        imagen.id_item = id_item
                        imagen.nombre_atributo = nombreatributo
                        imagen.save()
                        valoritems.item_id = id_item
                        valoritems.valor_id = imagen.id
                        valoritems.tabla_valor_nombre = 'tipoatributo_imagen'
                        valoritems.nombre_atributo = nombreatributo
                        valoritems.tipo_dato = tipodatoatributo
                        valoritems.version = versionitem
                        valoritems.orden = posicion
                        valoritems.proyecto_id = id_proyecto
                        valoritems.fase_id = id_fase
                        valoritems.save()
                        lista_desh.append(valoritems.id)
                    else:
                        existe=True
                        try:
                            valoritems_guardado = ValorItem.objects.get(item_id = id_item, nombre_atributo=nombreatributo, tipo_dato = tipodatoatributo, version = versionitem-1, orden = posicion)
                        except ValorItem.DoesNotExist:
                            existe = False
                        if existe:
                            valoritems.item_id = valoritems_guardado.item_id
                            valoritems.valor_id = valoritems_guardado.valor_id
                            valoritems.tabla_valor_nombre = 'tipoatributo_imagen'
                            valoritems.nombre_atributo = valoritems_guardado.nombre_atributo
                            valoritems.tipo_dato = valoritems_guardado.tipo_dato
                            valoritems.version = versionitem
                            valoritems.orden = valoritems_guardado.orden
                            valoritems.proyecto_id = valoritems_guardado.proyecto_id
                            valoritems.fase_id = valoritems_guardado.fase_id
                            valoritems.save()
                            lista_desh.append(valoritems.id)
#                       
            elif tipodatoatributo=='Texto':
                archivo = Texto()
                archivo.valor = request.POST.get(str(i), '')
                if obligatoriedad and archivo.valor == '':
                    error = True
                    nomb=nombreatributo
                    mensaje = 'El campo %s es obligatorio' % nombreatributo
                    tupla=(nomb, mensaje)
                    lista_error.append(tupla)
                else:
                    archivo.id_item = id_item
                    archivo.nombre_atributo = nombreatributo
                    for tipoatributoobjeto in tipoatributoobjetos:
                        archivo.longitud = tipoatributoobjeto.longitud
                    archivo.save()
                    valoritems.item_id = id_item
                    valoritems.valor_id = archivo.id
                    valoritems.tabla_valor_nombre = 'tipoatributo_texto'
                    valoritems.nombre_atributo = nombreatributo
                    valoritems.tipo_dato = tipodatoatributo
                    valoritems.version = versionitem
                    valoritems.orden = posicion
                    valoritems.proyecto_id = id_proyecto
                    valoritems.fase_id = id_fase
                    valoritems.save()
                    lista_desh.append(valoritems.id)
            elif tipodatoatributo=='Numerico':
                archivo = Numerico()
                archivo.valor = request.POST.get(str(i), '')
                
                if obligatoriedad and archivo.valor == '':
                    error = True
                    nomb=nombreatributo
                    mensaje = 'El campo %s es obligatorio' % nombreatributo
                    tupla=(nomb, mensaje)
                    lista_error.append(tupla)
                else:
                    #si el atributo no es obligatorio, se debe guardar como un numero la cadena vacia
                    if archivo.valor == '':
                        archivo.valor = 0
                    archivo.id_item = id_item
                    archivo.nombre_atributo = nombreatributo
                    for tipoatributoobjeto in tipoatributoobjetos:
                        archivo.longitud = tipoatributoobjeto.longitud
                        archivo.precision = tipoatributoobjeto.precision
                    archivo.save()
                    valoritems.item_id = id_item
                    valoritems.valor_id = archivo.id
                    valoritems.tabla_valor_nombre = 'tipoatributo_numerico'
                    valoritems.nombre_atributo = nombreatributo
                    valoritems.tipo_dato = tipodatoatributo
                    valoritems.version = versionitem
                    valoritems.orden = posicion
                    valoritems.proyecto_id = id_proyecto
                    valoritems.fase_id = id_fase
                    valoritems.save()
                    lista_desh.append(valoritems.id)
            elif tipodatoatributo=='Fecha':
                archivo = Fecha()
                archivo.valor = request.POST.get(str(i), '')
                if obligatoriedad and archivo.valor == '':
                    error = True
                    nomb=nombreatributo
                    mensaje = 'El campo %s es obligatorio' % nombreatributo
                    tupla=(nomb, mensaje)
                    lista_error.append(tupla)
                else:
                    archivo.id_item = id_item
                    archivo.nombre_atributo = nombreatributo
                    archivo.save()
                    valoritems.item_id = id_item
                    valoritems.valor_id = archivo.id
                    valoritems.tabla_valor_nombre = 'tipoatributo_fecha'
                    valoritems.nombre_atributo = nombreatributo
                    valoritems.tipo_dato = tipodatoatributo
                    valoritems.version = versionitem
                    valoritems.orden = posicion
                    valoritems.proyecto_id = id_proyecto
                    valoritems.fase_id = id_fase
                    valoritems.save()
                    lista_desh.append(valoritems.id)
            elif tipodatoatributo=='Logico':
                archivo = Logico()
                archivo.valor = request.POST.get(str(i), '')
                if obligatoriedad and archivo.valor == '':
                    error = True
                    nomb=nombreatributo
                    mensaje = 'El campo %s es obligatorio' % nombreatributo
                    tupla=(nomb, mensaje)
                    lista_error.append(tupla)
                else:
                    archivo.id_item = id_item
                    archivo.nombre_atributo = nombreatributo
                    archivo.save()
                    valoritems.item_id = id_item
                    valoritems.valor_id = archivo.id
                    valoritems.tabla_valor_nombre = 'tipoatributo_logico'
                    valoritems.nombre_atributo = nombreatributo
                    valoritems.tipo_dato = tipodatoatributo
                    valoritems.version = versionitem
                    valoritems.orden = posicion
                    valoritems.proyecto_id = id_proyecto
                    valoritems.fase_id = id_fase
                    valoritems.save()
                    lista_desh.append(valoritems.id)
            i = i+1
            posicion = posicion+1
        if error:
            #deshacemos las acciones del post, para que no se creem campos duplicados
            atributositem = ValorItem.objects.filter(pk__in=lista_desh)
            for atrib_item in atributositem:
                print atrib_item.nombre_atributo
                atrib_item.delete()
        else:
            rpadre = Relaciones.objects.filter(padre_id=itemactual.id, is_active=True, versionprimero=itemactual.version)
            rantecesor = Relaciones.objects.filter(antecesor_id=itemactual.id, is_active=True, versionprimero=itemactual.version)
            rhijo = Relaciones.objects.filter(hijo_id=itemactual.id, is_active=True, versionsegundo=itemactual.version)
            rsucesor = Relaciones.objects.filter(sucesor_id=itemactual.id, is_active=True, versionsegundo=itemactual.version)

            for padre in rpadre:
                relacionnueva = Relaciones()
                relacionnueva.padre_id = padre.padre_id
                relacionnueva.hijo_id = padre.hijo_id
                relacionnueva.antecesor_id = padre.antecesor_id
                relacionnueva.sucesor_id = padre.sucesor_id
                relacionnueva.is_active = True
                relacionnueva.proyecto = padre.proyecto
                relacionnueva.faseprimera = padre.faseprimera
                relacionnueva.fasesegunda = padre.fasesegunda
                relacionnueva.versionprimero = versionitem
                relacionnueva.versionsegundo = padre.versionsegundo
                padre_hijo = Items.objects.get(id=padre.hijo_id)
                if padre.versionsegundo==padre_hijo.version:
                    relacionnueva.save()
            for antecesor in rantecesor:
                relacionnueva = Relaciones()
                relacionnueva.padre_id = antecesor.padre_id
                relacionnueva.hijo_id = antecesor.hijo_id
                relacionnueva.antecesor_id = antecesor.antecesor_id
                relacionnueva.sucesor_id = antecesor.sucesor_id
                relacionnueva.is_active = True
                relacionnueva.proyecto = antecesor.proyecto
                relacionnueva.faseprimera = antecesor.faseprimera
                relacionnueva.fasesegunda = antecesor.fasesegunda
                relacionnueva.versionprimero = versionitem
                relacionnueva.versionsegundo = antecesor.versionsegundo
                antecesor_sucesor = Items.objects.get(id=antecesor.sucesor_id)
                if sucesor.versionsegundo==antecesor_sucesor.version:
                    relacionnueva.save()
            for sucesor in rsucesor:
                relacionnueva = Relaciones()
                relacionnueva.padre_id = sucesor.padre_id
                relacionnueva.hijo_id = sucesor.hijo_id
                relacionnueva.antecesor_id = sucesor.antecesor_id
                relacionnueva.sucesor_id = sucesor.sucesor_id
                relacionnueva.is_active = True
                relacionnueva.proyecto = sucesor.proyecto
                relacionnueva.faseprimera = sucesor.faseprimera
                relacionnueva.fasesegunda = sucesor.fasesegunda
                relacionnueva.versionprimero = sucesor.versionprimero
                relacionnueva.versionsegundo = versionitem
                sucesor_antecesor = Items.objects.get(id=padre.antecesor_id)
                if sucesor.versionprimero==sucesor_antecesor.version:
                    relacionnueva.save()
            for hijo in rhijo:
                relacionnueva = Relaciones()
                relacionnueva.padre_id = hijo.padre_id
                relacionnueva.hijo_id = hijo.hijo_id
                relacionnueva.antecesor_id = hijo.antecesor_id
                relacionnueva.sucesor_id = hijo.sucesor_id
                relacionnueva.is_active = True
                relacionnueva.proyecto = hijo.proyecto
                relacionnueva.faseprimera = hijo.faseprimera
                relacionnueva.fasesegunda = hijo.fasesegunda
                relacionnueva.versionprimero = hijo.versionprimero
                relacionnueva.versionsegundo = versionitem
                hijo_padre = Items.objects.get(id=hijo.padre_id)
                if hijo.versionprimero==hijo_padre.version:
                    relacionnueva.save()
                
            itemactual.version = versionitem
            itemactual.save()
            mensaje = 'Atributos modificados con extito.'
            template_name='./items/itemalerta.html'
            ctx = {'mensaje': mensaje, 'id_proyecto':id_proyecto, 'id_fase': id_fase,}
            return render_to_response(template_name, ctx, context_instance=RequestContext(request))

    idtipo = itemactual.tipo_item_id     
    lista_atributos = ordenar_mantener(idtipo)
    lista_valores = []
    orden = 0
    
    atributositem = ValorItem.objects.filter(proyecto_id=id_proyecto, fase_id=id_fase, item_id=id_item, version=itemactual.version).order_by('orden')

    #preparamos una lista con los elementos necesarios para controlar la obligatoriedad y la longitud y presicion de los atributos
    listaPresicionLongitud=[]
    ord = 0
    for l in lista_atributos:
        atrib = TipoAtributo.objects.get(id=l.id_atributo)
        minvalue = 0
        maxvalue = 0
        #si el atributo es numerico, rescatamos la longitud y la precision y creamos una cadena para el template
        if atrib.tipo == 'Numerico':
            num = int(atrib.longitud)
            maxvalue = 10**num -1
            
            num = int(atrib.precision)
            list=range(0, num)
            minvalue = '0.'
            maxvalue = '%s.' % maxvalue
            for lis in list:
                minvalue = '%s%s' % (minvalue, 0)
                maxvalue = '%s%s' % (maxvalue, 9)
        ord = ord+1
        #guardamos una lista de tuplas para el template
        tupla=(ord, atrib.nombre, atrib.longitud, atrib.precision, maxvalue, minvalue, atrib.obligatorio)
        listaPresicionLongitud.append(tupla)
    if atributositem:
        for i in atributositem:
            valorfuturo = ListaValores()
            valorfuturo.nombre_atributo = i.nombre_atributo
            valorfuturo.tipo_dato = i.tipo_dato
            valorfuturo.orden = i.orden
            if i.tipo_dato=='Texto':
                textos = Texto.objects.filter(id=i.valor_id)
                if textos:
                    for texto in textos:
                        valorfuturo.valor_texto = texto.valor
                else:
                    valorfuturo.valor_texto = ""
                valorfuturo.save()
                lista_valores.append(valorfuturo)
            if i.tipo_dato=='Numerico':
                textos = Numerico.objects.filter(id=i.valor_id)
                if textos:
                    for texto in textos:
                        valorfuturo.valor_numerico = texto.valor
                        #al momento de recuperar los datos de un valor numerico, truncamos la cadena de acuerdo con la presicion
                        for ord, nombre, long, precis, max, min, oblig in listaPresicionLongitud:
                            if nombre == valorfuturo.nombre_atributo:
                                valor = str(valorfuturo.valor_numerico)
                                num = valor.find('.') + precis +1
                                valorfuturo.valor_texto = valor[0:num]
                                
                else:
                    valorfuturo.valor_numerico = ""
                valorfuturo.save()
                lista_valores.append(valorfuturo)
            if i.tipo_dato=='Fecha':
                textos = Fecha.objects.filter(id=i.valor_id)
                if textos:
                    for texto in textos:
                        valorfuturo.valor_fecha = texto.valor
                else:
                    valorfuturo.valor_fecha = ""
                valorfuturo.save()
                lista_valores.append(valorfuturo)
            if i.tipo_dato=='Archivo Externo':
                textos = ArchivoExterno.objects.filter(id=i.valor_id)
                if textos:
                    for texto in textos:
                        valorfuturo.valor_archivoexterno = texto.valor
                else:
                    valorfuturo.valor_archivoexterno = ""
                valorfuturo.save()
                lista_valores.append(valorfuturo)
            if i.tipo_dato=='Imagen':
                textos = Imagen.objects.filter(id=i.valor_id)
                if textos:
                    for texto in textos:
                        valorfuturo.valor_imagen = texto.valor
                else:
                    valorfuturo.valor_imagen = ""
                valorfuturo.save()
                lista_valores.append(valorfuturo)
            if i.tipo_dato=='Logico':
                textos = Logico.objects.filter(id=i.valor_id)
                if textos:
                    for texto in textos:
                        valorfuturo.valor_logico = texto.valor
                else:
                    valorfuturo.valor_logico = ""
                valorfuturo.save()
                lista_valores.append(valorfuturo)
    else:
        
        for atributo in lista_atributos:
            orden = orden+1
            valorfuturo = ListaValores()
            valorfuturo.nombre_atributo = atributo.nombre
            atributoobjeto = TipoAtributo.objects.get(id=atributo.id_atributo)
            valorfuturo.tipo_dato = atributoobjeto.tipo
            valorfuturo.orden = orden
            valorfuturo.valor_archivoexterno = ""
            valorfuturo.valor_imagen= ""
            valorfuturo.valor_texto = ""
            valorfuturo.valor_numerico = ""
            valorfuturo.valor_fecha = ""
            
            lista_valores.append(valorfuturo)

    template_name='./items/cargaratributos.html'
    return render(request, template_name, {'id_proyecto':id_proyecto, 'id_fase': id_fase, 'id_tipoitem': idtipo, 'lista_valores': lista_valores, 'id_item': id_item, 'listaPresicionLongitud':listaPresicionLongitud, 'lista_error':lista_error, 'itemactual':itemactual})        

def listar_versiones(request, id_proyecto, id_fase, id_item):
    fase = Fases.objects.get(id=id_fase)
    proyecto = Proyectos.objects.get(id=id_proyecto)
    itemactual = Items.objects.get(id=id_item)
    if fase.estado =='FD' or proyecto.estado=='Inactivo' or itemactual.estado=='En Revision' or itemactual.estado=='Bloqueado' or itemactual.estado=='Validado':
        mensaje ='No se puede consultar esta opcion. Dirijase a consultar item.'
        ctx = {'mensaje':mensaje, 'id_proyecto': id_proyecto, 'id_fase': id_fase}
        template_name = './items/itemalerta.html'
        return render_to_response(template_name, ctx, context_instance=RequestContext(request))
    else:
        lista_versiones = []
        versionactual = itemactual.version
        versiones = int(versionactual)
        i=1
        while i<versiones:
            lista_versiones.append(i)
            i = i+1
             
    ctx={'lista_versiones':lista_versiones, 'id_proyecto':id_proyecto, 'id_fase':id_fase, 'id_item': id_item}
    template_name = './items/listarversiones.html'
    return render_to_response(template_name, ctx, context_instance=RequestContext(request))

def consultar_version(request, id_proyecto, id_fase, id_item, version):
    item = Items.objects.get(id=id_item)
    atributos = ValorItem.objects.filter(proyecto=id_proyecto, fase=id_fase, item=id_item, version=version).order_by('orden')
    lista_valores = []
    if atributos:
        for i in atributos:
            valorfuturo = ListaValores()
            valorfuturo.nombre_atributo = i.nombre_atributo
            valorfuturo.tipo_dato = i.tipo_dato
            valorfuturo.orden = i.orden
            if i.tipo_dato=='Texto':
                textos = Texto.objects.filter(id=i.valor_id)
                if textos:
                    for texto in textos:
                        valorfuturo.valor_texto = texto.valor
                else:
                    valorfuturo.valor_texto = ""
                valorfuturo.save()
                lista_valores.append(valorfuturo)
            if i.tipo_dato=='Numerico':
                textos = Numerico.objects.filter(id=i.valor_id)
                if textos:
                    for texto in textos:
                        valorfuturo.valor_numerico = texto.valor
                else:
                    valorfuturo.valor_numerico = ""
                valorfuturo.save()
                lista_valores.append(valorfuturo)
            if i.tipo_dato=='Fecha':
                textos = Fecha.objects.filter(id=i.valor_id)
                if textos:
                    for texto in textos:
                        valorfuturo.valor_fecha = texto.valor
                else:
                    valorfuturo.valor_fecha = ""
                valorfuturo.save()
                lista_valores.append(valorfuturo)
            if i.tipo_dato=='Archivo Externo':
                textos = Texto.objects.filter(id=i.valor_id)
                if textos:
                    for texto in textos:
                        valorfuturo.valor_archivoexterno = texto.valor
                else:
                    valorfuturo.valor_archivoexterno = ""
                valorfuturo.save()
                lista_valores.append(valorfuturo)
            
            if i.tipo_dato=='Logico':
                textos = Logico.objects.filter(id=i.valor_id)
                if textos:
                    for texto in textos:
                        valorfuturo.valor_logico = texto.valor
                else:
                    valorfuturo.valor_logico = ""
                valorfuturo.save()
                lista_valores.append(valorfuturo)
    rpadre = Relaciones.objects.filter(padre_id=id_item, faseprimera=id_fase, proyecto=id_proyecto, versionprimero=version, is_active=True)
    rantecesor = Relaciones.objects.filter(antecesor_id=id_item, faseprimera=id_fase, proyecto=id_proyecto, versionprimero=version, is_active=True)
    rhijo = Relaciones.objects.filter(hijo_id=id_item, fasesegunda=id_fase, proyecto=id_proyecto, versionsegundo=version, is_active=True)
    rsucesor = Relaciones.objects.filter(sucesor_id=id_item, fasesegunda=id_fase, proyecto=id_proyecto, versionsegundo=version, is_active=True)
    lista_relaciones = []
    for antecesor in rantecesor:
        valor = ListaRelaciones()
        valor.itemrelacionado = antecesor.sucesor_id
        valor.tiporelacion = 'Sucesor'
        itemrelacionado = Items.objects.get(id=valor.itemrelacionado)
        valor.nombreitemrelacionado = itemrelacionado.nombre
        valor.relacionid = antecesor.id
        valor.save()
        lista_relaciones.append(valor)
    for sucesor in rsucesor:
        valor = ListaRelaciones()
        valor.itemrelacionado = sucesor.antecesor_id
        valor.tiporelacion = 'Antecesor'
        itemrelacionado = Items.objects.get(id=valor.itemrelacionado)
        valor.nombreitemrelacionado = itemrelacionado.nombre
        valor.relacionid = sucesor.id
        valor.save()
        lista_relaciones.append(valor)
    for padre in rpadre:
        valor = ListaRelaciones()
        valor.itemrelacionado = padre.hijo_id
        valor.tiporelacion = 'Hijo'
        itemrelacionado = Items.objects.get(id=valor.itemrelacionado)
        valor.nombreitemrelacionado = itemrelacionado.nombre
        valor.relacionid = padre.id
        valor.save()
        lista_relaciones.append(valor)
    for hijo in rhijo:
        valor = ListaRelaciones()
        valor.itemrelacionado = hijo.padre_id
        valor.tiporelacion = 'Padre'
        itemrelacionado = Items.objects.get(id=valor.itemrelacionado)
        valor.nombreitemrelacionado = itemrelacionado.nombre
        valor.relacionid = hijo.id
        valor.save()
        lista_relaciones.append(valor)
    
    template_name='./items/mostraratributos.html'
    return render(request, template_name, {'id_proyecto':id_proyecto, 'id_fase': id_fase, 'lista_valores': lista_valores, 'lista_relaciones': lista_relaciones, 'id_item': id_item})

def revertir_version(request, id_proyecto, id_fase, id_item, version):
    item = Items.objects.get(proyecto_id=id_proyecto, fase_id=id_fase, id=id_item)
    versionnueva = item.version + 1
    valoresitem = ValorItem.objects.filter(proyecto=id_proyecto, fase=id_fase, item=id_item, version=version).order_by('orden')
    if valoresitem:
        for filaitem in valoresitem:
            if not (cargar_atributos(filaitem.valor_id, filaitem.nombre_atributo, filaitem.orden, filaitem.tabla_valor_nombre, id_proyecto, id_fase, int(id_item))):
                estamosenproblemas.append(sjetbg)
    
    rhijo = Relaciones.objects.filter(hijo_id=id_item, is_active=True, versionsegundo=version)
    for hijo in rhijo:
        pad = Items.objects.get(id=hijo.padre_id)
        if pad.is_active == True:
            if not aumentar_relaciones(pad):
                estamosenproblemas.append(sethrge)
            relacionnueva = Relaciones()
            relacionnueva.padre_id = hijo.padre_id
            relacionnueva.hijo_id = hijo.hijo_id
            relacionnueva.antecesor_id = hijo.antecesor_id
            relacionnueva.sucesor_id = hijo.sucesor_id
            relacionnueva.is_active = True
            relacionnueva.proyecto = hijo.proyecto
            relacionnueva.faseprimera = hijo.faseprimera
            relacionnueva.fasesegunda = hijo.fasesegunda
            relacionnueva.versionprimero = pad.version + 1
            relacionnueva.versionsegundo = versionnueva
            relacionnueva.save()
    
            itemotro = ValorItem.objects.filter(proyecto=id_proyecto, fase=id_fase, item=pad.id, version=pad.version).order_by('orden')
            if itemotro:
                for fila in itemotro:
                    if not (cargar_atributos(fila.valor_id, fila.nombre_atributo, fila.orden, fila.tabla_valor_nombre, id_proyecto, id_fase, int(pad.id))):
                        estamosenproblemas.append(sjetbg)
            pad.version = pad.version + 1
            pad.save()
    item.version = versionnueva
    item.save()
    
    mensaje = 'Version Revertida con exito.'
    template_name='./items/itemalerta.html'
    ctx = {'mensaje': mensaje, 'id_proyecto':id_proyecto, 'id_fase': id_fase}
    return render_to_response(template_name, ctx, context_instance=RequestContext(request))

def modificar_item(request, id_proyecto, id_fase, id_item):
    proyecto = Proyectos.objects.get(id=id_proyecto) 
    fase = Fases.objects.get(id=id_fase, proyecto_id=id_proyecto)
    item = Items.objects.get(proyecto_id=id_proyecto, fase_id=id_fase, id=id_item)
    mensaje=''
    if request.method == 'POST':
        if fase.estado == 'FD':
            mensaje = 'No se puede modificar item. Dirijase a consultar item.'
            ctx ={'mensaje':mensaje, 'id_proyecto':id_proyecto, 'id_fase':id_fase, 'id_item': id_item}      
            template_name='./items/itemalerta.html'
            return render_to_response(template_name, ctx, context_instance=RequestContext(request))
        else: 
            form = ItemModificadoForm(request.POST)
            if form.is_valid():
                form.clean()
                nombreNuevo = form.cleaned_data['Nombre_de_Item'] 
                descripcionNueva =  form.cleaned_data['Descripcion']
                prioridadNueva = form.cleaned_data['Prioridad']
                observacionNueva =  form.cleaned_data['Observaciones']
                costotNuevo =  form.cleaned_data['Costo_Temporal']
                costomNuevo =  form.cleaned_data['Costo_Monetario']
                complejidadNueva =  form.cleaned_data['Complejidad']
                estadoNuevo =  form.cleaned_data['Estado']
                mismo_nombres = Items.objects.filter(nombre=nombreNuevo, is_active=True, proyecto_id=id_proyecto, fase_id=id_fase)
                repetido='Vacio'
                    
                if (mismo_nombres):
                    for nombre in mismo_nombres:
                        if (nombre.id!=item.id):
                            repetido='No'
                    
                if nombreNuevo:
                    nombre = nombreNuevo
                else:
                    nombre = item.nombre
                if descripcionNueva:
                    descripcion = descripcionNueva
                else:
                    descripcion = item.descripcion
                if prioridadNueva:
                    prioridad = prioridadNueva
                else:
                    prioridad = item.prioridad
                if observacionNueva:
                    observaciones = observacionNueva
                else:
                    observaciones = item.observaciones
                if costotNuevo:
                    costotemporal = costotNuevo
                else: 
                    costotemporal = item.costoTemporal
                if costomNuevo:
                    costomonetario = costomNuevo
                else:
                    costomonetario = item.costoMonetario
                if complejidadNueva:
                    complejidad = complejidadNueva
                else:
                    complejidad = item.complejidad
                if estadoNuevo:
                    estado = estadoNuevo
                else:
                    estado = item.estado
                if (repetido=='No'):
                    mensaje = 'El nombre de Item ya existe'
                    data ={'Nombre_de_Item':nombre, 'Descripcion': descripcion, 'Prioridad': prioridad, 'Observaciones': observaciones, 'Costo_Monetario': costomonetario, 'Costo_Temporal': costotemporal, 'Complejidad': complejidad, 'Estado':estado}
                    form = ItemModificadoForm(data)
                    ctx ={'form': form, 'mensaje':mensaje, 'id_proyecto':id_proyecto, 'id_fase':id_fase, 'id_item': id_item}      
                    template_name='./items/modificaritem.html'
                    return render_to_response(template_name, ctx, context_instance=RequestContext(request))
                     #Si no se ha suministrado un nuevo lider, el proyecto se queda con el lider actua
                
                if estadoNuevo:
                    if (item.estado=='En Construccion') and (estadoNuevo=='Validado'):
                        mensaje = 'No se puede validar un Item en construccion.'
                        data ={'Nombre_de_Item':nombre, 'Descripcion': descripcion, 'Prioridad': prioridad, 'Observaciones': observaciones, 'Costo_Monetario': costomonetario, 'Costo_Temporal': costotemporal, 'Complejidad': complejidad, 'Estado':estado}
                        form = ItemModificadoForm(data)
                        ctx ={'form': form, 'mensaje':mensaje, 'id_proyecto':id_proyecto, 'id_fase':id_fase, 'id_item': id_item}      
                        template_name='./items/modificaritem.html'
                        return render_to_response(template_name, ctx, context_instance=RequestContext(request))
                    else:
                        item.estado = estadoNuevo
                item.nombre = nombre
                item.descripcion = descripcion
                item.prioridad = prioridad
                item.observaciones = observaciones
                item.costoMonetario = costomonetario
                item.costoTemporal = costotemporal
                item.complejidad = complejidad
                item.estado = estado
                item.save()
                mensaje="Item modificado exitosamente"
                ctx = {'mensaje':mensaje, 'id_proyecto': id_proyecto, 'id_fase':id_fase, 'id_item': id_item}
                template_name='./items/itemalerta.html'
                return render_to_response(template_name, ctx, context_instance=RequestContext(request))
            else:
                data ={'Nombre_de_Item': item.nombre, 'Descripcion': item.descripcion, 'Prioridad': item.prioridad, 'Observaciones': item.observaciones, 'Costo_Monetario': item.costoMonetario, 'Costo_Temporal': item.costoTemporal, 'Complejidad': item.complejidad, 'Estado': item.estado}   
                form = ItemModificadoForm(data)
            ctx ={'form': form, 'mensaje':mensaje, 'id_proyecto':id_proyecto, 'id_fase':id_fase, 'id_item': id_item}      
            template_name='./items/modificaritem.html'
            return render_to_response(template_name, ctx, context_instance=RequestContext(request))
    data ={'Nombre_de_Item': item.nombre, 'Descripcion': item.descripcion, 'Prioridad': item.prioridad, 'Observaciones': item.observaciones, 'Costo_Monetario': item.costoMonetario, 'Costo_Temporal': item.costoTemporal, 'Complejidad': item.complejidad, 'Estado': item.estado}   
    form = ItemModificadoForm(data)
    ctx ={'form': form, 'mensaje':mensaje, 'id_proyecto':id_proyecto, 'id_fase':id_fase, 'id_item': id_item}
    template_name='./items/modificaritem.html'
    return render_to_response(template_name, ctx, context_instance=RequestContext(request))

def consultar_item(request, id_proyecto, id_fase, id_item):
    fase = Fases.objects.get(id=id_fase, proyecto_id=id_proyecto)
    item = Items.objects.get(proyecto_id=id_proyecto, fase_id=id_fase, id=id_item)
    # conseguir el contexto de las fases y sus estados
    #fases = Fases.objects.filter(id_proyecto = id_proyecto)
    ctx = {'item':item}
    template_name = './items/consultaritem.html'
    return render(request, template_name, {'item': item, 'id_proyecto': id_proyecto, 'fase': fase, 'id_fase': id_fase, 'id_item': id_item})

def consultar_atributos(request, id_proyecto, id_fase, id_item):
    proyecto = Proyectos.objects.get(id=id_proyecto)
    fase = Fases.objects.get(proyecto_id=id_proyecto, id=id_fase)
    itemactual = Items.objects.get(proyecto_id=id_proyecto, fase_id=id_fase, id=id_item)
    
    idtipo = itemactual.tipo_item_id     
    lista_atributos = ordenar_mantener(idtipo)
    lista_valores = []
    orden = 0
    
    atributositem = ValorItem.objects.filter(proyecto_id=id_proyecto, fase_id=id_fase, item_id=id_item, version=itemactual.version).order_by('orden')
    if atributositem:
        for i in atributositem:
            valorfuturo = ListaValores()
            valorfuturo.nombre_atributo = i.nombre_atributo
            valorfuturo.tipo_dato = i.tipo_dato
            valorfuturo.orden = i.orden
            if i.tipo_dato=='Texto':
                textos = Texto.objects.filter(id=i.valor_id)
                if textos:
                    for texto in textos:
                        valorfuturo.valor_texto = texto.valor
                else:
                    valorfuturo.valor_texto = ""
                valorfuturo.save()
                lista_valores.append(valorfuturo)
            if i.tipo_dato=='Numerico':
                textos = Numerico.objects.filter(id=i.valor_id)
                if textos:
                    for texto in textos:
                        valorfuturo.valor_numerico = texto.valor
                else:
                    valorfuturo.valor_numerico = ""
                valorfuturo.save()
                lista_valores.append(valorfuturo)
            if i.tipo_dato=='Fecha':
                textos = Fecha.objects.filter(id=i.valor_id)
                if textos:
                    for texto in textos:
                        valorfuturo.valor_fecha = texto.valor
                else:
                    valorfuturo.valor_fecha = ""
                valorfuturo.save()
                lista_valores.append(valorfuturo)
            if i.tipo_dato=='Archivo Externo':
                textos = Texto.objects.filter(id=i.valor_id)
                if textos:
                    for texto in textos:
                        valorfuturo.valor_archivoexterno = texto.valor
                else:
                    valorfuturo.valor_archivoexterno = ""
                valorfuturo.save()
                lista_valores.append(valorfuturo)
            if i.tipo_dato=='Logico':
                textos = Logico.objects.filter(id=i.valor_id)
                if textos:
                    for texto in textos:
                        valorfuturo.valor_logico = texto.valor
                else:
                    valorfuturo.valor_logico = ""
                valorfuturo.save()
                lista_valores.append(valorfuturo)
    else:
        for atributo in lista_atributos:
            orden = orden+1
            valorfuturo = ListaValores()
            valorfuturo.nombre_atributo = atributo.nombre
            atributoobjeto = TipoAtributo.objects.get(id=atributo.id_atributo)
            valorfuturo.tipo_dato = atributoobjeto.tipo
            valorfuturo.orden = orden
            valorfuturo.valor_archivoexterno = ""
            valorfuturo.valor_texto = ""
            valorfuturo.valor_numerico = ""
            valorfuturo.valor_fecha = ""
            
            lista_valores.append(valorfuturo)
    template_name='./items/consultaratributos.html'
    return render(request, template_name, {'id_proyecto':id_proyecto, 'id_fase': id_fase, 'lista_valores': lista_valores, 'id_item': id_item})        

def eliminar_item(request, id_proyecto, id_fase, id_item):
    proyecto = Proyectos.objects.get(id=id_proyecto)
    fase = Fases.objects.get(proyecto_id=id_proyecto, id=id_fase)
    item = Items.objects.get(proyecto_id=id_proyecto, fase_id=id_fase, id=id_item)
    
    if fase.estado=='FD' or item.estado=='Validado' or item.estado=='En Revision' or item.estado=='Bloqueado':
        mensaje = 'No se puede eliminar el item. Dirijase a consultar.'
        template_name='./items/itemalerta.html'
        return render(request, template_name, {'id_proyecto':id_proyecto, 'id_fase': id_fase, 'mensaje': mensaje, 'id_item': id_item})
    else:
        rantecesor = Relaciones.objects.filter(proyecto=id_proyecto, faseprimera=id_fase, antecesor_id=id_item, is_active=True)
        rpadre = Relaciones.objects.filter(proyecto=id_proyecto, faseprimera=id_fase, padre_id=id_item, is_active=True)
        rsucesor = Relaciones.objects.filter(proyecto=id_proyecto, fasesegunda=id_fase, sucesor_id=id_item, is_active=True)
        rhijo = Relaciones.objects.filter(proyecto=id_proyecto, fasesegunda=id_fase, hijo_id=id_item, is_active=True)
        for padre in rpadre:
            pad = Items.objects.get(id=padre.hijo_id)
            itemotro = ValorItem.objects.filter(proyecto=id_proyecto, fase=id_fase, item=pad.id, version=pad.version).order_by('orden')
            if itemotro:
                for fila in itemotro:
                    if not (cargar_atributos(fila.valor_id, fila.nombre_atributo, fila.orden, fila.tabla_valor_nombre, id_proyecto, id_fase, int(pad.id))):
                        estamosenproblemas.append(sjetbg)
            aumentar_relaciones(pad)
            padre.versionprimera = padre.versionprimera -1
            pad.version = pad.version + 1
            pad.save()
        for hijo in rhijo:
            pad = Items.objects.get(id=hijo.padre_id)
            itemotro = ValorItem.objects.filter(proyecto=id_proyecto, fase=id_fase, item=pad.id, version=pad.version).order_by('orden')
            if itemotro:
                for fila in itemotro:
                    if not (cargar_atributos(fila.valor_id, fila.nombre_atributo, fila.orden, fila.tabla_valor_nombre, id_proyecto, id_fase, int(pad.id))):
                        estamosenproblemas.append(sjetbg)
            aumentar_relaciones(pad)
            hijo.versionprimera = hijo.versionprimera -1
            pad.version = pad.version + 1
            pad.save()
        for antecesor in rantecesor:
            pad = Items.objects.get(id=antecesor.sucesor_id)
            itemotro = ValorItem.objects.filter(proyecto=id_proyecto, fase=id_fase, item=pad.id, version=pad.version).order_by('orden')
            if itemotro:
                for fila in itemotro:
                    if not (cargar_atributos(fila.valor_id, fila.nombre_atributo, fila.orden, fila.tabla_valor_nombre, id_proyecto, id_fase, int(pad.id))):
                        estamosenproblemas.append(sjetbg)
            aumentar_relaciones(pad)
            pad.version = pad.version + 1
            pad.save()
        for sucesor in rsucesor:
            pad = Items.objects.get(id=sucesor.antecesor_id)
            itemotro = ValorItem.objects.filter(proyecto=id_proyecto, fase=id_fase, item=pad.id, version=pad.version).order_by('orden')
            if itemotro:
                for fila in itemotro:
                    if not (cargar_atributos(fila.valor_id, fila.nombre_atributo, fila.orden, fila.tabla_valor_nombre, id_proyecto, id_fase, int(pad.id))):
                        estamosenproblemas.append(sjetbg)
            aumentar_relaciones(pad)
            pad.version = pad.version + 1
            pad.save()
        item.is_active = False
        item.save()
        mensaje ='Eliminacion exitosa.'
    template_name = './items/itemalerta.html'
    return render(request, template_name, {'id_proyecto':id_proyecto, 'id_fase': id_fase, 'mensaje': mensaje, 'id_item': id_item})

def listar_eliminados(request, id_proyecto, id_fase):
    lista_eliminados = Items.objects.filter(proyecto_id=id_proyecto, fase_id=id_fase, is_active=False)
    template_name='./items/listareliminados.html'
    return render(request, template_name, {'id_proyecto':id_proyecto, 'id_fase': id_fase, 'lista_eliminados': lista_eliminados})

def revivir_eliminado(request, id_proyecto, id_fase, id_item, version):
    item = Items.objects.get(proyecto_id=id_proyecto, fase_id=id_fase, id=id_item)
    nombres = Items.objects.filter(proyecto_id=id_proyecto, fase_id=id_fase, nombre=item.nombre, is_active=True)
    if nombres:
        mensaje = 'El nombre de item ya existe actualmente.'
        lista_eliminados = Items.objects.filter(proyecto_id=id_proyecto, fase_id=id_fase, is_active=False)
        template_name='./items/listareliminados.html'
        ctx = {'mensaje': mensaje, 'id_proyecto':id_proyecto, 'id_fase': id_fase, 'lista_eliminados': lista_eliminados}
        return render_to_response(template_name, ctx, context_instance=RequestContext(request))
    versionnueva = item.version + 1
    valoresitem = ValorItem.objects.filter(proyecto=id_proyecto, fase=id_fase, item=id_item, version=version).order_by('orden')
    if valoresitem:
        for filaitem in valoresitem:
            if not (cargar_atributos(filaitem.valor_id, filaitem.nombre_atributo, filaitem.orden, filaitem.tabla_valor_nombre, id_proyecto, id_fase, int(id_item))):
                estamosenproblemas.append(sjetbg)
    mipadres = Relaciones.objects.filter(hijo_id=id_item, is_active=True, versionsegundo=version)
    
    for hijo in mipadres:
        pad = Items.objects.get(id=hijo.padre_id)
        if pad.is_active == True:
            if not aumentar_relaciones(pad):
                estamosenproblemas.append(sethrge)
            relacionnueva = Relaciones()
            relacionnueva.padre_id = hijo.padre_id
            relacionnueva.hijo_id = hijo.hijo_id
            relacionnueva.antecesor_id = hijo.antecesor_id
            relacionnueva.sucesor_id = hijo.sucesor_id
            relacionnueva.is_active = True
            relacionnueva.proyecto = hijo.proyecto
            relacionnueva.faseprimera = hijo.faseprimera
            relacionnueva.fasesegunda = hijo.fasesegunda
            relacionnueva.versionprimero = pad.version + 1
            relacionnueva.versionsegundo = versionnueva
            relacionnueva.save()
            itemotro = ValorItem.objects.filter(proyecto=id_proyecto, fase=id_fase, item=pad.id, version=pad.version).order_by('orden')
            if itemotro:
                for fila in itemotro:
                    if not (cargar_atributos(fila.valor_id, fila.nombre_atributo, fila.orden, fila.tabla_valor_nombre, id_proyecto, id_fase, int(pad.id))):
                        estamosenproblemas.append(sjetbg)
            pad.version = pad.version + 1
            pad.save()
    
    item.version = versionnueva
    item.save()
    
    mensaje = 'Item revivido con exito.'
    template_name='./items/itemalerta.html'
    ctx = {'mensaje': mensaje, 'id_proyecto':id_proyecto, 'id_fase': id_fase}
    return render_to_response(template_name, ctx, context_instance=RequestContext(request))

def consultar_eliminado(request, id_proyecto, id_fase, id_item):
    fase = Fases.objects.get(id=id_fase)
    proyecto = Proyectos.objects.get(id=id_proyecto)
    itemactual = Items.objects.get(id=id_item)
    if fase.estado =='FD' or proyecto.estado=='Inactivo' or itemactual.estado=='En Revision' or itemactual.estado=='Bloqueado' or itemactual.estado=='Validado':
        mensaje ='No se puede consultar esta opcion. Dirijase a consultar item.'
        ctx = {'mensaje':mensaje, 'id_proyecto': id_proyecto, 'id_fase': id_fase}
        template_name = './items/itemalerta.html'
        return render_to_response(template_name, ctx, context_instance=RequestContext(request))
    else:
        lista_versiones = []
        versionactual = itemactual.version
        versiones = int(versionactual)
        i=1
        while i<versiones:
            lista_versiones.append(i)
            i = i+1
        lista_versiones.append(i)
    ctx={'lista_versiones':lista_versiones, 'id_proyecto':id_proyecto, 'id_fase':id_fase, 'id_item': id_item}
    template_name = './items/eliminadoversiones.html'
    return render_to_response(template_name, ctx, context_instance=RequestContext(request))

def consultar_version_eliminado(request, id_proyecto, id_fase, id_item, version):
    item = Items.objects.get(id=id_item)
    atributos = ValorItem.objects.filter(proyecto=id_proyecto, fase=id_fase, item=id_item, version=version).order_by('orden')
    lista_valores = []
    if atributos:
        for i in atributos:
            valorfuturo = ListaValores()
            valorfuturo.nombre_atributo = i.nombre_atributo
            valorfuturo.tipo_dato = i.tipo_dato
            valorfuturo.orden = i.orden
            if i.tipo_dato=='Texto':
                textos = Texto.objects.filter(id=i.valor_id)
                if textos:
                    for texto in textos:
                        valorfuturo.valor_texto = texto.valor
                else:
                    valorfuturo.valor_texto = ""
                valorfuturo.save()
                lista_valores.append(valorfuturo)
            if i.tipo_dato=='Numerico':
                textos = Numerico.objects.filter(id=i.valor_id)
                if textos:
                    for texto in textos:
                        valorfuturo.valor_numerico = texto.valor
                else:
                    valorfuturo.valor_numerico = ""
                valorfuturo.save()
                lista_valores.append(valorfuturo)
            if i.tipo_dato=='Fecha':
                textos = Fecha.objects.filter(id=i.valor_id)
                if textos:
                    for texto in textos:
                        valorfuturo.valor_fecha = texto.valor
                else:
                    valorfuturo.valor_fecha = ""
                valorfuturo.save()
                lista_valores.append(valorfuturo)
            if i.tipo_dato=='Archivo Externo':
                textos = Texto.objects.filter(id=i.valor_id)
                if textos:
                    for texto in textos:
                        valorfuturo.valor_archivoexterno = texto.valor
                else:
                    valorfuturo.valor_archivoexterno = ""
                valorfuturo.save()
                lista_valores.append(valorfuturo)
            if i.tipo_dato=='Logico':
                textos = Logico.objects.filter(id=i.valor_id)
                if textos:
                    for texto in textos:
                        valorfuturo.valor_logico = texto.valor
                else:
                    valorfuturo.valor_logico = ""
                valorfuturo.save()
                lista_valores.append(valorfuturo)
    rpadre = Relaciones.objects.filter(padre_id=id_item, faseprimera=id_fase, proyecto=id_proyecto, versionprimero=version, is_active=True)
    rantecesor = Relaciones.objects.filter(antecesor_id=id_item, faseprimera=id_fase, proyecto=id_proyecto, versionprimero=version, is_active=True)
    rhijo = Relaciones.objects.filter(hijo_id=id_item, fasesegunda=id_fase, proyecto=id_proyecto, versionsegundo=version, is_active=True)
    rsucesor = Relaciones.objects.filter(sucesor_id=id_item, fasesegunda=id_fase, proyecto=id_proyecto, versionsegundo=version, is_active=True)
    lista_relaciones = []
    for antecesor in rantecesor:
        valor = ListaRelaciones()
        valor.itemrelacionado = antecesor.sucesor_id
        valor.tiporelacion = 'Sucesor'
        itemrelacionado = Items.objects.get(id=valor.itemrelacionado)
        valor.nombreitemrelacionado = itemrelacionado.nombre
        valor.relacionid = antecesor.id
        valor.save()
        lista_relaciones.append(valor)
    for sucesor in rsucesor:
        valor = ListaRelaciones()
        valor.itemrelacionado = sucesor.antecesor_id
        valor.tiporelacion = 'Antecesor'
        itemrelacionado = Items.objects.get(id=valor.itemrelacionado)
        valor.nombreitemrelacionado = itemrelacionado.nombre
        valor.relacionid = sucesor.id
        valor.save()
        lista_relaciones.append(valor)
    for padre in rpadre:
        valor = ListaRelaciones()
        valor.itemrelacionado = padre.hijo_id
        valor.tiporelacion = 'Hijo'
        itemrelacionado = Items.objects.get(id=valor.itemrelacionado)
        valor.nombreitemrelacionado = itemrelacionado.nombre
        valor.relacionid = padre.id
        valor.save()
        lista_relaciones.append(valor)
    for hijo in rhijo:
        valor = ListaRelaciones()
        valor.itemrelacionado = hijo.padre_id
        valor.tiporelacion = 'Padre'
        itemrelacionado = Items.objects.get(id=valor.itemrelacionado)
        valor.nombreitemrelacionado = itemrelacionado.nombre
        valor.relacionid = hijo.id
        valor.save()
        lista_relaciones.append(valor)
    
    template_name='./items/mostrareliminados.html'
    return render(request, template_name, {'id_proyecto':id_proyecto, 'id_fase': id_fase, 'lista_valores': lista_valores, 'lista_relaciones': lista_relaciones, 'id_item': id_item})

def aumentar_relaciones(item):
    hijos = Relaciones.objects.filter(padre_id=item.id, versionprimero=item.version, is_active=True)
    padres = Relaciones.objects.filter(hijo_id=item.id, versionsegundo=item.version, is_active=True)
    
    for hijo in hijos:
        nuevo = Relaciones()
        nuevo.padre_id = hijo.padre_id
        nuevo.hijo_id = hijo.hijo_id
        nuevo.antecesor_id = hijo.antecesor_id
        nuevo.sucesor_id = hijo.sucesor_id
        nuevo.faseprimera = hijo.faseprimera
        nuevo.fasesegunda = hijo.fasesegunda
        nuevo.proyecto = hijo.proyecto
        nuevo.is_active = True
        nuevo.versionprimero = item.version + 1
        nuevo.versionsegundo = hijo.versionsegundo
        nuevo.save()
    for padre in padres:
        nuevo = Relaciones()
        nuevo.padre_id = padre.padre_id
        nuevo.hijo_id = padre.hijo_id
        nuevo.antecesor_id = padre.antecesor_id
        nuevo.sucesor_id = padre.sucesor_id
        nuevo.faseprimera = padre.faseprimera
        nuevo.fasesegunda = padre.fasesegunda
        nuevo.proyecto = padre.proyecto
        nuevo.is_active = True
        nuevo.versionsegundo = item.version + 1
        nuevo.versionprimero = padre.versionsegundo
        nuevo.save()
    return (True)
