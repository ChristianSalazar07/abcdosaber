from django.urls import path
from . import views

app_name = 'turma'

urlpatterns = [
    path('', views.principal, name='principal'),
]