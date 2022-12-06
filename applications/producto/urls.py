from django.urls import path
from . import views

from .views import ProductoListView,buscarProducto,detalleProducto,productoPorCategoria

urlpatterns = [
    path('store/', ProductoListView.as_view(), name='listaproducto'),
    path('store/search-product/', buscarProducto.as_view(), name='search'),
    path('store/<slug:categoria_slug>/<slug:slug>', detalleProducto.as_view(), name='detalle'),
    path('store/<slug:categoria_slug>', productoPorCategoria.as_view(), name='categoria'),

]
