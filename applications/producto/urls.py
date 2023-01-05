from django.urls import path
from . import views
from applications.valoraciones.views import guardar_valoracion

from .views import (ProductoListView,buscarProducto,
                    detalleProducto,productoPorCategoria,
                    productosModa,crearProducto,modificarProducto,eliminarProducto)

urlpatterns = [
    path('store', ProductoListView.as_view(), name='listaproducto'),
    path('store/search-product/', buscarProducto.as_view(), name='search'),
    path('store/<slug:categoria_slug>/<slug:slug>', detalleProducto.as_view(), name='detalle'),
    path('store/<slug:categoria_slug>', productoPorCategoria.as_view(), name='categoria'),

    # GESTION DE PRODUCTOS SOLO ACCEDIDOS POR ADMINISTRADORES
    path('store/create/', crearProducto.as_view(), name='crearProducto'),
    path('store/update-product/<slug:categoria_slug>/<slug:slug>/', modificarProducto.as_view(), name='modificarProducto'),
    path('store/delete-product/<slug:categoria_slug>/<slug:slug>/', eliminarProducto.as_view(), name='eliminarProducto'),


    path('store/moda/', productosModa.as_view(), name='moda'),

    

   


]
