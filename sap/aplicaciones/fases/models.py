from django.db import models
from aplicaciones.proyectos.models import Proyectos

# Create your models here.

class Fases(models.Model):
    
    """ El modelo Fases describe la estructura de cada instancia de una fase, los campos
    que contiene el modelo son: 
    nombre: campo de tipo texto que contendra el nombre de la fase.
    estado: campo de tipo texto que contendra uno de los siguientes estado de fase: Definicion, Desarrollo, Finalizado.
    fecha_inicio: Campo de tipo fecha que contendra la fecha de inicio de la fase.
    duracion: campo de tipo numerico que contendra la duracion de la fase en semanas.
    is_active: campo de tipo logico que indicara si la fase esta eliminada.
    Las fases seran ordenadas en la tabla por nombre.
    
    @author: Ysapy Ortiz
    """
    
    nombre = models.CharField(max_length=20, null=True)
    nombre_eliminado=models.CharField(max_length=20, null = True)
    descripcion = models.CharField(max_length=300, null=True)
    estado = models.CharField(max_length=2, null=True)
    fechainicio = models.DateField(null=True)
    duracion = models.IntegerField(null=True)
    proyecto = models.ForeignKey(Proyectos)
    is_active = models.BooleanField(default=True)
    orden = models.IntegerField(null=True)
    
    class Meta:
        permissions = (
                      ("administrar_fases", "puede listar las Fases"),
                      ("importar_fase", "puede importar fases"),
                      )
    
    def __unicode__ (self):
        return self.nombre
