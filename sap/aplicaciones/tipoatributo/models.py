from django.db import models
from aplicaciones.proyectos.models import Proyectos

# Create your models here.
class TipoAtributo(models.Model):
    """ La clase TipoAtributo crea instancias para los tipos de atributo
        , con los atributos descritos en este modelo.
        Contiene como atributo los campos: nombre, tipo_de_dato (que pueden ser:
        Numerico, Fecha, Texto, Logico, Archivo Externo o Imagen), Precision,
        Longitud, descripcion, id_TipoDato, este ultimo representa la 
        clave foranea de las distintas clases definidas para cada tipo de dato,
        de esa manera para tipo de dato en el tipo de atributo, existe una clase
        que almacenara los datos de ese tipo de dato.
         
    @author: Eduardo Gimenez
    """  
    TIPOS_DATOS = (
                   ('Numerico', 'Numerico'),
                   ('Fecha', 'Fecha'),
                   ('Logico', 'Logico'),
                   ('Texto', 'Texto'),
                   ('Archivo Externo', 'Archivo Externo'),
                   ('Imagen', 'Imagen'),)
    nombre = models.CharField(max_length=20, unique=True)
    tipo = models.CharField(max_length=16, choices=TIPOS_DATOS)
    precision = models.IntegerField(max_length=2)
    longitud = models.IntegerField(max_length=2)
    obligatorio = models.BooleanField(default=False)
    proyecto = models.ManyToManyField(Proyectos)
    descripcion = models.TextField(max_length=300)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['nombre']
        permissions = (
                      ("administrar_tipos_de_atributo", "puede listar los roles"),
                      ("importar_tipo_de_atributo", "puede asignar un rol a un usuario"),
        )
    
    def __unicode__(self):
        return u'%s' % (self.nombre)
    
class Numerico(models.Model):
    """
    La clase Numerico almacenara los valores para tipos de datos "Numerico"
    en el tipo de atributo
    
    @author: Eduardo Gimenez
    """
    valor = models.DecimalField(max_digits=30, decimal_places=10)
    id_item = models.IntegerField()
    nombre_atributo = models.CharField(max_length=20)
    precision = models.IntegerField()
    longitud = models.IntegerField()
    obligatorio = models.BooleanField(default=False)
    
class Fecha(models.Model):
    """
    La clase Fecha almacenara los valores para tipos de datos "Fecha"
    en el tipo de atributo
    
    @author: Eduardo Gimenez
    """
    valor = models.DateField()
    id_item = models.IntegerField()
    nombre_atributo = models.CharField(max_length=20)
    obligatorio = models.BooleanField(default=False)

class Texto(models.Model):
    """
    La clase Texto almacenara los valores para tipos de datos "Texto"
    en el tipo de atributo
    
    @author: Eduardo Gimenez
    """
    valor = models.CharField(max_length=300)
    id_item = models.IntegerField()
    nombre_atributo = models.CharField(max_length=20)
    longitud = models.IntegerField()
    obligatorio = models.BooleanField(default=False)
    
class Logico(models.Model):
    """
    La clase Logico almacenara los valores para tipos de datos "Logico"
    en el tipo de atributo
    
    @author: Eduardo Gimenez
    """
    valor = models.BooleanField()
    id_item = models.IntegerField()
    nombre_atributo = models.CharField(max_length=20)
    obligatorio = models.BooleanField(default=False)

class ArchivoExterno(models.Model):
    """
    La clase ArchivoExterno almacenara los valores para tipos de datos "Archivo Externo"
    en el tipo de atributo
    
    @author: Eduardo Gimenez
    """
    valor = models.FileField(upload_to='archivos', blank=True)
    id_item = models.IntegerField()
    nombre_atributo = models.CharField(max_length=20)
    obligatorio = models.BooleanField(default=False)
    
class Imagen(models.Model):
    """
    La clase Imagen almacenara los valores para tipos de datos "Imagen"
    en el tipo de atributo
    
    @author: Eduardo Gimenez
    """
    valor = models.ImageField(upload_to='imagenes', blank=True)
    id_item = models.IntegerField()
    nombre_atributo = models.CharField(max_length=20)
    obligatorio = models.BooleanField(default=False)



