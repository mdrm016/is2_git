from django import forms
from django.contrib.auth.models import Group, Permission
from aplicaciones.proyectos.models import Proyectos
from django.core import validators
from django.core.exceptions import ValidationError
from django.db.models import Q

def validarNombreRolUnico(value):
    if Group.objects.filter(name=value).exists():
        raise ValidationError(u'El nombre del Rol ya existe')
        
def listaProyectos():
    proyectos = Proyectos.objects.filter(is_active=True)
    qset=(Q(estado__icontains='Inactivo') | Q(estado__icontains='En Construccion') )
    proyectos= proyectos.filter(qset).distinct()
    proyectos = [('', 'None')] + [(proyecto.id, proyecto.nombre) for proyecto in proyectos]
    return proyectos

def listaPermisos():
    permisos = Permission.objects.filter(id__gt=42)
    parte1 = permisos.filter(id__range=(43,70))
    parte2 = permisos.filter(id__range=(92,98))
    parte3 = permisos.filter(id__range=(114,117))
    permisos = []
    permisos.extend(parte1)
    permisos.extend(parte2)
    permisos.extend(parte3)
    permisos = [(permiso.codename, permiso.name) for permiso in permisos]
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
    Nombre_de_Rol = forms.CharField(widget=forms.TextInput(), validators=[validarNombreRolUnico], help_text='*', max_length=20, required=True, error_messages={'required': 'Ingrese un nombre de Rol', 'max_length': 'Longitud maxima: 20 caracteres'})
    Permisos = forms.MultipleChoiceField(required=True, widget=forms.CheckboxSelectMultiple(), help_text='*', choices=listaPermisos(), error_messages={'required': 'Debe escoger por lo menos  un Rol'})
    Proyecto = forms.ChoiceField(widget=forms.Select() , choices=listaProyectos(),  required=False)
    Descripcion = forms.CharField(widget=forms.Textarea(), required=False, max_length= 300, error_messages={'max_length': 'Longitud maxima: 300 caracteres'})
    
    def __init__(self, *args, **kwargs):
        self.Proyecto = listaProyectos()
        super(RolForm, self).__init__(*args, **kwargs)
        self.fields['Proyecto']= forms.ChoiceField(widget=forms.Select() , choices=listaProyectos(),  required=False)

    
class RolModificadoForm (forms.Form):
    
    """ Atributos de Rol necesarios para el registro en la base de datos
        de un nuevo rol. Este formulario con los campos descritos son 
        enviados al template html encargado de tomar los datos de registro.
        Control de datos ingresados por el usuario.
        
        @type forms.Form: django.forms
        @param forms.Form: Heredamos la clase forms.Form para hacer uso de sus funcionalidades en el formulario de registro
        @author: Eduardo Gimenez
        
    """
                
    Nombre_de_Rol = forms.CharField(widget=forms.TextInput(), max_length=20, required=True, error_messages={'max_length': 'Longitud maxima: 14 caracteres'})
    Permisos = forms.MultipleChoiceField(required=True, widget=forms.CheckboxSelectMultiple(), help_text='*', choices=listaPermisos(), error_messages={'required': 'Debe escoger por lo menos  un Rol'})
    Descripcion = forms.CharField(widget=forms.Textarea(), required=False, max_length= 300, error_messages={'max_length': 'Longitud maxima: 300 caracteres'})

