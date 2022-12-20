from django.db import models

# IMPORTAMOS EL MODELO PRODUCTOS PARA
# CREAR LA LOGICA DE CARRITO
from applications.producto.models import Producto

# Create your models here.
class Carrito(models.Model):
    carrito_id = models.CharField(max_length=250, blank=True)
    fecha_creacion = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.carrito_id

class CarritoItem(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    is_active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.producto

class Pedido(models.Model):
    estado_choices = (
        ('P','Pendiente'),
        ('E','Entregado'),
        ('A','Anulado'),
    )
    pago_choices = (
        ('P','Pendiente'),
       ('C','Cancelado'),
    )

    items = models.ForeignKey(CarritoItem, on_delete=models.CASCADE)
    estado = models.CharField(max_length=1, choices=estado_choices, blank=True)
    pago = models.CharField(max_length=1, choices=pago_choices, blank=True)

    def __str__(self):
        return self.id
