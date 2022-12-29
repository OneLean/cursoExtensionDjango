from django.urls import path

# IMPORTAMOS LAS VISTAS
from .views import *

urlpatterns = [
    path("store/cart/", cart, name="cart"),
    path('store/add_cart/<int:producto_id>',agregar_carrito,name="add_cart"),
    path('store/remove_cart/<int:producto_id>',quitar_carrito,name="remove_cart"),
    path('store/remove_item_cart/<int:producto_id>',quitar_item_carrito,name="remove_item_cart")
]
