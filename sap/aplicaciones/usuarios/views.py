from django.shortcuts import render
from django.views.generic import TemplateView

from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http.response import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.template.context import RequestContext

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
	los presenta en un html con la disponibilidad de regresar a la pagina anterior 
	@type request: django.http.HttpRequest
	@param request: Contiene informacion sobre la solic. web actual que llamo a esta vista
	
	@type id_usuario: integer
	@param id_usuario: es el id del usuario cuyos datos se quieren consultar
	
	@rtype: 
	@return: """
	usuario = User.objects.get(id = id_usuario)
	template_name='./Usuarios/consultar_usuario.html'
	return render(request, template_name, {'usuario' : usuario})

#Revisar alternativa A2.2 cuando exista la tabla proyectos.
def usuario_eliminar (request, id_usuario):
	""" La funcion usuario_eliminar comprueba que el id del usuario a ser eliminado
		no sea del administrador, osea id_usuario == 1. Caso contrario procede a eliminar
		de la base de datos los registros del usuario cuyo id corresponda.
        
        @type request: django.http.HttpRequest
        @type id_usuario : string
        @param request: Contiene informacion sobre la solicitud web actual que llamo a esta vista
        @param id_usuario : Contiene el id del usuario a ser eliminado.
        @rtype: django.http.HttpResponseRedirect
        @rtype: django.shortcuts.render_to_response
        @return: Se retorna al la administracion de usuarios o se manda a la pagina de notificacion
        @author: Marcelo Denis
	"""
	if id_usuario != '1':
		userDelOfTable = User.objects.get(pk=id_usuario)
		userDelOfTable.delete()
		return HttpResponseRedirect('/adm_usuarios/')
	
	elif id_usuario == '1':
		mensaje="Imposible eliminar usuario, el usuario es el Administrador"
		ctx = {'mensaje':mensaje}
		return render_to_response('Usuarios/usuarioalerta.html',ctx, context_instance=RequestContext(request))
		
