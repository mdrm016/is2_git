from django import forms
from .models import Proyectos
from django.contrib.auth.models import User
from django.core import validators
from django.core.exceptions import ValidationError
from django.contrib.admin.widgets import AdminDateWidget
from django.contrib.admin import widgets
from aplicaciones.usuarios.models import Usuarios

def validate_nombreproyecto_unique(value):
    if Proyectos.objects.filter(nombre=value).exists():
        raise ValidationError(u'El nombre del proyecto ya existe y no puede haber duplicados')
    
def validate_fechainicio_proyecto (value):
        raise ValidationError(u'Ingrese una fecha valida')

def validate_duracion_proyecto (value):
    if value < 1:
        raise ValidationError(u'La duracion debe ser mayor a cero.')
    
opcionLider = [('', '--seleccione un lider--')] + [(Usuario.id, Usuario.username) for Usuario in User.objects.exclude(id='1')] 
opcionMiembros = [(Usuario.user_id, Usuario.user.username) for Usuario in Usuarios.objects.exclude(user_id='1')]

ESTADOS_PROYECTO=(
        ('', '--seleccione un Estado--'),
        ('Inactivo', 'Inactivo'),
        ('En Construccion', 'En Construccion'),
        ('Finalizado', 'Finalizado'),
    )
  
class ProyectoNuevoForm(forms.Form):
    
    Nombre_del_Proyecto = forms.CharField(widget=forms.TextInput(), validators=[validate_nombreproyecto_unique], max_length=15, min_length=2, required=True, help_text='*', error_messages={'required': 'Ingrese un nombre para el proyecto', 'max_length': 'Longitud maxima: 15', 'min_length': 'Longitud minima: 2 caracteres'})
    Lider =  forms.ChoiceField(widget=forms.Select(), choices= (opcionLider), required=True, help_text='*', error_messages={'required': 'Seleccione un lider para el proyecto',})
    Fecha_de_Inicio =  forms.DateField(input_formats=['%Y-%m-%d'], widget=widgets.AdminDateWidget, required=True, help_text='* Ingrese en formato anho-mes-dia', error_messages={'required': 'Ingrese una fecha de inicio de proyecto'} )
    Duracion = forms.IntegerField(required=True, help_text='* En semanas', validators=[validate_duracion_proyecto], error_messages={'required': 'Ingrese la duracion del proyecto',})
    Miembros = forms.MultipleChoiceField(widget=forms.SelectMultiple(), required=False, help_text='Seleccione los miembros del proyecto', choices= (opcionMiembros))
    
        
class ProyectoModificadoForm(forms.Form):

    Nombre_del_Proyecto = forms.CharField(widget=forms.TextInput(), max_length=15, min_length=2, required=True, error_messages={'required': 'Ingrese un nombre para el proyecto', 'max_length': 'Longitud maxima: 15', 'min_length': 'Longitud minima: 2 caracteres'})
    Lider_Actual = forms.CharField(widget=forms.TextInput(), required=False)
    Nuevo_Lider =  forms.ChoiceField(widget=forms.Select(), choices= (opcionLider), required=False)
    Estado_Actual = forms.CharField(widget=forms.TextInput(), required=False)
    Nuevo_Estado = forms.ChoiceField(widget=forms.Select(), choices= (ESTADOS_PROYECTO), required=False)
    Duracion = forms.IntegerField(required=True, help_text='En semanas', validators=[validate_duracion_proyecto], error_messages={'required': 'Ingrese la duracion del proyecto',})
    Cambio_de_Miembros = forms.MultipleChoiceField(widget=forms.SelectMultiple(), required=False, help_text='* Seleccione los nuevos miembros del proyecto', choices= (opcionMiembros) )
    
    