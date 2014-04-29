from django.db import models
from aplicaciones.tipoatributo.models import TipoAtributo

class ListaAtributo (models.Model):
    id_atributo = models.IntegerField()
    id_tipoitem = models.IntegerField()
    orden = models.IntegerField()
    nombre = models.CharField(max_length=20)
    is_active = models.BooleanField(default=True)
    
    def __unicode__ (self):
        return self.nombre

class TipoItem (models.Model):
    
    """ El modelo Proyectos describe la estructura de cada instancia de un Tipo de Item, los campos
    que contiene el modelo son: 
    nombre: campo de tipo texto que contendra el nombre del Tipo de Item.
    descripcion: campo de tipo texto que contendra una breve descripcion del Tipo de Item.
    is_active: campo de tipo logico que indicara si el Tipo de Item esta eliminado.
    tipoAtributo: campo que listara la serie de atributos de los que esta compuesto el Tipo de Item.
    Los Tipo de Item seran ordenados en la tabla por nombre.
    
    @author: Marcelo Denis
    """
    
    nombre = models.CharField(max_length=30, null=True)
    descripcion = models.TextField(max_length=300)
    id_proyecto = models.IntegerField()
    is_active = models.BooleanField(default=True)
    listaAtributo = models.ManyToManyField(ListaAtributo)

    def __unicode__ (self):
        return self.nombre
    
    class Meta:
        ordering = ["nombre"]