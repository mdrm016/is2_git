from django.test import TestCase
from .models import Usuarios
from django.contrib.auth.models import User
from aplicaciones.usuarios.views import usuario_eliminar, usuarionuevo
from aplicaciones.usuarios.views import modificarUsuario, administrarUsuarios, consultarUsuario
from django.core.urlresolvers import reverse

from django.test.client import RequestFactory
from aplicaciones.usuarios.forms import UsuarioModificadoForm

class TestUsuario(TestCase):
    """ Se realizan todas las pruebas respecto a la aplicacion Usuario """
    fixtures = ['users.json']
    
    def setUp(self):
        
        self.factory = RequestFactory()
    
    def testConsultarUsuario(self):
        
        self.user = User.objects.get(pk=1)
        request = self.factory.get('/adm_usuarios/consultar/1/')
        request.user = self.user
        response = consultarUsuario(request, 1)
        self.assertEqual(response.status_code, 200)
        
    def testAdministrarUsuario(self):
        
        self.user = User.objects.get(pk=1)  
        request = self.factory.get('/adm_usuarios/')
        request.user = self.user
        response = administrarUsuarios(request)                                    #Pasamos a la pagina de administracion de usuarios
        self.assertEqual(response.status_code, 200)           
        
    def testModificarUsuario(self):
        
        self.user = User.objects.get(pk=1)
        print User.objects.all()
        usuario = User.objects.get(username='sap123')
        request = self.factory.post('/adm_usuarios/modificar/1/', {'Nombre_de_Usuario': 'sapMod', 'Contrasenha': '', 'Nueva_contrasenha': '', 'Email': usuario.email, 'Nombre': usuario.first_name,'Apellido': usuario.last_name, 'Telefono': '2333443545', 'Direccion' : 'xxxxxxxxxxx', 'Especialidad' : '' , 'Observaciones' : ''})
        request.user = self.user
        response = modificarUsuario(request, 1)
        self.assertEqual(response.status_code, 200)
        print User.objects.all()
        
    def test_details(self):
        self.user = User.objects.get(pk=1)
        request = self.factory.get('/adm_usuarios/eliminar/6/')
        request.user = self.user
        print User.objects.all()
        response = usuario_eliminar(request, 6)
        print User.objects.all()
            
    if __name__ == '__main__':
        unittest.main()
        
        
    



        

    