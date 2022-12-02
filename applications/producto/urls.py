from django.urls import path

from .views import ProductoListView

urlpatterns = [
    path('store/', ProductoListView.as_view(), name='listaproducto')
]
