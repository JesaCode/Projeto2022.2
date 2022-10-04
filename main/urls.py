from pipes import Template
from django.urls import path
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path('cadastro/', views.cadastro),
    path('', views.index)
]


#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)