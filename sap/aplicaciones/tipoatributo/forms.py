from django import forms
from aplicaciones.tipoatributo.models import TipoAtributo
from django.core import validators
from django.core.exceptions import ValidationError

def validarNombreUnico(value):
    if TipoAtributo.objects.filter(nombre=value).exists():
        raise ValidationError(u'El nombre del Tipo de Atributo ya existe')
    
class TipoAtributoForm (forms.Form):
    
    """ Campos del Tipo de atributo necesarios para el registro en la base de datos
        de un nuevo Tipo de atributo. Este formulario con los campos descritos son 
        enviados al template html encargado de tomar los datos de registro.
        Control de datos ingresados por el usuario.
        
        @type forms.Form: django.forms
        @param forms.Form: Heredamos la clase forms.Form para hacer uso de sus funcionalidades en el formulario de registro
        @author: Eduardo Gimenez
        
    """
    TIPOS_DATOS = (
                   ('Numerico', 'Numerico'),
                   ('Fecha', 'Fecha'),
                   ('Logico', 'Logico'),
                   ('Texto', 'Texto'),
                   ('Archivo Externo', 'Archivo Externo'),
                   ('Imagen', 'Imagen'),)
    OBLIG = (('S', 'si'), ('N', 'no'))
    Nombre_tipo_atributo = forms.CharField(widget=forms.TextInput(), validators=[validarNombreUnico], max_length=20, required=True, error_messages={'required': 'Ingrese un nombre para el tipo de atributo', 'max_length': 'Longitud maxima: 20 caracteres'})
    Tipo_de_dato = forms.ChoiceField(required=True, widget=forms.Select(), choices=TIPOS_DATOS, error_messages={'required': 'Debe escoger por lo menos  un Tipo de dato'})
    Precision = forms.IntegerField(max_value=10, min_value=0, error_messages={'max_value': 'Valor maximo: 10'})
    Longitud = forms.IntegerField(max_value=30 ,min_value=0, error_messages={'max_length': 'Valor maximo: 30'})
    Obligatorio = forms.ChoiceField(choices=OBLIG)
    Descripcion = forms.CharField(widget=forms.Textarea(), required=False, max_length= 300, error_messages={'max_length': 'Longitud maxima: 300 caracteres'})
    
   
class TipoAtributoModificadoForm (forms.Form):
    
    """ Campos del Tipo de atributo necesarios para el registro en la base de datos
        de los datos modificados de un Tipo de atributo. Este formulario con los campos descritos son 
        enviados al template html encargado de tomar los datos de registro.
        Control de datos ingresados por el usuario.
        
        @type forms.Form: django.forms
        @param forms.Form: Heredamos la clase forms.Form para hacer uso de sus funcionalidades en el formulario de registro
        @author: Eduardo Gimenez
        
    """
    TIPOS_DATOS = (
                   ('Numerico', 'Numerico'),
                   ('Fecha', 'Fecha'),
                   ('Logico', 'Logico'),
                   ('Texto', 'Texto'),
                   ('Archivo Externo', 'Archivo Externo'),
                   ('Imagen', 'Imagen'),)
    OBLIG = (('S', 'si'), ('N', 'no'))
    Nombre_tipo_atributo = forms.CharField(widget=forms.TextInput(), max_length=20, required=True, error_messages={'required': 'Ingrese un nombre para el tipo de atributo', 'max_length': 'Longitud maxima: 20 caracteres'})
    Tipo_de_dato = forms.ChoiceField(required=True, widget=forms.Select(), choices=TIPOS_DATOS, error_messages={'required': 'Debe escoger por lo menos  un Tipo de dato'})
    Precision = forms.IntegerField(max_value=10, min_value=0, error_messages={'max_value': 'Valor maximo: 10'})
    Longitud = forms.IntegerField(max_value=30 ,min_value=0, error_messages={'max_length': 'Valor maximo: 30'})
    Obligatorio = forms.ChoiceField(choices=OBLIG)
    Descripcion = forms.CharField(widget=forms.Textarea(), required=False, max_length= 300, error_messages={'max_length': 'Longitud maxima: 300 caracteres'})
    
        
