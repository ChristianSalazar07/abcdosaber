from django.urls import path
from . import views

urlpatterns = [
    path('cadastrar_aluno', views.cadastrar_aluno, name='cadastrar_aluno'),
    path('listar_aluno/', views.listar_aluno, name='listar_aluno'),
]