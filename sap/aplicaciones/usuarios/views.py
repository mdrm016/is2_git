from django.shortcuts import render
from .models import Usuarios
from django.views.generic import TemplateView

from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http.response import HttpResponseRedirect
from django.shortcuts import render_to_response
#from django.template.context import RequestContext

from forms import UsuarioNuevoForm

# Create your views here.

def Administrar_usuarios(request):
	""" Recibe un request, obtiene la lista de todos los usuarios del sistema y 
	luego retorna el html renderizado con la lista de usuarios 
	@type request: django.http.HttpRequest
	@param request: Contiene informacion sobre la solic. web actual que llamo a esta vista
	
	@rtype: django.http.HttpResponse
	@return: usuarios.html, donde se listan los usuarios, ademas de las funcionalidades para un usuario
	
	@author: eduardo gimenez
	
	"""
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
			password2 = form.cleaned_data['password2']
			email = form.cleaned_data['email']
			first_name = form.cleaned_data['first_name']
			last_name = form.cleaned_data['last_name']
			
		#	if (password != password2):
		#		template_name='./Usuarios/usuarionuevo.html'
		#		mensaje='contrasenhas no coinciden'
		#		return render(request, template_name)
			
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
			template_name='./Usuarios/usuariocreado.html'
			return render(request, template_name)
		else: 
			form = UsuarioNuevoForm()
			template_name='./Usuarios/usuariocreado.html'
			return render(request, template_name)
			
	template_name='./Usuarios/usuariocreado.html'
	return render(request, template_name)