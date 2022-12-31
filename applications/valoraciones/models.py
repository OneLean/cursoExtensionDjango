from django.db import models

# Create your models here.
from applications.usuario.models import User
from applications.producto.models import Producto

class ValoracionProducto(models.Model):
    valoracion_choices=(
        (1,'1'),
        (2,'2'),
        (3,'3'),
        (4,'4'),
        (5,'5'),                        

    )   
    usuario = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    producto = models.ForeignKey(Producto,on_delete=models.CASCADE, null=True)
    valoracion = models.CharField(choices=valoracion_choices,max_length=150)
    resenia = models.TextField(null=True,blank=True)

    def __str__(self):
        return 'Valoracion N° '+ str(self.id)
