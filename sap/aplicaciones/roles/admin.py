from django.contrib import admin
from .models import Roles

class RolesAdmin (admin.ModelAdmin):
    list_display = ('id', 'proyecto', 'descripcion', 'is_active')
    list_filter = ('proyecto',)
    search_fields = ('proyecto',)
    list_editable = ('proyecto', 'descripcion', 'is_active')

admin.site.register(Roles, RolesAdmin)
