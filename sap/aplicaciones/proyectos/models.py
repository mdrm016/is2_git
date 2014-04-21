from django.db import models
from django.contrib.auth.models import User
from aplicaciones.usuarios.models import Usuarios

class Proyectos(models.Model):
    
    """ El modelo Proyectos describe la estructura de cada instancia de un proyecto, los campos
    que contiene el modelo son: 
    nombre: campo de tipo texto que contendra el nombre del proyecto.
    lider: campo que contendra una clave foranea a la tabla user, donde solo un usuario pude ser lider
    de un proyecto.
    estado: campo de tipo texto que contendra uno de los siguientes estado de proyecto: Inactivo, En construccion, Finalizado.
    fecha_inicio: Campo de tipo fecha que contendra la fecha de inicio del proyecto.
    duracion: campo de tipo numerico que contendra la duracion de proyecto en semanas.
    is_active: campo de tipo logico que indicara si el proyecto esta eliminado.
    miembros: campo que contendra la lista de miembros que trabajan en un proyecto. Es un muchos a muchos con la tabla Usuarios.
    Los proyectos seran ordenados en la tabla por nombre.
    
    @author: Marcelo Denis
    """
    ESTADOS_PROYECTO=(
        ('Inactivo', 'Inactivo'),
        ('En Construccion', 'En Construccion'),
        ('Finalizado', 'Finalizado'),
    )
    
    nombre = models.CharField(max_length=30)
    lider = models.ForeignKey(User)
    estado = models.CharField(max_length=15, choices=ESTADOS_PROYECTO, default='Inactivo')
    fecha_inicio = models.DateField()
    duracion = models.IntegerField()
    is_active = models.BooleanField(default=True)
    miembros = models.ManyToManyField(Usuarios, null=True,blank=True)
    
    def __unicode__ (self):
        return self.nombre

    class Meta:
        ordering = ["nombre"]
        permissions = (
                      ("listar_miembros", "puede listar los miembros de un proyecto"),
                      ("importar_proyecto", "puede importar proyectos"),
                      )