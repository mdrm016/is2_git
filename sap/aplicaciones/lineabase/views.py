import ho.pisa as pisa
import cStringIO as StringIO
import cgi
from django.shortcuts import render, render_to_response, HttpResponseRedirect
from aplicaciones.proyectos.models import Proyectos
from aplicaciones.fases.models import Fases
from aplicaciones.items.models import Items
from aplicaciones.roles.models import Roles
from models import LineaBase
from django.core.exceptions import PermissionDenied 
from django.template import RequestContext
from django.contrib.auth.decorators import login_required, permission_required
from django.db.models import Q
from datetime import datetime
from django.template import RequestContext
from django.template.loader import render_to_string
from django.conf import settings
from aplicaciones.solicitudes.models import Credenciales
import logging

logger = logging.getLogger(__name__)

# Create your views here.
def administrarLineaBase(request, id_proyecto, id_fase):
    """ Recibe un request, se obtiene la lista de Lineas Base con las que estan relacionados el proyecto y la fase 
    desplegandola en pantalla, ademas permite realizar busquedas avanzadas sobre
    las fases que puede mostrar.
    
    @type request: django.http.HttpRequest.
    @param request: Contiene informacion sobre la solicitud web actual que llamo a esta vista.
    
    @rtype: django.http.HttpResponse
    @return: lineas_base.html, donde se listan las Lineas Base, ademas de las funcionalidades para cada Linea Base.
    
    @author: Eduardo Gimenez.
    
    """
    proyecto = Proyectos.objects.get(id=id_proyecto)
    fase = Fases.objects.get(id=id_fase)
    if request.user.has_perm('roles.administrar_roles'):
        logger.info('Administracion de Lineas Base de fase % del proyecto %s, hecho por %s' % (fase.nombre, proyecto.nombre, request.user.username))
        lineasbase = LineaBase.objects.filter(is_active=True, proyecto=id_proyecto, fase=id_fase)
        template_name='./lineaBase/lineas_base.html'
        return render(request, template_name, {'lista_lineas_base': lineasbase, 'proyecto': proyecto, 'fase': fase})
    else:
        raise PermissionDenied()
        
@login_required(login_url='/login/')
#@permission_required('lineabase.generar_linea_base',raise_exception=True)
def generarLineaBase(request, id_proyecto, id_fase):
    """ Recibe un request, se verifica cual es el usuario registrado, el proyecto del cual se solicita,
    la fase en la que se esta trabajando, de acuerdo a si el rol del usuario esta o no relacionado con el proyecto
    y la fase actual, se despliega un formulario para Generar la Linea base, en donde se puede agregar una 
    descripcion de la Linea Base y tambien los items que se pueden incluir en la Linea Base. Una vez que el usuario
    levanta el formulario hacia el servidor, se realizado los controles y las operaciones para poder generar la linea base
    de manera correcta.
    
    @type request: django.http.HttpRequest.
    @param request: Contiene informacion sobre la solicitud web actual que llamo a esta vista.
    
    @type id_proyecto: Integer
    @param id_proyecto: Es el id del proyecto actual en el que se esta trabajando
    
    @type id_fase: Integer
    @param id_fase: Es el id de la fase actual en el que se esta trabajando
    
    @rtype: django.http.HttpResponse
    @return: alerta_linea_base.html, mensaje de exito
    
    @author: Eduardo Gimenez.
    
    """
    
    proyecto = Proyectos.objects.get(id=id_proyecto)
    fase = Fases.objects.get(id=id_fase)
    #Primero verificamos Si el usuario tiene permisos sobre esta Fase del Proyecto
    tiene_permiso = True
    if tiene_permiso:
        #Recibimos el request y verificamos si es POST para generar la Linea Base y hacer los controles correspondientes al formulario
        lineas_base = LineaBase.objects.filter(proyecto = id_proyecto, fase = id_fase)
        numero = len(lineas_base) + 1
        items = ()
        errors = []
        if request.method == 'POST':
            if not request.POST.getlist('Items'):
                errors.append('Debe escoger por lo menos un item')
            if not errors:
                linea_base = LineaBase(numero = numero, proyecto = Proyectos.objects.get(id=id_proyecto), fase = Fases.objects.get(id=id_fase), descripcion = request.POST.get('Descripcion', ''), fecha_creacion = datetime.now())
                linea_base.save()
                for id_item in request.POST.getlist('Items'):
                    item = Items.objects.get(id=id_item)
                    linea_base.items.add(item)
                    item.estado = 'Bloqueado'
                    item.save()
                linea_base.save()
                logger.info('Generacion de Linea Base %s de la fase % del proyecto %s, hecho por %s' % (linea_base.numero, fase.nombre, proyecto.nombre, request.user.username))
                mensaje="Linea Base creada exitosamente"
                ctx = {'mensaje':mensaje, 'proyecto':proyecto, 'fase':fase}
                return render_to_response('lineaBase/linea_base_alerta.html',ctx, context_instance=RequestContext(request))
        else:
            items = Items.objects.filter(Q(proyecto = id_proyecto), Q(is_active = True), Q(fase = id_fase), Q(estado = 'Validado') )
            items = [(item.id, item.nombre) for item in items]  
            itemshabilitados = Items.objects.filter(proyecto_id=id_proyecto, fase_id=id_fase, is_active=True, estado='Habilitado')
            lsb = []
            if itemshabilitados:
                todaslaslineasbase = LineaBase.objects.filter(fase_id=id_fase, is_active=False)
                for lineab in todaslaslineasbase:
                    itemslb = lineab.items.all()
                    for itemh in itemshabilitados:
                        if itemh in itemslb:
                            lsb.append(lineab)
            
            if (not items) and (not lsb):
                 mensaje="Imposible generar Linea Base: No hay items en estado Validado!"
                 ctx = {'mensaje':mensaje, 'proyecto':proyecto, 'fase':fase}
                 return render_to_response('lineaBase/linea_base_alerta.html',ctx, context_instance=RequestContext(request))

            template_name='./lineaBase/generar_linea_base.html'
            return render(request, template_name, {'lineasbase': lsb, 'numero': numero, 'items': items, 'errors': errors, 'proyecto':proyecto, 'fase':fase, 'id_fase': id_fase, 'id_proyecto': id_proyecto})
    else:
        raise PermissionDenied()

@login_required(login_url='/login/')
@permission_required('lineabase.consultar_linea_base',raise_exception=True)     
def consultar_lineabase (request, id_proyecto, id_fase, id_lineabase):
    
    """ Recibe un request, el id de proyecto, el id de fase y el id de la linea base a ser consultada, se verifica
    si el usuario tiene permisos para consultar los datos de una linea base y se lo redirige a una pagina que 
    despliega los datos de la linea base solicitada.
    
    @type request: django.http.HttpRequest.
    @param request: Contiene informacion sobre la solicitud web actual que llamo a esta vista consultar_tipoitem.
    
    @type id_proyecto: string.
    @param id_proyecto: Contiene el id del proyecto al cual pertenece el tipo de item a consultar.
    
    @type id_fase: string.
    @param id_fase: Contiene el id de la fase a la cual pertenece la linea base a consultar.
    
    @type id_lineabase: string.
    @param id_lineabase: Contiene el id de la linea base a consultar.
    
    @rtype: django.shortcuts.render_to_response.
    @return: consultarlineabase.html, donde se encuentra la pagina de consulta de linea base.
    
    @author: Marcelo Denis.
    
    """
    
    proyecto = Proyectos.objects.get(id=id_proyecto)
    fase = Fases.objects.get(id=id_fase)
    lineabase = LineaBase.objects.get(id=id_lineabase)
    items = lineabase.items.all()
    logger.info('Consulta de Linea Base % de la fase %s del proyecto %s, hecho por %s' % (lineabase.numero, fase.nombre, proyecto.nombre, request.user.username))
    template_name='lineaBase/consultarlineabase.html'
    ctx = {'lineabase':lineabase, 'items':items, 'proyecto':proyecto, 'fase':fase}
    return render_to_response(template_name, ctx, context_instance=RequestContext(request) )

@login_required(login_url='/login/')
#@permission_required('lineabase.generar_informe_linea_base',raise_exception=True)
def informe_lineabase(request, id_proyecto, id_fase, id_lineabase):
    
    """ Recibe un request, el id de proyecto, el id de fase y el id de la linea base de la cual se generara el
    informe, se verifica si el usuario tiene permisos para empezar el procedimiento de generacion de informe de
    una linea base y se lo redirige a un archivo pdf que contirne los datos de la linea base solicitada.
    
    @type request: django.http.HttpRequest.
    @param request: Contiene informacion sobre la solicitud web actual que llamo a esta vista consultar_tipoitem.
    
    @type id_proyecto: string.
    @param id_proyecto: Contiene el id del proyecto al cual pertenece el tipo de item a consultar.
    
    @type id_fase: string.
    @param id_fase: Contiene el id de la fase a la cual pertenece la linea base a consultar.
    
    @type id_lineabase: string.
    @param id_lineabase: Contiene el id de la linea base a consultar.
    
    @rtype: PDF.
    @return: linea_base_numero.html, donde se encuentra el informe de linea base.
    
    @author: Marcelo Denis.
    
    """
    proyecto = Proyectos.objects.get(id=id_proyecto)
    fase = Fases.objects.get(id=id_fase)
    lineabase=LineaBase.objects.get(id=id_lineabase)
    filename = 'linea_Base_%s.pdf' % lineabase.numero
    ctx ={'pagesize':'A4', 'lineabase':lineabase, 'fecha':datetime.now(), 'items':lineabase.items.all()}
    html = render_to_string('lineaBase/informelineabase.html', ctx, context_instance=RequestContext(request))
    logger.info('Generacion de  informe de linea base %s de la fase %s del proyecto %s, hecho por %s' % (lineabase.numero, fase.nombre, proyecto.nombre, request.user.username))
    return generar_pdf(html, filename)

def generar_pdf(html, filename):
    
    """ Recibe un template html y el nombre del archivo pdf a crear, se resuelve la ruta donde se alojara
    el archivo pdf y se procede a la creacion del mismo a partir del template creado de la funcion llamadora.
    
    @type html: html.
    @param request: Contiene el formato y los datos del informe, el cual, posteriormente se convertira en pdf.
    
    @type filename: string.
    @param filename: Contiene el nombre del archivo pdf a crear.
    
    @rtype: PDF.
    @return: linea_base_numero.html, donde se encuentra el informe de linea base.
    
    @author: Marcelo Denis.
    
    """
    
    STATICFILES_DIRS, = settings.STATICFILES_DIRS
    path = '%s/aplicaciones/informes/%s' % (STATICFILES_DIRS, filename)
    result = open(path, 'wb')
    pdf = pisa.pisaDocument(StringIO.StringIO(html.encode("UTF-8")), result)
    result.close()
   
    if not pdf.err:
        return HttpResponseRedirect('/static/aplicaciones/informes/%s' % filename)
    return HttpResponse('Error al generar el informe PDF: %s' % cgi.escape(html))
    
def reactivarLineaBase(request, id_proyecto, id_fase, id_lineabase):
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
    lb = LineaBase.objects.get(id=id_lineabase)
    proyecto = Proyectos.objects.get(id=id_proyecto)
    fase = Fases.objects.get(id=id_fase)        
    items = lb.items.all()
    for item in items:
        if item.estado=='Habilitado':
            credencial = Credenciales.objects.get(item_id=item.id, estado='Habilitado')
            if request.user.id!=credencial.usuario.user.id:
                mensaje = 'No posee credencial.'
                ctx = {'mensaje':mensaje, 'proyecto':proyecto, 'fase':fase}
                return render_to_response('lineaBase/linea_base_alerta.html',ctx, context_instance=RequestContext(request))
            credencial.estado='Finalizado'
            credencial.save()
    for item in items:
        item.estado = 'Bloqueado'
        item.save()
    lb.is_active=True
    lb.save()
    logger.info('Reactivacion de Linea Base %s de la fase %s del proyecto %s, hecho por %s' % (lb.numero, fase.nombre, proyecto.nombre, request.user.username))
    mensaje="Linea Base creada exitosamente"
    ctx = {'mensaje':mensaje, 'proyecto':proyecto, 'fase':fase}
    return render_to_response('lineaBase/linea_base_alerta.html',ctx, context_instance=RequestContext(request))