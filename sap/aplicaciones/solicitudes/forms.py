from django import forms
from django.forms.extras.widgets import Select
from .models import Solicitudes
from django.forms import ModelForm
from django.core import validators
from django.core.exceptions import ValidationError
    
ESTADOS_SOLICITUD=(
        ('Pendiente', 'Pendiente'),
        ('Aprobado', 'Aprobado'),
        ('Rechazado', 'Rechazado'),
        ('Cancelado', 'Cancelado'),
    )

class SolicitudNuevaForm(forms.Form):

    """ Atributos de Fase necesarios para el registro en la base de datos
    enviados al template html encargado de tomar los datos de registro.
    Control de datos ingresados por el usuario.
        
    @type forms.Form: django.forms
    @param forms.Form: Heredamos la clase forms.Form para hacer uso de sus funcionalidades en el formulario de registro
    @author: Ysapy Ortiz
        
    """

    #Usuario = forms.CharField(max_length=20, required=True, error_messages={'required':'Ingrese nombre de usuario', 'max_length':'Longitud maxima 20'})
    Proyecto = forms.CharField(required=True, max_length=300, error_messages={'required':'Ingrese nombre de proyecto', 'max_length':'Longitud maxima 300'})
    Fase = forms.CharField(required=True, error_messages={'required': 'Ingrese nombre de fase'})
    Item = forms.CharField(required=True, max_length=300, error_messages={'required': 'Ingrese nombre de item', 'max_length':'Longitud maxima 300'})
    Fecha_de_Solicitud = forms.CharField(required=True, error_messages={'required':'Ingrese fecha de solicitud'})
    Tiempo_Solicitado_en_Dias = forms.IntegerField(required=True, error_messages={'required':'Ingrese el tiempo necesario en dias'}) 
    Descripcion = forms.CharField(required=True, error_messages={'required': 'Ingrese una breve descripcion de las razones de la solicitud'})
    Observaciones = forms.CharField(required=False)
    Estado = forms.CharField(required=True, error_messages={'required': 'Ingrese un numero calificador de complejidad'})
    Duracion_Solicitud_en_Dias = forms.IntegerField(required=True, error_messages={'required': 'Ingrese (en dias) el tiempo valido para responder la solicitud'})

class SolicitudPrimeraForm(forms.Form):

    """ Atributos de Fase necesarios para el registro en la base de datos
    enviados al template html encargado de tomar los datos de registro.
    Control de datos ingresados por el usuario.
        
    @type forms.Form: django.forms
    @param forms.Form: Heredamos la clase forms.Form para hacer uso de sus funcionalidades en el formulario de registro
    @author: Ysapy Ortiz
        
    """

    #Usuario = forms.CharField(required=False, max_length=20, error_messages={'max_length':'Longitud maxima 20'})
    Proyecto = forms.CharField(required=False, max_length=300, error_messages={'max_length':'Longitud maxima 300'})
    Fase = forms.CharField(required=False)
    Item = forms.CharField(required=False, max_length=300, error_messages={'max_length':'Longitud maxima 300'})
    Fecha_de_Solicitud = forms.CharField(required=False)
    Tiempo_Solicitado_en_Dias = forms.IntegerField(required=False) 
    Descripcion = forms.CharField(required=False)
    Observaciones = forms.CharField(required=False)
    Estado = forms.CharField(required=False)
    Duracion_Solicitud_en_Dias = forms.IntegerField(required=False)
