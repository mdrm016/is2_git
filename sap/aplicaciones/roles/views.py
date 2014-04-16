from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required
from models import Roles
# Create your views here.

@login_required(login_url='/login/')
def administrarRoles(request):
    """ Recibe un request, obtiene la lista de todos los Roles del sistema y 
    luego retorna el html renderizado con la lista de usuarios 
    @type request: django.http.HttpRequest
    @param request: Contiene informacion sobre la solic. web actual que llamo a esta vista
    
    @rtype: django.http.HttpResponse
    @return: usuarios.html, donde se listan los Roles, ademas de las funcionalidades para un Rol
    
    @author: eduardo gimenez
    
    """
    roles = 0
    mis_roles = request.user.groups
    if request.user.has_perm('usuarios.administrar_roles'):
        roles = Roles.objects.all()
    
    template_name='./Roles/roles.html'
    return render(request, template_name, {'lista_roles': roles, 'mis_roles': mis_roles})
    
