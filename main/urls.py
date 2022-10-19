from pipes import Template

from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index),
    path('registro/', views.registro_cadastro, name='registro'),
    path('login/', views.login, name='login'),
    # path('registro/criado/', views.registro_criado, name='criado'),
]


#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
