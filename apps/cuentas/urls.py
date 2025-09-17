from django.urls import path
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from .views.personal import ListadoPersonal, RegistrarPersonal
from .views.contrato_view import ListadoContrato, RegistrarContrato

urlpatterns = [
    path('iniciar-sesion/', auth_views.LoginView.as_view(), name='iniciar_sesion'),
    path('cerrar-sesion/', auth_views.LogoutView.as_view(), name='cerrar_sesion'),

    # Rutas para la gestión de personal
    path('personal/', login_required(ListadoPersonal.as_view()), name='personal'),
    path('personal/crear/', login_required(RegistrarPersonal.as_view()), name='crear_personal'),
    
    path('contratos/', login_required(ListadoContrato.as_view()), name='contratos'),
    path('contratos/crear/', login_required(RegistrarContrato.as_view()), name='crear_contrato')
]

urlpatterns += [
    path('personal/', login_required(
        TemplateView.as_view(template_name='cuentas/personal/listar_personal.html')
    ))
]
