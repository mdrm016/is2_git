from django import forms
from django.contrib.auth.models import Group, Permission

def validateRolnameUnique(value):
    if Group.objects.filter(name=value).exists():
        raise ValidationError(u'El nombre de usuario ya existe')

class RolForm (forms.Form):
    
    """ Atributos de Rol necesarios para el registro en la base de datos
        de un nuevo rol. Este formulario con los campos descritos son 
        enviados al template html encargado de tomar los datos de registro.
        Control de datos ingresados por el usuario.
        
        @type forms.Form: django.forms
        @param forms.Form: Heredamos la clase forms.Form para hacer uso de sus funcionalidades en el formulario de registro
        @author: Eduardo Gimenez
        
    """
    
    Nombre_de_Rol = forms.CharField(widget=forms.TextInput(), validators=[validate_username_unique], max_length=20, required=True, error_messages={'required': 'Ingrese un nombre de usuario', 'max_length': 'Longitud maxima: 14 caracteres'})
    Permisos = forms.MultipleChoiceField(required=True, widget=forms.CheckboxSelectMultiple, choices=Permission.objects.all())
    Proyecto = forms.CharField()
    
    
    
    
    
    