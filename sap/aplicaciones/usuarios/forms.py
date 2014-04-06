from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm

class UsuarioNuevoForm(ModelForm):
    class Meta:
        model = Usuarios
        fields = ['username', 'password', 'email', 'telefono', 'direccion', 'especialidad', 'observaciones']
        widgets = {
            'password': forms.PasswordInput(),
        }