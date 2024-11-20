from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_casos, name='lista_casos'),
    path('caso/<int:pk>/', views.detalhe_caso, name='detalhe_caso'),
    path('caso/novo/', views.novo_caso, name='novo_caso'),
    path('caso/<int:pk>/editar/', views.editar_caso, name='editar_caso'),
    path('caso/<int:pk>/deletar/', views.deletar_caso, name='deletar_caso'),
    path('mural/', views.mural, name='mural'),
    path('caso/<int:pk>/curtir/', views.curtir_caso, name='curtir_caso'),
    path('caso/<int:pk>/comentar/', views.adicionar_comentario, name='adicionar_comentario'),
]

