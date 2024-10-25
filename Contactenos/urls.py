from django.urls import path  # Importa la función path para definir rutas
from . import views  # Importa el módulo views que contiene las funciones de vista

from django.conf import settings  # Importa la configuración del proyecto
from django.conf.urls.static import static  # Importa la función para manejar archivos estáticos

urlpatterns = [  # Lista que contiene las rutas de la aplicación
    path('', views.contacto, name="contactenos"),  # Ruta para acceder a la vista contacto
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # Configura el manejo de archivos multimedia