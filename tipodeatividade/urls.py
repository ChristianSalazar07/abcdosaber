from django.urls import path
from . import views

app_name = 'tipodeatividade'

urlpatterns = [
    path('listar', views.listar, name='listar'),
    path('cadastrar', views.cadastrar, name='cadastrar'),
    path('excluir/<int:codigoAtividade>', views.excluir, name='excluir_atividade'),
    path('atualizar/<int:codigoAtividade>', views.atualizar, name='atualizar')
]