from django.db import models
from aplicaciones.proyectos.models import Proyectos
from aplicaciones.fases.models import Fases
from aplicaciones.items.models import Items
from aplicaciones.usuarios.models import Usuarios
#from aplicaciones.lineabase.models import LineaBase

# Create your models here.

class Solicitud(models.Model):
    
    """ El modelo Solicitud describe la estructura de cada instancia de una fase, los campos
    que contiene el modelo son: 
    nombre: campo de tipo texto que contendra el nombre de la fase.
    estado: campo de tipo texto que contendra uno de los siguientes estado de fase: Definicion, Desarrollo, Finalizado.
    fecha_inicio: Campo de tipo fecha que contendra la fecha de inicio de la fase.
    duracion: campo de tipo numerico que contendra la duracion de la fase en semanas.
    is_active: campo de tipo logico que indicara si la fase esta eliminada.
    Las fases seran ordenadas en la tabla por nombre.
    
    @author: Ysapy Ortiz
    """
    
    nombre = models.CharField(max_length=30, null=True)
    usuario = models.ForeignKey(Usuarios)
    proyecto = models.ForeignKey(Proyectos)
    fase = models.ForeignKey(Fases)
    item = models.ForeignKey(Items)
    fecha_solicitud = models.DateField(null=True)
    tiempo_solicitado = models.IntegerField(null=True)
    descripcion = models.CharField(null=True, max_length=500)
    observaciones = models.CharField(null=True, max_length=500)
    estado = models.CharField(null=True, max_length=50)
    tiempo_esperado = models.IntegerField(null=True)

    def __unicode__(self):
        return self.nombre
