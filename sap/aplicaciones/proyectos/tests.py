from django.test import TestCase
from .models import Proyectos
from aplicaciones.fases.models import Fases
from aplicaciones.usuarios.models import Usuarios
from django.contrib.auth.models import User
from django.test.client import RequestFactory 
from .views import adm_proyectos, crear_proyecto, modificar_proyecto, consultar_proyecto, eliminar_proyecto, listar_miembros, importar_proyecto, importar

class test_proyectos (TestCase):
    
    fixtures = ['user_views_testdata.json']+ ['proyectos_views_testdata.json'] + ['fases_views_testdata.json']  
    
    def setUp(self):
        """ Inicializamos la variable factory que posteriormente nos permitira cargar
            un request para utilizarlo en las vista.
        """
        self.factory = RequestFactory()
        
    def test_adm_proyectos (self):
        
        self.user = User.objects.get(id=1)
        request = self.factory.get('/adm_proyectos/')
        request.user = self.user
        response = adm_proyectos(request)
        self.assertEqual(response.status_code, 200)
        print 'Test de adminitracion de proyectos ejecutado exitosamente.'    
        
    def test_buscar_proyecto(self):  
        self.user = User.objects.get(pk=1) 
        request = self.factory.post('/adm_proyectos/', {'busqueda': 'Proyecto 1'})
        request.user = self.user
        response = adm_proyectos(request)
        self.assertEqual(response.status_code, 200)
        print 'Test de buscar un proyecto ejecutado exitosamente.'
        
    def test_crear_proyecto(self): 

        self.user = User.objects.get(pk=1) 
        request = self.factory.post('/adm_proyectos/crear/', {'Nombre_del_Proyecto': 'Proyecto 10', 'Lider': '2', 'Fecha_de_Inicio': '2014-04-19', 'Duracion': '2'})
        request.user = self.user 
        response = crear_proyecto(request) 
        self.assertEqual(response.status_code, 200)
        proyectoNuevo = Proyectos.objects.get(nombre='Proyecto 10')
        self.assertTrue(proyectoNuevo)
        print 'Test de crear un proyecto ejecutado exitosamente.'
        
    def test_modificar_proyecto(self):
        
        self.user = User.objects.get(pk=1)
        proyecto = Proyectos.objects.get(id=1)
        request = self.factory.post('adm_proyectos/modificar/1/', {'Nombre_del_Proyecto': 'Proyecto 12', 'Lider': '2', 'Fecha_de_Inicio': '2014-04-19', 'Duracion': '2'})
        request.user = self.user
        proyecto_id = '1'
        response = modificar_proyecto(request, proyecto_id)
        self.assertEqual(response.status_code, 200)
        proyectoModificado = Proyectos.objects.get(nombre='Proyecto 12')
        self.assertEqual(proyecto.id, proyectoModificado.id)
        print 'Test de modificar los datos de proyecto ejecutado exitosamente.'
        
    def test_proyecto_eliminar(self):

        request = self.factory.get('/adm_proyectos/eliminar/1')
        self.user = User.objects.get(pk=1)
        request.user = self.user
        proyecto_id = '1'
        response = eliminar_proyecto(request, proyecto_id)
        proyecto = Proyectos.objects.get(pk=proyecto_id)
        self.assertFalse(proyecto.is_active)
        self.assertTrue(proyecto) 
        print 'Test de eliminar de forma logica un proyecto ejecutado exitosamente.'
        
    def test_listarmiembros(self):
        
        request = self.factory.get('adm_proyectos/listar_miembros/1')
        self.user = User.objects.get(pk=1)
        request.user = self.user
        proyecto_id='1'
        response = listar_miembros(request, proyecto_id)
        self.assertEqual(response.status_code, 200)
        print 'Test de listar miembros de un proyecto ejecutado exitosamente.'
        
    def test_importar_proyecto(self):
        
        request = self.factory.get('adm_proyectos/importar_proyecto')
        self.user = User.objects.get(pk=1)
        request.user = self.user
        response = importar_proyecto(request)
        self.assertEqual(response.status_code, 200)
        print 'Test de seleccionar proyecto a importar ejecutado exitosamente.'
        
    def test_importar (self):
        
        proyecto_id = '1'
        fases = Fases.objects.filter(proyecto=1)
        self.assertTrue(fases)
        request = self.factory.post('adm_proyectos/importar_proyecto/importar/1', {'Nombre_del_Proyecto': 'Proyecto 15 imp', 'Lider': '2', 'Fecha_de_Inicio': '2014-04-19', 'Duracion': '2'})
        self.user = User.objects.get(pk=1)
        request.user = self.user
        response = importar(request, proyecto_id)
        self.assertEqual(response.status_code, 200)
        proyectoImportado = Proyectos.objects.get(nombre='Proyecto 15 imp')
        self.assertTrue(proyectoImportado)
        print 'Test de Importar proyecto ejecutado exitosamente.'
        
    if __name__ == '__main__':
        unittest.main()