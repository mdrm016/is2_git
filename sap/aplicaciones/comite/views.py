from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect, HttpResponse
from django.template.context import RequestContext
from aplicaciones.proyectos.models import Proyectos
from aplicaciones.fases.models import Fases
from aplicaciones.usuarios.models import Usuarios
from aplicaciones.items.models import Items
from .models import Comite
from django.contrib.auth.decorators import login_required, permission_required
from django.db.models import Q
from django.contrib.auth.models import User
from aplicaciones.roles.models import Roles
from aplicaciones.solicitudes.models import Solicitudes
import logging

# Create your views here.

logger = logging.getLogger(__name__)

def consultar_comite(request, id_proyecto):
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
    if request.user.id==proyecto.lider_id:
        template_name = './comite/usuariosparacomite.html'
        ctx = agregar_miembro(request, id_proyecto) 
        return render_to_response(template_name, ctx, context_instance=RequestContext(request))
    comite = Comite.objects.get(proyecto_id=id_proyecto)
    miembros = comite.miembros.all()
    logger.info('Consulta de Comite %s, hecho por %s' % (comite.nombre, request.user.username))
    template_name='./comite/miembroscomite.html'
    ctx = {'id_proyecto':id_proyecto, 'proyecto': proyecto, 'miembros': miembros}
    return render_to_response(template_name, ctx, context_instance=RequestContext(request))

def agregar_miembro(request, id_proyecto):
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
    
    solicitudes = Solicitudes.objects.filter(proyecto_id=id_proyecto, estado='Pendiente')
    if solicitudes:
        mensaje = 'Existen solicitudes pendientes. No se puede modificar el comite.'
        template_name = './comite/comitealerta.html'
        proyecto = Proyectos.objects.get(id=id_proyecto)
        ctx = {'id_proyecto':id_proyecto, 'proyecto': proyecto, 'mensaje': mensaje}
        return render_to_response(template_name, ctx, context_instance=RequestContext(request))
    
    comite = Comite.objects.get(proyecto_id=id_proyecto)
    miembros = comite.miembros.all()
    template_name = './comite/usuariosparacomite.html'
    users = User.objects.filter(is_active=True)
    rolesProyecto = Roles.objects.filter(proyecto=id_proyecto)   
    lista = []
    roluser=[]
    for user in users:
        rols = user.groups.all()
        for rol in rols:
            for roluser in rolesProyecto:
                if rol.name == roluser.name:
                    lista.append(user)  
    listamiembros = []                    
    for lis in lista:
        if lis not in listamiembros:
            listamiembros.append(lis)

    if request.method == 'POST':
         miembrosid = request.POST.getlist('Miembro', '')
         cantidad = len(miembrosid)
         imparnum = len(miembrosid)%2
         if len(miembrosid)<3 and len(listamiembros)>2:
            mensaje = 'El comite debe estar conformado por al menos 3 miembros'
         elif (len(listamiembros)>2 and (len(miembrosid)%2)==0):
             mensaje = 'La cantidad de miembros debe ser impar'
         else: 
             for miem in miembros:
                 comite.miembros.remove(miem)
             for idmiembro in miembrosid:
                 user = User.objects.get(id=idmiembro)
                 usuario = Usuarios.objects.get(user_id=user.id)
                 comite.miembros.add(usuario)
                 comite.save()
             miembros = comite.miembros.all()
             logger.info('Agregacion de miembros de comite %s, hecho por %s ' % (comite.nombre, request.user.username))
             mensaje = 'Cambios guardados.'
    else:
        mensaje = ''
        
    miembros_id = []
    for miembro in miembros:
        miembros_id.append(miembro.user.id)
    id_listamiembros = []
    for listamiem in listamiembros:
        id_listamiembros.append(listamiem.id)
    
    proyecto = Proyectos.objects.get(id=id_proyecto)
    ctx = {'id_proyecto':id_proyecto, 'proyecto': proyecto, 'miembros': miembros, 'listamiembros': listamiembros, 'mensaje': mensaje}
    return ctx;
