from django.shortcuts import render
from .models import Usuarios

# Create your views here.
def Administrar_usuarios(request):
	#recibir la solicitud y listar los usuarios
	cusuarios = Usuarios.objects.all()
	return render(request, 'usuarios.html', {'lista_usuarios': usuarios})
