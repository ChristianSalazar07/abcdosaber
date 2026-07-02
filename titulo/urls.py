from django.urls import path
from . import views

app_name = 'titulo'

urlpatterns = [
    path('cadastrar/', views.cadastrar, name='cadastrar'),
    path('listar/', views.listar, name='listar'),
    path('excluir/<int:codigoTitulo>', views.excluir, name='excluir_titulo'),
    path('atualizar/<int:codigoTitulo>', views.atualizar, name='atualizar')
]
