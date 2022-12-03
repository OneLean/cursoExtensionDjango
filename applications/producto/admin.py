from django.contrib import admin

# Se importan los modelos de models.py que
# se quieran registrar en el administrador de Django
from .models import Categoria, Producto


# Paquete para mostrar fotos en el administrador Django
from django.utils.html import format_html

# Visualizacion de productos en el
# administrador de Django
class  ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre_prod', 'descripcion', 'precio', 'categoria','fotoAdmin')
    prepopulated_fields = {'slug':('nombre_prod',)}
    
    def fotoAdmin(self,obj):
        return format_html('<img src={} width="100" />', obj.imagen.url)

class  CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre_cat',)
    prepopulated_fields = {'categoria_slug':('nombre_cat',)}

# Registro los modelos
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Producto, ProductoAdmin)
