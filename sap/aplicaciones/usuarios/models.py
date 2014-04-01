from django.db import models

# Create your models here.

from django.contrib.auth.models import User

class Usuarios(models.Model):
    
    user = models.OneToOneField(User)
    telefono = models.CharField(max_length=30)
    direccion = models.CharField(max_length=50)
    especialidad = models.CharField(max_length=50)
    observaciones = models.TextField(max_length=300)
    
    def __unicode__(self):
        return self.user.username