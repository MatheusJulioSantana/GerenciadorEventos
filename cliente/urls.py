# Arquivo urls.py
from django.urls import path
from . import views

# Define as URLs da aplicação
urlpatterns = [
    path("meus_certificados/", views.meus_certificados, name="meus_certificados"),
]
