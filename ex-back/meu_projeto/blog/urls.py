from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('registrar/', views.registrar_view, name='registrar'),
    path('resetar_senha/', views.resetar_senha_usuario, name='resetar_senha_usuario'),
    path('resetar_senha/<int:user_id>/nova/', views.resetar_nova_senha, name='resetar_nova_senha'),
    path('perfil/', views.perfil_view, name='perfil'),
    path('restrito/', views.pagina_restrita_view, name='pagina_restrita'),
    path('erro500/', views.erro_500_view, name='erro_500'),
]