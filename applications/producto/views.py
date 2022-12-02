from django.shortcuts import render

# Create your views here.

from django.views.generic.list import ListView

from .models import Producto

class ProductoListView(ListView):

    model = Producto
    paginate_by = 2  # if pagination is desired
    template_name = 'producto/productos.html'

    def get_context_data(self, **kwargs):
        productos = Producto.objects.all()
        context = super().get_context_data(**kwargs)
        context['productos'] = productos
        return context
    