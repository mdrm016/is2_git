from django import forms
from django.contrib.auth.models import User
from .models import Usuarios
from django.forms import ModelForm
from django.core import validators
from django.core.exceptions import ValidationError

def validate_username_unique(value):
    if User.objects.filter(username=value).exists():
        raise ValidationError(u'El nombre de usuario ya existe')

class UsuarioNuevoForm (forms.Form):
    
    """ Atributos de Usuario necesarios para el registro en la base de datos
        de un nuevo usuario. Este formulario con los campos descritos son 
        enviados al template html encargado de tomar los datos de registro.
        Control de datos ingresados por el usuario.
        
        @type forms.Form: django.forms
        @param forms.Form: Heredamos la clase forms.Form para hacer uso de sus funcionalidades en el formulario de registro
        @author: Ysapy Ortiz
        
    """
    
    Nombre_de_Usuario = forms.CharField(widget=forms.TextInput(), validators=[validate_username_unique], max_length=14, min_length=5, required=True, error_messages={'required': 'Ingrese un nombre de usuario', 'max_length': 'Longitud maxima: 14', 'min_length': 'Longitud minima: 5 caracteres'})
    Contrasenha = forms.CharField(widget=forms.PasswordInput(render_value=False), max_length=14, min_length=5, required=True, error_messages={'required': 'Ingrese contrasenha', 'max_length': 'Longitud maxima: 14', 'min_length': 'Longitu minima: 5 caracteres',})
    Confirmar_contrasenha = forms.CharField(widget=forms.PasswordInput(render_value=False), max_length=14, min_length=5, required=True, error_messages={'required': 'Ingrese contrasenha', 'max_length': 'Longitud maxima: 14', 'min_length': 'Longitu minima: 5 caracteres',})
    Email = forms.CharField(widget=forms.TextInput(), required=False)
    Nombre = forms.CharField(widget=forms.TextInput(), max_length=30, required=True, error_messages={'required': 'Ingrese nombre', })
    Apellido = forms.CharField(widget=forms.TextInput(), max_length=30, required=True, error_messages={'required': 'Ingrese Apellido', })
    Telefono = forms.CharField(widget=forms.TextInput(), max_length=30, required=True, error_messages={'required': 'Ingrese Telefono', })
    Direccion = forms.CharField(widget=forms.TextInput(), max_length=100, required=True, error_messages={'required': 'Ingrese Direccion', })
    Especialidad = forms.CharField(widget=forms.TextInput(), max_length=100, required=False)
    Observaciones = forms.CharField(widget=forms.TextInput(), max_length=1000, required=False)
    
    def clean(self):
        super(forms.Form,self).clean()
        if 'Contrasenha' in self.cleaned_data and 'Confirmar_contrasenha' in self.cleaned_data:
            if self.cleaned_data['Contrasenha'] != self.cleaned_data['Confirmar_contrasenha']:
                self._errors['Contrasenha'] = [u'Las contrasenhas deben coincidir.']
                self._errors['Confirmar_contrasenha'] = [u'Las contrasenhas deben coincidir.']
        return self.cleaned_data
    
class UsuarioModificadoForm (forms.Form):
    Nombre_de_Usuario = forms.CharField(widget=forms.TextInput(), max_length=14, required=True, error_messages={'required': 'Ingrese un nombre de usuario', 'max_length': 'Longitud maxima: 14', 'min_length': 'Longitud minima: 5 caracteres'})
    Contrasenha = forms.CharField(widget=forms.PasswordInput(render_value=False), max_length=14, min_length=5, required=False, error_messages={'required': 'Ingrese contrasenha', 'max_length': 'Longitud maxima: 14', 'min_length': 'Longitu minima: 5 caracteres',})
    Nueva_contrasenha = forms.CharField(widget=forms.PasswordInput(render_value=False), max_length=14, min_length=5, required=False, error_messages={'required': 'Ingrese contrasenha', 'max_length': 'Longitud maxima: 14', 'min_length': 'Longitu minima: 5 caracteres',})
    Email = forms.CharField(widget=forms.TextInput(), required=False)
    Nombre = forms.CharField(widget=forms.TextInput(), max_length=30, required=True, error_messages={'required': 'Ingrese nombre', })
    Apellido = forms.CharField(widget=forms.TextInput(), max_length=30, required=True, error_messages={'required': 'Ingrese Apellido', })
    Telefono = forms.CharField(widget=forms.TextInput(), max_length=30, required=True, error_messages={'required': 'Ingrese Telefono', })
    Direccion = forms.CharField(widget=forms.TextInput(), max_length=100, required=True, error_messages={'required': 'Ingrese Direccion', })
    Especialidad = forms.CharField(widget=forms.TextInput(), max_length=100, required=False)
    Observaciones = forms.CharField(widget=forms.TextInput(), max_length=1000, required=False)

    def clean(self):
        super(forms.Form,self).clean()
        if 'Contrasenha' in self.cleaned_data and 'Confirmar_contrasenha' in self.cleaned_data:
            if self.cleaned_data['Contrasenha'] != self.cleaned_data['Confirmar_contrasenha']:
                self._errors['Contrasenha'] = [u'Las contrasenhas deben coincidir.']
                self._errors['Confirmar_contrasenha'] = [u'Las contrasenhas deben coincidir.']
        return self.cleaned_data
    