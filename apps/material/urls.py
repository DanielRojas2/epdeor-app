from django.urls import path
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from .views.material_views import ListadoMaterial, RegistrarMaterial

urlpatterns = [
    path('material/', ListadoMaterial.as_view(), name='listar_material'),
    path('material/crear/', RegistrarMaterial.as_view(), name='crear_material'),
]

urlpatterns += [
    path('material/', login_required(
        TemplateView.as_view(template_name='almacen/estante_nivel/listar_material.html')
    ))
]
