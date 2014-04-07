from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm

from .models import Usuarios

class UsuarioNuevoForm (forms.Form):
    username = forms.CharField(widget=forms.TextInput(), max_length=14, min_length=5, required=True, error_messages={'required': 'Ingrese un nombre de usuario', })
    password = forms.CharField(widget=forms.PasswordInput(render_value=False), max_length=14, min_length=5, required=True, error_messages={'required': 'Ingrese contrasenha', })
 #   password2 = forms.CharField(widget=forms.PasswordInput(render_value=False), max_length=14, min_length=5, required=True, error_messages={'required': 'Ingrese contrasenha', })
    email = forms.CharField(widget=forms.TextInput())
    first_name = forms.CharField(widget=forms.TextInput())
    last_name = forms.CharField(widget=forms.TextInput())
    telefono = forms.CharField(widget=forms.TextInput())
    direccion = forms.CharField(widget=forms.TextInput())
    especialidad = forms.CharField(widget=forms.TextInput())
    observaciones = forms.CharField(widget=forms.TextInput())

    
#    subject = forms.CharField(max_length=100)