from django.urls import path
from .views import contact, message_list, message_detail

urlpatterns = [
    path('', contact, name='contact'),  # Ruta para el formulario de contacto
    path('messages/', message_list, name='message_list'),  # Ruta para ver todos los mensajes
    path('messages/<int:message_id>/', message_detail, name='message_detail'),  # Ruta para ver un mensaje específico
]
