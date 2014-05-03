from django.db import models
from aplicaciones.proyectos.models import Proyectos
from aplicaciones.fases.models import Fases
from aplicaciones.items.models import Items

# Create your models here.

class Relaciones(models.Model):
    nombre = models.CharField(max_length=30, null=True)
    padre_id = models.IntegerField(null=True)
    antecesor_id = models.IntegerField(null=True)
    sucesor_id = models.IntegerField(null=True)
    hijo_id = models.IntegerField(null=True)
    is_active = models.BooleanField(default=True)
    proyecto = models.IntegerField(null=True)
    faseprimera = models.IntegerField(null=True)
    fasesegunda = models.IntegerField(null=True)
    versionprimero = models.IntegerField(null=True)
    versionsegundo = models.IntegerField(null=True)
    
    def __unicode__(self):
        return self.snombre

class ListaRelaciones(models.Model):
    nombre = models.CharField(max_length=30, null=True)
    itemrelacionado = models.IntegerField(null=True)
    nombreitemrelacionado = models.CharField(max_length=30, null=True)
    tiporelacion = models.CharField(max_length=30, null=True)
    relacionid = models.IntegerField(null=True)
    
    def __unicode__(self):
        return self.nombre