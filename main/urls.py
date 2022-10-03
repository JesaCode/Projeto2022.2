from pipes import Template

from django.urls import path

from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index),
    path('registro/', views.registro_cadastro, name='registro'),
    path('registro/criado/', views.registro_criado, name='criado'),
]
