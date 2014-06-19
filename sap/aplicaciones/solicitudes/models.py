from django.db import models
from aplicaciones.proyectos.models import Proyectos
from aplicaciones.fases.models import Fases
from aplicaciones.items.models import Items
from aplicaciones.usuarios.models import Usuarios
from django.contrib.auth.models import User

# Create your models here.

class Solicitudes(models.Model):
    
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
    miembros_que_votaron = models.ManyToManyField(User, through='Votos')

    def __unicode__(self):
        return self.nombre

class Credenciales(models.Model):
    
    nombre = models.CharField(max_length=30, null=True)
    usuario = models.ForeignKey(Usuarios)
    proyecto = models.ForeignKey(Proyectos)
    fase = models.ForeignKey(Fases)
    item = models.ForeignKey(Items)
    version = models.IntegerField(null=True)
    fecha_aprobacion = models.DateField(null=True)
    fecha_expiracion = models.DateField(null=True)
    estado = models.CharField(null=True, max_length=50)
    observaciones = models.CharField(null=True, max_length=500)
    
    def __unicode__(self):
        return self.nombre
class Votos(models.Model):
    """ El modelo Votos contiene los votos de cada miembro del comite del proyecto
    al que pertenece ese comite y la solicitud, tambien se registra la fecha en la que
    se realizo la votacion
    miembro: id del usuario miembro del comite de cambio del proyecto
    solicitud: id de la solicitud a votar
    fechaDeVotacion: registra la fecha en la que fue votada la solicitud por el miembro de comite
    voto: campo que indica si la solicitud fue aprobada o no por el miembro de comite
    """
    miembro = models.ForeignKey(User)
    solicitud = models.ForeignKey(Solicitudes)
    fechaDeVotacion = models.DateField()
    voto = models.CharField(max_length=2)

    def __unicode__(self):
        return self.voto

