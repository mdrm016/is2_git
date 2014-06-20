from django.shortcuts import render_to_response, render, HttpResponseRedirect
from django.template import RequestContext
from aplicaciones.proyectos.models import Proyectos
from datetime import datetime
import ho.pisa as pisa
import cStringIO as StringIO
import cgi
from django.conf import settings
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from aplicaciones.roles.models import Roles
from aplicaciones.fases.models import Fases
from aplicaciones.items.models import Items
from aplicaciones.solicitudes.models import Solicitudes, Votos
from aplicaciones.lineabase.models import LineaBase
from aplicaciones.tipoitem.models import TipoItem

#Funciones
def proyecto_tupla (proyectos_lista):
    lista_P=[]
    for pi in proyectos_lista:
        users = User.objects.all()
        proyecto = Proyectos.objects.get(id=pi.id)
        rolesProyecto = Roles.objects.filter(proyecto=pi.id)
        
        #conseguimos la lista de usuarios que tienen un rol en el proyecto
        lista = []
        roluser=[]
        for user in users:
            if user.is_active:
                rols = user.groups.all()
                for rol in rols:
                    for roluser in rolesProyecto:
                        if rol.name == roluser.name:
                            lista.append(user)
                            
        #eliminamos los usuarios duplicados si existen
        c=0
        listamiembro = []                    
        for lis in lista:
            if lis not in listamiembro:
                listamiembro.append(lis)
                c=c+1
            
        fases=Fases.objects.filter(proyecto=pi.id).count()
        items=Items.objects.filter(proyecto=pi.id).count()
        lineabase=LineaBase.objects.filter(proyecto=pi.id).count()
        tipoitems = TipoItem.objects.filter(id_proyecto=pi.id).count()
        progress=Fases.objects.filter(proyecto=pi.id, estado='FD').count()
        if fases == 0:
            progreso = 0
        else:
            progreso = (progress*100)/fases
        tupla=(pi, c, fases, items, lineabase, tipoitems, progreso)
        lista_P.append(tupla)
    return lista_P
    
def informes (request):
    
    template_name = 'informes/informes.html'
    return render_to_response(template_name, context_instance=RequestContext(request))

def informe_proyecto_pdf(request):
    
    proyectos_inactivos=Proyectos.objects.filter(estado='Inactivo')
    cantidad_pi=Proyectos.objects.filter(estado='Inactivo').count()
    lista_P_I = proyecto_tupla(proyectos_inactivos)
    
    proyectos_en_construccion=Proyectos.objects.filter(estado='En Construccion')
    cantidad_pc=Proyectos.objects.filter(estado='En Construccion').count()
    lista_P_C = proyecto_tupla(proyectos_en_construccion)
    
    proyectos_Finalizados=Proyectos.objects.filter(estado='Finalizado')
    cantidad_pf=Proyectos.objects.filter(estado='Finalizado').count()
    lista_P_F = proyecto_tupla(proyectos_Finalizados)
      
    filename = 'informe_proyecto.pdf'
    ctx ={'pagesize':'A4', 'lista_P_I':lista_P_I, 'cantidad_pi':cantidad_pi, 'lista_P_C':lista_P_C, 'cantidad_pc':cantidad_pc, 'lista_P_F':lista_P_F, 'cantidad_pf':cantidad_pf, 'fecha':datetime.now()}
    html = render_to_string('informes/proyecto_pdf.html', ctx, context_instance=RequestContext(request))
    return generar_pdf(html, filename)

def generar_pdf(html, filename):
    
    STATICFILES_DIRS, = settings.STATICFILES_DIRS
    path = '%s/aplicaciones/informes/%s' % (STATICFILES_DIRS, filename)
    result = open(path, 'wb')
    pdf = pisa.pisaDocument(StringIO.StringIO(html.encode("UTF-8")), result)
    result.close()
   
    if not pdf.err:
        return HttpResponseRedirect('/static/aplicaciones/informes/%s' % filename)
    return HttpResponse('Error al generar el informe PDF: %s' % cgi.escape(html))

def informe_proyecto (request):
    proyectos_inactivos=Proyectos.objects.filter(estado='Inactivo')
    cantidad_pi=Proyectos.objects.filter(estado='Inactivo').count()
    lista_P_I = proyecto_tupla(proyectos_inactivos)
    
    proyectos_en_construccion=Proyectos.objects.filter(estado='En Construccion')
    cantidad_pc=Proyectos.objects.filter(estado='En Construccion').count()
    lista_P_C = proyecto_tupla(proyectos_en_construccion)
    
    proyectos_Finalizados=Proyectos.objects.filter(estado='Finalizado')
    cantidad_pf=Proyectos.objects.filter(estado='Finalizado').count()
    lista_P_F = proyecto_tupla(proyectos_Finalizados)
    
    ctx ={ 'lista_P_I':lista_P_I, 'cantidad_pi':cantidad_pi, 'lista_P_C':lista_P_C, 'cantidad_pc':cantidad_pc, 'lista_P_F':lista_P_F, 'cantidad_pf':cantidad_pf, 'fecha':datetime.now()}
    template_name = 'informes/proyecto_html.html'
    return render_to_response(template_name, ctx, context_instance=RequestContext(request))

def informe_solicitudes(request, id_proyecto):
    proyecto = Proyectos.objects.get(id=id_proyecto)
    solicitudes_pendientes = Solicitudes.objects.filter(estado='Pendiente', proyecto_id=id_proyecto)
    lista_SP = preparar_solicitudes(solicitudes_pendientes)
    total = len(solicitudes_pendientes)
    
    solicitudes_aprobadas = Solicitudes.objects.filter(estado='Aprobada', proyecto_id=id_proyecto)
    lista_SA = preparar_solicitudes(solicitudes_aprobadas)
    total = total + len(solicitudes_aprobadas)
    
    solicitudes_reprobadas = Solicitudes.objects.filter(estado='Reprobada', proyecto_id=id_proyecto)
    lista_SR = preparar_solicitudes(solicitudes_reprobadas)
    total = total + len(solicitudes_reprobadas)
    
    solicitudes_canceladas = Solicitudes.objects.filter(estado='Cancelado', proyecto_id=id_proyecto)
    lista_SC = preparar_solicitudes(solicitudes_canceladas)
    total = total + len(solicitudes_canceladas)

    if solicitudes_pendientes or solicitudes_aprobadas or solicitudes_reprobadas or solicitudes_canceladas:
        existen = True
    else:
        existen = False
    
    ctx ={'lista_SP': lista_SP, 'lista_SA': lista_SA, 'lista_SR': lista_SR, 'lista_SC': lista_SC, 'fecha':datetime.now(), 'existen': existen, 'total': total, 'proyecto': proyecto}
    template_name = 'informes/solicitudes_html.html'
    return render_to_response(template_name, ctx, context_instance=RequestContext(request))

def informe_solicitudes_pdf(request, id_proyecto):
    
    solicitudes_pendientes = Solicitudes.objects.filter(estado='Pendiente', proyecto_id=id_proyecto)
    cantidad_sp = len(solicitudes_pendientes)
    lista_SP = preparar_solicitudes(solicitudes_pendientes)
    
    solicitudes_aprobadas = Solicitudes.objects.filter(estado='Aprobada', proyecto_id=id_proyecto)
    cantidad_sa = len(solicitudes_aprobadas)
    lista_SA = preparar_solicitudes(solicitudes_aprobadas)
    
    solicitudes_reprobadas = Solicitudes.objects.filter(estado='Reprobada', proyecto_id=id_proyecto)
    cantidad_sr = len(solicitudes_reprobadas)
    lista_SR = preparar_solicitudes(solicitudes_reprobadas)
    
    solicitudes_canceladas = Solicitudes.objects.filter(estado='Cancelado', proyecto_id=id_proyecto)
    cantidad_sc = len(solicitudes_canceladas)
    lista_SC = preparar_solicitudes(solicitudes_canceladas)
    
    proyecto = Proyectos.objects.get(id=id_proyecto)
    filename = 'informe_solicitudes_'+proyecto.nombre+'.pdf'
    
    if solicitudes_pendientes or solicitudes_aprobadas or solicitudes_reprobadas or solicitudes_canceladas:
        existen = True
    else:
        existen = False
    
    ctx ={'pagesize':'A4', 'lista_SP':lista_SP, 'cantidad_sp':cantidad_sp, 'lista_SA':lista_SA, 'cantidad_sa':cantidad_sa, 'lista_SR':lista_SR, 'cantidad_sr':cantidad_sr, 'lista_SC':lista_SC, 'cantidad_sc':cantidad_sc, 'existen': existen, 'fecha':datetime.now(), 'proyecto': proyecto}
    html = render_to_string('informes/solicitudes_pdf.html', ctx, context_instance=RequestContext(request))
    return generar_pdf(html, filename)
        
def preparar_solicitudes(solicitudes):
    lista_SP = []
    for solic in solicitudes:
        proyecto = solic.proyecto
        fase = solic.fase
        item = solic.item
        lineabase = LineaBase.objects.get(id=item.lb)
        votos = Votos.objects.filter(solicitud=solic)
        usuario = solic.usuario
        ya_voto = False
        for voto in votos:
            if usuario.user_id==voto.miembro.id:
                ya_voto=True
                usu = voto.miembro
        tupla=(solic, usu, lineabase, ya_voto)
        lista_SP.append(tupla)
        
    return lista_SP

def seleccionar_proyecto(request):
    if request.user.id != 1:
        id_p=[]
        usuario = User.objects.get(id=request.user.id)
        proyectos = Proyectos.objects.filter(lider_id=request.user.id, estado='En Construccion')
    else:
        proyectos = Proyectos.objects.filter(is_active=True)

    ctx = {'proyectos':proyectos}   
    template_name = 'informes/seleccionar_proyecto.html'
    return render_to_response(template_name, ctx, context_instance=RequestContext(request))

def informe_items(request, id_proyecto):
    proyecto = Proyectos.objects.get(id=id_proyecto)
    fases = Fases.objects.filter(proyecto_id=id_proyecto, is_active=True).order_by('orden')
    lista_fases = []
    existen = False
    for fase in fases:
        lista_items = []
        items = Items.objects.filter(fase_id=fase.id, is_active=True)
        for it in items:
            id = it.id
            nombre = it.nombre
            tipoitem = it.tipo_item.nombre
            if it.padre!=0:
                padre = Items.objects.get(id=it.padre)
            else:
                padre = 'No posee'
            version = it.version
            costoM = it.costoMonetario
            costoT = it.costoTemporal
            tupla_item = (id, nombre, tipoitem, padre, version, costoM, costoT)
            lista_items.append(tupla_item)
            existen = True
        tupla_fase = (fase, lista_items)
        lista_fases.append(tupla_fase)
        
    ctx ={'lista_fases': lista_fases, 'fecha':datetime.now(), 'proyecto': proyecto, 'existen': existen}
    template_name = 'informes/items_html.html'
    return render_to_response(template_name, ctx, context_instance=RequestContext(request))

def informe_items_pdf(request, id_proyecto):
        
    proyecto = Proyectos.objects.get(id=id_proyecto)
    fases = Fases.objects.filter(proyecto_id=id_proyecto, is_active=True).order_by('orden')
    lista_fases = []
    for fase in fases:
        lista_items = []
        items = Items.objects.filter(fase_id=fase.id, is_active=True)
        for it in items:
            id = it.id
            nombre = it.nombre
            tipoitem = it.tipo_item.nombre
            if it.padre!=0:
                padre = Items.objects.get(id=it.padre)
            else:
                padre = 'No posee'
            version = it.version
            costoM = it.costoMonetario
            costoT = it.costoTemporal
            tupla_item = (id, nombre, tipoitem, padre, version, costoM, costoT)
            lista_items.append(tupla_item)
        tupla_fase = (fase, lista_items)
        lista_fases.append(tupla_fase)
    
    filename = 'informe_items_'+proyecto.nombre+'.pdf'
    ctx ={'pagesize':'A4', 'fecha':datetime.now(), 'lista_fases': lista_fases, 'proyecto': proyecto}
    html = render_to_string('informes/items_pdf.html', ctx, context_instance=RequestContext(request))
    return generar_pdf(html, filename)

def acercaDe(request):
    ctx = {'para_que_ande': 0}
    return render_to_response('informes/acerca_de.html',ctx, context_instance=RequestContext(request))