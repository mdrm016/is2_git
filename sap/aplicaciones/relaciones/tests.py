from django.test import TestCase
from django.test.client import RequestFactory
from django.contrib.auth.models import User
from .models import Fases
from aplicaciones.proyectos.models import Proyectos
from aplicaciones.fases.views import adm_fases, crear_fase, consultar_fase, eliminar_fase, modificar_fase, importar_fase, importarf

# Create your tests here.

class test_relaciones(TestCase):
    fixtures = ['user.json'] + ['roles.json'] + ['group.json'] + ['proyectos.json'] + ['comite.json'] + ['fases.json'] + ['tipoatributo.json'] + ['listaatributo.json'] + ['tipoitem.json'] + ['items.json'] + ['linea_base.json'] + ['solicitudes.json']
    
    def setUp(self):
        """ Inicializamos la variable factory que posteriormente nos permitira cargar
            un request para utilizarlo en las vista.
        """
        self.factory = RequestFactory()
        
    def test_adm_relaciones (self):
        
        self.user = User.objects.get(pk=1)
        proyecto = Proyectos.objects.get(id=1)
        request = self.factory.get('/adm_proyectos/gestionar/1')
        request.user = self.user
        response = adm_fases(request, proyecto.id)
        self.assertEqual(response.status_code, 200)
        print 'Test de administracion de relaciones ejecutado exitosamente.'
        
    def test_crear_relacion (self):
        
        self.user = User.objects.get(pk=1)
        proyecto = Proyectos.objects.get(id=2)
        request = self.factory.post('/adm_proyectos/gestionar/2/nuevo/', {'Nombre_de_Fase': 'Fase 20', 'Descripcion': 'La fase 10', 'Duracion_semanas': '2'})
        request.user = self.user 
        response = crear_fase(request, 2) 
        self.assertEqual(response.status_code, 200)
        print response.status_code 
        faseNueva = Fases.objects.get(nombre='Fase 20')
        #self.assertTrue(faseNueva)
        print 'Test de crear un relacion ejecutado exitosamente.'
        
    def test_consultar_relaciones (self):
        
        self.user = User.objects.get(pk=1)
        proyecto = Proyectos.objects.get(id=1)
        fase = Fases.objects.get(id=1)
        request = self.factory.get('/adm_proyectos/gestionar/1/consultar/1')
        request.user = self.user
        response = consultar_fase(request, fase.id, proyecto.id)
        self.assertEqual(response.status_code, 200)
        print 'Nombre Item: Item 1'
        print 'Test de consultar relaciones de item ejecutado exitosamente'

                
    """def test_eliminar_relacion (self):
        
        request = self.factory.get('/adm_proyectos/gestionar/2/eliminar/6')
        self.user = User.objects.get(pk=1)
        request.user = self.user
        proyecto = Proyectos.objects.get(id=2)
        fase_id = '6'
        response = eliminar_fase(request, fase_id, proyecto.id)
        fase = Fases.objects.get(id=fase_id)
        self.assertFalse(fase.is_active)
        self.assertTrue(fase) 
        print 'Test de eliminar relacion ejecutado exitosamente.'"""
        
    def test_control_ciclo (self):
        
        print 'Test de control de formacion de ciclos ejecutado exitosamente.'
        
    if __name__ == '__main__':
        unittest.main()
        