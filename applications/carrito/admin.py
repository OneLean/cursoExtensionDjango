from django.contrib import admin

# IMPORTAMOS LOS MODELOS
from .models import *

class ItemCarritoAdmin(admin.ModelAdmin):
    list_display = ['producto','usuario','carrito','quantity']
    list_per_page = 10

class CarritoAdmin(admin.ModelAdmin):
    list_display = ['id','usuario']
    list_per_page = 10

# Register your models here.
admin.site.register(Carrito,CarritoAdmin)
admin.site.register(CarritoItem,ItemCarritoAdmin)

