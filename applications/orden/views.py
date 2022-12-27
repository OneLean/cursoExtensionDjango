from django.shortcuts import render,redirect

from applications.carrito.models import Carrito,CarritoItem

from .models import Pedido, PedidoItem

# Create your views here.

from .forms import pedidoForm

def crear_pedido(request):
    items_del_carrito = CarritoItem.objects.filter(usuario=request.user)
    total = 0
    impuesto = 0
    for item in items_del_carrito:
        total += (item.producto.precio)*(item.quantity)
        print(total)
    
    impuesto = total*0.02
    total_a_pagar = total+impuesto
    print(total_a_pagar)

    context = {
        'items_del_carrito' : items_del_carrito
    }

    if request.method == 'POST':
        form = pedidoForm(request.POST)

        if form.is_valid():
            datos = Pedido() # Nuevo pedido!
            datos.usuario = request.user
            datos.first_name = form.cleaned_data['first_name']
            datos.last_name = form.cleaned_data['last_name']
            datos.telefono = form.cleaned_data['telefono']
            datos.direccion = form.cleaned_data['direccion']
            datos.ciudad = form.cleaned_data['ciudad']
            datos.provincia = form.cleaned_data['provincia']
            datos.codPostal = form.cleaned_data['codPostal']
            datos.total = total_a_pagar
            datos.impuesto = impuesto
            datos.orden = Carrito.objects.get(usuario=request.user)
            datos.save()

            for item in items_del_carrito:
                datosItem = PedidoItem()
                datosItem.orden = datos
                datosItem.usuario = request.user
                datosItem.producto = item.producto
                datosItem.quantity = item.quantity
                datosItem.save()

            items_del_carrito.delete()

            return redirect('pedidos')
    else:
        return render(request,'pedido/pedido.html',context)

def pedidos(request):
    itemsP = Pedido.objects.filter(usuario=request.user)

    context = {
        'pedidos': itemsP,
    }

    return render(request,'pedido/mostrarPedidos.html',context)

def pedidosItem(request,id):
    itemsP = PedidoItem.objects.filter(usuario=request.user,orden__id=id)

    print(itemsP)

    context = {
        'pedidos': itemsP,
        'id_pedido':id,
    }

    return render(request,'pedido/mostrarItemsPedido.html',context)
