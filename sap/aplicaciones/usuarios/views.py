from django.views.generic import TemplateView
from django.contrib.auth.models import User, Permission
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect, HttpResponse
from django.template.context import RequestContext
from django.contrib.auth.hashers import check_password, make_password
from forms import UsuarioNuevoForm, UsuarioModificadoForm
from .models import Usuarios
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from collections import OrderedDict

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
	error = False
	if 'busqueda' in request.GET:
		busqueda = request.GET['busqueda']
		if not busqueda:
			error = True
			template_name= './Usuarios/usuarios.html'
			return render(request, template_name, {'error': error})
		else:
			usuarioname = User.objects.filter(username=busqueda)
			usuarionombre = User.objects.filter(first_name=busqueda)
			usuarioapellido = User.objects.filter(last_name=busqueda)
			usuarioemail = User.objects.filter(email=busqueda)
			usuariotelefono = Usuarios.objects.filter(telefono=busqueda)
			usuariodireccion = Usuarios.objects.filter(direccion=busqueda)
			usuarioespecialidad = Usuarios.objects.filter(especialidad=busqueda)
			usuarioobservaciones = Usuarios.objects.filter(observaciones=busqueda)
			if (not usuarioname) & (not usuarionombre) & (not usuarioemail) & (not usuariotelefono) & (not usuariodireccion) & (not usuarioespecialidad) & (not usuarioobservaciones):
				error = True
				template_name= './Usuarios/usuarios.html'
				return render(request, template_name, {'error': error})
			else:
				user=[]
				if (usuarioname):
					user.extend(usuarioname)
				if (usuarioname):
					user.extend(usuarioname)
				if (usuarionombre):
					user.extend(usuarionombre)
				if (usuarioapellido):
					user.extend(usuarioapellido)
				if (usuarioemail):
					user.extend(usuarioemail)
				if (usuariotelefono):
					user.extend(usuariotelefono)
				if (usuariodireccion):
					user.extend(usuariodireccion)
				if (usuarioespecialidad):
					user.extend(usuarioespecialidad)
				if (usuarioobservaciones):
					user.extend(usuarioobservaciones)
				useri = set(user)
				template_name='./Usuarios/usuarios.html'
				return render(request, template_name, {'lista_usuarios': useri, 'error': error})

	user = User.objects.all()
	template_name='./Usuarios/usuarios.html'
	return render(request, template_name, {'lista_usuarios': user})
	

@login_required(login_url='/login/')
def usuarionuevo(request):
	""" Recibe un request, obtiene el formulario con los datos del usuario a crear
	o la solicitud de envio de dicho formulario. Luego verifica los datos recibidos
	y registra al nuevo usuario.  
	
	@type request: django.http.HttpRequest
	@param request: Contiene informacion sobre la solic. web actual que llamo a esta vista
	
	@rtype: django.http.HttpResponse
	@return: usuariocreado.html, mensaje de exito
	
	@author: Ysapy Ortiz
	
	"""
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
	return render(request, template_name, {'form': form})

@login_required(login_url='/login/')
def modificarUsuario(request, id_usuario):
	""" Busca en la base de datos al usuario cuyos datos se quieren modificar.
	Presenta esos datos en un formulario y luego se guardan los cambios realizados.
	Con la posibilidad de que el usuario cancele la operacion
	 
	@type request: django.http.HttpRequest
	@param request: Contiene informacion sobre la solic. web actual que llamo a esta vista
	
	@type id_usuario: integer
	@param id_usuario: es el id del usuario cuyos datos se quieren modificar
	
	@rtype: django.HttpResponse
	@return: modificar_usuario.html,un formulario donde se despliegan los datos que el usuario puede modificar ,usuario_modificado.html, donde se notifica al usuario el exito de la operacion 
	
	@author: eduardo gimenez"""
	
	usuario = User.objects.get(id=id_usuario)
	perfil = usuario.get_profile()
	if request.method == 'POST':
		form = UsuarioModificadoForm(request.POST)
		if form.is_valid():
			form.clean()
			username = form.cleaned_data['Nombre_de_Usuario']
			password = form.cleaned_data['Contrasenha']
			nuevo_password= form.cleaned_data['Nueva_contrasenha']
			email = form.cleaned_data['Email']
			first_name = form.cleaned_data['Nombre']
			last_name = form.cleaned_data['Apellido']
			telefono = form.cleaned_data['Telefono']
			direccion = form.cleaned_data['Direccion']
			especialidad = form.cleaned_data['Especialidad']
			observaciones = form.cleaned_data['Observaciones']
			
			if password:
				if check_password(password, usuario.password):
					password = make_password(nuevo_password)
				else:
					template_name='./Usuarios/modificar_usuario.html'
					return render(request, template_name, {'form': form})
			else: 
				password = usuario.password
				
			usuario.username= username
			usuario.password = password
			usuario.email = email 
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
		data = {'Nombre_de_Usuario': usuario.username, 'Contrasenha': '', 'Nueva_contrasenha': '', 'Email': usuario.email, 'Nombre':usuario.first_name,'Apellido':usuario.last_name, 'Telefono': perfil.telefono, 'Direccion':perfil.direccion, 'Especialidad':perfil.especialidad , 'Observaciones':perfil.observaciones}
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
	
	@rtype: django.HttpResponse
	@return: consultar_usuario.html, donde se le despliega al usuario los datos
	
	@author: eduardo gimenez"""
	usuario = User.objects.get(id = id_usuario)
	perfil = usuario.get_profile()
	template_name='./Usuarios/consultar_usuario.html'
	return render(request, template_name, {'usuario' : usuario, 'perfil':perfil})
	

#Revisar alternativa A2.2 cuando exista la tabla proyectos.
@login_required(login_url='/login/')
def usuario_eliminar (request, id_usuario):
	"""	
		Comprueba que el id del usuario a eliminar no se sea del administrador,
		caso contrario procede a eliminar de la base de datos los registros del usuario.
        
	@type request: django.http.HttpRequest
	@param request: Contiene informacion sobre la solicitud web actual que llamo a esta vista
        
	@type id_usuario : string
 	@param id_usuario : Contiene el id del usuario a ser eliminado.
        
	@rtype: django.shortcuts.render_to_response
	@return: Se retorna al la administracion de usuarios o se manda a la pagina de notificacion
        
	@author: Marcelo Denis"""
	if id_usuario != '1':
		userDelOfTable = User.objects.get(pk=id_usuario)
		userDelOfTable.delete()
		return HttpResponseRedirect('/adm_usuarios/')
	
	elif id_usuario == '1':
		mensaje="Imposible eliminar usuario, el usuario es el Administrador"
		ctx = {'mensaje':mensaje}
		return render_to_response('Usuarios/usuarioalerta.html',ctx, context_instance=RequestContext(request))
		
#def buscar_usuario(request):
	""" Recibe un request, obtiene la lista de todos los usuarios del sistema que tengan
	coincidencias con lo solicitado luego retorna el html renderizado con la lista de
	dichos usuarios 
	@type request: django.http.HttpRequest
	@param request: Contiene informacion sobre la solic. web actual que llamo a esta vista
	
	@rtype: django.http.HttpResponse
	@return: usuarios.html, donde se listan los usuarios, ademas de las funcionalidades para un usuario
	
	@author: ysapy ortiz
	
	
	if request.POST:
		dato=request.POST.get()
		usuario = User.objects.get(username=dato)
		#if (not usuario):
		#	return HttpResponseRedirect('/adm_usuarios/')
		template_name='./Usuarios/buscar_usuario.html'
		return render(request, template_name, {'lista_usuarios': usuario})
	return HttpResponseRedirect('/adm_usuarios/buscar/')"""

def buscar_usuario(request):
	error = False
	if 'busqueda' in request.GET:
		busqueda = request.GET['busqueda']
		if not busqueda:
			error = True
		else:
			user = User.objects.filter(username=busqueda)
			if not user:
				error = True
			else:
				template_name='./Usuarios/buscar_usuario.html'
				return render_to_response(template_name, {'lista_usuarios': user, 'query': busqueda})
	template_name='./Usuarios/buscar_usuario.html'
	return render_to_response(template_name, {'error': error})
