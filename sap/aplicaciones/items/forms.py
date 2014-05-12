from django import forms
from django.forms.extras.widgets import Select
from .models import Items
from django.forms import ModelForm
from django.core import validators
from django.core.exceptions import ValidationError
    
ESTADOS_ITEM=(
        ('En Construccion', 'En Construccion'),
        ('Terminado', 'Terminado'),
        ('Validado', 'Validado'),
    )

class ItemNuevoForm(forms.Form):
#, validators=[validar_fasenombre_unico]
    """ Atributos de Fase necesarios para el registro en la base de datos
    enviados al template html encargado de tomar los datos de registro.
    Control de datos ingresados por el usuario.
        
    @type forms.Form: django.forms
    @param forms.Form: Heredamos la clase forms.Form para hacer uso de sus funcionalidades en el formulario de registro
    @author: Ysapy Ortiz
        
    """

    Nombre_de_Item = forms.CharField(widget=forms.TextInput(), max_length=20, required=True, error_messages={'required':'Ingrese un nombre de item', 'max_length':'Longitud maxima 20'})
    Descripcion = forms.CharField(widget=forms.TextInput(), required=True, max_length=300, error_messages={'required':'Ingrese una descripcion para la fase', 'max_length':'Longitud maxima 300'})
    Prioridad = forms.IntegerField(required=True, error_messages={'required': 'Ingrese un numero calificador de prioridad'})
    Observaciones = forms.CharField(widget=forms.TextInput(), required=False, max_length=300, error_messages={'max_length':'Longitud maxima 300'})
    Costo_Temporal = forms.IntegerField(required=True, error_messages={'required':'Ingrese un costo temporal'})
    Costo_Monetario= forms.IntegerField(required=True, error_messages={'required':'Ingrese un costo monetario'}) 
    Complejidad = forms.IntegerField(required=True, error_messages={'required': 'Ingrese un numero calificador de complejidad'})
  
class ItemModificadoForm(forms.Form):
    Nombre_de_Item = forms.CharField(widget=forms.TextInput(), max_length=20, required=True, error_messages={'required':'Ingrese un nombre de item', 'max_length':'Longitud maxima 20'})
    Descripcion = forms.CharField(widget=forms.TextInput(), required=True, max_length=300, error_messages={'required':'Ingrese una descripcion para la fase', 'max_length':'Longitud maxima 300'})
    Prioridad = forms.IntegerField(required=True, error_messages={'required': 'Ingrese un numero calificador de prioridad'})
    Observaciones = forms.CharField(widget=forms.TextInput(), required=False, max_length=300, error_messages={'max_length':'Longitud maxima 300'})
    Costo_Temporal = forms.IntegerField(required=True, error_messages={'required':'Ingrese un costo temporal'})
    Costo_Monetario= forms.IntegerField(required=True, error_messages={'required':'Ingrese un costo monetario'}) 
    Complejidad = forms.IntegerField(required=True, error_messages={'required': 'Ingrese un numero calificador de complejidad'})
    Estado = forms.ChoiceField(widget=forms.Select(), choices= (ESTADOS_ITEM), required=False)
  