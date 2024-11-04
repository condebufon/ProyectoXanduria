from django.urls import path  # Importa la función path para definir rutas
from . import views  # Importa el módulo views que contiene las funciones de vista

urlpatterns = [  # Lista que contiene las rutas de la aplicación
    path('', views.contacto, name="contactenos"),  # Ruta para acceder a la vista contacto
]



