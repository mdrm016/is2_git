from django.core.urlresolvers import reverse
from django.test import TestCase
from django.contrib.auth.models import User

class TestLoguin(TestCase):
    """ Inicializamos variables globales """
    
    #Usuario administrador
    username = 'sap'
    password = 'sap'
    
    #Un usuario cualquiera
    u1 = 'mdrm016'
    p1 = '123456'
    
    #Un usuario inexistente
    u2 = 'xxxxx'
    p2 = 'xxxxx'
    
    """    Cargamos los usuarios de prueba en la base de datos    """
    fixtures = ['users.json']
        
    def test_loguin_admin(self):
        """ Test para loguear al administrador. """
        
        resp = self.client.get('/login/')                                           #Solicitud de la pagina de autenticacion
        self.assertEqual(resp.status_code, 200)                                     #Pagina de login recibida con exito
        login = self.client.login(username=self.username, password=self.password)  #Proceso de autenticacion
        self.assertTrue(login)                                                     #Comprobamos si el usuario esta autenticado
        resp = self.client.get('/')                                                 #Pasamos a la pagina de inicio
        self.assertEqual(resp.status_code, 200)                                     #Pagina de inicio recibida con exito
        resp = self.client.get('/adm_usuarios/')                                    #Pasamos a la pagina de administracion de usuarios
        self.assertEqual(resp.status_code, 200)                                     #Pagina de adm_usuarios recibida con exito
        self.assertTrue('lista_usuarios' in resp.context)                           #Comprobamos si recibimos la lista de usuarios
    
    def test_loguin_user(self):
        """ Test para loguear a un usuario. """
        
        resp = self.client.get('/login/')                                           #Solicitud de la pagina de autenticacion
        self.assertEqual(resp.status_code, 200)                                     #Pagina de login recibida con exito
        login = self.client.login(username=self.u1, password=self.p1)              #Proceso de autenticacion
        self.assertTrue(login)                                                     #Comprobamos si el usuario esta autenticado
        resp = self.client.get('/')                                                 #Pasamos a la pagina de inicio
        self.assertEqual(resp.status_code, 200)                                     #Pagina de inicio recibida con exito
        resp = self.client.get('/adm_usuarios/')                                    #Pasamos a la pagina de administracion de usuarios
        self.assertEqual(resp.status_code, 200)                                     #Pagina de adm_usuarios recibida con exito
        self.assertTrue('lista_usuarios' in resp.context)                           #Comprobamos si recibimos la lista de usuarios
    
    def test_loguin_userAnonimo(self):
        """ Test para loguear a un usuario no registardo.
        """
        
        resp = self.client.get('/login/')                                           #Solicitud de la pagina de autenticacion
        self.assertEqual(resp.status_code, 200)                                     #Pagina de login recibida con exito
        login = self.client.login(username=self.u2, password=self.p2)              #Proceso de autenticacion
        self.assertFalse(login)                                                     #Comprobamos si el usuario esta autenticado
        resp = self.client.get('/')                                                 #Pasamos a la pagina de inicio
        self.assertEqual(resp.status_code, 302)                                     #Pagina de inicio recibida con exito
        resp = self.client.get('/adm_usuarios/')                                    #Pasamos a la pagina de administracion de usuarios
        self.assertEqual(resp.status_code, 302)                                     #Pagina de adm_usuarios recibida con exito
        
        
    def test_ingresar_sin_registrarse(self):
        """ Error 302 "movido Temporalmente",
            al ingresar intentar ingresar a la pagina
            de inicio sin antes habernos logueado
            el error 302 nos imposibilita el acceso
            
        """ 
        resp = self.client.get('/')                                                 #Pasamos a la pagina de inicio
        self.assertEqual(resp.status_code, 302)                                     #Ocurre el erro 302
        resp = self.client.get('/adm_usuarios/')                                    #Pasamos a la pagina de administracion de usuarios
        self.assertEqual(resp.status_code, 302)                                     #Ocurre el error 302
        
        if __name__ == '__main__':
            unittest.main()
    