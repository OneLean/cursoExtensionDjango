from django.urls import path
from .views import crear_pedido,pedidos

urlpatterns = [
    path('checkout',crear_pedido,name="checkout"),
    path('orders',pedidos,name="pedidos"),
]
