from django.test import TestCase
from django.contrib.auth.models import User 
from django.test.client import RequestFactory
from aplicaciones.roles.views import administrarRoles, rolNuevo, modificarRol
from aplicaciones.roles.views import eliminarRol, consultarRol, asignarRol, desasignarRol
from aplicaciones.roles.models import Roles

# Create your tests here.
class test_user(TestCase):
    """    Cargamos los usuarios y roles de prueba en la base de datos    """
    fixtures = ['roles.json'] + ['auth_group.json'] + ['users.json']
    
    def setUp(self):
        """ Inicializamos la variable factory que posteriormente nos permitira cargar
            un request para utilizarlo en las visata.
        """
        self.factory = RequestFactory()
        
    def testAdministrarRoles(self):
        
        self.user = User.objects.get(pk=1)  
        request = self.factory.get('/adm_roles/')
        request.user = self.user
        response = administrarRoles(request)                                    #Pasamos a la pagina de administracion de roles
        self.assertEqual(response.status_code, 200) 
        print 'Test de administracion de Roles ejecutado exitosamente.'
    
    def testRolNuevo(self):
        
        self.user = User.objects.get(pk=1) 
        request = self.factory.post('/adm_roles/nuevo/', {'Nombre_de_Rol': 'pruebaRol3','Permisos':['administrar_roles', 'administrar_usuario'], 'Proyecto': '', 'Descripcion':'Listar Usuarios y Roles' })
        request.user = self.user 
        response = rolNuevo(request) 
        self.assertEqual(response.status_code, 200)
        rol = Roles.objects.get(name='pruebaRol3')
        print rol.permissions.all()
        
        print 'Test de Crear un Rol Nuevo ejecutado exitosamente.'
        
        
    def testModificarRol(self):
        
        self.user = User.objects.get(pk=1)
        print Roles.objects.all()
        request = self.factory.post('/adm_roles/modificar/2/', {'Nombre_de_Rol': 'pruebaRol3', 'Permisos': ['crear_usuarios'], 'Descripcion':'Agregamos crear usuarios'})
        request.user = self.user
        response = modificarRol(request, 2)
        print response.status_code
        self.assertEqual(response.status_code, 200)
        rol = Roles.objects.get(name='pruebaRol3')
        print rol
        print Roles.objects.all()
        print 'Test de Modificar Rol ejecutado exitosamente.'
    
    def testEliminarRol(self):
        
        self.user = User.objects.get(pk=1)
        request = self.factory.get('/adm_roles/eliminar/1/')
        request.user = self.user
        rol = Roles.objects.get(pk=1)
        self.assertTrue(rol.is_active)
        response = eliminarRol(request, 1)
        rol = Roles.objects.get(pk=1)
        self.assertFalse(rol.is_active)
        print 'Test de Eliminar Rol ejecutado exitosamente.'
        
    def testConsultarRol(self):
        
        self.user = User.objects.get(pk=1)
        request = self.factory.get('/adm_roles/consultar/2/')
        request.user = self.user
        response = consultarRol(request, 2)
        self.assertEqual(response.status_code, 200)
        print 'Test de Consultar un Rol ejecutado exitosamente.'
        
    def testBucarRol(self):
        
        self.user = User.objects.get(pk=1)
        request = self.factory.get('/adm_roles/', {'busqueda': 'rolPrueba'})
        request.user = self.user
        response = administrarRoles(request)
        self.assertEqual(response.status_code, 200)
        print 'Test de Buscar Rol ejecutado exitosamente.'
        
    def testAsignarRol(self):
        
        self.user = User.objects.get(pk=1)
        request = self.factory.get('/adm_roles/asignar/2/', {'Usuario': 'ysapy'})
        request.user = self.user
        response = asignarRol(request, 2)
        self.assertEqual(response.status_code, 200)
        print 'Test de Asignar Rol a Usuario ejecutado exitosamente.'
        
    def testDesasignarRol(self):
        
        self.user = User.objects.get(pk=1)
        request = self.factory.get('/adm_roles/desasignar/2/', {'Usuario': 'ysapy'})
        request.user = self.user
        response = desasignarRol(request, 2)
        self.assertEqual(response.status_code, 200)
        print 'Test de Desasignar Rol a usuario ejecutado exitosamente.'
    
    if __name__ == '__main__':
        unittest.main()