"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

# Importamos las configuraciones para
# poder cargar imagenes NO estaticas
from django.conf import settings
from django.conf.urls.static import static

from applications.home.views import Error404View, Error403View

urlpatterns = [
    path('admin/', admin.site.urls),
    # Incluimos las urls de las aplicaciones
    #URLs de carrito
    path('', include('applications.carrito.urls')),
    #URLs de home
    path('', include('applications.home.urls')),
    #URLs de producto
    path('', include('applications.producto.urls')),
    #URLs de usuario
    path('', include('applications.usuario.urls')),
    #Django-Reload-Browser
    path("__reload__/", include("django_browser_reload.urls")),
] + static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

handler404 = Error404View.as_view()
handler403 = Error403View.as_view()