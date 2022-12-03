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

class buscarProducto(ListView):
    model = Producto
    template_name= "producto/buscar_prod.html"
    context_object_name="productos"

    def get_queryset(self):
        palabra_clave = self.request.GET.get('kword','')
        resultado = Producto.objects.filter(
            nombre_prod__icontains = palabra_clave
        )
        return resultado

