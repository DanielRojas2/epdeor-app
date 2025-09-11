from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('iniciar-sesion/', auth_views.LoginView.as_view(), name='iniciar_sesion'),
    path('cerrar-sesion/', auth_views.LogoutView.as_view(), name='cerrar_sesion'),
]
