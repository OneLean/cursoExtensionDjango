from django.shortcuts import render,redirect
from applications.producto.models import Producto
from .models import Carrito,CarritoItem

# Create your views here.
def _carrito_id(request):
    carrito = request.session.session_key
    if not carrito:
        carrito = request.session.create()
    return carrito

def agregar_carrito(request, producto_id):
    producto = Producto.objects.get(id=producto_id)
    try:
        carrito = Carrito.objects.get(carrito_id=_carrito_id(request))
    except Carrito.DoesNotExist:
        carrito = Carrito.objects.create(
            carrito_id=_carrito_id(request)
        )
    carrito.save()

    try:
        carrito_item = CarritoItem.objects.get(producto=producto,carrito=carrito)
        carrito_item.quantity += 1
        carrito_item.save()
    except CarritoItem.DoesNotExist:
        carrito_item = CarritoItem.objects.create(
            producto=producto,
            quantity = 1,
            carrito = carrito
        )
        carrito_item.save()
    return redirect('cart')

from django.views.generic import ListView

class CarritoListView(ListView):
    model = CarritoItem
    template_name = 'carrito/carrito.html'
    ordering= 'producto'

    def get_context_data(self, **kwargs):
        productos = CarritoItem.objects.all()
        context = super(CarritoListView,self).get_context_data(**kwargs)
        context['itemsCarrito'] = productos
        return context
