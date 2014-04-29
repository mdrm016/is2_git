from django.shortcuts import render_to_response, render, HttpResponseRedirect
from django.template import RequestContext
from .models import TipoItem, ListaAtributo
from .forms import TipoItemNuevoForm, TipoItemModificadoForm
from django.db.models import Q
from aplicaciones.tipoatributo.models import TipoAtributo
from aplicaciones.proyectos.models import Proyectos

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
            tipoitem.id_proyecto=id_proyecto
            tipoitem.is_active='True'
            tipoitem.save()

            mensaje="Tipo Item creado exitosamente"
            ctx = {'mensaje':mensaje, 'id_proyecto':id_proyecto}
            return render_to_response('tipoitem/tipoitemalerta.html',ctx, context_instance=RequestContext(request))
    else:
        form = TipoItemNuevoForm()
        
    ctx ={'form': form, 'id_proyecto':id_proyecto}      
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
    
    elementos_existentes = ordenar_mantener (id_tipoitem)
    for elemento in elementos_existentes:
        elemento.is_active = False
        elemento.orden = 0
        elemento.save()
        
    tipoitem.is_active = False
    tipoitem.save()
    return HttpResponseRedirect('/adm_proyectos/gestionar/%s/adm_tipos_item/' % id_proyecto)

def consultar_tipoitem (request, id_tipoitem, id_proyecto):
    
    tipoitem = TipoItem.objects.get(id=id_tipoitem)
    
    elementos_existentes = ordenar_mantener (id_tipoitem)
    consulta = []
    for elemento in elementos_existentes:
        tupla = (elemento.nombre, TipoAtributo.objects.get(id=elemento.id_atributo).descripcion)
        consulta.append(tupla)
        
    ctx = {'tipoitem':tipoitem, 'atributos':consulta, 'id_proyecto':id_proyecto}
    template_name = 'tipoitem/consultartipoitem.html'
    return render_to_response(template_name, ctx, context_instance=RequestContext(request))

def gestionar_tipoitem (request, id_tipoitem, id_proyecto):
    
    
    tipoitem = TipoItem.objects.get(id=id_tipoitem)
    tablaTipoAtributo = TipoAtributo.objects.filter(is_active=True)
    lista_atributos = tipoitem.listaAtributo.all().filter(is_active=True).order_by('orden')
                
    ctx = {'tipoatributos_dispon':tablaTipoAtributo, 'tipoatributo_selec':lista_atributos, 'id_proyecto':id_proyecto, 'tipoitem':tipoitem}
    template_name = 'tipoitem/gestionartipoitem.html'
    return render_to_response(template_name, ctx, context_instance=RequestContext(request))

def agregar_tipo_atributo (request, id_tipoitem, id_proyecto, id_tipoatributo):
    
    tipoAtributo = TipoAtributo.objects.get(id=id_tipoatributo)
    
    lista_atributo = ListaAtributo()
    lista_atributo.id_atributo = tipoAtributo.id
    lista_atributo.id_tipoitem = id_tipoitem
    lista_atributo.nombre = tipoAtributo.nombre
    lista_atributo.is_active = True
    
    elementos_existentes = ordenar_mantener(id_tipoitem)
    if elementos_existentes:
        lista_atributo.orden = len(elementos_existentes) + 1
    else:
        lista_atributo.orden = 1
    lista_atributo.save()
    
    tipoitem = TipoItem.objects.get(id=id_tipoitem)
    print tipoitem
    tipoitem.listaAtributo.add(lista_atributo)
    
    return HttpResponseRedirect('/adm_proyectos/gestionar/%s/adm_tipos_item/gestionar_tipoitem/%s/' % (id_proyecto, id_tipoitem))

def quitar_tipo_atributo (request, id_tipoitem, id_proyecto, id_tipoatributo):
    
    tipo_atributo = ListaAtributo.objects.get(id=id_tipoatributo)
    tipo_atributo.is_active = False
    tipo_atributo.orden = 0
    tipo_atributo.save()
    elementos_existentes = ordenar_mantener(id_tipoitem)
    return HttpResponseRedirect('/adm_proyectos/gestionar/%s/adm_tipos_item/gestionar_tipoitem/%s/' % (id_proyecto, id_tipoitem))

def ordenar_mantener (id_tipoitem):
    elementos_existentes = ListaAtributo.objects.filter(id_tipoitem=id_tipoitem, is_active=True).exclude(orden='0').order_by('orden')
    control = 1
    for elemento in elementos_existentes:
        if elemento.orden != control:
            elemento.orden = control
            elemento.save()
        control = control + 1
    return elementos_existentes

def subir_tipo_atributo (request, id_tipoitem, id_proyecto, id_tipoatributo):
    atributo_a_subir=ListaAtributo.objects.get(id=id_tipoatributo)
    if atributo_a_subir.orden-1 > 0:
        atributo_a_bajar=ListaAtributo.objects.get(orden=(atributo_a_subir.orden-1))
        orden = atributo_a_bajar.orden
        atributo_a_bajar.orden = atributo_a_subir.orden
        atributo_a_subir.orden = orden
        atributo_a_bajar.save()
        atributo_a_subir.save()
        
    return HttpResponseRedirect('/adm_proyectos/gestionar/%s/adm_tipos_item/gestionar_tipoitem/%s/' % (id_proyecto, id_tipoitem))
    
def bajar_tipo_atributo (request, id_tipoitem, id_proyecto, id_tipoatributo):
    
    atributo_a_bajar=ListaAtributo.objects.get(id=id_tipoatributo)
    cantidad = len(ordenar_mantener (id_tipoitem))
    if atributo_a_bajar.orden+1 <= cantidad:
        atributo_a_subir=ListaAtributo.objects.get(orden=(atributo_a_bajar.orden+1))
        orden = atributo_a_subir.orden
        atributo_a_subir.orden = atributo_a_bajar.orden
        atributo_a_bajar.orden = orden
        atributo_a_subir.save()
        atributo_a_bajar.save()
        
    return HttpResponseRedirect('/adm_proyectos/gestionar/%s/adm_tipos_item/gestionar_tipoitem/%s/' % (id_proyecto, id_tipoitem))

def listar_proyectos (request, id_proyecto):
    
    proyectos = Proyectos.objects.filter(is_active=True)
    ctx = {'id_proyecto':id_proyecto, 'lista_proyectos':proyectos}
    template_name = 'tipoitem/listarproyectos.html'
    return render_to_response(template_name, ctx, context_instance=RequestContext(request))
    
def listar_tipoitem(request, id_proyecto, proyecto_select):
    
    tipoitem = TipoItem.objects.filter(id_proyecto=proyecto_select, is_active=True)
    proyecto = Proyectos.objects.get(id=id_proyecto)
    ctx = {'proyecto':proyecto, 'lista_tipoitem':tipoitem}
    template_name = 'tipoitem/listartipoitem.html'
    return render_to_response(template_name, ctx, context_instance=RequestContext(request))

def importar_tipoitem(request, id_proyecto, proyecto_select, id_tipoitem):
    
    tipoI = TipoItem.objects.get(id=id_tipoitem)
    if request.method == 'POST':
        form = TipoItemNuevoForm(request.POST)
        if form.is_valid():
            form.clean()
            nombre = form.cleaned_data['Nombre_Tipo_de_Item'] 
            descripcion =  form.cleaned_data['Descripcion']
            
            tipoitem = TipoItem()
            tipoitem.nombre=nombre
            tipoitem.descripcion=descripcion
            tipoitem.id_proyecto=id_proyecto
            tipoitem.is_active='True'
            tipoitem.save()
            
            elementos_existentes = ordenar_mantener(id_tipoitem)
            for elemento in elementos_existentes:
                lista_atributo = ListaAtributo()
                lista_atributo.id_atributo = elemento.id
                lista_atributo.id_tipoitem = tipoitem.id
                lista_atributo.nombre = elemento.nombre
                lista_atributo.is_active = True
                
                elementos = ordenar_mantener(tipoitem.id)
                if elementos:
                    lista_atributo.orden = len(elementos_existentes) + 1
                else:
                    lista_atributo.orden = 1
                lista_atributo.save()
                
                tipoitem.listaAtributo.add(lista_atributo)
            
            
            mensaje="Tipo Item Importado exitosamente"
            ctx = {'mensaje':mensaje, 'id_proyecto':id_proyecto}
            return render_to_response('tipoitem/tipoitemalerta.html',ctx, context_instance=RequestContext(request))
    else:
        form = TipoItemNuevoForm()
        
    ctx ={'form': form, 'tipoitem':tipoI}      
    template_name='tipoitem/creartipoitemimportado.html'
    return render_to_response(template_name, ctx, context_instance=RequestContext(request))
