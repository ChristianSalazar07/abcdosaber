from django.urls import path
from . import views

urlpatterns = [
    path('cadastrar_titulo', views.cadastrar_titulo, name='cadastrar_titulo'),
    path('listar_titulo/', views.listar_titulo, name='listar_titulo'),
    path('abc/', views.abc, name='abc'),
]
