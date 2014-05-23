from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect, HttpResponse
from django.template.context import RequestContext
from aplicaciones.proyectos.models import Proyectos
from aplicaciones.fases.models import Fases
from aplicaciones.items.models import Items
from .models import Solicitudes
from .forms import SolicitudNuevaForm, SolicitudPrimeraForm
from datetime import datetime
from django.contrib.auth.decorators import login_required, permission_required
from django.db.models import Q
from aplicaciones.comite.models import Comite

# Create your views here.

def administrar_solicitud_recibidas (request):
    
    comites = Comite.objects.filter(miembros=request.user)
    list_proyect = []
    for comite in comites:
        list_proyect.append(comite.proyecto)
    solicitudes = Solicitudes.objects.filter(proyecto__in=list_proyect)
    qset = (
                Q(estado__icontains='Pendiente') 
            )
    pendientes=solicitudes.filter(qset).distinct().count()
    
    template_name='solicitudes/solicitudesrecibidas.html'
    ctx = {'solicitudes':solicitudes, 'pendientes':pendientes}
    return render_to_response(template_name, ctx, context_instance=RequestContext(request))

def administrar_solicitud_realizadas (request):
    
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
            form.clean()
            nombreRol = form.cleaned_data['Nombre_de_Rol']
            permisos = form.cleaned_data['Permisos']
            proyecto = form.cleaned_data['Proyecto']
            descripcion = form.cleaned_data['Descripcion']

            rol = Roles.objects.create(name = nombreRol)
            for permiso in permisos:
                rol.permissions.add(Permission.objects.get(codename=permiso))
            if proyecto:
                p = Proyectos.objects.get(id=proyecto)
            else:
                p = ''
            rol.proyecto = p
            rol.descripcion = descripcion
            rol.save()

            template_name='./Roles/rolcreado.html'
            return render(request, template_name)
    else:
        form = RolForm()

    permisos = Permission.objects.filter(id__gt=18)
    parte1 = permisos.filter(id__range=(19,46))
    parte2 = permisos.filter(id__gt=65)
    permisos = []
    permisos.extend(parte1)
    permisos.extend(parte2)
    permisos = [(permiso.codename, permiso.name) for permiso in permisos]
    template_name='./Roles/rolnuevo.html'
    return render(request, template_name, {'form': form, 'permisos': permisos})
