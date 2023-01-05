from django.urls import path
from .views import valoracion, guardar_valoracion

urlpatterns = [
    path('valoracion/',valoracion,name="valoracion"),
    path('<int:id>', guardar_valoracion, name='guardar-valoracion'),
]