from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect, HttpResponse
from django.template.context import RequestContext
from aplicaciones.proyectos.models import Proyectos
from aplicaciones.fases.models import Fases
from aplicaciones.items.models import Items
from .models import Solicitud
from .forms import SolicitudNuevaForm, SolicitudPrimeraForm
from datetime import datetime
from django.contrib.auth.decorators import login_required, permission_required
from django.db.models import Q

# Create your views here.

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
            usuarionuevo = form.cleaned_data['Usuario']
            proyectonuevo = proyecto
            fasenueva = fase
            itemnuevo = item
            fechasolic = datetime.now()
            tiemposolic = form.cleaned_data['Tiempo_Solicitado_en_Dias']
            descripcion = form.cleaned_data['Descripcion']
            observaciones = form.cleaned_data['Observaciones']
            estado = 'Pendiente'
            duracionsolic = form.cleaned_data['Duracion_Solicitud_en_Dias']

            solicitud = Solicitud()
            solicitud.usuario_id = usuarionuevo
            solicitud.proyecto_id = proyectonuevo
            solicitud.fase_id = fasenueva
            solicitud.item_id = itemnuevo
            solicitud.fecha_solicitud = fechasolic
            solicitud.tiempo_solicitado = tiemposolic
            solicitud.descripcion = descripcion
            solicitud.observaciones = observaciones
            solicitud.estado = estado
            solicitud.tiempo_esperado = duracionsolic
            solicitud.save()

            mensaje = 'Solicitud creada con exito.'
            template_name='./solicitudes/solicitudalerta.html'
            ctx = {'mensaje': mensaje, 'id_proyecto':id_proyecto, 'id_fase': id_fase, 'id_item': id_item, 'proyecto':proyecto, 'fase':fase, 'item': item}
            return render_to_response(template_name, ctx, context_instance=RequestContext(request))
                
            #return render(request, template_name, {'id_proyecto': id_proyecto, 'id_fase': id_fase, 'id_item': id_item, 'id_tipoitem': id_tipoitem, 'lista_valores': lista_valores, 'lista_atributos': lista_atributos})
    else:
        fechasolic = datetime.now()
        estado = 'Pendiente'
        data = {'Proyecto': proyecto, 'Fase': fase, 'Item': item, 'Fecha_de_Solicitud': fechasolic, 'Estado': estado}
        form = SolicitudPrimeraForm(data)  
        
    template_name='./solicitudes/solicitudnueva.html'
    return render(request, template_name, {'form': form, 'id_proyecto':id_proyecto, 'id_fase': id_fase, 'id_item': id_item, 'proyecto':proyecto, 'fase':fase, 'item': item})

