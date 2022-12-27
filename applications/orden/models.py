from django.db import models

from applications.usuario.models import User
from applications.producto.models import Producto
from applications.carrito.models import Carrito

# Create your models here.
class Pedido(models.Model):
    estado_choices = (
        ('Pendiente','Pendiente'),
        ('Entregado','Entregado'),
        ('Anulado','Anulado'),
    )
    pago_choices = (
        ('Pendiente','Pendiente'),
        ('Cancelado','Cancelado'),
    )
    # Datos del usuario que compra:
    usuario = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    first_name = models.CharField(max_length=200, null=True)
    last_name = models.CharField(max_length=200, null=True)
    direccion = models.CharField(max_length=200, null=True)
    telefono = models.CharField(max_length=50, null=True)
    ciudad = models.CharField(max_length=200, null=True)
    provincia = models.CharField(max_length=200, null=True)
    codPostal = models.CharField(max_length=200, null=True)
    fecha = models.DateTimeField(auto_now_add=True)

    total = models.IntegerField()
    impuesto = models.IntegerField()

    orden = models.ForeignKey(Carrito, on_delete=models.CASCADE, null=True)
    estado = models.CharField(max_length=100, choices=estado_choices,default='Pendiente', blank=True)
    pago = models.CharField(max_length=100, choices=pago_choices,default='Pendiente', blank=True)

    def __str__(self):
        return 'Pedido Nº '+ str(self.id)

class PedidoItem(models.Model):
    orden = models.ForeignKey(Pedido, on_delete=models.CASCADE, null=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    producto = models.ForeignKey(Producto,on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField()

    fechaCreacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Item id "+str(self.id)+" de Pedido Nº "+str(self.orden.id)