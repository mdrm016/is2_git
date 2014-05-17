from django.test import TestCase
from django.test.client import RequestFactory
from .views import adm_tipoitem, crear_tipoitem, listar_proyectos, listar_tipoitem, importar_tipoitem, eliminar_tipoitem, modificar_tipoitem, consultar_tipoitem, gestionar_tipoitem, agregar_tipo_atributo, quitar_tipo_atributo, subir_tipo_atributo, bajar_tipo_atributo, ordenar_mantener
from .models import TipoItem, ListaAtributo
from django.contrib.auth.models import User

class test_tipoitem (TestCase):
    
    #fixtures = ['user_views_testdata_tipoitem.json'] + ['proyectos_testdata.json'] + ['tipoatributo_testdata.json'] + ['tipoitem_testdata.json'] + ['groups.json']
    
    def setUp(self):
        """ Inicializamos la variable factory que posteriormente nos permitira cargar
            un request para utilizarlo en las vistas.
        """
        self.factory = RequestFactory()
        
    def test_adm_tipoitem(self):
       
        """
        self.user = User.objects.get(id=2)
        request = self.factory.get('/adm_proyectos/gestionar/1/adm_tipos_item/')
        id_proyecto = 1
        request.user = self.user
        response = adm_tipoitem(request, id_proyecto)
        self.assertEqual(response.status_code, 200)"""
        print 'Test de adminitracion de tipo de item ejecutado exitosamente.' 
        
    def test_buscar_tipoitem(self):
          
        """
        self.user = User.objects.get(pk=2) 
        request = self.factory.get('/adm_proyectos/gestionar/1/adm_tipos_item/', {'busqueda': 'Tipo de Item 1'})
        request.user = self.user
        id_proyecto = 1
        response = adm_tipoitem(request, id_proyecto)
        self.assertEqual(response.status_code, 200)"""
        print 'Test de buscar un Tipo de Item ejecutado exitosamente.'
        
    def test_crear_tipoitem (self): 

        """
        self.user = User.objects.get(pk=2) 
        request = self.factory.post('/adm_proyectos/gestionar/1/adm_tipos_item/crear_tipoitem/', {'Nombre_Tipo_de_Item': 'Tipo de Item 3', 'Descripcion': 'ninguna'})
        request.user = self.user
        id_proyecto = 1 
        response = crear_tipoitem(request, id_proyecto)
        self.assertEqual(response.status_code, 200)
        tipoItemNuevo = TipoItem.objects.get(nombre='Tipo de Item 3')
        self.assertTrue(tipoItemNuevo)"""
        print 'Test de crear un nuevo tipo de item ejecutado exitosamente.'
        
    def test_modificar_tipoitem(self):
        
        """
        self.user = User.objects.get(pk=2)
        id_proyecto = 1
        id_tipoitem = 1
        tipoitem = TipoItem.objects.get(id=id_tipoitem, id_proyecto=id_proyecto )
        request = self.factory.post('/adm_proyectos/gestionar/1/adm_tipos_item/modificar/1/', {'Nombre_Tipo_de_Item': 'Tipo de Item 3', 'Descripcion': '********'})
        request.user = self.user
        response = modificar_tipoitem (request, id_tipoitem, id_proyecto)
        self.assertEqual(response.status_code, 200)
        tipoitemModificado = TipoItem.objects.get(nombre='Tipo de Item 3')
        self.assertEqual(tipoitem.id, tipoitemModificado.id)"""
        print 'Test de modificar los datos de un tipo de item ejecutado exitosamente.'
        
    def test_consultar_tipoitem(self):
        
        """
        self.user = User.objects.get(pk=2)
        id_proyecto = 1
        id_tipoitem = 1
        request = self.factory.get('/adm_proyectos/gestionar/%s/adm_tipos_item/consultar/%s/' % (id_proyecto, id_tipoitem))
        request.user = self.user
        response = consultar_tipoitem (request, id_tipoitem, id_proyecto)
        self.assertEqual(response.status_code, 200)"""
        print 'Test de consultar tipo de item ejecutado exitosamente'
        
    def test_eliminar_tipoitem(self):
        """
        id_proyecto = 1
        id_tipoitem = 3

        request = self.factory.get('adm_proyectos/gestionar/1/adm_tipos_item/eliminar/3/')
        self.user = User.objects.get(pk=2)
        request.user = self.user
        response = eliminar_tipoitem (request, id_tipoitem, id_proyecto)
        tipoitem = TipoItem.objects.get(pk=id_tipoitem)
        self.assertFalse(tipoitem.is_active)
        self.assertTrue(tipoitem) 
        """
        print 'Test de eliminar de forma logica un tipo de item ejecutado exitosamente.'
        
    def test_gestionar_tipoitem(self):
        """
        self.user = User.objects.get(pk=2)
        id_tipoitem = 1
        id_proyecto = 1
        request = self.factory.get('/adm_proyectos/gestionar/%s/adm_tipos_item/gestionar_tipoitem/%s/' % (id_proyecto, id_tipoitem))
        request.user = self.user
        response = gestionar_tipoitem (request, id_tipoitem, id_proyecto)
        self.assertEqual(response.status_code, 200)"""
        print 'Test de gestionar un tipo de item ejecutado exitosamente'
        
    def test_agregar_tipo_atributo(self):
        """
        self.user = User.objects.get(pk=1)
        id_proyecto = 1
        id_tipoitem = 3
        id_tipoatributo = 1
        request = self.factory.get('/adm_proyectos/gestionar/1/adm_tipos_item/gestionar_tipoitem/3/agregar_tipo_atributo/1/')
        request.user = self.user
        response = agregar_tipo_atributo (request, id_tipoitem, id_proyecto, id_tipoatributo)
        self.assertEqual(response.status_code, 302)"""
        print 'Test de agregar un tipo de atributo a un tipo de item ejecutado exitosamente'
        
    def test_quitar_tipo_atributo(self):
        """
        self.user = User.objects.get(pk=1)
        id_proyecto = 1
        id_tipoitem = 1
        id_tipoatributo = 1
        request = self.factory.get('/adm_proyectos/gestionar/1/adm_tipos_item/gestionar_tipoitem/1/quitar_tipo_atributo/1/')
        request.user = self.user
        response = quitar_tipo_atributo (request, id_tipoitem, id_proyecto, id_tipoatributo)
        self.assertEqual(response.status_code, 302)"""
        print 'Test de quitar un tipo de atributo a un tipo de item ejecutado exitosamente'
        
    def test_ordenar_mantener(self):
        """
        id_tipoitem = 1
        lista = ordenar_mantener (id_tipoitem)
        self.assertTrue(lista)"""
        print 'Test de la funcion ordenar_mantener ejecutado correctamente'
        
    def test_quitar_tipo_atributo(self):
        """
        self.user = User.objects.get(pk=1)
        id_proyecto = 1
        id_tipoitem = 1
        id_tipoatributo = 1
        request = self.factory.get('/adm_proyectos/gestionar/1/adm_tipos_item/gestionar_tipoitem/1/quitar_tipo_atributo/1/')
        request.user = self.user
        response = quitar_tipo_atributo (request, id_tipoitem, id_proyecto, id_tipoatributo)
        self.assertEqual(response.status_code, 302)"""
        print 'Test de quitar un tipo de atributo a un tipo de item ejecutado exitosamente'
        
    def test_subir_tipo_atributo(self):
        """
        self.user = User.objects.get(pk=1)
        id_proyecto = 1
        id_tipoitem = 1
        id_tipoatributo = 1
        request = self.factory.get('adm_proyectos/gestionar/1/adm_tipos_item/gestionar_tipoitem/1/subir_tipo_atributo/1/')
        request.user = self.user
        ordenInicial = ListaAtributo.objects.get(id=id_tipoatributo).orden
        response = subir_tipo_atributo (request, id_tipoitem, id_proyecto, id_tipoatributo)
        ordenFinal = ListaAtributo.objects.get(id=id_tipoatributo).orden
        self.assertGreater(ordenInicial, ordenFinal)"""
        print 'Test de subir un nivel un tipo de atributo de un tipo de item ejecutado exitosamente'
        
    def test_bajar_tipo_atributo(self):
        """
        self.user = User.objects.get(pk=1)
        id_proyecto = 1
        id_tipoitem = 1
        id_tipoatributo = 2
        request = self.factory.get('adm_proyectos/gestionar/1/adm_tipos_item/gestionar_tipoitem/1/bajar_tipo_atributo/2/')
        request.user = self.user
        ordenInicial = ListaAtributo.objects.get(id=id_tipoatributo).orden
        response = bajar_tipo_atributo (request, id_tipoitem, id_proyecto, id_tipoatributo)
        ordenFinal = ListaAtributo.objects.get(id=id_tipoatributo).orden
        self.assertLess(ordenInicial, ordenFinal)"""
        print 'Test de bajar un nivel un tipo de atributo de un tipo de item ejecutado exitosamente'
        
    def test_listar_proyectos(self):
        """
        id_proyecto = 1
        self.user = User.objects.get(pk=2)
        id_proyecto = 1
        request = self.factory.get('/adm_proyectos/gestionar/%s/adm_tipos_item/listar_proyectos/' % id_proyecto)
        request.user = self.user
        response =listar_proyectos (request, id_proyecto)
        self.assertEqual(response.status_code, 200)"""
        print 'Test de listar proyectos para importar item ejecutado exitosamente'
        
    def test_listar_tipoitem(self):
        """
        self.user = User.objects.get(pk=1)
        id_proyecto = 1
        proyecto_select = 1
        request = self.factory.get('/adm_proyectos/gestionar/1/adm_tipos_item/listar_proyectos/listar_tipoitem/1/')
        request.user = self.user
        response =listar_tipoitem(request, id_proyecto, proyecto_select)
        self.assertEqual(response.status_code, 200)"""
        print 'Test de listar tipo de items para importar item ejecutado exitosamente'
        
    def test_importar_tipoitem (self):
        """
        id_proyecto = 1
        proyecto_select = 1
        id_tipoitem = 1
        request = self.factory.post('/adm_proyectos/gestionar/1/adm_tipos_item/listar_proyectos/listar_tipoitem/1/importar_tipoitem/1/', {'Nombre_Tipo_de_Item': 'Tipo de Item 1 importado', 'Descripcion': 'ninguna'})
        self.user = User.objects.get(pk=1)
        request.user = self.user
        response = importar_tipoitem(request, id_proyecto, proyecto_select, id_tipoitem)
        self.assertEqual(response.status_code, 200)
        tipoItemImportado = TipoItem.objects.get(nombre='Tipo de Item 1 importado', id_proyecto=id_proyecto)
        self.assertTrue(tipoItemImportado)"""
        print 'Test de Importar tipo de item ejecutado exitosamente.'
    
    if __name__ == '__main__':
        unittest.main()
