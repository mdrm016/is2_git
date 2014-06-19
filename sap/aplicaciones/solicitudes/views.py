from django.shortcuts import render
from math import ceil
from django.views.generic import TemplateView
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect, HttpResponse
from django.template.context import RequestContext
from aplicaciones.proyectos.models import Proyectos
from aplicaciones.fases.models import Fases
from aplicaciones.items.models import Items, ValorItem
from aplicaciones.relaciones.models import Relaciones
from aplicaciones.lineabase.models import LineaBase
from .models import Solicitudes, Votos, Credenciales
from .forms import SolicitudNuevaForm, SolicitudPrimeraForm, votarSolicitudForm
from datetime import datetime, date, timedelta
from django.contrib.auth.decorators import login_required, permission_required
from django.db.models import Q
from aplicaciones.comite.models import Comite
import logging

# Create your views here.
logger = logging.getLogger(__name__)

def administrar_solicitud_recibidas (request):
    
    """ Recibe un request, se verifica cual es el usuario registrado y se obtiene la lista de solicitudes
    recibidas con los que esta relacionado desplegandolo en pantalla.
    
    @type request: django.http.HttpRequest.
    @param request: Contiene informacion sobre la solicitud web actual que llamo a esta vista administrar_solicitud_recibidas.
    
    @rtype: django.shortcuts.render_to_response.
    @return: solicitudesrecibidas.html, donde se listan las solicitudes de modificacion de item recibidas.
    
    @author: Marcelo Denis.
    
    """
    
    comites = Comite.objects.filter(miembros=request.user)
    list_proyect = []
    for comite in comites:
        list_proyect.append(comite.proyecto)
    solicitudes = Solicitudes.objects.filter(proyecto__in=list_proyect, estado='Pendiente')
    
    pendientes = 0
    lista_solicitud=[]
    for s in solicitudes:
        votantes = s.miembros_que_votaron.all()
        solic_votada = False
        for votante in votantes:
            if votante == request.user:
                solic_votada = True
        tupla = (s, solic_votada)
        if not solic_votada:
            pendientes = pendientes + 1
        lista_solicitud.append(tupla)
    logger.info('Listado de Solicitudes recibidas, hecho por %s' % request.user.username)
    template_name='solicitudes/solicitudesrecibidas.html'
    ctx = {'lista_solicitud':lista_solicitud, 'pendientes':pendientes}
    return render_to_response(template_name, ctx, context_instance=RequestContext(request))

def administrar_solicitud_realizadas (request):
    
    """ Recibe un request, se verifica cual es el usuario registrado y se obtiene la lista de solicitudes
    realizadas con los que esta relacionado desplegandolo en pantalla.
    
    @type request: django.http.HttpRequest.
    @param request: Contiene informacion sobre la solicitud web actual que llamo a esta vista administrar_solicitud_realizadas.
    
    @rtype: django.shortcuts.render_to_response.
    @return: solicitudesrealizadas.html, donde se listan las solicitudes de modificacion de item realizadas.
    
    @author: Marcelo Denis.
    
    """
    
    solicitudes = Solicitudes.objects.filter(usuario=request.user)
    logger.info('Listado de solicitudes realizadas, hecho por %s' % request.user.username)
    template_name='solicitudes/solicitudesrealizadas.html'
    ctx = {'solicitudes':solicitudes}
    return render_to_response(template_name, ctx, context_instance=RequestContext(request))
    
def crear_solicitud(request, id_proyecto, id_fase, id_item):
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
    if proyecto.estado=='Finalizado':
        mensaje = 'El proyecto se encuentra finalizado, no se puede solicitar modificaciones.'
        template_name='./solicitudes/solicitudalerta.html'
        ctx = {'mensaje': mensaje, 'id_proyecto':id_proyecto, 'id_fase': id_fase, 'id_item': id_item, 'proyecto':proyecto, 'fase':fase, 'item': item}
        return render_to_response(template_name, ctx, context_instance=RequestContext(request))
    try:
        credencial = Credenciales.objects.get(item_id=item.id, estado='Habilitado')
    except Credenciales.DoesNotExist:
        credencial = False
    if credencial:
        mensaje = 'Ya existe una solicitud aprobada en proceso para el item seleccionado.'
        template_name='./solicitudes/solicitudalerta.html'
        ctx = {'mensaje': mensaje, 'id_proyecto':id_proyecto, 'id_fase': id_fase, 'id_item': id_item, 'proyecto':proyecto, 'fase':fase, 'item': item}
        return render_to_response(template_name, ctx, context_instance=RequestContext(request))
        
    if request.method == 'POST':
        form = SolicitudNuevaForm(request.POST)
        if form.is_valid():
            usuarionuevo = request.user
            proyectonuevo = proyecto
            fasenueva = fase
            itemnuevo = item
            fechasolic = datetime.today()
            tiemposolic = form.cleaned_data['Tiempo_Solicitado_en_Dias']
            descripcion = form.cleaned_data['Descripcion']
            observaciones = form.cleaned_data['Observaciones']
            estado = 'Pendiente'
            duracionsolic = form.cleaned_data['Duracion_Solicitud_en_Dias']

            solicitud = Solicitudes()
            solicitud.usuario_id = usuarionuevo.id
            solicitud.proyecto_id = proyectonuevo.id
            solicitud.fase_id = fasenueva.id
            solicitud.item_id = itemnuevo.id
            solicitud.fecha_solicitud = fechasolic
            solicitud.tiempo_solicitado = tiemposolic
            solicitud.descripcion = descripcion
            solicitud.observaciones = observaciones
            solicitud.estado = estado
            solicitud.tiempo_esperado = duracionsolic
            solicitud.votos_rechazado = 0
            solicitud.votos_aprobado = 0
            solicitud.save()
            logger.info('Creacion de Solicitud de cambio id %s, hecho por %s' % (solicitud.id, request.user.username))
            mensaje = 'Solicitud creada con exito.'
            template_name='./solicitudes/solicitudcreada.html'
            ctx = {'mensaje': mensaje, 'id_proyecto':id_proyecto, 'id_fase': id_fase, 'id_item': id_item, 'proyecto':proyecto, 'fase':fase, 'item': item}
            return render_to_response(template_name, ctx, context_instance=RequestContext(request))
                
            #return render(request, template_name, {'id_proyecto': id_proyecto, 'id_fase': id_fase, 'id_item': id_item, 'id_tipoitem': id_tipoitem, 'lista_valores': lista_valores, 'lista_atributos': lista_atributos})
    else:
        fechasolic = datetime.today()
        estado = 'Pendiente'
        data = {'Proyecto': proyecto, 'Fase': fase, 'Item': item, 'Fecha_de_Solicitud': fechasolic, 'Estado': estado}
        form = SolicitudPrimeraForm(data)  
        
    template_name='./solicitudes/solicitudnueva.html'
    return render(request, template_name, {'form': form, 'id_proyecto':id_proyecto, 'id_fase': id_fase, 'id_item': id_item, 'proyecto':proyecto, 'fase':fase, 'item': item})

def cancelar_solicitud(request, id_solicitud):
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
    solicitud = Solicitudes.objects.get(id=id_solicitud)
    solicitud.estado = 'Cancelado'
    solicitud.save()
    proyecto = solicitud.proyecto
    fase = solicitud.fase
    
    mensaje = 'Solicitud eliminada con exito.'
    logger.info('Cancelacion de solicitud id %s, hecho por %s' % (solicitud.id, request.user.username))
    template_name='./solicitudes/solicitudalerta.html'
    ctx = {'mensaje': mensaje, 'proyecto':proyecto, 'fase':fase}
    return render_to_response(template_name, ctx, context_instance=RequestContext(request))

def consultar_solicitud(request, id_solicitud):
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
    solicitud = Solicitudes.objects.get(id=id_solicitud)
    proyecto = solicitud.proyecto
    fase = solicitud.fase
    #item = Items.objects.get(proyecto_id=id_proyecto, fase_id=id_fase, id=id_item)
    # conseguir el contexto de las fases y sus estados
    #fases = Fases.objects.filter(id_proyecto = id_proyecto)
    logger.info('Consultad de solicitud con id %s, hecho por %s' % (solicitud.id, request.user.username))
    template_name = './solicitudes/consultarsolicitud.html'
    return render(request, template_name, {'fase': fase, 'proyecto':proyecto, 'fase':fase, 'solicitud': solicitud})

def votar_solicitud(request, id_solicitud):
    """ Recibe un request y el id de la solicitud  que se quiere  votar.
    Se retorna un html que indica al usuario que proceda a aceptar, rechazar la solicitud o
    cancelar la operacion de votar la solicitud

    @type request: django.http.HttpRequest.
    @param request: Contiene informacion sobre la solicitud web actual que llamo a esta vista.

    @rtype: HttpRequest.HttpResponse
    @return: votar.html, donde se solicita el voto a  favor o en contra del miembro del comite

    @author: Eduardo Gimenez

    """

    if request.method == 'POST':
        form = votarSolicitudForm(request.POST)
        if form.is_valid():
            voto = form.cleaned_data['voto']
            solicitud = Solicitudes.objects.get(id = id_solicitud)
            #Registramos el voto del usuario miembro de comite
            if voto == "A":
                miVoto = Votos(miembro=request.user, solicitud=solicitud, fechaDeVotacion=datetime.today(), voto="A")
            else:
                miVoto = Votos(miembro=request.user, solicitud=solicitud, fechaDeVotacion=datetime.today(), voto="R")
            miVoto.save()
            comite = Comite.objects.get(proyecto=solicitud.proyecto)
            cantidad_miembros = comite.miembros.count()
            promedio = int(ceil(cantidad_miembros/2)) + 1
            #Calculamos la  cantidad de votos a favor  y en contra
            votos = Votos.objects.filter(solicitud=solicitud)
            votosAprobado = 0
            votosRechazado = 0
            for votoMiembro in votos:
                if votoMiembro.voto == 'A':
                    votosAprobado = votosAprobado + 1
                if votoMiembro.voto == 'R':
                    votosRechazado = votosRechazado + 1
            #Verificamos los votos para rechazar o aprobar la  solicitud
            cantidad_votos = votosAprobado + votosRechazado
            if cantidad_votos==cantidad_miembros:
                try:
                    credencialitem = Credenciales.objects.get(item_id=solicitud.item_id, estado='Habilitado')
                except Credenciales.DoesNotExist:
                    credencialitem = False
                if credencialitem:
                    solicitud.estado = 'Cancelado'
                    solicitud.save()
                    mensaje = 'Ya existe una solicitud aprobada en proceso para el item. Esta solicitud ha sido descartada.'
                    template_name='./solicitudes/solicitudalerta.html'
                    ctx = {'mensaje': mensaje}
                    return render_to_response(template_name, ctx, context_instance=RequestContext(request))
                if votosAprobado > votosRechazado:
                    solicitud.estado = 'Cancelado'
                    credencial = Credenciales()
                    credencial.usuario = solicitud.usuario
                    credencial.proyecto = solicitud.proyecto
                    credencial.fase = solicitud.fase
                    credencial.item = solicitud.item
                    credencial.version = solicitud.item.version
                    credencial.fecha_aprobacion = date.today()
                    credencial.fecha_expiracion = date.today()+timedelta(days=solicitud.tiempo_solicitado)
                    credencial.estado = 'Habilitado'
                    solicitud.save()
                    credencial.save()
                    logger.info('Generacion de credencial id %s, hecho por %s' % (credencial.id, request.user.username))
                    habilitar_items(credencial)
                    mensaje = 'Credencial Generada'
                    template_name='./solicitudes/credencialcreada.html'
                    ctx = {'mensaje': mensaje, 'credencial': credencial}
                    return render_to_response(template_name, ctx, context_instance=RequestContext(request))
                else:
                    solicitud.estado = 'Reprobada'
                    mensaje = 'La solicitud ha sido Reprobada'
            else:
                mensaje = 'Su voto ha sido procesado'

            logger.info('Votacion de solicitud con id %d, hecho por %s' % (solicitud.id, request.user.username))
            solicitud.save()
            template_name='./solicitudes/solicitudalerta.html'
            ctx = {'mensaje': mensaje}
            return render_to_response(template_name, ctx, context_instance=RequestContext(request))

    else:
        form = votarSolicitudForm()
    template_name='./solicitudes/votarsolicitud.html'
    return render(request, template_name, {'form': form, 'id_solicitud':id_solicitud})

def impacto(request, id_proyecto, id_fase, id_item):
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
    
    imonetario = impacto_monetario(id_item)
    itemporal = impacto_temporal(id_item)
    items_afectado = calcular_items_afectados(id_item)
    items_afectados = []
    for items_af in items_afectado:
        if items_af.id!=item.id:
            items_afectados.append(items_af)

    logger.info('Calculo de impacto para item %s para la Solicitud de cambio, hecho por %s' % (item.nombre, request.user.username))
    ctx = {'id_proyecto':id_proyecto, 'id_fase': id_fase, 'id_item': id_item, 'impacto_monetario': imonetario, 'impacto_temporal': itemporal, 'items_afectados': items_afectados}
    template_name = './items/impacto.html'
    return render_to_response(template_name, ctx, context_instance=RequestContext(request))

def impacto_monetario(id_item):
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
    costo = 0
    try:
        hijos = Items.objects.filter(padre=id_item)
    except Items.DoesNotExist:
        hijos = False
    if hijos:
        for hijo in hijos:
            costo = costo + impacto_monetario(hijo.id)
        costo = costo + item.costoMonetario
        return costo
    else:
        return item.costoMonetario
            
def impacto_temporal(id_item):
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
    costo = 0
    try:
        hijos = Items.objects.filter(padre=id_item)
    except Items.DoesNotExist:
        hijos = False
    if hijos:
        for hijo in hijos:
            costo = costo + impacto_temporal(hijo.id)
        costo = costo + item.costoTemporal
        return costo
    else:
        return item.costoTemporal

def calcular_items_afectados(id_item):
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
    lista_hijos = []
    try:
        hijos = Items.objects.filter(padre=id_item)
    except Items.DoesNotExist:
        hijos = False
    if hijos:
        for hijo in hijos:
            lista_hijos.extend(calcular_items_afectados(hijo.id))
        lista_hijos.append(item)
        return lista_hijos
    else:
        lista_hijos.append(item)
        return lista_hijos

def habilitar_items(credencial):
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
    item = Items.objects.get(id=credencial.item_id)
    fase = Items.objects.get(id=credencial.fase_id)
    lineasbase = LineaBase.objects.filter(fase_id=credencial.fase_id)
    items = []
    for lb in lineasbase:
        itemslb = lb.items.all()
        if item in itemslb:
            lineabase = lb
            items = lineabase.items.all()
            lineabase.is_active = False
            lineabase.save()
    
    for itemhijo in items:
        if itemhijo.estado=='Bloqueado' or itemhijo.estado=='Validado':
            itemhijo.estado='En Revision'
            itemhijo.save()
    
    lista_hijos = calcular_items_afectados(item.id)
    for hijo in lista_hijos:
        if hijo.estado=='Bloqueado' or hijo.estado=='Validado':
            hijo.estado = 'En Revision'
            hijo.save()
    item.estado = 'Habilitado'
    item.save()
    
def administrar_credenciales (request):
    
    """ Recibe un request, se verifica cual es el usuario registrado y se obtiene la lista de credenciales
    habilitadas con los que esta relacionado desplegandolo en pantalla.
    
    @type request: django.http.HttpRequest.
    @param request: Contiene informacion sobre la solicitud web actual que llamo a esta vista administrar_credenciales.
    
    @rtype: django.shortcuts.render_to_response.
    @return: credenciales.html, donde se listan las credenciales de modificacion de item habilitadas.
    
    @author: Marcelo Denis.
    
    """
    
    credenciales = Credenciales.objects.filter(usuario=request.user)
    logger.info('Listado de Credenciales, hecho por %s' % request.user.username)
    template_name='solicitudes/credenciales.html'
    ctx = {'lista_credenciales':credenciales}
    return render_to_response(template_name, ctx, context_instance=RequestContext(request))

def consultarCredencial(request, id_credencial):

    """ Recibe un request, se verifica cual es el usuario registrado y despliega los
     datos que pertenece a la credencial que se consulta

    @type request: django.http.HttpRequest.
    @param request: Contiene informacion sobre la solicitud web actual que llamo a esta vista administrar_credenciales.

    @rtype: django.shortcuts.render_to_response.
    @return: consultar_credencial.html, donde se despliega los datos de la credencial.

    @author: Eduardo Gimenez.

    """

    credencial = Credenciales.objects.get(id=id_credencial)
    logger.info('Consulta de credncial con id %s, hecho por %s' % (credencial.id, request.user.username))
    template_name='solicitudes/consultar_credencial.html'
    ctx = {'credencial':credencial}
    return render_to_response(template_name, ctx, context_instance=RequestContext(request))

def cancelar_credencial(request, id_credencial):
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
    credencial = Credenciales.objects.get(id=id_credencial)
    
    lbs = LineaBase.objects.filter(fase_id=credencial.fase.id)
    eslb = False
    for lb in lbs:
        items = lb.items.all()
        for item in items:
            if credencial.item_id==item.id:
                eslb = lb
    if eslb:
        items = eslb.items.all()
        for item in items:
            item.estado = 'Bloqueado'
            item.save()
        eslb.is_active = True
        eslb.save()
    credencial.estado='Finalizado'
    credencial.save()

    revertir_credencial(credencial.proyecto_id, credencial.fase_id, credencial)
    
    mensaje = 'Credencial cancelada.'
    logger.info('Cancelacion de Credencial con id %s, hecho por %s' % (credencial.id, request.user.username))
    template_name='./solicitudes/solicitudalerta.html'
    ctx = {'mensaje': mensaje}
    return render_to_response(template_name, ctx, context_instance=RequestContext(request))

def revertir_credencial(id_proyecto, id_fase, credencial):
    version_anterior = credencial.version
    item = Items.objects.get(id=credencial.item_id)
    version_actual = item.version
    if version_actual>version_anterior:
        for i in range(version_anterior+1,version_actual+1):
            atributositem = ValorItem.objects.filter(proyecto_id=id_proyecto, fase_id=id_fase, item_id=item.id, version=i)
            if atributositem:
                for atrib in atributositem:
                    atrib.version=0
                    atrib.save()
            try:
                relacionitem = Relaciones.objects.get(item=item.id, version=i)
            except Relaciones.DoesNotExist:
                relacionitem = False
            if relacionitem:
                relacionitem.version = 0
                relacionitem.save()