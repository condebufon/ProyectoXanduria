from django.urls import path  # Importa la función path para definir las rutas de la aplicación
from . import views  # Importa el módulo views que contiene las funciones de vista
from django.conf import settings  # Importa la configuración del proyecto
from django.conf.urls.static import static  # Importa la función para manejar archivos estáticos y multimedia

urlpatterns = [  # Lista que contiene las rutas de la aplicación
    path('', views.tienda, name="tienda"),  # Ruta para acceder a la vista 'tienda' y le asigna el nombre 'tienda'
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # Configura el manejo de archivos multimedia durante el desarrollo