from django.urls import path

# Importamos las vistas
from .views import *

# Importamos el manejador de errores 400,500
from django.conf.urls import handler404

urlpatterns = [
    path('', inicio.as_view(), name="home"),
]



