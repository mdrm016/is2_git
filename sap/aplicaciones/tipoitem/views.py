from django.shortcuts import render_to_response, render, HttpResponseRedirect
from django.template import RequestContext
from .models import TipoItem, ListaAtributo
from .forms import TipoItemNuevoForm, TipoItemModificadoForm
from django.db.models import Q
from aplicaciones.tipoatributo.models import TipoAtributo

def adm_tipoitem (request, id_proyecto):
    
    tipoitem = TipoItem.objects.filter(is_active=True)
    
    busqueda = ''
    error=False
    if 'busqueda' in request.GET:
        busqueda = request.GET.get('busqueda', '')
        if busqueda:
            qset = (
                Q(nombre__icontains=busqueda) |
                Q(descripcion__icontains=busqueda) 
            )
            tipoitem = tipoitem.filter(qset).distinct()
            if not tipoitem:
                error = True
                
    ctx = {'lista_tipoitem':tipoitem, 'query':busqueda, 'error':error, 'id_proyecto':id_proyecto}   
    template_name = 'tipoitem/tipoitem.html'
    return render_to_response(template_name, ctx, context_instance=RequestContext(request))

def crear_tipoitem (request, id_proyecto):
    if request.method == 'POST':
        form = TipoItemNuevoForm(request.POST)
        if form.is_valid():
            form.clean()
            nombre = form.cleaned_data['Nombre_Tipo_de_Item'] 
            descripcion =  form.cleaned_data['Descripcion']
            #tipoatributos= form.cleaned_data['Tipo_Atributo']
            
            tipoitem = TipoItem()
            tipoitem.nombre=nombre
            tipoitem.descripcion=descripcion
            tipoitem.is_active='True'
            tipoitem.save()
            
            tablaTipoAtributo = TipoAtributo.objects.filter(is_active=True)
            
            for tipoatributo in tablaTipoAtributo:
                tipoitem.tipoAtributo.add(tipoatributo)
                
            print tipoitem.tipoAtributo.all()
            
            """for tipoatributo_id in tipoatributos:
                tipoatributo = TipoAtributo.objects.get(id=tipoatributo_id)
                tipoitem.tipoAtributo.add(tipoatributo)"""

            mensaje="Tipo Item creado exitosamente"
            ctx = {'mensaje':mensaje, 'id_proyecto':id_proyecto}
            return render_to_response('tipoitem/tipoitemalerta.html',ctx, context_instance=RequestContext(request))
    else:
        form = TipoItemNuevoForm()
        
    ctx ={'form': form}      
    template_name='tipoitem/creartipoitem.html'
    return render_to_response(template_name, ctx, context_instance=RequestContext(request))

def modificar_tipoitem (request, id_tipoitem, id_proyecto):
    
    
    tipoitem = TipoItem.objects.get(id=id_tipoitem)
    mensaje=''
    if request.method == 'POST':
        form = TipoItemModificadoForm(request.POST)
        if form.is_valid():
            form.clean()
            nombre = form.cleaned_data['Nombre_Tipo_de_Item'] 
            descripcion =  form.cleaned_data['Descripcion']
            #tipoatributos= form.cleaned_data['Tipo_Atributo']
            
            
            # Comprobar cantidad miembros de comite para pasar a un estado en construccion con un elif
            #si exite ya un proyecto con el nombre suministrado y el nombre suminitrado es distinto al del proyecto que esta siendo modificado
            if TipoItem.objects.filter(nombre=nombre, is_active=True) and nombre != tipoitem.nombre:
                data ={'Nombre_Tipo_de_Item':tipoitem.nombre, 'Descripcion':tipoitem.descripcion}  
                form = TipoItemModificadoForm(data)
                mensaje = 'El nombre del Tipo de Item ya existe y no puede haber duplicados'
            
            else:
                if nombre == tipoitem.nombre and  descripcion == tipoitem.descripcion:
                      mensaje="Tipo de Item guardado sin modificaciones"
                      
                else:
                    tipoitem.nombre=nombre
                    tipoitem.descripcion=descripcion
                    tipoitem.save()
                        
                    mensaje="Tipo de Item modificado exitosamente"
                    
                ctx = {'mensaje':mensaje, 'id_proyecto':id_proyecto}
                template_name='tipoitem/tipoitemalerta.html'
                return render_to_response(template_name, ctx, context_instance=RequestContext(request))
    else:
        data ={'Nombre_Tipo_de_Item':tipoitem.nombre, 'Descripcion':tipoitem.descripcion}
        form = TipoItemModificadoForm(data)
        
    ctx ={'form': form, 'mensaje':mensaje, 'tipoitem':tipoitem}      
    template_name='tipoitem/modificartipoitem.html'
    return render_to_response(template_name, ctx, context_instance=RequestContext(request))


def eliminar_tipoitem (request, id_tipoitem, id_proyecto):
    
    tipoitem = TipoItem.objects.get(id=id_tipoitem)
    #si algun item usa este tipo de item, ya no se podra borrar
    tipoitem.is_active = False
    tipoitem.save()
    return HttpResponseRedirect('/adm_proyectos/gestionar/%s/adm_tipos_item/' % id_proyecto)

def consultar_tipoitem (request, id_tipoitem, id_proyecto):
    
    tipoitem = TipoItem.objects.get(id=id_tipoitem)
    #consegir los tipos de atributos
    ctx = {'tipoitem':tipoitem}
    template_name = 'tipoitem/consultartipoitem.html'
    return render_to_response(template_name, ctx, context_instance=RequestContext(request))

def gestionar_tipoitem (request, id_tipoitem, id_proyecto):
    
    tipoitem = TipoItem.objects.get(id=id_tipoitem)
    tablaTipoAtributo = TipoAtributo.objects.filter(is_active=True)
    tablaListaAtributo = ListaAtributo.objects.filter(id_tipoitem=id_tipoitem, is_active=True)
                
    ctx = {'tipoatributos_dispon':tablaTipoAtributo, 'tipoatributo_selec':tablaListaAtributo, 'tipoitem':tipoitem}
    template_name = 'tipoitem/gestionartipoitem.html'
    return render_to_response(template_name, ctx, context_instance=RequestContext(request))

def agregar_tipo_atributo (request, id_tipoitem, id_proyecto, id_tipoatributo):
    
    tipoAtributo = TipoAtributo.objects.get(id=id_tipoatributo)
    
    lista_atributo = ListaAtributo()
    lista_atributo.id_atributo = tipoAtributo.id
    lista_atributo.id_tipoitem = id_tipoitem
    lista_atributo.nombre = tipoAtributo.nombre
    lista_atributo.is_active = True
    
    elementos_existentes = ListaAtributo.objects.filter(id_tipoitem=id_tipoitem, is_active=True)
    if elementos_existentes:
        lista_atributo.orden = len(elementos_existentes) + 1
    else:
        lista_atributo.orden = 1
    lista_atributo.save()
    return HttpResponseRedirect('/adm_proyectos/gestionar/%s/adm_tipos_item/gestionar_tipoitem/%s/' % (id_proyecto, id_tipoitem))
    