from django import forms
from django.core import validators
from django.core.exceptions import ValidationError
from django.db.models import Q
from .models import TipoItem
#from aplicaciones.tipoatributo.models import TipoAtributo

def validate_nombretipoitem_unique(value):
    if TipoItem.objects.filter(nombre=value, is_active=True).exists():
        raise ValidationError(u'El nombre del tipo de item ya existe y no puede haber duplicados')
    
"""def opcionTipoAtributo():
    tipoatributos = TipoAtributo.objects.filter(is_active=True)
    tipoatributos = [(tipoatributo.id, tipoatributo.nombre) for tipoatributo in tipoatributos]
    return tipoatributos"""

class TipoItemNuevoForm(forms.Form):
    
    Nombre_Tipo_de_Item = forms.CharField(widget=forms.TextInput(), validators=[validate_nombretipoitem_unique], max_length=30, min_length=2, required=True, help_text='*', error_messages={'required': 'Ingrese un nombre para el tipo de item', 'max_length': 'Longitud maxima: 30', 'min_length': 'Longitud minima: 2 caracteres'})
    Descripcion = forms.CharField(widget=forms.Textarea(), required=True, min_length=5, max_length= 300, help_text='*', error_messages={'required': 'Ingrese una breve descripcion para el tipo de item', 'max_length': 'Longitud maxima: 300 caracteres'})
    #Tipo_Atributo = forms.MultipleChoiceField(widget=FilteredSelectMultiple(('Tipo_Atributo'),False,), required=False, help_text='*', choices= (opcionTipoAtributo()))
    
    """def __init__(self, *args, **kwargs):
        self.Tipo_Atributo = opcionTipoAtributo()
        super(ProyectoNuevoForm, self).__init__(*args, **kwargs)
        self.fields['Tipo_Atributo']= forms.MultipleChoiceField(widget=FilteredSelectMultiple(('Tipo_Atributo'),False,), required=False, help_text='*', choices= (self.Tipo_Atributo))"""
        
class TipoItemModificadoForm(forms.Form):
    
    Nombre_Tipo_de_Item = forms.CharField(widget=forms.TextInput(), max_length=30, min_length=2, required=False, error_messages={'max_length': 'Longitud maxima: 30', 'min_length': 'Longitud minima: 2 caracteres'})
    Descripcion = forms.CharField(widget=forms.Textarea(), required=True, min_length=5, max_length= 300, error_messages={'required': 'Ingrese una breve descripcion para el tipo de item', 'max_length': 'Longitud maxima: 300 caracteres'})
    #Tipo_Atributo = forms.MultipleChoiceField(widget=FilteredSelectMultiple(('Tipo_Atributo'),False,), required=False, choices= (opcionTipoAtributo()))
    
    """def __init__(self, *args, **kwargs):
        self.Tipo_Atributo = opcionTipoAtributo()
        super(ProyectoNuevoForm, self).__init__(*args, **kwargs)
        self.fields['Tipo_Atributo']= forms.MultipleChoiceField(widget=FilteredSelectMultiple(('Tipo_Atributo'),False,), required=False, choices= (self.Tipo_Atributo))"""
        