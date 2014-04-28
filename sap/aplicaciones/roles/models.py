from django.db import models

# Create your models here.
from django.contrib.auth.models import Group

class Roles(Group):
    """ La clase Roles crea un perfil a cada instancia de la clase
         Group, con los atributos descritos en este modelo.
         Contiene como atributo los campos: proyecto (Clave foranea 
         de la clase Proyectos), descripcion, rol, este ultimo representa la 
         clave foranea de la clase Group, de esa manera para cada
         Rol existe un unico odjeto Group, y para cada Group un unico Rol.
         
    
    @author: eduardo gimenez
    """  
    
    proyecto = models.CharField(max_length=30)
    descripcion = models.TextField(max_length=300)
    is_active = models.BooleanField(default=True)
    objects = models.Manager()
    
    class Meta:
        ordering = ['name']
        permissions = (
                      ("crear_roles", "puede crear roles"),
                      ("modificar_roles", "puede modificar roles"),
                      ("eliminar_roles", "puede eliminar roles"),
                      ("administrar_roles", "puede listar los roles"),
                      ("asignar_rol", "puede asignar un rol a un usuario"),
                      ("desasignar_rol", "puede desasignar un rol de un usuario"),
        )
    
    def __unicode__(self):
        return u'%s' % (self.name)
    
    