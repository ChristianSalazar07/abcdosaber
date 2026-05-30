from django.urls import path
from . import views

app_name = 'tipodeatividade'

urlpatterns = [
    path('', views.principal, name='principal'),
]