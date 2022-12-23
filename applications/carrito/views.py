from django.shortcuts import render,redirect
from applications.producto.models import Producto
from applications.usuario.models import User
from .models import Carrito,CarritoItem

# Create your views here.
def _carrito_id(request):
    carrito = request.session.session_key
    if not carrito:
        carrito = request.session.create()
    return carrito

def agregar_carrito(request, producto_id):
    if request.user.is_authenticated:
        producto = Producto.objects.get(id=producto_id)
        try:
            carrito = Carrito.objects.get(usuario__id=request.user.id)
        except Carrito.DoesNotExist:
            carrito = Carrito.objects.create(
                usuario=request.user,
                carrito_id=request.user.id
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
                carrito = carrito,
            )
            carrito_item.save()
        return redirect('cart')
    else:
        # no está logueado asi que no se puede agregar ningun carrito
        return redirect('listaproducto')

from django.shortcuts import get_object_or_404


def quitar_carrito(request, producto_id):
    carrito = Carrito.objects.get(usuario__id=request.user.id)
    producto = get_object_or_404(Producto, id=producto_id)
    carrito_item = CarritoItem.objects.get(producto=producto,carrito=carrito)

    if carrito_item.quantity > 1:
        carrito_item.quantity -= 1  
        carrito_item.save()
    else:
        carrito_item.delete()
    
    return redirect('cart')

def quitar_item_carrito(request, producto_id):
    carrito = Carrito.objects.get(usuario__id=request.user.id)
    producto = get_object_or_404(Producto, id=producto_id)
    carrito_item = CarritoItem.objects.get(producto=producto,carrito=carrito)

    carrito_item.delete()
    
    return redirect('cart')

from django.core.exceptions import ObjectDoesNotExist

def cart(request, total=0, quantity=0, carrito_items=None):
    try:
        carrito = Carrito.objects.get(usuario__id=request.user.id)
        carrito_items = CarritoItem.objects.filter(carrito=carrito,is_active=True)
        for carrito_item in carrito_items:
            total += (carrito_item.producto.precio*carrito_item.quantity)
            quantity += carrito_item.quantity
        impuesto=0.02*total
        totalPagar=total+impuesto

    except ObjectDoesNotExist:
        impuesto=0
        totalPagar=0
        pass # Lo que ignora la excepcion

    context = {
        'total': total,
        'quantity': quantity,
        'carrito_items': carrito_items,
        'impuesto':impuesto,
        'totalPagar':totalPagar,
    }

    return render(request, 'carrito/carrito.html', context)
