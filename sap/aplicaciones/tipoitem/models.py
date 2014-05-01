from django.db import models
from aplicaciones.tipoatributo.models import TipoAtributo

class ListaAtributo (models.Model):
    
    """ El modelo ListaAtributo describe la estructura de la tabla utilizada para almacenar
    los tipos de atributos seleccionados por el usuario para un tipo de item dado.
    Los campos que contien el modelo son:
    id_atributo: Campo que contendra el id del tipo de atributo seleccionado.
    id_tipoitem: Campo que contendra el id del tipo de item al cual pertenece el tipo de atributo.
    orden: Campo que contiene el orden de manera ascendente del tipo de atributo en un tipo de item dado.
    nombre: Campo que contiene el nombre del tipo de atributo.
    is_active: Campo logico que indica si el tipo de atributo ha sido borrado o no del tipo de item.
    
    @author: Marcelo Denis
    """
    
    id_atributo = models.IntegerField()
    id_tipoitem = models.IntegerField()
    orden = models.IntegerField()
    nombre = models.CharField(max_length=20)
    is_active = models.BooleanField(default=True)
    
    def __unicode__ (self):
        return self.nombre

class TipoItem (models.Model):
    
    """ El modelo TipoItem describe la estructura de cada instancia de un Tipo de Item, los campos
    que contiene el modelo son: 
    nombre: campo de tipo texto que contendra el nombre del Tipo de Item.
    descripcion: campo de tipo texto que contendra una breve descripcion del Tipo de Item.
    id_proyecto: campo que contendra el id del proyecto al cual pertenece el tipo de item.
    is_active: campo de tipo logico que indicara si el Tipo de Item esta eliminado.
    listaAtributo: campo que listara la serie de atributos de los que esta compuesto el Tipo de Item.
    Los Tipos de Item seran ordenados en la tabla por nombre.
    
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