from django.urls import path

# Importamos las vistas

from . import views

urlpatterns = [
    path('', views.inicio.as_view(), name="home"),
]
