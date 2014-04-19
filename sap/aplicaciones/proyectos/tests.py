from django.test import TestCase

def setUp(self):
        """ Inicializamos la variable factory que posteriormente nos permitira cargar
            un request para utilizarlo en las vista.
        """
        self.factory = RequestFactory()
        
def test_adm_proyectos (self):
    resp = self.client.get('/adm_proyectos/')                                           #Solicitud de la pagina de autenticacion
    self.assertEqual(resp.status_code, 200)