from django.db import models

# Create your models here.
from applications.usuario.models import User
from applications.producto.models import Producto

class ValoracionProducto(models.Model):
    VALORACION_CHOICES=(
        ('1','★'),
        ('2','★★'),
        ('3','★★★'),
        ('4','★★★★'),
        ('5','★★★★★'),                        

    )   
    usuario = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    producto = models.ForeignKey(Producto,on_delete=models.CASCADE, null=True)
    valoracion = models.CharField(choices=VALORACION_CHOICES,max_length=20,default='5')
    resenia = models.TextField(null=True,blank=True)
    created_at = models.DateTimeField( auto_now_add = True, null=True)

    def __str__(self):
        return self.valoracion
