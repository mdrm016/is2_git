from django import forms
from django.contrib.auth.models import Group, Permission
from aplicaciones.proyectos.models import Proyectos
from django.core import validators
from django.core.exceptions import ValidationError

def validarNombreRolUnico(value):
    if Group.objects.filter(name=value).exists():
        raise ValidationError(u'El nombre del Rol ya existe')
        
def listaProyectos():
    proyectos = [('', 'None')] + [(proyecto.nombre, proyecto.id) for proyecto in Proyectos.objects.all()]
    return proyectos

def listaPermisos():
    permisos = [('', 'None')] + [(permiso.codename, permiso.name) for permiso in Permission.objects.all()]
    return permisos

class RolForm (forms.Form):
    
    """ Atributos de Rol necesarios para el registro en la base de datos
        de un nuevo rol. Este formulario con los campos descritos son 
        enviados al template html encargado de tomar los datos de registro.
        Control de datos ingresados por el usuario.
        
        @type forms.Form: django.forms
        @param forms.Form: Heredamos la clase forms.Form para hacer uso de sus funcionalidades en el formulario de registro
        @author: Eduardo Gimenez
        
    """
    
    Nombre_de_Rol = forms.CharField(widget=forms.TextInput(), validators=[validarNombreRolUnico], max_length=20, required=True, error_messages={'required': 'Ingrese un nombre de usuario', 'max_length': 'Longitud maxima: 14 caracteres'})
    Permisos = forms.MultipleChoiceField(required=True, widget=forms.CheckboxSelectMultiple(), choices=listaPermisos(), error_messages={'required': 'Debe escoger por lo menos  un Rol'})
    Proyecto = forms.ChoiceField(widget=forms.Select() , choices=listaProyectos(),  required=False)
    Descripcion = forms.CharField(widget=forms.Textarea(), required=False, max_length= 300, error_messages={'max_length': 'Longitud maxima: 300 caracteres'})
    
class RolModificadoForm (forms.Form):
    
    """ Atributos de Rol necesarios para el registro en la base de datos
        de un nuevo rol. Este formulario con los campos descritos son 
        enviados al template html encargado de tomar los datos de registro.
        Control de datos ingresados por el usuario.
        
        @type forms.Form: django.forms
        @param forms.Form: Heredamos la clase forms.Form para hacer uso de sus funcionalidades en el formulario de registro
        @author: Eduardo Gimenez
        
    """
    
    Nombre_de_Rol = forms.CharField(widget=forms.TextInput(), max_length=20, required=True, error_messages={'required': 'Ingrese un nombre de usuario', 'max_length': 'Longitud maxima: 14 caracteres'})
    Permisos = forms.MultipleChoiceField(required=False, widget=forms.CheckboxSelectMultiple(), choices=listaPermisos())
    Descripcion = forms.CharField(widget=forms.Textarea(), required=False, max_length= 300, error_messages={'max_length': 'Longitud maxima: 300 caracteres'})
    
    
    
    
    
    