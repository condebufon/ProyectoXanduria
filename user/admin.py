from django.contrib import admin  # Importa el módulo admin para gestionar el panel de administración de Django
from django.contrib.auth.admin import UserAdmin  # Importa la clase UserAdmin para personalizar la administración del modelo de usuario
from user.models import User  # Importa el modelo 'User' desde el archivo models.py de la aplicación 'user'

# Register your models here.

@admin.register(User)  # Decora la clase UserAdmin para registrar el modelo 'User' en el panel de administración
class UserAdmin(UserAdmin):  # Define una clase personalizada para la administración del modelo 'User', heredando de UserAdmin
    fieldsets = (  # Define los grupos de campos que se mostrarán en el formulario de edición del usuario
        (None, {"fields": ('username', 'password'),}),  # Grupo sin título con campos 'username' y 'password'
        #('Informacion Personal', {"fields": ('first_name', 'last_name', 'email'),}),  # Grupo con información personal 
        ('Permissions', {"fields": ('is_active', 'is_staff','is_superuser','grupo','user_permissions'),}),
    )
    list_display = [
                    'id',
                    'username',
                    'email',
                    'pais',
                    'grupo',
                 ]
    # pass # Indica que no hay más código en esta clase (puede ser eliminado si no se necesita)