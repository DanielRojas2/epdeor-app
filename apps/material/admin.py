from django.contrib import admin
from .models.Material import Material
from .models.Partida import Partida
from .models.UdM import UdM

@admin.register(Partida)
class PartidaAdmin(admin.ModelAdmin):
    list_display = ['codigo', 'descripcion']
    list_filter = ['codigo']
    search_fields = ['codigo', 'descripcion']

@admin.register(UdM)
class UdMAdmin(admin.ModelAdmin):
    list_display = ['unidad_medida']
    search_fields = ['unidad_medida']
