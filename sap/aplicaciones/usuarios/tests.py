from django.test import TestCase
from .models import Usuarios
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpRequest
from aplicaciones.usuarios.views import usuario_eliminar, usuarionuevo
from django.core.urlresolvers import reverse

class TestUsuario(TestCase):
    fixtures = ['users.json']
    username = 'sap'
    password = 'sap'
         
      
    def testUsereliminar(self):
        usuario= User.objects.get(pk=1) 
        resp = self.client.get('/login/')                                           #Solicitud de la pagina de autenticacion
        self.assertEqual(resp.status_code, 200)                                     #Pagina de login recibida con exito
        login = self.client.login(username=self.username, password=self.password)  #Proceso de autenticacion
        self.assertTrue(login)               
        url = '/adm_usuarios/eliminar/2'
        p = self.client.get(url)
        usuario= User.objects.all()
        print usuario
        self.assertNotEqual(self.username, 'sap')
            
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