from django.db import models
from aplicaciones.proyectos.models import Proyectos
from aplicaciones.fases.models import Fases
from aplicaciones.items.models import Items

# Create your models here.

class LineaBase(models.Model):
    """ El modelo LineaBase describe la estructura de cada instancia de una Linea Base, los campos
    que contiene el modelo son: 
    numero: campo que contendra un numero identificador para cada linea base en una Fase, la numeracion sera independiente entre Fases
    proyecto: campo que contendra una Clave Foranea a la tabla proyectos, en donde una Linea Base pertenece solo a un Proyecto
    fase: Campo que contendra una Clave Foranea a la tabla fases, en donde una Linea Base pertenece a una solo fase
    items: campo que contendra un conjunto de calves relacionadas con la tabla items, un item pertenece solo a una linea base
    descripcion: campo en el que se detalla algunos aspectos no tan relevantes de la Linea Base
    is_active: campo que define si una linea base esta o no activa.
    Las Lineas Base seran ordenadas en la tabla por id.
    
    @author: Eduardo Gimenez
    """
    numero = models.IntegerField()
    proyecto = models.ForeignKey(Proyectos)
    fase = models.ForeignKey(Fases)
    items = models.ManyToManyField(Items)
    is_active = models.BooleanField(default=True)
    descripcion = models.CharField(max_length=300)
    fecha_creacion = models.DateField()
    
    class Meta:
        ordering = ['id']
        permissions = (
                      ("administrar_lineas_base", "puede listar las Lineas Base"),
                      ("generar_linea_base", "puede generar Linea Base"),
                      ("generar_informe_linea_base", "puede generar informe de Linea Base"),
        )
    
    def __unicode__(self):
        return u'%s' % (self.numero)