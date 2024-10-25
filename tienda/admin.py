from django.contrib import admin  # Importa el módulo admin para gestionar el panel de administración de Django
from .models import Product, category  # Importa el modelo 'product' desde el archivo models.py de la misma aplicación

# class ProductoAdmin(admin.ModelAdmin):  # Define una clase para personalizar la administración del modelo 'product'
#     readonly_fields = ("created", "updated")  # Especifica que los campos 'created' y 'updated' son de solo lectura en el panel de administración

# admin.site.register(product, ProductoAdmin)  # Registra el modelo 'product' con su configuración personalizada en el panel de administración

class categoryAdmin(admin.ModelAdmin):  # Define una clase para personalizar la administración del modelo 'product'
    list_display=(
        "id",
        "nombre",
        "imagenCategoria",
        "created",
    )
    # readonly_fields = ("created", "updated")  # Especifica que los campos 'created' y 'updated' son de solo lectura en el panel de administración
    search_fields=("nombre", "created")#campo de busqueda
    list_filter=("created",)# filtro
    date_hierarchy="created"# visualizador del filtro

class productAdmin(admin.ModelAdmin):
    list_display=(
        "nombre",
        "imagen",
        "contenido",
        "precio",   
        "disponibilidad",
        "created",
        "updated",
    )
    search_fields=("nombre", "contenido","precio","created","updated")#campo de busqueda
    list_filter=("created",)# filtro
    date_hierarchy="created"# visualizador del filtro

admin.site.register(Product, productAdmin)  # Registra el modelo 'product' con su configuración personalizada en el panel de administración
admin.site.register(category, categoryAdmin)# Registra el modelo 'category' con su configuración personalizada en el panel de administración



        