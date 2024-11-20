from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('perfil/', views.perfil, name='perfil'),
    path('perfil/<str:username>/', views.visualizar_perfil, name='visualizar_perfil'),
    path('login/', auth_views.LoginView.as_view(template_name='usuarios/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
    path('perfil/<str:username>/seguir/', views.seguir_usuario, name='seguir_usuario'),
    path('perfil/<str:username>/deixar_de_seguir/', views.deixar_de_seguir_usuario, name='deixar_de_seguir_usuario'),
    path('buscar/', views.buscar_usuarios, name='buscar_usuarios'),
    path('perfil/<str:username>/seguidores/', views.lista_seguidores, name='lista_seguidores'),
    path('perfil/<str:username>/seguindo/', views.lista_seguindo, name='lista_seguindo'),
]

