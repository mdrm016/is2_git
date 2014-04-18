from django.db import models
from django.contrib.auth.models import User
from aplicaciones.usuarios.models import Usuarios

class Proyectos(models.Model):
    ESTADOS_PROYECTO=(
        ('Inactivo', 'Inactivo'),
        ('En Construccion', 'En Construccion'),
        ('Finalizado', 'Finalizado'),
    )
    
    nombre = models.CharField(max_length=30, unique=True)
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