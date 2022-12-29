from .models import Carrito,CarritoItem
from django.core.exceptions import ObjectDoesNotExist


def menu_carrito(request, total=0, quantity=0, carrito_items=None):
    try:
        if request.user.is_authenticated:
            carrito = Carrito.objects.get(usuario=request.user)
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

    return (context)