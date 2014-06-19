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
    