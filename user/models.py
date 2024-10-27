from django.contrib.auth.models import AbstractUser  # Importa la clase AbstractUser para crear un modelo de usuario personalizado
from django.db import models  # Importa el módulo models para definir modelos de base de datos



class User(AbstractUser):  # Define un modelo de usuario personalizado que hereda de AbstractUser
    rh = models.CharField(blank=True, default="Pendiente", null=True, max_length=50)  # Campo para el grupo sanguíneo, permite valores en blanco y nulos, con un valor por defecto "Pendiente"
    grupo = models.CharField(blank=True , default="Pendiente" , null=True, max_length=50)
    # pass