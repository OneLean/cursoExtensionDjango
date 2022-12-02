from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre_cat = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=500)
    def __str__(self):
        return self.nombre_cat

class Producto(models.Model):
    # Modelo que hace referencia a un producto de la tienda
    nombre_prod = models.CharField(max_length=100, unique=True) # Nombre de producto
    descripcion = models.TextField(max_length=500) # Descripcion de producto
    precio = models.IntegerField()  # Precio de producto
    imagen = models.ImageField(upload_to='productos',blank=True,null=True)  # Imagen de producto
    stock = models.IntegerField()   # Stock de producto
    is_available = models.BooleanField(default=True)    # Disponibilidad de producto
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateField(auto_now=True)

    slug = models.SlugField(max_length=200,unique=True) # Solo sirve para personalizar la url

    def __str__(self):
        return self.nombre_prod
