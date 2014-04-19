from django import forms
from django.forms.extras.widgets import Select
from .models import Fases

from django.forms import ModelForm
from django.core import validators
from django.core.exceptions import ValidationError

def validar_fasenombre_unico(value):
    if Fases.objects.filter(nombre=value).exists():
        raise ValidationError(u'El nombre de fase ya existe')

class FaseNuevaForm(forms.Form):
    
    ESTADOS_CREAR = (
                     (u'DF', u'Definicion'),
                     )
    Nombre_de_Fase = forms.CharField(widget=forms.TextInput(), validators=[validar_fasenombre_unico], max_length=20, required=True, error_messages={'required':'Ingrese un nombre de fase', 'max_length':'Longitud maxima 20'})
    Descripcion = forms.CharField(widget=forms.TextInput(), required=True, max_length=300, error_messages={'required':'Ingrese una descripcion para la fase', 'max_length':'Longitud maxima 300'})
   # Estado = forms.ChoiceField(widget=Select, choice=ESTADOS_CREAR, required=True)
    Duracion_semanas = forms.IntegerField(required=True, error_messages={'required':'Ingrese una duracion estimada en semanas'})
    