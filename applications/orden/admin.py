from django.contrib import admin

from .models import  Pedido,PedidoItem

class itemsDelPedido(admin.TabularInline):
    model = PedidoItem
    readonly_fields = ('producto','quantity')
    extra = 0

class PedidoAdmin(admin.ModelAdmin):
    list_display = ['id','last_name', 'telefono','ciudad','total','estado','pago']
    list_filter = ['estado']
    search_fields =['id','last_name','telefono','ciudad']
    list_per_page = 10
    inlines = [itemsDelPedido]

# Register your models here.
admin.site.register(Pedido,PedidoAdmin)
admin.site.register(PedidoItem)