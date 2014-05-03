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
                        valoritems_guardado = ValorItem.objects.get(item_id = id_item, nombre_atributo = nombreatributo, tipo_dato = tipodatoatributo, version = versionitem-1, orden = posicion)
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
                        valoritems_guardado = ValorItem.objects.get(item_id = id_item, nombre_atributo=nombreatributo, tipo_dato = tipodatoatributo, version = versionitem-1, orden = posicion)
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
        if not error:
            itemactual.version = versionitem
            itemactual.save()
            mensaje = 'Atributos modificados con extito.'
            template_name='./items/itemalerta.html'
            ctx = {'mensaje': mensaje, 'id_proyecto':id_proyecto, 'id_fase': id_fase,}
            return render_to_response(template_name, ctx, context_instance=RequestContext(request))
        else:
            #deshacemos las acciones del post, para que no se creem campos duplicados
            atributositem = ValorItem.objects.filter(pk__in=lista_desh)
            for atrib_item in atributositem:
                atrib_item.delete()

        
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
                
    template_name='./items/mostraratributos.html'
    return render(request, template_name, {'id_proyecto':id_proyecto, 'id_fase': id_fase, 'lista_valores': lista_valores, 'id_item': id_item})

def revertir_version(request, id_proyecto, id_fase, id_item, version):
    item = Items.objects.get(id=id_item)
    versionnueva = item.version + 1
    valoresitem = ValorItem.objects.filter(proyecto=id_proyecto, fase=id_fase, item=id_item, version=version).order_by('orden')
    if valoresitem:
        for filaitem in valoresitem:
            valor = ValorItem()
            valor.item_id = id_item
            valor.orden = filaitem.orden
            valor.proyecto_id = id_proyecto
            valor.fase_id = id_fase
            valor.version = versionnueva
            if filaitem.tipo_dato=='Numerico':
                num = Numerico()
                viejo = Numerico.objects.get(id=filaitem.valor_id)
                num.valor = viejo.valor
                num.id_item = id_item
                num.nombre_atributo = viejo.nombre_atributo
                num.precision = viejo.precision
                num.longitud = viejo.longitud
                num.obligatorio = viejo.obligatorio
                num.save()
                valor.valor_id = num.id
                valor.tabla_valor_nombre = 'tipoatributo_numerico'
                valor.nombre_atributo = filaitem.nombre_atributo
                valor.tipo_dato = filaitem.tipo_dato
                valor.save()
            if filaitem.tipo_dato=='Texto':
                num = Texto()
                viejo = Texto.objects.get(id=filaitem.valor_id)
                num.valor = viejo.valor
                num.id_item = id_item
                num.nombre_atributo = viejo.nombre_atributo
                num.longitud = viejo.longitud
                num.obligatorio = viejo.obligatorio
                num.save()
                valor.valor_id = num.id
                valor.tabla_valor_nombre = 'tipoatributo_texto'
                valor.nombre_atributo = filaitem.nombre_atributo
                valor.tipo_dato = filaitem.tipo_dato
                valor.save()
            if filaitem.tipo_dato=='Fecha':
                num = Fecha()
                viejo = Fecha.objects.get(id=filaitem.valor_id)
                num.valor = viejo.valor
                num.id_item = id_item
                num.nombre_atributo = viejo.nombre_atributo
                num.obligatorio = viejo.obligatorio
                num.save()
                valor.valor_id = num.id
                valor.tabla_valor_nombre = 'tipoatributo_fecha'
                valor.nombre_atributo = filaitem.nombre_atributo
                valor.tipo_dato = filaitem.tipo_dato
                valor.save()
            if filaitem.tipo_dato=='Logico':
                num = Logico()
                viejo = Logico.objects.get(id=filaitem.valor_id)
                num.valor = viejo.valor
                num.id_item = id_item
                num.nombre_atributo = viejo.nombre_atributo
                num.obligatorio = viejo.obligatorio
                num.save()
                valor.valor_id = num.id
                valor.tabla_valor_nombre = 'tipoatributo_logico'
                valor.nombre_atributo = filaitem.nombre_atributo
                valor.tipo_dato = filaitem.tipo_dato
                valor.save()
            if filaitem.tipo_dato=='Archivo Externo':
                num = ArchivoExterno()
                viejo = ArchivoExterno.objects.get(id=filaitem.valor_id)
                num.valor = viejo.valor
                num.id_item = id_item
                num.nombre_atributo = viejo.nombre_atributo
                num.obligatorio = viejo.obligatorio
                num.save()
                valor.valor_id = num.id
                valor.tabla_valor_nombre = 'tipoatributo_archivoexterno'
                valor.nombre_atributo = filaitem.nombre_atributo
                valor.tipo_dato = filaitem.tipo_dato
                valor.save()
    item.version = versionnueva
    item.save()
    
    mensaje = 'Version Revertida con exito.'
    template_name='./items/itemalerta.html'
    ctx = {'mensaje': mensaje, 'id_proyecto':id_proyecto, 'id_fase': id_fase}
    return render_to_response(template_name, ctx, context_instance=RequestContext(request))

