from django.urls import path

from .views import ProductoListView,buscarProducto

urlpatterns = [
    path('store/', ProductoListView.as_view(), name='listaproducto'),
    path('store/search-product/', buscarProducto.as_view(), name='search'),
]
