from django.shortcuts import render,get_object_or_404

#
from django.db.models import Q

# Create your views here.

from django.urls import reverse_lazy

from django.views.generic import ListView, DetailView

from django.views.generic.edit import CreateView,UpdateView,DeleteView

from .models import Producto

class ProductoListView(ListView):
    model = Producto
    paginate_by = 3
    template_name = 'producto/productos.html'
    ordering= 'nombre_prod'

    def get_context_data(self, **kwargs):
        productos = Producto.objects.all()
        context = super(ProductoListView,self).get_context_data(**kwargs)
        context['productos'] = productos
        return context

class productoPorCategoria(ListView):
    template_name= "producto/productos.html"
    paginate_by = 3

    def get_queryset(self):
        slugRecuperado = self.kwargs['categoria_slug']
        listaFiltrada = Producto.objects.filter(
            categoria__categoria_slug=slugRecuperado
        )
        return listaFiltrada

class buscarProducto(ListView):
    model = Producto
    template_name= "producto/productos.html"
    paginate_by = 3
    ordering= 'nombre_prod'

    def get_queryset(self):
        palabra_clave = self.request.GET.get('kword','')
        resultado = Producto.objects.filter(
            Q(nombre_prod__icontains = palabra_clave)|Q(descripcion__icontains = palabra_clave))
        return resultado

class detalleProducto(DetailView):
    model = Producto
    template_name= "producto/detalleProducto.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['detalle'] = self.get_object()
        return context

class productosModa(ListView):
    model = Producto
    template_name= "producto/productos.html"
    paginate_by = 3

    def get_queryset(self):
        listaFiltrada = Producto.objects.filter(
            Q(categoria__categoria_slug = 'ropa-y-accesorios')|Q(categoria__categoria_slug = 'belleza-e-higiene-personal')
        )
        return listaFiltrada

from django.contrib.auth.mixins import PermissionRequiredMixin

class crearProducto(PermissionRequiredMixin, CreateView):
    template_name = "producto/crear.html"
    model = Producto
    fields = ('__all__')
    success_url = reverse_lazy('listaproducto')
    permission_required = 'producto.change_producto'
    permission_denied_message = 'No estas autorizado para acceder'

class modificarProducto(PermissionRequiredMixin, UpdateView):
    model = Producto
    fields = ('__all__')
    template_name = 'producto/crear.html'
    success_url = reverse_lazy('listaproducto')
    permission_required = 'producto.change_producto'
    permission_denied_message = 'No estas autorizado para acceder'

class eliminarProducto(PermissionRequiredMixin, DeleteView):
    model = Producto
    template_name = 'producto/borrar.html'
    success_url = reverse_lazy('listaproducto')
    permission_required = 'producto.change_producto'
    permission_denied_message = 'No estas autorizado para acceder'
