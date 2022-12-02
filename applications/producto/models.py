from django.db import models

# Create your models here.´

"""
class Producto(models.Model):
    # Modelo que hace referencia a un producto de la tienda
    nombre_prod = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=500)
    precio = models.IntegerField()
    imagen = models.ImageField()
    stock = models.IntegerField()
    is_available = models.BooleanField()
    fecha_creacion = models.DateField()
    fecha_modificacion = models.DateField()
    categoria = models.ForeignKey(Categoria, null=True, blank=True)
    slug = models.SlugField(max_length=25)

    def __str__(self):
        return self.nombre_prod
"""