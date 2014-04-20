from django.db import models
from aplicaciones.proyectos.models import Proyectos

# Create your models here.

class Fases(models.Model):
    
    nombre = models.CharField(max_length=20, null=True)
    nombre_eliminado=models.CharField(max_length=20, null = True)
    descripcion = models.CharField(max_length=300, null=True)
    estado = models.CharField(max_length=2, null=True)
    fechainicio = models.DateField(null=True)
    duracion = models.IntegerField(null=True)
    proyecto = models.ForeignKey(Proyectos)
    is_active = models.BooleanField(default=True)
    
    def __unicode__ (self):
        return self.nombre