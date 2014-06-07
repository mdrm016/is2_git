from django.test import TestCase
from django.test.client import RequestFactory
from aplicaciones.tipoatributo.views import administrarTipoAtributo, tipoAtributoNuevo, modificarTipoAtributo
from aplicaciones.tipoatributo.views import eliminarTipoAtributo, consultarTipoAtributo, importarTipoAtributo
from aplicaciones.tipoatributo.models import TipoAtributo
from django.contrib.auth.models import User 
from aplicaciones.roles.models import Roles

class test_user(TestCase):
    """    Cargamos Proyectos, tipos de Item y Tipos de Atributo de prueba en la base de datos    """
    fixtures = ['user.json'] + ['roles.json'] + ['group.json'] + ['proyectos.json'] + ['comite.json'] + ['fases.json'] + ['tipoatributo.json'] + ['listaatributo.json'] + ['tipoitem.json'] + ['items.json'] + ['linea_base.json'] + ['solicitudes.json']
    
    def setUp(self):
        """ Inicializamos la variable factory que posteriormente nos permitira cargar
            un request para utilizarlo en las visata.
        """
        self.factory = RequestFactory()
    
    def testAdministrarTipoAtributo(self):
    
        self.user = User.objects.get(pk=1)  
        request = self.factory.get('/adm_proyectos/gestionar/1/adm_tipos_atributo/')
        request.user = self.user
        response = administrarTipoAtributo(request, 1)                                    #Pasamos a la pagina de administracion de Tipos de Atributo
        self.assertEqual(response.status_code, 200)
        print 'Test de adminitracion de tipo de Atributo ejecutado exitosamente.' 
    
    def testTipoAtributoNuevo(self):
        
        self.user = User.objects.get(pk=1) 
        request = self.factory.post('/adm_proyectos/gestionar/1/adm_tipos_atributo/nuevo/', {'Nombre_tipo_atributo': 'Detalle', 'Tipo_de_dato': 'Texto', 'Precision': '0', 'Longitud': '5', 'Obligatorio': 'N', 'Descripcion': ''})
        request.user = self.user 
        response = tipoAtributoNuevo(request, 1) 
        self.assertEqual(response.status_code, 200)
        print 'Test de Crear Tipo de Atributo ejecutado exitosamente'
        
    def testModificarTipoAtributo(self):
        
        self.user = User.objects.get(pk=1)
        request = self.factory.post('/adm_proyectos/gestionar/2/adm_tipos_atributo/modificar/3/', {'Nombre_tipo_atributo': 'Foto Adjunta', 'Tipo_de_dato': 'Imagen', 'Precision': 0, 'Longitud': 0, 'Obligatorio':'N', 'Descripcion': 'Para publicidades de terceros'})
        request.user = self.user
        response = modificarTipoAtributo(request, 2, 3)
        self.assertEqual(response.status_code, 200)
        print 'Test de Modificar Tipo de Atributo ejecutado exitosamente'
        
    def testEliminarTipoAtributo(self):
        
        self.user = User.objects.get(pk=1)
        request = self.factory.get('/adm_proyectos/gestionar/1/adm_tipos_atributo/eliminar/6/')
        request.user = self.user
        tipoAtributo = TipoAtributo.objects.get(pk=6)
        self.assertTrue(tipoAtributo.is_active)
        response = eliminarTipoAtributo(request, 1, 6)
        tipoAtributo = TipoAtributo.objects.get(pk=6)
        self.assertFalse(tipoAtributo.is_active)
        print 'Test de Eliminar Tipo de Atributo ejecutado exitosamente'
        
    def testConsultarTipoAtributo(self):
        
        self.user = User.objects.get(pk=1)
        request = self.factory.get('adm_proyectos/gestionar/1/adm_tipos_atributo/consultar/1/')
        request.user = self.user
        response = consultarTipoAtributo(request, 1, 1)
        self.assertEqual(response.status_code, 200)
        print 'Test de Consultar un Tipo de Atributo ejecutado exitosamente'
    
    def testBucarTipoAtributo(self):
        
        self.user = User.objects.get(pk=1)
        request = self.factory.get('/adm_proyectos/gestionar/1/adm_tipos_atributo/', {'busqueda': 'Foto'})
        request.user = self.user
        response = administrarTipoAtributo(request, 1)
        self.assertEqual(response.status_code, 200)
        print 'Test Buscar Tipo de Atributo ejecutado exitosamente'
        
    def testImportarTipoAtributo(self):
        
        self.user = User.objects.get(pk=1)
        request = self.factory.get('adm_proyectos/gestionar/2/adm_tipos_atributo/listar_proyectos/listar_tipo_atributo/1/importar_tipo_atributo/1/')
        request.user = self.user
        response = importarTipoAtributo(request, 2, 1, 1)
        self.assertEqual(response.status_code, 200)
        print 'Test Importar Tipo de Atributo ejecutado exitosamente'
    

    if __name__ == '__main__':
        unittest.main()
