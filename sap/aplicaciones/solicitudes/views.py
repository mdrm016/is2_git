from django.shortcuts import render
from math import ceil
from django.views.generic import TemplateView
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect, HttpResponse
from django.template.context import RequestContext
from aplicaciones.proyectos.models import Proyectos
from aplicaciones.fases.models import Fases
from aplicaciones.items.models import Items
from .models import Solicitudes, Votos, Credenciales
from .forms import SolicitudNuevaForm, SolicitudPrimeraForm, votarSolicitudForm
from datetime import datetime, date, timedelta
from django.contrib.auth.decorators import login_required, permission_required
from django.db.models import Q
from aplicaciones.comite.models import Comite

# Create your views here.

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
    solicitudes = Solicitudes.objects.filter(proyecto__in=list_proyect)
    
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
    if fase.estado=='FD':
        mensaje = 'La fase se encuentra en estado finalizado, no se puede solicitar modificaciones.'
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

            mensaje = 'Solicitud creada con exito.'
            template_name='./solicitudes/solicitudcreada.html'
            ctx = {'mensaje': mensaje, 'id_proyecto':id_proyecto, 'id_fase': id_fase, 'id_item': id_item, 'proyecto':proyecto, 'fase':fase, 'item': item}
            return render_to_response(template_name, ctx, context_instance=RequestContext(request))
                
            #return render(request, template_name, {'id_proyecto': id_proyecto, 'id_fase': id_fase, 'id_item': id_item, 'id_tipoitem': id_tipoitem, 'lista_valores': lista_valores, 'lista_atributos': lista_atributos})
    try:
        solicitudexistente = Solicitudes.objects.get(item_id=id_item, estado='Pendiente')
    except Solicitudes.DoesNotExist:
        solicitudexistente = False
    if solicitudexistente:
        mensaje = 'Ya existe una solicitud pendiente para la modificacion del item seleccionado.'
        template_name='./solicitudes/solicitudalerta.html'
        ctx = {'mensaje': mensaje, 'id_proyecto':id_proyecto, 'id_fase': id_fase, 'id_item': id_item, 'proyecto':proyecto, 'fase':fase, 'item': item}
        return render_to_response(template_name, ctx, context_instance=RequestContext(request))
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
                if votosAprobado > votosRechazado:
                    solicitud.estado = 'Aprobada'
                    credencial = Credenciales()
                    credencial.usuario = solicitud.usuario
                    credencial.proyecto = solicitud.proyecto
                    credencial.fase = solicitud.fase
                    credencial.item = solicitud.item
                    credencial.fecha_aprobacion = date.today()
                    credencial.fecha_expiracion = date.today()+timedelta(days=solicitud.tiempo_solicitado)
                    credencial.estado = 'Habilitado'
                    credencial.save()
                    mensaje = 'Credencial Generada'
                    template_name='./solicitudes/credencialcreada.html'
                    ctx = {'mensaje': mensaje, 'credencial': credencial}
                    return render_to_response(template_name, ctx, context_instance=RequestContext(request))
                else:
                    solicitud.estado = 'Reprobada'
                    mensaje = 'La solicitud ha sido Reprobada'
            else:
                mensaje = 'Su voto ha sido procesado'
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