from django.shortcuts import render
from django.views.generic import TemplateView

from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http.response import HttpResponseRedirect
from django.shortcuts import render_to_response
#from django.template.context import RequestContext

from forms import UsuarioNuevoForm

# Create your views here.

def administrarUsuarios(request):
	""" Recibe un request, obtiene la lista de todos los usuarios del sistema y 
	luego retorna el html renderizado con la lista de usuarios 
	@type request: django.http.HttpRequest
	@param request: Contiene informacion sobre la solic. web actual que llamo a esta vista
	
	@rtype: django.http.HttpResponse
	@return: usuarios.html, donde se listan los usuarios, ademas de las funcionalidades para un usuario
	
	@author: eduardo gimenez
	
	"""
	usuarios = User.objects.all()
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
			telefono = form.cleaned_data['telefono']
			direccion = form.cleaned_data['direccion']
			especialidad = form.cleaned_data['especialidad']
			observaciones = form.cleaned_data['observaciones']
			
			if (password != password2):
				template_name='./Usuarios/usuarionuevo.html'
				#mensaje='contrasenhas no coinciden'
				return render(request, template_name, {'form': form})
			
			user = User.objects.create_user(username, password, email)
			user.first_name = first_name
			user.last_name = last_name
			user.telefono = telefono
			user.direccion = direccion
			user.especialidad = especialidad
			user.observaciones = observaciones
			user.save()
			template_name='./Usuarios/usuariocreado.html'
			return render(request, template_name)
	else: 
		form = UsuarioNuevoForm()
	template_name='./Usuarios/usuarionuevo.html'
	return render(request, template_name, {'form': form})

def modificarUsuario(request, id_usuario):
	""" Busca en la base de datos al usuario cuyos datos se quieren modificar.
	Presenta esos datos en un formulario y luego se guardan los cambios realizados """
	#if request.method == 'POST':
		
	template_name='./Usuarios/modificar_usuario.html'
	return render(request, template_name)

def consultarUsuario(request, id_usuario):
	""" Busca en la base de datos al usuario cuyos datos se quieren consultar, 
	los presenta en un html con la disponibilidad de regresar a la pagina anterior """
	
	template_name='./Usuarios/consultar_usuario.html'
	return render(request, template_name)
