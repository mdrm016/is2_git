from django import forms

class LoginForms (forms.Form):
    """ Atributos Usuario y Clave del Formulario del login
        este formulario es usado para ser enviado al template html
        encargado de tomar los datos de autenticacion.
        
        @type forms.Form: django.forms
        @param forms.Form: Heredamos la clase forms.Form para hacer uso de sus funcionalidades en el formulario de login
        @author: Marcelo Denis
        
    """
    Usuario = forms.CharField(widget=forms.TextInput())
    Clave = forms.CharField(widget=forms.PasswordInput(render_value=False))