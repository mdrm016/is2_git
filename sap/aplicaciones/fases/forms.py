from django import forms
from django.forms.extras.widgets import Select
from .models import Fases

from django.forms import ModelForm
from django.core import validators
from django.core.exceptions import ValidationError

def validar_fasenombre_unico(value):
    if Fases.objects.filter(nombre=value, is_active=True).exists():
        raise ValidationError(u'El nombre de fase ya existe')
    
def validate_duracion_fase (value):
    if value < 1:
        raise ValidationError(u'Ingrese una duracion valida')
    
ESTADOS_FASE=(
        ('', '--seleccione un Estado--'),
        ('DF', 'Definicion'),
        ('DR', 'Desarrollo'),
        ('FD', 'Finalizado'),
    )

ESTADOS_FASE_ACTIVO=(
        ('', '--seleccione un Estado--'),
        ('DF', 'Definicion'),
        ('DR', 'Desarrollo'),
        ('FD', 'Finalizado'),
    )


class FaseNuevaForm(forms.Form):
#, validators=[validar_fasenombre_unico]
    """ Atributos de Fase necesarios para el registro en la base de datos
    enviados al template html encargado de tomar los datos de registro.
    Control de datos ingresados por el usuario.
        
    @type forms.Form: django.forms
    @param forms.Form: Heredamos la clase forms.Form para hacer uso de sus funcionalidades en el formulario de registro
    @author: Ysapy Ortiz
        
    """

    Nombre_de_Fase = forms.CharField(widget=forms.TextInput(), max_length=20, required=True, error_messages={'required':'Ingrese un nombre de fase', 'max_length':'Longitud maxima 20'})
    Descripcion = forms.CharField(widget=forms.TextInput(), required=True, max_length=300, error_messages={'required':'Ingrese una descripcion para la fase', 'max_length':'Longitud maxima 300'})
   # Estado = forms.ChoiceField(widget=Select, choice=ESTADOS_CREAR, required=True)
    Duracion_semanas = forms.IntegerField(required=True, error_messages={'required':'Ingrese una duracion estimada en semanas'})
    
class FaseModificadaForm(forms.Form):
#, validators=[validar_fasenombre_unico]

    """ Atributos de fase necesarios para la modificacion en la base de datos
    de una fase. Este formulario con los campos descritos son 
    enviados al template html encargado de desplegar los datos de la fase a modificar.
    
    Control de datos ingresados por el usuario.
        
    @type forms.Form: django.forms
    @param forms.Form: Heredamos la clase forms.Form para hacer uso de sus funcionalidades en el formulario de registro
    @author: Ysapy Ortiz
    
    """
    Nombre_de_Fase = forms.CharField(widget=forms.TextInput(), max_length=20, required=True, error_messages={'required': 'Ingrese un nombre de fase', 'max_length': 'Longitud maxima: 20'})
    Descripcion = forms.CharField(widget=forms.TextInput(), required=False, max_length=300, error_messages={'required': 'Ingrese una descripcion para la fase', 'max_length': 'Longitud maxima 300'})
    Estado = forms.ChoiceField(widget=forms.Select(), choices= (ESTADOS_FASE), required=False)
    Duracion = forms.IntegerField(required=True, help_text='En semanas', validators=[validate_duracion_fase], error_messages={'required': 'Ingrese una duracion aproximada de fase',})    
    
class FaseModificadaFormProyectoActivo(forms.Form):
    Estado = forms.ChoiceField(widget=forms.Select(), choices= (ESTADOS_FASE_ACTIVO), required=False)
    Duracion = forms.IntegerField(required=True, help_text='En semanas', validators=[validate_duracion_fase], error_messages={'required': 'Ingrese una duracion aproximada de fase',})
