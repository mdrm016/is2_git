from django.contrib.auth.models import User
from django.test import TestCase
from django.test.client import RequestFactory
from aplicaciones.usuarios.views import administrarUsuarios
from aplicaciones.usuarios.views import usuario_eliminar

class SimpleTest(TestCase):
    """    Cargamos los usuarios de prueba en la base de datos    """
    fixtures = ['users.json']
    username = 'sap'
    password = 'sap'
    
    def setUp(self):
        """ Inicializamos la variable factory que posteriormente nos permitira cargar
            un request para utilizarlo en las visata.
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
        id = '2'
        usuarioname = User.objects.filter(pk=id)
        self.assertTrue(usuarioname)
        
        """ Borramos al usuario con id 2 """
        response = usuario_eliminar(request, id)
        
        """ Nos aseguramos que el usuario con id se ha eliminado. """
        usuarioname = User.objects.filter(pk=id)
        self.assertFalse(usuarioname)
        
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
            
    def testUsernuevo(self):
        usuario = User.objects.get(pk=1)
        
        resp = self.client.get('/login/')
        self.assertEqual(resp.status_code, 200)
        login = self.client.login(username=self.username, password=self.password)
        self.assertTrue(login)
        url = '/adm_usuarios/nuevo/'
        p = self.client.post('/adm_usuarios/nuevo/', {'username': 'mama', 'password': 'ysapy', 'email': 'ysa@correo', 'first_name': 'mimbi', 'last_name': 'ortiz', 'telefono': '021', 'direccion': 'lambare', 'especialidad': 'desarrollador'})
        res = self.client.get(url)
        usuario = User.objects.all()
        print usuario
        
    def testBuscarusuario(self):
        usuario = User.objects.get(pk=1)
        resp = self.client.get('/login/')
        self.assertEqual(resp.status_code, 200)
        login = self.client.login(username=self.username, password=self.password)
        self.assertTrue(login)
        url = '/adm_usuarios/?busqueda=ysapy/'
        res = self.client.get(url)
        usuario = User.first_name.filter(username='ysapy')
        print usuario
        
        
    if __name__ == '__main__':
        unittest.main()
