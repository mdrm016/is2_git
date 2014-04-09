from django.db import models

# Create your models here.

from django.contrib.auth.models import User

User.add_to_class('telefono', models.CharField(max_length=30))
User.add_to_class('direccion', models.CharField(max_length=100))
User.add_to_class('especialidad', models.CharField(max_length=50))
User.add_to_class('observaciones', models.CharField(max_length=300))

"""class Usuarios(models.Model):
    
    user = models.OneToOneField(User)
    telefono = models.CharField(max_length=30)
    direccion = models.CharField(max_length=50)
    especialidad = models.CharField(max_length=50)
    observaciones = models.TextField(max_length=300)"""
    
    #def __unicode__(self):
     #   return self.user.username