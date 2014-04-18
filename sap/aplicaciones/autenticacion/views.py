from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic import TemplateView
from aplicaciones.autenticacion.forms import LoginForms
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponseRedirect
from aplicaciones.proyectos.models import Proyectos
from django.contrib.auth.models import User

class Autenticacion(TemplateView):
    """"Verificacion de autenticacion de usuario
        si el usuario esta registrado pasa a la pagina de adminitracion de proyectos
        de lo contrario pasa a la pagina de autenticacion.
        
        @type TemplateView: django.views.generic.TemplateView
        @param TemplateView: Heredamos la clase TemplateView para hacer uso de sus funcionalidades en la vista
        @rtype: django.shortcuts.render_to_response 
        @return: inicio.html, plantilla reenderizada con el contexto o redireccion al login
        @author: Marcelo Denis
    """
    def get(self, request, *args, **kwargs):
        """ La funcion get, sobreescrita en este caso realiza
            la funcion de comprobacion, ya que sera llamada ca vez que se 
            solicite acceso a la pagina de inicio.
        
        """
        if not request.user.is_authenticated():
            return HttpResponseRedirect('login/')
        else:
            return HttpResponseRedirect('/adm_proyectos/')

    
def login_view(request):
    """ La funcion login view tiene la logica de autenticacion,
        un usuario logueado en el sistema no puede moverse a la pagina 
        del login ni ver el formulario de login, por lo que sera redirigido
        a la pagina de inicio si intentase acceder a la misma.
        
        @type request: django.http.HttpRequest
        @param request: Contiene informacion sobre la solicitud web actual que llamo a esta vista
        @rtype: django.http.HttpResponseRedirect
        @rtype: django.shortcuts.render_to_response
        @return: Se retorna al inicio o se manda a la pagina de login
        @author: Marcelo Denis
        
    """
    mensaje = ""
    if request.user.is_authenticated():
        return HttpResponseRedirect('/')
    else:
        if request.method == "POST":
            form = LoginForms(request.POST)
            if form.is_valid():
                username = form.cleaned_data['Usuario']
                password = form.cleaned_data['Clave']
                usuario = authenticate(username=username, password=password)
                if usuario is not None and usuario.is_active:
                    login(request, usuario)
                    return HttpResponseRedirect('/')
                else:
                    mensaje = 'Disculpa, el Nombre de Usuario o la Clave no coinciden.'
        form = LoginForms()
        ctx = {'form':form, 'mensaje':mensaje}
        return render_to_response ('autenticacion/autenticacion.html', ctx, context_instance=RequestContext(request))      
        
def logout_view (request):
    """ La funcion loguot_view sew encarga de cerrar la sesion actual de un usuario. 
    
    @type request: django.http.HttpRequest
    @param request: Contiene informacion sobre la solicitud web actual que llamo a esta vista
    @rtype: django.http.HttpResponseRedirect
    @return: Se retorna a la pagina de login
    @author: Marcelo Denis
    """  
    logout(request)
    return HttpResponseRedirect('/')
              