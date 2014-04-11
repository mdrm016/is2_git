from django.contrib.auth.models import User 
from django.test import TestCase 
from django.test.client import RequestFactory 
from aplicaciones.usuarios.views import administrarUsuarios 
from aplicaciones.usuarios.views import usuario_eliminar, usuarionuevo

class SimpleTest(TestCase): 
    fixtures = ['users.json'] 
    def setUp(self): 
        # Every test needs access to the request factory. 
        self.factory = RequestFactory()

    def test_details(self): # Create an instance of a GET request. 
        self.user = User.objects.get(pk=1) 
        request = self.factory.get('/adm_usuarios/eliminar/2/') 
        # Recall that middleware are not suported. You can simulate a 
        # logged-in user by setting request.user manually. 
        request.user = self.user 
        print User.objects.all() 
        response = usuario_eliminar(request, 3) 
         
        print User.objects.all() 
        #como ven pude eliminar al usuario com pk=2 osea mdrm016 
        
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
              
    if __name__ == '__main__':
        unittest.main()