from django.contrib.auth.models import AbstractUser  # Importa la clase AbstractUser para crear un modelo de usuario personalizado


class User(AbstractUser):  # Define un modelo de usuario personalizado que hereda de AbstractUser
    pass  # Indica que no se han añadido campos o métodos adicionales al modelo (puede ser eliminado si no se necesita)