from django.urls import path
from .views import valoracion

urlpatterns = [
    path('valoracion/',valoracion,name="valoracion"),
]