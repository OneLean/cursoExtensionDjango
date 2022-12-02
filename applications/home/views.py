from django.shortcuts import render

# AQUI IMPORTAMOS LAS VISTAS GENERICAS
from django.views.generic import TemplateView


# AQUI VAN LAS VISTAS DE HOME

# FUNCION DE VISTA HOME
#   def home(request):
#       return render(request, 'home/base.html', {})

# VISTA BASADA EN CLASES

class inicio(TemplateView):
    template_name = "home/home.html"