from django.contrib import admin

# IMPORTAMOS LOS MODELOS
from .models import *

# Register your models here.
admin.site.register(Carrito)
admin.site.register(CarritoItem)

