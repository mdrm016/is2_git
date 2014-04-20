from django import forms
from .models import Proyectos
from django.contrib.auth.models import User
from django.core import validators
from django.core.exceptions import ValidationError
from django.contrib.admin.widgets import AdminDateWidget
from django.contrib.admin import widgets
from aplicaciones.usuarios.models import Usuarios
from django.contrib.admin.widgets import FilteredSelectMultiple

def validate_nombreproyecto_unique(value):
    if Proyectos.objects.filter(nombre=value, is_active=True).exists():
        raise ValidationError(u'El nombre del proyecto ya existe y no puede haber duplicados')

def validate_duracion_proyecto (value):
    if value < 1:
        raise ValidationError(u'La duracion debe ser mayor a cero.')
    

def opcionLider():
    usuarios = User.objects.exclude(id='1')
    resultado = []
    tupla = ('', '--seleccione un lider--')
    resultado.append(tupla)
    for usuario in usuarios: 
        if usuario.is_active:
            tupla = (usuario.id, usuario.username)
            resultado.append(tupla)
    return resultado

def opcionMiembros():
    usuarios = Usuarios.objects.exclude(user_id='1')
    resultado = []
    for usuario in usuarios: 
        if usuario.user.is_active:
            tupla = (usuario.user_id, usuario.user.username)
            resultado.append(tupla)
    return resultado

ESTADOS_PROYECTO=(
        ('', '--seleccione un Estado--'),
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
    
    Nombre_del_Proyecto = forms.CharField(widget=forms.TextInput(), validators=[validate_nombreproyecto_unique], max_length=15, min_length=2, required=True, help_text='*', error_messages={'required': 'Ingrese un nombre para el proyecto', 'max_length': 'Longitud maxima: 15', 'min_length': 'Longitud minima: 2 caracteres'})
    Lider =  forms.ChoiceField(widget=forms.Select(), choices= (opcionLider()), required=True, help_text='*', error_messages={'required': 'Seleccione un lider para el proyecto',})
    Fecha_de_Inicio =  forms.DateField(input_formats=['%d/%m/%Y'], widget=widgets.AdminDateWidget, required=True, help_text='* Ingrese en formato dia/mes/anho', error_messages={'required': 'Ingrese una fecha de inicio de proyecto'} )
    Duracion = forms.IntegerField(required=True, help_text='* En semanas', validators=[validate_duracion_proyecto], error_messages={'required': 'Ingrese la duracion del proyecto',})
    Miembros = forms.MultipleChoiceField(widget=FilteredSelectMultiple(('Miembros'),False,), required=False, choices= (opcionMiembros()))
    
    
    def __init__(self, *args, **kwargs):
        self.Lider = opcionLider()
        self.Miembros = opcionMiembros()
        super(ProyectoNuevoForm, self).__init__(*args, **kwargs)
        self.fields['Lider']= forms.ChoiceField(widget=forms.Select(), choices= (self.Lider), required=True, help_text='*', error_messages={'required': 'Seleccione un lider para el proyecto',})
        self.fields['Miembros'] = forms.MultipleChoiceField(widget=FilteredSelectMultiple(('Miembros'),False,), required=False, choices= (self.Miembros))

    
class ProyectoModificadoForm(forms.Form):
    
    """ Atributos de proyecto necesarios para la modificacion en la base de datos
    de un proyecto. Este formulario con los campos descritos son 
    enviados al template html encargado de desplegar los datos del proyecto a modificar.
    
    Control de datos ingresados por el usuario.
        
    @type forms.Form: django.forms
    @param forms.Form: Heredamos la clase forms.Form para hacer uso de sus funcionalidades en el formulario de registro
    @author: Marcelo Denis
    
    """

    Nombre_del_Proyecto = forms.CharField(widget=forms.TextInput(), max_length=15, min_length=2, required=True, error_messages={'required': 'Ingrese un nombre para el proyecto', 'max_length': 'Longitud maxima: 15', 'min_length': 'Longitud minima: 2 caracteres'})
    Lider_Actual = forms.CharField(widget=forms.TextInput(), required=False)
    Nuevo_Lider =  forms.ChoiceField(widget=forms.Select(), choices= (opcionLider()), required=False)
    Estado_Actual = forms.CharField(widget=forms.TextInput(), required=False)
    Nuevo_Estado = forms.ChoiceField(widget=forms.Select(), choices= (ESTADOS_PROYECTO), required=False)
    Duracion = forms.IntegerField(required=True, help_text='En semanas', validators=[validate_duracion_proyecto], error_messages={'required': 'Ingrese la duracion del proyecto',})
    Cambio_de_Miembros = forms.MultipleChoiceField(widget=FilteredSelectMultiple(('Cambio_de_Miembros'),False,), required=False, choices= (opcionMiembros()) )
    
    def __init__(self, *args, **kwargs):
        self.Nuevo_Lider = opcionLider()
        self.Cambio_de_Miembros = opcionMiembros()
        super(ProyectoModificadoForm, self).__init__( *args, **kwargs)
        self.fields['Nuevo_Lider']= forms.ChoiceField(widget=forms.Select(), choices= (self.Nuevo_Lider), required=False)
        self.fields['Cambio_de_Miembros'] = forms.MultipleChoiceField(widget=FilteredSelectMultiple(('Cambio_de_Miembros'),False,), required=False, choices= (self.Cambio_de_Miembros))

   