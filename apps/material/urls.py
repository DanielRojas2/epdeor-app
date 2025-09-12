from django.urls import path
from .views import material_view, partida_view, udm_view

urlpatterns = [
    # Material
    path("", material_view.material_list, name="material_list"),
    path("material/create/", material_view.material_create, name="material_create"),
    path("material/<int:pk>/update/", material_view.material_update, name="material_update"),
    path("material/<int:pk>/delete/", material_view .material_delete, name="material_delete"),

    # Partida
    path("partida/create/", partida_view.partida_create, name="partida_create"),
    path("partida/<int:pk>/update/", partida_view.partida_update, name="partida_update"),
    path("partida/<int:pk>/delete/", partida_view.partida_delete, name="partida_delete"),

    # UdM
    path("udm/create/", udm_view.udm_create, name="udm_create"),
    path("udm/<int:pk>/update/", udm_view.udm_update, name="udm_update"),
    path("udm/<int:pk>/delete/", udm_view.udm_delete, name="udm_delete"),
]