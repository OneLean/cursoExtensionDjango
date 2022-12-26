from django.db import models

# IMPORTAMOS EL MODELO PRODUCTOS PARA
# CREAR LA LOGICA DE CARRITO
from applications.producto.models import Producto
from applications.usuario.models import User

# Create your models here.
class Carrito(models.Model):
    usuario = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    carrito_id = models.CharField(max_length=250, blank=True) # Borro este atributo?
    fecha_creacion = models.DateField(auto_now_add=True)

    def __str__(self):
        return 'Carrito ID - '+str(self.id)

class CarritoItem(models.Model):
    usuario = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.producto.nombre_prod