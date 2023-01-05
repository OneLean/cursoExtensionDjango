from django.shortcuts import render

# AQUI IMPORTAMOS LAS VISTAS GENERICAS
from django.views.generic import ListView, TemplateView

# DE AQUI IMPORTAMOS LOS MODELOS DE LA
# OTRA APLICACION
from applications.producto.models import Producto

# AQUI VAN LAS VISTAS DE HOME
# FUNCION DE VISTA HOME
#   def home(request):
#       return render(request, 'home/base.html', {})

# VISTA BASADA EN CLASES
# Esta vista muestra la parte principal de la web
# Explicacion: es un listView porque lista los 
# productos que sean populares
class inicio(ListView):
    # Ubicacion de la plantilla a renderizar
    template_name = "home/home.html"
    # Nombre de contexto con el que llamamos a los objetos
    # en la plantilla
    context_object_name = 'productoshome'

    # Funcion que filtra los productos populares
    def get_queryset(self):
        resultado = Producto.objects.filter(
            es_popular = True)
        return resultado

# Acá se define que se va a mostrar ante los
# errores de tipo 404, 403, etc...
class Error404View(TemplateView):
    template_name = "home/error404.html"

class Error403View(TemplateView):
    template_name = "home/error403.html"

# Aquí tambien se podria agregar el error 500 por ejemplo...