from django.shortcuts import render

# AQUI IMPORTAMOS LAS VISTAS GENERICAS
from django.views.generic import ListView

# DE AQUI IMPORTAMOS LOS MODELOS DE LA
# OTRA APLICACION
from applications.producto.models import Producto

# AQUI VAN LAS VISTAS DE HOME

# FUNCION DE VISTA HOME
#   def home(request):
#       return render(request, 'home/base.html', {})

# VISTA BASADA EN CLASES

class inicio(ListView):
    model: Producto
    template_name = "home/home.html"
    paginate_by: 2
    context_object_name = 'productoshome'

    def get_queryset(self):
        resultado = Producto.objects.filter(
            es_popular = True)
        return resultado