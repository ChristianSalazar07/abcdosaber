from django.urls import path
from . import views

app_name = 'turma'

urlpatterns = [
    path('listar', views.listar, name='listar'),
    path('cadastrar', views.cadastrar, name='cadastrar'),
    path('ausencia', views.ausencia, name='ausencia'),
]