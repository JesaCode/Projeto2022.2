from pipes import Template
from django.urls import path

from . import views

urlpatterns = [
    path('cadastro/', views.cadastro),
    path('', views.index)
]
