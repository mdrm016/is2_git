
from django.contrib.auth.models import User 
from django.test import TestCase 
from django.test.client import RequestFactory 
from aplicaciones.usuarios.views import administrarUsuarios, modificarUsuario
from aplicaciones.usuarios.views import usuario_eliminar, usuarionuevo

class test_user(TestCase):
    """    Cargamos los usuarios de prueba en la base de datos    """
    fixtures = ['users.json'] + ['groups.json']
    
    def setUp(self):
        """ Inicializamos la variable factory que posteriormente nos permitira cargar
            un request para utilizarlo en las vista.
        """
        self.factory = RequestFactory()
        

    def test_usuario_eliminar(self):
        """ Cargamos en objeto request con el requerimiento de la url que nos 
            permite eliminar un usuario.
        """
        request = self.factory.get('/adm_usuarios/eliminar/2/')
        
        """ Asignamos a la variable user el usuario Sap, osea el administrador.
        """
        self.user = User.objects.get(pk=1)
        
        """ Logueamos al usuario manualmente en el request 
            ya que esta tecnica no es compatible con el middleware.
            Atributos de sesion y autenticacion deben ser suministrados 
            por la prueba en si, para que funcione correctamente.
        """
        request.user = self.user
        """ Nos aseguramos que el usuario con id existe. """
        id = '4'
        usuarioname = User.objects.filter(pk=id)
        self.assertTrue(usuarioname)
        
        """ Borramos al usuario con id 2 """
        response = usuario_eliminar(request, id)
        
        """ Nos aseguramos que el usuario con id se ha eliminado. """
        usuarioname = User.objects.get(pk=id)
        self.assertFalse(usuarioname.is_active)
        
        """ Ahora nos aseguramos de que el Administrador no puede ser eliminado
            utilizando la tecnica anterior.
        """
        id = '1'
        usuarioname = User.objects.filter(pk=id)
        self.assertTrue(usuarioname)
        response = usuario_eliminar(request, '1')
        
        """ Comprobamos que el administrador no puede ser eliminado.
        """
        usuarioname = User.objects.filter(pk=id)
        self.assertTrue(usuarioname) 
        
    def testUsuarioNuevo(self): # Create an instance of a GET request. 
        self.user = User.objects.get(pk=1) 
        request = self.factory.post('/adm_usuarios/nuevo/', {'Nombre_de_Usuario': 'usuario2', 'Contrasenha': 'ysapy', 'Confirmar_contrasenha': 'ysapy', 'Email': 'ysapy', 'Nombre': 'ysa', 'Apellido':'ortiz', 'Telefono': '021', 'Direccion': 'lambare'})
        request.user = self.user 
        response = usuarionuevo(request) 
        self.assertEqual(response.status_code, 200)
        busco = User.objects.get(username='usuario2')
        perfil = busco.get_profile()
        print perfil.telefono 
        
    def testUsuarioBuscar(self):  
        self.user = User.objects.get(pk=1) 
        request = self.factory.get('/adm_usuarios/', {'busqueda': 'ysapy'})
        request.user = self.user
        response = administrarUsuarios(request) 
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
        usuario = User.objects.get(username='sap')
        request = self.factory.post('/adm_roles/modificar/1/', {'Nombre_de_Usuario': 'sapMod', 'Contrasenha': '', 'Nueva_contrasenha': '', 'Email': usuario.email, 'Nombre': usuario.first_name,'Apellido': usuario.last_name, 'Telefono': '2333443545', 'Direccion' : 'xxxxxxxxxxx', 'Especialidad' : '' , 'Observaciones' : ''})
        request.user = self.user
        response = modificarUsuario(request, 1)
        self.assertEqual(response.status_code, 200)
        print User.objects.all()


    if __name__ == '__main__':
        unittest.main()