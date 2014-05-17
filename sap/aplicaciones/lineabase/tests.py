from django.test import TestCase
from django.test.client import RequestFactory
from aplicaciones.lineabase.views import administrarLineaBase, generarLineaBase, consultar_lineabase, informe_lineabase
from django.contrib.auth.models import User 
from aplicaciones.proyectos.models import Proyectos
from aplicaciones.fases.models import Fases
from aplicaciones.lineabase.models import LineaBase

# Create your tests here.
class test_user(TestCase):
    """    Cargamos Proyectos, Fases, items, Lineas Base y Usuarios de prueba en la base de datos    """
    fixtures = ['proyectos.json'] + ['fases.json'] + ['items.json'] + ['linea_base.json'] + ['tipo_item.json'] + ['tipo_atributo.json'] + ['users.json'] + ['groups.json']
    
    def setUp(self):
        """ Inicializamos la variable factory que posteriormente nos permitira cargar
            un request para utilizarlo en las visata.
        """
        self.factory = RequestFactory()
        
    def testAdministrarLineaBase(self):    
        self.user = User.objects.get(pk=2)  
        request = self.factory.get('/adm_proyectos/gestionar/1/adm_items/1/adm_lineas_base/')
        request.user = self.user
        response = administrarLineaBase(request, 1, 1)
        self.assertEqual(response.status_code, 200)
        print 'Test de adminitracion de Linea Base ejecutado exitosamente.'
        
    def testGenerarLineaBase(self):
        self.user = User.objects.get(pk=2) 
        request = self.factory.post('/adm_proyectos/gestionar/1/adm_items/1/adm_lineas_base/nuevo/', {'Descripcion': 'Prueba', 'Items': ['3']})
        request.user = self.user 
        response = generarLineaBase(request, 1, 1) 
        self.assertEqual(response.status_code, 200)
        print 'Test de Crear Linea Base ejecutado exitosamente'
        
    def test_buscar_lineabase(self):
          
        self.user = User.objects.get(pk=1)
        id_proyecto = 1
        id_fase = 1
        id_lineabase = 1
        request = self.factory.get('/adm_proyectos/gestionar/%s/adm_items/%s/adm_lineas_base/' % (id_proyecto, id_fase), {'busqueda': '1'})
        request.user = self.user
        response = administrarLineaBase(request, id_proyecto, id_fase)
        self.assertEqual(response.status_code, 200)
        print 'Test de buscar una linea base ejecutado exitosamente.'
        
    def test_consultar_lineabase(self):

        self.user = User.objects.get(pk=1)
        id_proyecto = 1
        id_fase = 1
        id_lineabase = 1
        request = self.factory.get('/adm_proyectos/gestionar/%s/adm_items/%s/adm_lineas_base/consultar/%s/' % (id_proyecto, id_fase, id_lineabase))
        request.user = self.user
        response = consultar_lineabase (request, id_proyecto, id_fase, id_lineabase)
        self.assertEqual(response.status_code, 200)
        print 'Test de consultar linea base ejecutado exitosamente'
        
    def test_informe_lineabase(self):
        
        self.user = User.objects.get(pk=1)
        id_proyecto = 1
        id_fase = 1
        id_lineabase = 1
        request = self.factory.get('/adm_proyectos/gestionar/%s/adm_items/%s/adm_lineas_base/informe_lineabase/%s)/' % (id_proyecto, id_fase, id_lineabase))
        request.user = self.user
        response = informe_lineabase(request, id_proyecto, id_fase, id_lineabase)
        self.assertEqual(response.status_code, 302)
        print 'Test de generar informe de linea base ejecutado exitosamente'
        
        
    if __name__ == '__main__':
        unittest.main()


