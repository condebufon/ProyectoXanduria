from django.urls import path  # Importa la función path para definir las rutas de la aplicación
from Principalapp import views  # Importa el módulo views de la aplicación Principalapp

from django.conf import settings  # Importa la configuración del proyecto
from django.conf.urls.static import static  # Importa la función para manejar archivos estáticos y multimedia

urlpatterns = [  # Lista que contiene las rutas de la aplicación
    path('', views.index, name="index"),  # Ruta raíz que llama a la vista 'index' y le asigna el nombre 'index'
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # Configura el manejo de archivos multimedia durante el desarrollo