"""
URL configuration for ProyectoXanduria project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.contrib import admin  # Importa el módulo admin para gestionar el panel de administración de Django
from django.urls import path, include  # Importa las funciones path e include para definir rutas

urlpatterns = [  # Lista que contiene todas las rutas del proyecto
    path('admin/', admin.site.urls),  # Ruta para acceder al panel de administración de Django
    path('', include('Principalapp.urls')),  # Incluye las rutas definidas en 'Principalapp.urls' para la ruta raíz
    path('contactenos/', include('Contactenos.urls')),  # Incluye las rutas definidas en 'Contactenos.urls' para la ruta raíz
    # path('registro/', include('registro.urls')),  # Incluye las rutas definidas en 'registro.urls' para la ruta raíz
    path('tienda/', include('tienda.urls')),  # Incluye las rutas definidas en 'tienda.urls' para la ruta raíz
    path('carro', include('carro.urls')),
    path('autenticacion/', include('autenticacion.urls')),
]
