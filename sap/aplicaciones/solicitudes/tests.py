from django.test import TestCase
from django.test.client import RequestFactory
from django.contrib.auth.models import User 
from aplicaciones.solicitudes.views import administrar_solicitud_recibidas, administrar_solicitud_realizadas, votar_solicitud, administrar_credenciales, consultarCredencial
from aplicaciones.usuarios.views import Usuarios

class test_solicitudes (TestCase):
    
    """    Cargamos los datos de prueba en la base de datos    """
    fixtures = ['user.json'] + ['roles.json'] + ['group.json'] + ['proyectos.json'] + ['comite.json'] + ['fases.json'] + ['tipoatributo.json'] + ['listaatributo.json'] + ['tipoitem.json'] + ['items.json'] + ['linea_base.json'] + ['solicitudes.json'] + ['credenciales.json']
    
    
    def setUp(self):
        """ Inicializamos la variable factory que posteriormente nos permitira cargar
            un request para utilizarlo en las vista.
        """
        self.factory = RequestFactory()
        
    def test_administrar_solicitud_recibidas(self): 
           
        self.user = User.objects.get(pk=2)  
        request = self.factory.get('/adm_proyectos/solicitudes_recibidas/')
        request.user = self.user
        response = administrar_solicitud_recibidas(request)
        self.assertEqual(response.status_code, 200)
        print 'Test de administrar solicitudes recibidas ejecutado exitosamente.'
        
    def test_administrar_solicitud_realizadas(self): 
           
        self.user = User.objects.get(pk=2)  
        request = self.factory.get('/adm_proyectos/solicitudes_realizadas/')
        request.user = self.user
        response = administrar_solicitud_realizadas(request)
        self.assertEqual(response.status_code, 200)
        print 'Test de administrar solicitudes realizadas ejecutado exitosamente.'
        
    def testVotarSolicitud(self):
        self.user = User.objects.get(pk=3)
        request = self.factory.post('adm_proyectos/solicitudes_recibidas/votar_solicitud/2/', {'voto': 'R'})
        request.user = self.user
        response = votar_solicitud(request, 2)
        self.assertEqual(response.status_code, 200)
        print 'Test de Votar Solicitud ejecutado exitosamente'
        
    def test_administrar_credenciales (self):
        self.user = User.objects.get(pk=1)  
        request = self.factory.get('/adm_proyectos/admin_credenciales/')
        request.user = self.user
        response = administrar_credenciales (request)
        self.assertEqual(response.status_code, 200)
        print 'Test de administrar credenciales ejecutado exitosamente.'

    def testConsultarCredencial(self):
        self.user = User.objects.get(pk=1)
        request = self.factory.get('adm_proyectos/admin_credenciales/consultar_credencial/1/')
        request.user = self.user
        response = consultarCredencial(request, 1)
        self.assertEqual(response.status_code, 200)
        print 'Test de consultar credencial ejecutado exitosamente'

    if __name__ == '__main__':
        unittest.main()
