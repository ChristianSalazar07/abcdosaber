from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='titulo_index'),
    path('show_view/', views.show_view, name='show_view'),
    path('listar_exemplo/', views.listar_exemplo, name='listar_exemplo'),
    path('abc/', views.abc, name='abc'),
]
