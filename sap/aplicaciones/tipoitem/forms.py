from django import forms
from django.core import validators
from django.core.exceptions import ValidationError
from django.db.models import Q
from .models import TipoItem

def validate_nombretipoitem_unique(value):
    if TipoItem.objects.filter(nombre=value, is_active=True).exists():
        raise ValidationError(u'El nombre del tipo de item ya existe y no puede haber duplicados')

class TipoItemNuevoForm(forms.Form):
    
    
    """ Atributos de tipo de item necesarios para el registro en la base de datos del mismo, estos son
    enviados al template html encargado de tomar los datos de registro.
    Control de datos ingresados por el usuario.
        
    @type forms.Form: django.forms
    @param forms.Form: Heredamos la clase forms.Form para hacer uso de sus funcionalidades en el formulario de registro
    @author: Marcelo Denis
        
    """
    
    Nombre_Tipo_de_Item = forms.CharField(widget=forms.TextInput(), validators=[validate_nombretipoitem_unique], max_length=30, min_length=2, required=True, help_text='*', error_messages={'required': 'Ingrese un nombre para el tipo de item', 'max_length': 'Longitud maxima: 30', 'min_length': 'Longitud minima: 2 caracteres'})
    Descripcion = forms.CharField(widget=forms.Textarea(), min_length=5, max_length= 300, required=True, help_text='*', error_messages={'required': 'Ingrese una breve descripcion para el tipo de item', 'max_length': 'Longitud maxima: 300 caracteres'})
        
class TipoItemModificadoForm(forms.Form):
    
    """ Atributos de tipo de item necesarios para la modificacion en la base de datos del mismo, estos son
    enviados al template html encargado de tomar los datos de modificacion.
    Control de datos ingresados por el usuario.
        
    @type forms.Form: django.forms
    @param forms.Form: Heredamos la clase forms.Form para hacer uso de sus funcionalidades en el formulario de registro
    @author: Marcelo Denis
        
    """
    
    Nombre_Tipo_de_Item = forms.CharField(widget=forms.TextInput(), max_length=30, min_length=2, required=True, error_messages={'max_length': 'Longitud maxima: 30', 'min_length': 'Longitud minima: 2 caracteres'})
    Descripcion = forms.CharField(widget=forms.Textarea(), required=True, min_length=5, max_length= 300, error_messages={'required': 'Ingrese una breve descripcion para el tipo de item', 'max_length': 'Longitud maxima: 300 caracteres'})