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
from aplicaciones.relaciones.models import Relaciones, ListaRelacion, VersionRelacion
from .models import Items, ListaValores, ValorItem
from datetime import datetime
from django.contrib.auth.decorators import login_required, permission_required
from django.db.models import Q
from forms import ItemNuevoForm, ItemModificadoForm
from aplicaciones.tipoitem.views import ordenar_mantener
from aplicaciones.relaciones.views import cargar_atributos, aumentar_version

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
            item.padre=0
            item.save()
            
            if fase.estado == 'DF':
                fase.estado = 'DR'
                fase.save()

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
            relaciones = VersionRelacion.objects.get(item_id=itemactual.id, version=itemactual.version)
            relacionpadre = Relaciones.objects.get(id=relaciones.relacion_id)
            padre = Items.objects.get(id=relacionpadre.padre)
            if padre.is_active==True:
                aumentar_version(relaciones, itemactual)
                
            itemactual.version = itemactual.version + 1
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
    
    relacionversion = VersionRelacion.objects.get(item_id=item.id, version=item.version)
    relacionpadre = Relaciones.objects.get(id=relacionversion.relacion_id)
    itempadre = Items.objects.get(id=relacionpadre.padre)
    if item.padre!=0:
        itempadre = Items.objects.get(id=item.padre)
        if itempadre.is_active==True:
            padre = ListaRelacion()
            padre.nombreitem = itempadre.nombre
            relacionpadre = Relaciones.objects.get(padre=item.padre, hijo=item.id)
            padre.relacion = relacionpadre.id

    template_name='./items/mostraratributos.html'
    return render(request, template_name, {'id_proyecto':id_proyecto, 'id_fase': id_fase, 'lista_valores': lista_valores, 'lista_relaciones': lista_relaciones, 'id_item': id_item, 'padre':padre})

def revertir_version(request, id_proyecto, id_fase, id_item, version):
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
    item = Items.objects.get(proyecto_id=id_proyecto, fase_id=id_fase, id=id_item)
    
    valoresitem = ValorItem.objects.filter(proyecto=id_proyecto, fase=id_fase, item=id_item, version=version).order_by('orden')
    if valoresitem:
        for filaitem in valoresitem:
            if not (cargar_atributos(filaitem.valor_id, filaitem.nombre_atributo, filaitem.orden, filaitem.tabla_valor_nombre, id_proyecto, id_fase, int(id_item))):
                estamosenproblemas.append(sjetbg)
                
    relacionesactuales = VersionRelacion.objects.filter(item_id=item.id, version=item.version)
    for raversion in relacionesactuales:
        ractual = Relaciones.objects.filter(id=raversion.relacion_id)
        for ra in ractual:
            if ra.hijo==item.id:
                padreitem = Items.objects.filter(id=ra.padre)    
            else:
                padreitem = Items.objects.filter(id=ra.hijo)
            versionrelacionespadre = VersionRelacion.objects.filter(item_id=padreitem.id, version=padreitem.version).exclude(relacion_id=raversion.relacion_id)
            aumentar_version(versionrelacionespadre, padreitem)
            valorespadre = ValorItem.objects.filter(proyecto=id_proyecto, fase=id_fase, item=padreitem.id, version=padreitem.version).order_by('orden')
            if valorespadre:
                for fila in valorespadre:
                    if not (cargar_atributos(fila.valor_id, fila.nombre_atributo, fila.orden, fila.tabla_valor_nombre, id_proyecto, id_fase, int(padreitem.id))):
                        estamosenproblemas.append(sjetbg)
            padreitem.version = padreitem.version +1
            padreitem.save()

    relversiones = VersionRelacion.objects.filter(item_id=item.id, version=version)
    for rv in relversiones:
        relaciontodo = Relaciones.objects.filter(id=rv.relacion_id)
        for relacion in relaciontodo:
            if relacion.hijo==item.id:
                padre = Items.objects.get(id=relacion.padre)
                if padre.is_active==True:
                    relacionespadre = VersionRelacion.objects.filter(item_id=padre.id, version=padre.version)
                    aumentar_version(relacionespadre, padre)
                    padrevalores = ValorItem.objects.filter(proyecto=id_proyecto, fase=id_fase, item=padre.id, version=padre.version).order_by('orden')
                    if padrevalores:
                        for fila in padrevalores:
                            if not (cargar_atributos(fila.valor_id, fila.nombre_atributo, fila.orden, fila.tabla_valor_nombre, id_proyecto, id_fase, int(padre.id))):
                                estamosenproblemas.append(sjetbg)
                    nuevoversion = VersionRelacion()
                    nuevoversion.relacion_id = relacion.id
                    nuevoversion.item_id = item.id
                    nuevoversion.version = item.version + 1
                    nuevoversion.save()
                    if padre.estado=='Terminado':
                        padre.estado = 'En Construccion'
                    nuevoversion = VersionRelacion()
                    nuevoversion.relacion_id = relacion.id
                    nuevoversion.item_id = padre.id
                    nuevoversion.version = padre.version + 1
                    nuevoversion.save()
                    padre.version = padre.version + 1
                    padre.save()
                    item.padre = padre.id
    
    item.version = item.version + 1
    if item.estado=='Terminado':
        item.estado = 'En Construccion'
    item.save()
    mensaje = 'Version Revertida con exito.'
    template_name='./items/itemalerta.html'
    ctx = {'mensaje': mensaje, 'id_proyecto':id_proyecto, 'id_fase': id_fase}
    return render_to_response(template_name, ctx, context_instance=RequestContext(request))

def modificar_item(request, id_proyecto, id_fase, id_item):
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
    fase = Fases.objects.get(id=id_fase, proyecto_id=id_proyecto)
    item = Items.objects.get(proyecto_id=id_proyecto, fase_id=id_fase, id=id_item)
    mensaje=''
    if request.method == 'POST':
        if fase.estado == 'FD' or item.estado=='En Revision' or item.estado=='Bloqueado' or item.estado=='Validado':
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
    fase = Fases.objects.get(id=id_fase, proyecto_id=id_proyecto)
    item = Items.objects.get(proyecto_id=id_proyecto, fase_id=id_fase, id=id_item)
    # conseguir el contexto de las fases y sus estados
    #fases = Fases.objects.filter(id_proyecto = id_proyecto)
    ctx = {'item':item}
    template_name = './items/consultaritem.html'
    return render(request, template_name, {'item': item, 'id_proyecto': id_proyecto, 'fase': fase, 'id_fase': id_fase, 'id_item': id_item})

def consultar_atributos(request, id_proyecto, id_fase, id_item):
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
    fase = Fases.objects.get(proyecto_id=id_proyecto, id=id_fase)
    item = Items.objects.get(proyecto_id=id_proyecto, fase_id=id_fase, id=id_item)
    version = item.version
    if fase.estado=='FD' or item.estado=='Validado' or item.estado=='En Revision' or item.estado=='Bloqueado':
        mensaje = 'No se puede eliminar el item. Dirijase a consultar.'
        template_name='./items/itemalerta.html'
        return render(request, template_name, {'id_proyecto':id_proyecto, 'id_fase': id_fase, 'mensaje': mensaje, 'id_item': id_item})
    else:
        versionesrelacion = VersionRelacion.objects.filter(item_id=item.id, version=item.version)
        for vr in versionesrelacion:
            relacion = Relaciones.objects.get(id=vr.relacion_id)
            if relacion.hijo==item.id:
                itemrelacionado = Items.objects.get(id=relacion.padre)
            else:
                itemrelacionado = Items.objects.get(id=relacion.hijo)
            relacionespadre = VersionRelacion.objects.filter(item=itemrelacionado.id, version=itemrelacionado.version).exclude(relacion_id=relacion.id)
            aumentar_version(relacionespadre, itemrelacionado)
            itemrelacionadovalores = ValorItem.objects.filter(proyecto=id_proyecto, fase=id_fase, item=itemrelacionado.id, version=itemrelacionado.version).order_by('orden')
            if itemrelacionadovalores:
                for fila in itemrelacionadovalores:
                    if not cargar_atributos(fila.valor_id, fila.nombre_atributo, fila.orden, fila.tabla_valor_nombre, id_proyecto, id_fase, int(itemrelacionado.id)):
                        estamosenproblemas.append(sthwet)
            itemrelacionado.version = itemrelacionado.version + 1
            itemrelacionado.save()
            
        item.is_active = False
        item.save()
        mensaje ='Eliminacion exitosa.'
    template_name = './items/itemalerta.html'
    return render(request, template_name, {'id_proyecto':id_proyecto, 'id_fase': id_fase, 'mensaje': mensaje, 'id_item': id_item})

def listar_eliminados(request, id_proyecto, id_fase):
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
    if proyecto.estado=='Finalizado':
        mensaje = 'El proyecto ha finzalizado.'
        template_name = './items.itemalerta.html'
        return render(request, template_name, {'id_proyecto':id_proyecto, 'id_fase': id_fase, 'mensaje': mensaje})
    lista_eliminados = Items.objects.filter(proyecto_id=id_proyecto, fase_id=id_fase, is_active=False)
    template_name='./items/listareliminados.html'
    return render(request, template_name, {'id_proyecto':id_proyecto, 'id_fase': id_fase, 'lista_eliminados': lista_eliminados})

def revivir_eliminado(request, id_proyecto, id_fase, id_item, version):
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
    item = Items.objects.get(proyecto_id=id_proyecto, fase_id=id_fase, id=id_item)
    versionesrel = VersionRelacion.objects.filter(item_id=item.id, version=version)
    for vr in versionesrel:
        relacion = Relaciones.objects.get(id=vr.relacion_id)
        if (relacion.hijo==item.id):
            padre = Items.objects.get(id=relacion.padre)
            if padre.is_active==True:
                valorespadre = ValorItem.objects.filter(proyecto=id_proyecto, fase=id_fase, item=padre.id, version=padre.version).order_by('orden')
                for filaitem in valorespadre:
                    if not (cargar_atributos(filaitem.valor_id, filaitem.nombre_atributo, filaitem.orden, filaitem.tabla_valor_nombre, id_proyecto, id_fase, int(padre.id))):
                        estamosenproblemas.append(sjetbg)
                relacionespadre = VersionRelacion.objects.filter(item_id=padre.id, version=padre.version)
                aumentar_version(relacionespadre, padre)
                versionnueva = VersionRelacion()
                versionnueva.item_id = padre.id
                versionnueva.relacion_id = relacion.id
                versionnueva.version = padre.version + 1
                versionnueva.save()
                padre.version = padre.version +1
                versionnueva = VersionRelacion()
                versionnueva.item_id = item.id
                versionnueva.relacion_id = relacion.id
                versionnueva.version = item.version + 1
                versionnueva.save()
                item.padre = padre.id
                padre.save()
    nombres = Items.objects.filter(proyecto_id=id_proyecto, fase_id=id_fase, nombre=item.nombre, is_active=True)
    if nombres:
        mensaje = 'El nombre de item ya existe actualmente.'
        lista_eliminados = Items.objects.filter(proyecto_id=id_proyecto, fase_id=id_fase, is_active=False)
        template_name='./items/listareliminados.html'
        ctx = {'mensaje': mensaje, 'id_proyecto':id_proyecto, 'id_fase': id_fase, 'lista_eliminados': lista_eliminados}
        return render_to_response(template_name, ctx, context_instance=RequestContext(request))
    
    valoresitem = ValorItem.objects.filter(proyecto=id_proyecto, fase=id_fase, item=id_item, version=version).order_by('orden')
    if valoresitem:
        for filaitem in valoresitem:
            if not (cargar_atributos(filaitem.valor_id, filaitem.nombre_atributo, filaitem.orden, filaitem.tabla_valor_nombre, id_proyecto, id_fase, int(id_item))):
                estamosenproblemas.append(sjetbg)

    item.is_active=True
    item.version = item.version + 1
    item.save()
    
    mensaje = 'Item revivido con exito.'
    template_name='./items/itemalerta.html'
    ctx = {'mensaje': mensaje, 'id_proyecto':id_proyecto, 'id_fase': id_fase}
    return render_to_response(template_name, ctx, context_instance=RequestContext(request))

def consultar_eliminado(request, id_proyecto, id_fase, id_item):
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
                
    versionrelaciones = VersionRelacion.objects.filter(item_id=item.id, version=version) 
    itempadre = Items.objects.get(id=item.padre, is_active=True)
    if itempadre:
        padre = ListaRelacion()
        padre.nombreitem = itempadre.nombre
        relacionpadre = Relaciones.objects.filter(padre=item.padre, hijo=item.id)
        for rp in relacionpadre:
            padre.relacion = rp.id
    relaciones = VersionRelacion.objects.filter(item_id=item.id, version=item.version).exclude(relacion_id=padre.relacion)
    lista_relaciones = []
    for relacion in relaciones:
        hijo = ListaRelacion()
        rhijo = Relaciones.objects.get(id=relacion.relacion_id)
        itemhijo = Items.objects.get(id=rhijo.hijo)
        hijo.nombreitem = itemhijo.nombre
        hijo.relacion = rhijo.id
        hijo.save()
        lista_relaciones.append(hijo)
        hijo.delete()

    template_name='./items/mostrareliminados.html'
    return render(request, template_name, {'id_proyecto':id_proyecto, 'id_fase': id_fase, 'lista_valores': lista_valores, 'lista_relaciones': lista_relaciones, 'id_item': id_item, 'padre': padre})

def consultar_relaciones(request, id_proyecto, id_fase, id_item):
    """ 
    Recibe un request, se verifica cual es el usuario registrado y el proyecto del cual se solicita,
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
    idpadre = item.padre
    versionrelaciones = VersionRelacion.objects.filter(item_id=item.id, version=item.version) 
    itemspadre = Items.objects.filter(id=idpadre)
    lista_relaciones = []
    for i in itemspadre:
        itempadre = i
        if itempadre and itempadre.is_active==True:
            padre = ListaRelacion()
            padre.nombreitem = itempadre.nombre
            relacionpadre = Relaciones.objects.filter(padre=item.padre, hijo=item.id)
            for rp in relacionpadre:
                padre.relacion = rp.id
            relaciones = VersionRelacion.objects.filter(item_id=item.id, version=item.version).exclude(relacion_id=padre.relacion)
            for relacion in relaciones:
                hijo = ListaRelacion()
                rhijo = Relaciones.objects.get(id=relacion.relacion_id)
                itemhijo = Items.objects.get(id=rhijo.hijo)
                hijo.nombreitem = itemhijo.nombre
                hijo.relacion = rhijo.id
                hijo.save()
                lista_relaciones.append(hijo)
                hijo.delete()

    ctx = {'lista_relaciones': lista_relaciones, 'id_proyecto':id_proyecto, 'id_fase': id_fase, 'id_item': id_item}
    template_name = './items/relaciones.html'
    return render_to_response(template_name, ctx, context_instance=RequestContext(request))
