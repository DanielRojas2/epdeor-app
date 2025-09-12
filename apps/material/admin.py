from django.contrib import admin
from .models.Material import Material
from .models.Partida import Partida
from .models.UdM import UdM

admin.site.register(Material)
admin.site.register(Partida)
admin.site.register(UdM)
