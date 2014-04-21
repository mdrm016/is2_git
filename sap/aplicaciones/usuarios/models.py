from django.db import models

# Create your models here.

from django.contrib.auth.models import User, Permission
from django.db.models.signals import post_save

class Usuarios(models.Model):
    """ La clase Usuarios crea un perfil a cada instancia de la clase
         User, con los atributos descritos en este modelo.
         Contiene como atributo los campos: telefono, direccion,
         especialidad, observaciones, id_user, este ultimo representa la 
         clave foranea de la clase User, de esa manera para cada
         User existe un unico perfil, y para cada perfil un unico User.
    
    @author: Ysapy Ortiz
    """  
    
    user = models.OneToOneField(User)
    telefono = models.CharField(max_length=30)
    direccion = models.CharField(max_length=50)
    especialidad = models.CharField(max_length=50)
    observaciones = models.TextField(max_length=300)
    
    class Meta:
        permissions = (
                       ("administrar_usuario", "puede listar usuarios"),
        )
    
    def __unicode__(self):
        return self.user.username
    
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Usuarios.objects.create(user=instance)
            
    post_save.connect(create_user_profile, sender=User)
    