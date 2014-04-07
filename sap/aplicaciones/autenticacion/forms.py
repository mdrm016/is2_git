from django import forms

class LoginForms (forms.Form):
    Usuario = forms.CharField(widget=forms.TextInput())
    Clave = forms.CharField(widget=forms.PasswordInput(render_value=False))