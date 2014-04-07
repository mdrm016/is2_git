from django.shortcuts import render
from .models import Usuarios
from django.contrib.auth import create
from django.views.generic import TemplateView

from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http.response import HttpResponseRedirect
from django.shortcuts import render_to_response
#from django.template.context import RequestContext

from forms import UsuarioNuevoForm

# Create your views here.

def Administrar_usuarios(request):
	#recibir la solicitud y listar los usuarios
	usuarios = Usuarios.objects.all()
	template_name='./Usuarios/usuarios.html'
	return render(request, template_name, {'lista_usuarios': usuarios})

def usuario_nuevo(request):
	template_name='./Usuarios/usuarionuevo.html'
	return render(request, template_name)
	
def usuarionuevo(request):
	if request.method == 'POST':
		form = UsuarioNuevoForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			email = form.cleaned_data['email']
			first_name = form.cleaned_data['first_name']
			last_name = form.cleaned_data['last_name']
			
			user = User.objects.create_user(self, username, email, password, *extra_fields)
			user.first_name = first_name
			user.last_name = last_name
			
			user.save()
			
			telefono = form.cleaned_data['telefono']
			direccion = form.cleaned_data['direccion']
			especialidad = form.cleaned.data['especialidad']
			observaciones = form.cleaned_data['observaciones']
			
			usuario = Usuarios.objects.create_user(user, telefono, direccion, especialidad, observaciones)
			
			usuario.save()
			return HttpResponseRedirect('/adm_usuarios/')
		else: 
			mensaje = 'Complete correctamente los campos.'
			form = UsuarioNuevoForm()
	form = UsuarioNuevoForm()
	ctx = {'form':form, 'mensaje':mensaje}
	return render_to_response ('/Usuarios/usuarionuevo.html', ctx, context_instance=RequestContext(request))
