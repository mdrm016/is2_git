from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect, HttpResponse
from django.template.context import RequestContext
from aplicaciones.proyectos.models import Proyectos
from aplicaciones.fases.models import Fases
from .models import Items, ListaValores, ValorItem
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
    item = Items.objects.get(id=id_tipoitem)
    if request.method == 'POST':
        form = ItemNuevoForm(request.POST)
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
            
            repetido = 'Vacio'
            rep= Items.objects.filter(proyecto_id=id_proyecto, fase_id=id_fase, is_active=True, nombre=nombre)
            if rep:
                mensaje = 'El nombre de item ya existe para esta fase'
                data = {'Nombre_de_Item': nombre, 'Prioridad': prioridad, 'Descripcion': descripcion, 'Observaciones': observaciones, 'Costo_Temporal': costo_temporal, 'Costo_Monetario': costo_monetario, 'Complejidad': complejidad}
                form = ItemNuevoForm(data)
                ctx = {'form': form, 'mensaje':mensaje, 'id_proyecto': id_proyecto, 'id_fase': id_fase, 'id_tipoitem': id_tipoitem, 'proyecto':proyecto, 'fase':fase}
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
            ctx = {'mensaje': mensaje, 'id_proyecto':id_proyecto, 'id_fase': id_fase, 'proyecto':proyecto, 'fase':fase}
            return render_to_response(template_name, ctx, context_instance=RequestContext(request))
                
            #return render(request, template_name, {'id_proyecto': id_proyecto, 'id_fase': id_fase, 'id_item': id_item, 'id_tipoitem': id_tipoitem, 'lista_valores': lista_valores, 'lista_atributos': lista_atributos})
    else: 
        form = SolicitudNuevaForm()  
        
    template_name='./solicitudes/solicitudnueva.html'
    return render(request, template_name, {'form': form, 'id_proyecto':id_proyecto, 'id_fase': id_fase, 'id_tipoitem': id_tipoitem, 'proyecto':proyecto, 'fase':fase})

