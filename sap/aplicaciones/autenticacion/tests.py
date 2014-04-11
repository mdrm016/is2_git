from django.core.urlresolvers import reverse
from django.test import TestCase
from django.contrib.auth.models import User

class UsuarioViewTestCase(TestCase):
    
    
    #Usuario administrador
    username = 'sap'
    password = 'sap'
    
    #Un usuario cualquiera
    u1 = 'mdrm016'
    p1 = '123456'
    
    #Un usuario inexistente
    u2 = 'xxxxx'
    p2 = 'xxxxx'
    
    
    def setUp(self):
        User.objects.create_user(username=self.username, password=self.password)
        User.objects.create_user(username=self.u1, password=self.p1)
        
    def test_loguin_admin(self):
        """ Test para loguear al administrador, este test debe funcionar correctamente """
        
        resp = self.client.get('/login/')                                           #Solicitud de la pagina de autenticacion
        self.assertEqual(resp.status_code, 200)                                     #Pagina de login recibida con exito
        loguin = self.client.login(username=self.username, password=self.password)  #Proceso de autenticacion
        self.assertTrue(loguin)                                                     #Comprobamos si el usuario esta autenticado
        resp = self.client.get('/')                                                 #Pasamos a la pagina de inicio
        self.assertEqual(resp.status_code, 200)                                     #Pagina de inicio recibida con exito
        resp = self.client.get('/adm_usuarios/')                                    #Pasamos a la pagina de administracion de usuarios
        self.assertEqual(resp.status_code, 200)                                     #Pagina de adm_usuarios recibida con exito
        self.assertTrue('lista_usuarios' in resp.context)                           #Comprobamos si recibimos la lista de usuarios
    
    def test_loguin_user(self):
        """ Test para loguear a un usuario, este test debe funcionar correctamente """
        
        resp = self.client.get('/login/')                                           #Solicitud de la pagina de autenticacion
        self.assertEqual(resp.status_code, 200)                                     #Pagina de login recibida con exito
        loguin = self.client.login(username=self.u1, password=self.p1)              #Proceso de autenticacion
        self.assertTrue(loguin)                                                     #Comprobamos si el usuario esta autenticado
        resp = self.client.get('/')                                                 #Pasamos a la pagina de inicio
        self.assertEqual(resp.status_code, 200)                                     #Pagina de inicio recibida con exito
        resp = self.client.get('/adm_usuarios/')                                    #Pasamos a la pagina de administracion de usuarios
        self.assertEqual(resp.status_code, 200)                                     #Pagina de adm_usuarios recibida con exito
        self.assertTrue('lista_usuarios' in resp.context)                           #Comprobamos si recibimos la lista de usuarios
    
    def test_loguin_userAnonimo(self):
        """ Test para loguear a un usuario no registardo, 
            este test debe fallar """
        
        resp = self.client.get('/login/')                                           #Solicitud de la pagina de autenticacion
        self.assertEqual(resp.status_code, 200)                                     #Pagina de login recibida con exito
        loguin = self.client.login(username=self.u2, password=self.p2)              #Proceso de autenticacion
        self.assertTrue(loguin)                                                     #Comprobamos si el usuario esta autenticado
        resp = self.client.get('/')                                                 #Pasamos a la pagina de inicio
        self.assertEqual(resp.status_code, 200)                                     #Pagina de inicio recibida con exito
        resp = self.client.get('/adm_usuarios/')                                    #Pasamos a la pagina de administracion de usuarios
        self.assertEqual(resp.status_code, 200)                                     #Pagina de adm_usuarios recibida con exito
        self.assertTrue('lista_usuarios' in resp.context)                           #Comprobamos si recibimos la lista de usuarios