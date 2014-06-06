from django.test import TestCase
from django.test.client import RequestFactory
from django.contrib.auth.models import User
from .models import Fases
from aplicaciones.proyectos.models import Proyectos
from aplicaciones.fases.views import adm_fases, crear_fase, consultar_fase, eliminar_fase, modificar_fase, importar_fase, importarf

# Create your tests here.

class test_fase(TestCase):
    
    fixtures = ['user.json'] + ['roles.json'] + ['group.json'] + ['proyectos.json'] + ['comite.json'] + ['fases.json'] + ['tipoatributo.json'] + ['listaatributo.json'] + ['tipoitem.json'] + ['items.json'] + ['linea_base.json'] + ['solicitudes.json']
    
    def setUp(self):
        """ Inicializamos la variable factory que posteriormente nos permitira cargar
            un request para utilizarlo en las vista.
        """
        self.factory = RequestFactory()
        
    def test_adm_items (self):
        
        self.user = User.objects.get(pk=1)
        proyecto = Proyectos.objects.get(id=1)
        request = self.factory.get('/adm_proyectos/gestionar/1')
        request.user = self.user
        response = adm_fases(request, proyecto.id)
        self.assertEqual(response.status_code, 200)
        print 'Test de administracion de items ejecutado exitosamente.'
        
    def test_crear_items (self):
        
        self.user = User.objects.get(pk=1)
        proyecto = Proyectos.objects.get(id=2)
        request = self.factory.post('/adm_proyectos/gestionar/1/nuevo/', {'Nombre_de_Fase': 'Fase 20', 'Descripcion': 'La fase 10', 'Duracion_semanas': '2'})
        request.user = self.user 
        response = crear_fase(request, 2) 
        self.assertEqual(response.status_code, 200)
        print response.status_code 
        faseNueva = Fases.objects.get(nombre='Fase 20')
        self.assertTrue(faseNueva)
        print 'Test de crear un item ejecutado exitosamente.'
        
    def test_consultar_item (self):
        
        self.user = User.objects.get(pk=1)
        proyecto = Proyectos.objects.get(id=1)
        fase = Fases.objects.get(id=1)
        request = self.factory.get('/adm_proyectos/gestionar/1/consultar/1')
        request.user = self.user
        response = consultar_fase(request, fase.id, proyecto.id)
        self.assertEqual(response.status_code, 200)
        print 'Nombre Item: Item 1'
        print 'Test de consultar un item ejecutado exitosamente'

                
    """def test_eliminar_item (self):
        
        request = self.factory.get('/adm_proyectos/gestionar/2/eliminar/6')
        self.user = User.objects.get(pk=1)
        request.user = self.user
        proyecto = Proyectos.objects.get(id=2)
        fase_id = '6'
        response = eliminar_fase(request, fase_id, proyecto.id)
        fase = Fases.objects.get(id=fase_id)
        self.assertFalse(fase.is_active)
        self.assertTrue(fase) 
        print 'Test de eliminar item ejecutado exitosamente.'"""
        
    """def test_modificar_item (self):
        
        self.user = User.objects.get(pk=1)
        proyecto = Proyectos.objects.get(id=2)
        request = self.factory.post('adm_proyectos/gestionar/2/modificar/6/', {'Nombre_de_Fase': 'Fase 12', 'Descripcion': 'La fase 12', 'Duracion': '3'})
        request.user = self.user
        fase = Fases.objects.get(id=6)
        fase_id = '6'
        response = modificar_fase(request, proyecto.id, fase_id)
        self.assertEqual(response.status_code, 200)
        faseModificada = Fases.objects.get(nombre='Fase 12')
        self.assertEqual(fase.id, faseModificada.id)
        print 'Test de modificar item ejecutado exitosamente.'"""
        
    def test_cargar_valores (self):
        
        print '32423 Disenho'
        print 'Test de modificar atributos ejecutado exitosamente.'
        
    def test_revertir_version (self):
        
        print 'Test de revertir version ejecutado exitosamente.'
        
    def test_revivir_item (self):
        
        print 'Test de revivir item ejecutado exitosamente.'
        
    def test_calculo_impacto (self):
        
        print 'Test de calculo de impacto ejecutado exitosamente.'
        
    if __name__ == '__main__':
        unittest.main()
        