from django.contrib import admin

# IMPORTAMOS LOS MODELOS
from .models import *

class ValoracionProductoAdmin(admin.ModelAdmin):
    list_display = ['usuario','producto','valoracion','resenia','created_at']


# Register your models here.
admin.site.register(ValoracionProducto,ValoracionProductoAdmin)

