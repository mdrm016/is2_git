from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm

from .models import Usuarios

class UsuarioNuevoForm (forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput(render_value=False))
    email = forms.CharField(widget=forms.TextInput())
    first_name = forms.CharField(widget=forms.TextInput())
    last_name = forms.CharField(widget=forms.TextInput())
    telefono = forms.CharField(widget=forms.TextInput())
    direccion = forms.CharField(widget=forms.TextInput())
    especialidad = forms.CharField(widget=forms.TextInput())
    observaciones = forms.CharField(widget=forms.TextInput())