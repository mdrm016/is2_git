from django import forms
from .models import Proyectos
from django.contrib.auth.models import User
from django.core import validators
from django.core.exceptions import ValidationError
from django.contrib.admin.widgets import AdminDateWidget
from django.contrib.admin import widgets
from aplicaciones.usuarios.models import Usuarios
from django.contrib.admin.widgets import FilteredSelectMultiple
from aplicaciones.roles.models import Roles

def validate_nombreproyecto_unique(value):
    if Proyectos.objects.filter(nombre=value, is_active=True).exists():
        raise ValidationError(u'El nombre del proyecto ya existe y no puede haber duplicados')

def validate_duracion_proyecto (value):
    if value < 1:
        raise ValidationError(u'La duracion debe ser mayor a cero.')
    
def opcionLider():
    usuarios = User.objects.exclude(id='1')
    resultado = []
    for usuario in usuarios: 
        if usuario.is_active:
            tupla = (usuario.id, usuario.username)
            resultado.append(tupla)
    return resultado
        
ESTADOS_PROYECTO=(
        ('Inactivo', 'Inactivo'),
        ('En Construccion', 'En Construccion'),
        ('Finalizado', 'Finalizado'),
    )
  
class ProyectoNuevoForm(forms.Form):
    
    """ Atributos de Proyecto necesarios para el registro en la base de datos
    enviados al template html encargado de tomar los datos de registro.
    Control de datos ingresados por el usuario.
        
    @type forms.Form: django.forms
    @param forms.Form: Heredamos la clase forms.Form para hacer uso de sus funcionalidades en el formulario de registro
    @author: Marcelo Denis
        
    """
    
    Nombre_del_Proyecto = forms.CharField(widget=forms.TextInput(), validators=[validate_nombreproyecto_unique], max_length=30, min_length=2, required=True, help_text='*', error_messages={'required': 'Ingrese un nombre para el proyecto', 'max_length': 'Longitud maxima: 15', 'min_length': 'Longitud minima: 2 caracteres'})
    Fecha_de_Inicio =  forms.DateField(input_formats=['%Y-%m-%d'], widget=widgets.AdminDateWidget, required=True, help_text='* Ingrese en formato dia/mes/anho', error_messages={'required': 'Ingrese una fecha de inicio de proyecto'} )
    Duracion = forms.IntegerField(required=True, help_text='* En semanas', validators=[validate_duracion_proyecto], error_messages={'required': 'Ingrese la duracion del proyecto',})
    
    
class ProyectoModificadoForm(forms.Form):
    
    """ Atributos de proyecto necesarios para la modificacion en la base de datos
    de un proyecto. Este formulario con los campos descritos son 
    enviados al template html encargado de desplegar los datos del proyecto a modificar.
    
    Control de datos ingresados por el usuario.
        
    @type forms.Form: django.forms
    @param forms.Form: Heredamos la clase forms.Form para hacer uso de sus funcionalidades en el formulario de registro
    @author: Marcelo Denis
    
    """
    
    Nombre_del_Proyecto = forms.CharField(widget=forms.TextInput(), max_length=30, min_length=2, required=True, error_messages={'required': 'Ingrese un nombre para el proyecto', 'max_length': 'Longitud maxima: 15', 'min_length': 'Longitud minima: 2 caracteres'})
    Nuevo_Lider =  forms.ChoiceField(widget=forms.Select(), choices= (opcionLider()), required=False)
    Nuevo_Estado = forms.ChoiceField(widget=forms.Select(), choices= (ESTADOS_PROYECTO), required=False)
    Duracion = forms.IntegerField(required=True, help_text='En semanas', validators=[validate_duracion_proyecto], error_messages={'required': 'Ingrese la duracion del proyecto',})
    
    def __init__(self, *args, **kwargs):
        self.Nuevo_Lider = opcionLider()
        super(ProyectoModificadoForm, self).__init__( *args, **kwargs)
        self.fields['Nuevo_Lider']= forms.ChoiceField(widget=forms.Select(), choices= (self.Nuevo_Lider), required=False)
        

   