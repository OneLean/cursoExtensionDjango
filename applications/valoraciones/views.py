from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.http import HttpResponse
from applications.producto.models import Producto
from .models import ValoracionProducto

# Create your views here.
def valoracion(request):
    return render(request, 'valoracion/valoracion.html', {})


def guardar_valoracion(request,id):
    producto = Producto.objects.get(pk=id)
    user=request.user
    review=ValoracionProducto.objects.create(
        usuario = user,
        producto = producto,
        valoracion = request.POST['valoracion'],
        resenia = request.POST['resenia'],
    )

    return redirect('store/'+ producto.categoria.categoria_slug +'/'+ producto.slug)
