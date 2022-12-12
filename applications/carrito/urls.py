from django.urls import path

# IMPORTAMOS LAS VISTAS
from .views import *

urlpatterns = [
    path("cart/", CarritoListView.as_view(), name="cart"),
    path('add_cart/<int:producto_id>',agregar_carrito,name="add_cart")
]
