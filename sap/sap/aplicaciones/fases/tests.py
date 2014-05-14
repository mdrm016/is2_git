from django.test import TestCase
from django.test.client import RequestFactory
from django.contrib.auth.models import User
from .models import Fases
from aplicaciones.proyectos.models import Proyectos
from .views import adm_fases, crear_fase, consultar_fase, eliminar_fase, modificar_fase, importar_fase, importarf

# Create your tests here.

class test_fase(TestCase):
    
    fixtures = ['users.json']+ ['proyectos.json'] + ['fases.json']
    
    def setUp(self):
        """ Inicializamos la variable factory que posteriormente nos permitira cargar
            un request para utilizarlo en las vista.
        """
        self.factory = RequestFactory()
        
    def test_adm_fases (self):
        
        self.user = User.objects.get(pk=1)
        proyecto = Proyectos.objects.get(id=1)
        request = self.factory.get('/adm_proyectos/gestionar/1')
        request.user = self.user
        response = adm_fases(request, proyecto.id)
        self.assertEqual(response.status_code, 200)
        print 'Test de administracion de fases ejecutado exitosamente.'
        
    def test_crear_fase (self):
        
        self.user = User.objects.get(pk=1)
        proyecto = Proyectos.objects.get(id=1)
        request = self.factory.post('/adm_proyectos/gestionar/1/nuevo/', {'Nombre_de_Fase': 'Fase 20', 'Descripcion': 'La fase 10', 'Duracion_semanas': '2'})
        request.user = self.user 
        response = crear_fase(request, 1) 
        self.assertEqual(response.status_code, 200)
        print response.status_code 
        faseNueva = Fases.objects.get(nombre='Fase 20')
        self.assertTrue(faseNueva)
        print 'Test de crear una fase ejecutado exitosamente.'
        
    def test_consultar_fase (self):
        
        self.user = User.objects.get(pk=1)
        proyecto = Proyectos.objects.get(id=1)
        fase = Fases.objects.get(id=1)
        request = self.factory.get('/adm_proyectos/gestionar/1/consultar/1')
        request.user = self.user
        response = consultar_fase(request, fase.id, proyecto.id)
        self.assertEqual(response.status_code, 200)
        print 'Test de consultar una fase ejecutado exitosamente'

                
    def test_eliminar_fase (self):
        
        request = self.factory.get('/adm_proyectos/gestionar/1/eliminar/1')
        self.user = User.objects.get(pk=1)
        request.user = self.user
        proyecto = Proyectos.objects.get(id=1)
        fase_id = '1'
        response = eliminar_fase(request, fase_id, proyecto.id)
        fase = Fases.objects.get(id=fase_id)
        self.assertFalse(fase.is_active)
        self.assertTrue(fase) 
        print 'Test de eliminar de forma logica una fase ejecutado exitosamente.'
        
    def test_modificar_fase (self):
        
        self.user = User.objects.get(pk=1)
        proyecto = Proyectos.objects.get(id=1)
        request = self.factory.post('adm_proyectos/gestionar/1/modificar/1/', {'Nombre_de_Fase': 'Fase 12', 'Descripcion': 'La fase 12', 'Duracion': '3'})
        request.user = self.user
        fase = Fases.objects.get(id=1)
        fase_id = '1'
        response = modificar_fase(request, proyecto.id, fase_id)
        self.assertEqual(response.status_code, 200)
        faseModificada = Fases.objects.get(nombre='Fase 12')
        self.assertEqual(fase.id, faseModificada.id)
        print 'Test de modificar los datos de fase ejecutado exitosamente.'
    
    def test_importar_fase (self):
        
        request = self.factory.get('adm_proyectos/gestionar/1/importar_fase')
        self.user = User.objects.get(pk=1)
        request.user = self.user
        proyecto = Proyectos.objects.get(id=1)
        response = importar_fase(request, proyecto.id)
        self.assertEqual(response.status_code, 200)
        print 'Test de seleccionar fase a importar ejecutado exitosamente.'
        
    def test_importarf (self):
        
        fase_id = '1'
        proyecto = Proyectos.objects.get(id=1)
        request = self.factory.post('adm_proyectos/gestionar/1/importar_fase/importarf/1', {'Nombre_de_Fase': 'Fase 15 imp', 'Descripcion': 'La fase 15', 'Duracion': '2'})
        self.user = User.objects.get(pk=1)
        request.user = self.user
        response = importarf(request, 1, 1)
        self.assertEqual(response.status_code, 200)
        faseImportada = Fases.objects.get(nombre='Fase 15 imp')
        self.assertTrue(faseImportada)
        print 'Test de Importar fase ejecutado exitosamente.'
        
    if __name__ == '__main__':
        unittest.main()
        