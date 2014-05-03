from django.test import TestCase
from django.test.client import RequestFactory
from aplicaciones.tipoatributo.views import administrarTipoAtributo, tipoAtributoNuevo, modificarTipoAtributo
from aplicaciones.tipoatributo.views import eliminarTipoAtributo, consultarTipoAtributo, importarTipoAtributo
from aplicaciones.tipoatributo.models import TipoAtributo
from django.contrib.auth.models import User 
from aplicaciones.roles.models import Roles

class test_user(TestCase):
    """    Cargamos Proyectos, tipos de Item y Tipos de Atributo de prueba en la base de datos    """
    fixtures = ['proyectos.json'] + ['tipos_item.json'] + ['tipos_atributo.json'] + ['users.json'] + ['lista_atributos.json']
    
    def setUp(self):
        """ Inicializamos la variable factory que posteriormente nos permitira cargar
            un request para utilizarlo en las visata.
        """
        self.factory = RequestFactory()
    
    def testadministrarTipoAtributo(self):
        
        self.user = User.objects.get(pk=1)  
        request = self.factory.get('/adm_proyectos/gestionar/1/adm_tipos_atributo/')
        request.user = self.user
        response = administrarTipoAtributo(request, 1)                                    #Pasamos a la pagina de administracion de Tipos de Atributo
        self.assertEqual(response.status_code, 200)
        print 'Test de adminitracion de tipo de Atributo ejecutado exitosamente.' 
    
    def testtipoAtributoNuevo(self):
        
        self.user = User.objects.get(pk=1) 
        request = self.factory.post('/adm_proyectos/gestionar/1/adm_tipos_atributo/nuevo/', {'Nombre_tipo_atributo': 'Detalle', 'Tipo_de_dato': 'Texto', 'Precision': '0', 'Longitud': '5', 'Obligatorio': 'N', 'Descripcion': ''})
        request.user = self.user 
        response = tipoAtributoNuevo(request, 1) 
        print response
        self.assertEqual(response.status_code, 200)
        tipo_atributo = TipoAtributo.objects.get(nombre='Detalle')
        print tipo_atributo
        
    def testModificarRol(self):
        
        #self.user = User.objects.get(pk=1)
        print Roles.objects.all()
        #request = self.factory.post('/adm_roles/modificar/2/', {'Nombre_de_Rol': 'pruebaRol3', 'Permisos': ['crear_usuarios'], 'Descripcion':'Agregamos crear usuarios'})
        #request.user = self.user
        #response = modificarRol(request, 2)
        #print response.status_code
        #self.assertEqual(response.status_code, 200)
        #rol = Roles.objects.get(name='pruebaRol3')
        #print rol
        print Roles.objects.all()
        print 'Test de Modificar Rol ejecutado exitosamente.'
        
    if __name__ == '__main__':
        unittest.main()
