from django.shortcuts import render
from .models import Usuarios

from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http.response import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template.context import RequestContext

from forms import UsuarioNuevoForm


# Create your views here.

def Administrar_usuarios(request):
	#recibir la solicitud y listar los usuarios
	cusuarios = Usuarios.objects.all()
	return render(request, 'usuarios.html', {'lista_usuarios': usuarios})

def UsuarioNuevo(request):
    if request.method == 'POST':
        form = UsuarioNuevoForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            email = form.cleaned_data["email"]
            telefono = form.cleaned_data["telefono"] 
            direccion = form.cleaned_data["direccion"]
            especialidad = form.cleaned_data["especialidad"]
            observaciones = form.cleaned_data["observaciones"]
            
            user = User.objects.create_user(username, email, password, telefono, direccion, especialidad, observaciones)
            user.save()
            
            return HttpResponseRedirect(reverse('inicio'))
        else:
            form = UsuarioNuevoForm()
            
        data = {
                'form': form,
                }
        return render_to_response('usuarionuevo.html', data, context_instance=ResquestContext(request))

