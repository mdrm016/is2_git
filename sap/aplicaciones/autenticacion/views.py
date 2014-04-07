from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic import TemplateView
from aplicaciones.autenticacion.forms import LoginForms
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponseRedirect


class Autenticacion(TemplateView):
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            return HttpResponseRedirect('login/')
        else:
            return render_to_response('inicio.html', context_instance=RequestContext(request))

    
def login_view(request):
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
                    mensaje = 'Disculpa, el nombre de Usuario o la Clave no coinciden.'
        form = LoginForms()
        ctx = {'form':form, 'mensaje':mensaje}
        return render_to_response ('autenticacion/autenticacion.html', ctx, context_instance=RequestContext(request))      
        
def logout_view (request):  
    logout(request)
    return HttpResponseRedirect('/')
              