from django.urls import path

from .views import ProductoListView,buscarProducto,detalleProducto

urlpatterns = [
    path('store/', ProductoListView.as_view(), name='listaproducto'),
    path('store/search-product/', buscarProducto.as_view(), name='search'),
    path('store/<slug:categoria_slug>/<slug:slug>', detalleProducto.as_view(), name='detalle'),
]
