from django.contrib import admin
from .models.Almacen import Almacen
from .models.Estante import Estante
from .models.Nivel import Nivel
from .models.EstanteNivel import EstanteNivel

@admin.register(Almacen)
class AlmacenAdmin(admin.ModelAdmin):
    list_display = ('tipo_almacen', 'ubicacion', 'estado')
    search_fields = ('tipo_almacen', 'ubicacion')
    list_filter = ('tipo_almacen', 'estado')

@admin.register(Estante)
class EstanteAdmin(admin.ModelAdmin):
    list_display = ('nro_estante', 'almacen', 'estado')
    search_fields = ('nro_estante', 'almacen__tipo_almacen')
    list_filter = ('almacen', 'estado')

@admin.register(Nivel)
class NivelAdmin(admin.ModelAdmin):
    list_display = ('nro_nivel',)
    search_fields = ('nro_nivel',)
    list_filter = ('nro_nivel',)
