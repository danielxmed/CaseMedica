from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('perfil/', views.perfil, name='perfil'),
    path('perfil/<str:username>/', views.visualizar_perfil, name='visualizar_perfil'),
    path('login/', auth_views.LoginView.as_view(template_name='usuarios/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
]
