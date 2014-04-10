from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm

class UsuarioNuevoForm (forms.Form):
    username = forms.CharField(widget=forms.TextInput(), max_length=14, min_length=5, required=True, error_messages={'required': 'Ingrese un nombre de usuario', 'max_length': 'Longitud maxima: 14', 'min_length': 'Longitud minima: 5 caracteres'})
    password = forms.CharField(widget=forms.PasswordInput(render_value=False), max_length=14, min_length=5, required=True, error_messages={'required': 'Ingrese contrasenha', 'max_length': 'Longitud maxima: 14', 'min_length': 'Longitu minima: 5 caracteres',})
    password2 = forms.CharField(widget=forms.PasswordInput(render_value=False), max_length=14, min_length=5, required=True, error_messages={'required': 'Ingrese contrasenha', 'max_length': 'Longitud maxima: 14', 'min_length': 'Longitu minima: 5 caracteres',})
    email = forms.CharField(widget=forms.TextInput(), required=False)
    first_name = forms.CharField(widget=forms.TextInput(), max_length=30, required=True, error_messages={'required': 'Ingrese nombre', })
    last_name = forms.CharField(widget=forms.TextInput(), max_length=30, required=True, error_messages={'required': 'Ingrese Apellido', })
    telefono = forms.CharField(widget=forms.TextInput(), max_length=30, required=True, error_messages={'required': 'Ingrese Telefono', })
    direccion = forms.CharField(widget=forms.TextInput(), max_length=100, required=True, error_messages={'required': 'Ingrese Direccion', })
    especialidad = forms.CharField(widget=forms.TextInput(), max_length=100, required=False)
    observaciones = forms.CharField(widget=forms.TextInput(), max_length=1000, required=False)
    #fields = ['username', 'password', 'email', 'last_name', 'first_name', 'telefono', 'direccion', 'especialidad', 'observaciones']
    
class UsuarioModificadoForm (forms.Form):
    username = forms.CharField(widget=forms.TextInput(), max_length=14, required=True, error_messages={'required': 'Ingrese un nombre de usuario', 'max_length': 'Longitud maxima: 14', 'min_length': 'Longitud minima: 5 caracteres'})
    password = forms.CharField(widget=forms.PasswordInput(render_value=False), max_length=14, min_length=5, required=False, error_messages={'required': 'Ingrese contrasenha', 'max_length': 'Longitud maxima: 14', 'min_length': 'Longitu minima: 5 caracteres',})
    nuevo_password = forms.CharField(widget=forms.PasswordInput(render_value=False), max_length=14, min_length=5, required=False, error_messages={'required': 'Ingrese contrasenha', 'max_length': 'Longitud maxima: 14', 'min_length': 'Longitu minima: 5 caracteres',})
    email = forms.CharField(widget=forms.TextInput(), required=False)
    first_name = forms.CharField(widget=forms.TextInput(), max_length=30, required=True, error_messages={'required': 'Ingrese nombre', })
    last_name = forms.CharField(widget=forms.TextInput(), max_length=30, required=True, error_messages={'required': 'Ingrese Apellido', })
    telefono = forms.CharField(widget=forms.TextInput(), max_length=30, required=True, error_messages={'required': 'Ingrese Telefono', })
    direccion = forms.CharField(widget=forms.TextInput(), max_length=100, required=True, error_messages={'required': 'Ingrese Direccion', })
    especialidad = forms.CharField(widget=forms.TextInput(), max_length=100, required=False)
    observaciones = forms.CharField(widget=forms.TextInput(), max_length=1000, required=False)