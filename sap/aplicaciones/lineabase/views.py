from django.shortcuts import render, render_to_response
from aplicaciones.proyectos.models import Proyectos
from aplicaciones.fases.models import Fases
from aplicaciones.items.models import Items
from aplicaciones.roles.models import Roles
from models import LineaBase
from django.core.exceptions import PermissionDenied 
from django.template import RequestContext
from django.contrib.auth.decorators import login_required, permission_required
from django.db.models import Q

# Create your views here.
def administrarLineaBase(request, id_proyecto, id_fase):
    lineasbase = LineaBase.objects.filter(is_active=True)
    template_name='./lineaBase/lineas_base.html'
    return render(request, template_name, {'lista_lineas_base': lineasbase, 'id_proyecto': id_proyecto, 'id_fase': id_fase})

@login_required(login_url='/login/')
@permission_required('lineabase.generar_linea_base',raise_exception=True)
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
    #Primero verificamos Si el usuario tiene permisos sobre esta Fase del Proyecto
    tiene_permiso = True
    #roles = request.user.groups.all()
    #for rol in roles:
    #    rol_usuario = Roles.objects.get(id=rol.id)
    #    if rol_usuario.proyecto == id_proyecto:
    #        for fase in rol_usuario.fases.all():
    #            if fase.id == id_fase:
    #                tiene_permiso = True
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
                linea_base = LineaBase(numero = numero, proyecto = Proyectos.objects.get(id=id_proyecto), fase = Fases.objects.get(id=id_fase), descripcion = request.POST.get('Descripcion', ''))
                linea_base.save()
                for id_item in request.POST.getlist('Items'):
                    linea_base.items.add(Items.objects.get(id=id_item))
                linea_base.save()
                mensaje="Linea Base creada exitosamente"
                ctx = {'mensaje':mensaje, 'id_proyecto':id_proyecto, 'id_fase':id_fase}
                return render_to_response('lineaBase/linea_base_alerta.html',ctx, context_instance=RequestContext(request))
        else:
            items = Items.objects.filter(Q(proyecto = id_proyecto), Q(is_active = True), Q(fase = id_fase), Q(estado = 'Validado') )  
            items = [(item.id, item.nombre) for item in items]
            if not items:
                 mensaje="Imposible generar Linea Base: No hay items en estado Validado!"
                 ctx = {'mensaje':mensaje, 'id_proyecto':id_proyecto, 'id_fase':id_fase}
                 return render_to_response('lineaBase/linea_base_alerta.html',ctx, context_instance=RequestContext(request))
        
        template_name='./lineaBase/generar_linea_base.html'
        return render(request, template_name, {'numero': numero, 'items': items, 'errors': errors})
    else:
        raise PermissionDenied()
        
    