from django.contrib import admin
from .models import Proyectos

class ProyectoAdmin (admin.ModelAdmin):
    list_display = ('id', 'nombre', 'lider', 'estado', 'fecha_inicio', 'duracion', 'is_active')
    list_filter = ('lider',)
    search_fields = ('nombre', 'lider__username')
    list_editable = ('nombre', 'lider', 'estado', 'fecha_inicio', 'duracion', 'is_active')

admin.site.register(Proyectos, ProyectoAdmin)
