from django.test import TestCase
from django.test.client import RequestFactory
from django.contrib.auth.models import User 
from aplicaciones.solicitudes.views import administrar_solicitud_recibidas, administrar_solicitud_realizadas

class test_solicitudes (TestCase):
    
    """    Cargamos los datos de prueba en la base de datos    """
    fixtures = ['proyectos.json'] + ['fases.json'] + ['items.json'] + ['linea_base.json'] + ['tipo_item.json'] + ['tipo_atributo.json'] + ['users.json'] + ['groups.json']
    
    def setUp(self):
        """ Inicializamos la variable factory que posteriormente nos permitira cargar
            un request para utilizarlo en las visata.
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

    if __name__ == '__main__':
        unittest.main()
