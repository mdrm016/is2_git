from django.views.generic import TemplateView
from django.contrib.auth.models import User, Permission
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect, HttpResponse
from django.template.context import RequestContext
from django.contrib.auth.hashers import check_password
from .forms import UsuarioNuevoForm, UsuarioModificadoForm
from .models import Usuarios
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='/login/')
def administrarUsuarios(request):
	""" Recibe un request, obtiene la lista de todos los usuarios del sistema y 
	luego retorna el html renderizado con la lista de usuarios 
	@type request: django.http.HttpRequest
	@param request: Contiene informacion sobre la solic. web actual que llamo a esta vista
	
	@rtype: django.http.HttpResponse
	@return: usuarios.html, donde se listan los usuarios, ademas de las funcionalidades para un usuario
	
	@author: eduardo gimenez
	
	"""
	user = User.objects.all()
	template_name='./Usuarios/usuarios.html'
	return render(request, template_name, {'lista_usuarios': user})

@login_required(login_url='/login/')
def usuarionuevo(request):
	if request.method == 'POST':
		form = UsuarioNuevoForm(request.POST)
		if form.is_valid():
			form.clean()
			username = form.cleaned_data['Nombre_de_Usuario']
			password = form.cleaned_data['Contrasenha']
			password2 = form.cleaned_data['Confirmar_contrasenha']
			email = form.cleaned_data['Email']
			first_name = form.cleaned_data['Nombre']
			last_name = form.cleaned_data['Apellido']
			telefono = form.cleaned_data['Telefono']
			direccion = form.cleaned_data['Direccion']
			especialidad = form.cleaned_data['Especialidad']
			observaciones = form.cleaned_data['Observaciones']
			
			if (password != password2):
				template_name='./Usuarios/usuarionuevo.html'
				#mensaje='contrasenhas no coinciden'
				return render(request, template_name, {'form': form, 'mensaje': 'el password no coincide'})

			useri = User.objects.create_user(username, email, password)
			useri.first_name = first_name
			useri.last_name = last_name
			useri.save()
			
			profile = useri.get_profile()
			profile.telefono=telefono
			profile.direccion=direccion
			profile.especialidad=especialidad
			profile.observaciones=observaciones
			
			profile.save()
					
			template_name='./Usuarios/usuariocreado.html'
			return render(request, template_name)
	else: 
		form = UsuarioNuevoForm()	
	template_name='./Usuarios/usuarionuevo.html'
	if form.is_bound:
		mensaje = 'esta completo'
	else:
		mensaje = 'error en el form'
	return render(request, template_name, {'form': form, 'mensaje': mensaje})

@login_required(login_url='/login/')
def modificarUsuario(request, id_usuario):
	""" Busca en la base de datos al usuario cuyos datos se quieren modificar.
	Presenta esos datos en un formulario y luego se guardan los cambios realizados """
	
	usuario = User.objects.get(id=id_usuario)
	perfil = usuario.get_profile()
	if request.method == 'POST':
		form = UsuarioModificadoForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			nuevo_password= form.cleaned_data['nuevo_password']
			email = form.cleaned_data['email']
			first_name = form.cleaned_data['first_name']
			last_name = form.cleaned_data['last_name']
			telefono = form.cleaned_data['telefono']
			direccion = form.cleaned_data['direccion']
			especialidad = form.cleaned_data['especialidad']
			observaciones = form.cleaned_data['observaciones']
			
			if password is not '':
				if check_password(password, usuario.password):
					template_name='./Usuarios/modificar_usuario.html'
					return render(request, template_name, {'form': form, 'mensajer': 'la contrasenha antigua no coincide'})
			
			usuario.username= username
			usuario.email = email 
			usuario.password = nuevo_password
			usuario.first_name = first_name
			usuario.last_name = last_name
			usuario.save()
			
			profile = usuario.get_profile()
			profile.telefono=telefono
			profile.direccion=direccion
			profile.especialidad=especialidad
			profile.observaciones=observaciones
			
			profile.save()
					
			template_name='./Usuarios/usuario_modificado.html'
			return render(request, template_name)
	else: 
		data = {'username': usuario.username, 'password': '', 'nuevo_password': '', 'email': usuario.email, 'first_name':usuario.first_name,'last_name':usuario.last_name, 'telefono': perfil.telefono, 'direccion':perfil.direccion, 'especialidad':perfil.especialidad , 'observaciones':perfil.observaciones}
		form = UsuarioModificadoForm(data)
	template_name='./Usuarios/modificar_usuario.html'
	return render(request, template_name,{'form':form})

@login_required(login_url='/login/')
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
	perfil = usuario.get_profile()
	template_name='./Usuarios/consultar_usuario.html'
	return render(request, template_name, {'usuario' : usuario, 'perfil':perfil})

#Revisar alternativa A2.2 cuando exista la tabla proyectos.
@login_required(login_url='/login/')
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
		
