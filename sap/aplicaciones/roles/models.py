from django.db import models

# Create your models here.
from django.contrib.auth.models import Group

class Roles(models.Model):
    """ La clase Roles crea un perfil a cada instancia de la clase
         Group, con los atributos descritos en este modelo.
         Contiene como atributo los campos: proyecto (Clave foranea 
         de la clase Proyectos), descripcion, rol, este ultimo representa la 
         clave foranea de la clase Group, de esa manera para cada
         Rol existe un unico odjeto Group, y para cada Group un unico Rol.
         
    
    @author: eduardo gimenez
    """  
    rol = models.OneToOneField(Group)
    proyecto = models.CharField(max_length=10)
    descripcion = models.TextField(max_length=300)
    
    class Meta:
        permissions = (
                      ("administrar_roles", "puede listar los roles"),
                      ("asignar_rol", "puede asignar un rol a un usuario"),
                      ("desasignar_rol", "puede desasignar un rol de un usuario"),
        )
    
    def __unicode__(self):
        return self.rol.name
    
    