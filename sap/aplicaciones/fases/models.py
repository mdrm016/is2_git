from django.db import models
from aplicaciones.proyectos.models import Proyectos

# Create your models here.

class Fases(models.Model):
    
    nombre = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=300)
    estado = models.CharField(max_length=2)
    fechainicio = models.DateField()
    duracion = models.IntegerField()
    proyecto = models.ForeignKey(Proyectos)
    is_active = models.BooleanField(default=True)
    
    def __unicode__ (self):
        return self.nombre