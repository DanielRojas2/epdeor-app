from django.urls import path
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from .views.estante_nivel_view import ListadoEstanteNivel, RegistrarEstanteNivel

urlpatterns = [
    path('estante_nivel/', ListadoEstanteNivel.as_view(), name='listar_estante_nivel'),
    path('estante_nivel/crear/', RegistrarEstanteNivel.as_view(), name='crear_estante_nivel'),
]

urlpatterns += [
    path('estante_nivel/', login_required(
        TemplateView.as_view(template_name='almacen/estante_nivel/listar_estante_nivel.html')
    ))
]
