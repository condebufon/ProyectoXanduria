from django.contrib import admin
from .models import product, category

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display=(
        "id",
        "nombre",
        "imagenCategoria",
        "created",
    )
    # readonly_fields=("created","updated")
    search_fields=("nombre","created") #campo de busqueda
    list_filter=("created",) #Filtrar
    date_hierarchy="created" #visualizacion del filtro

class ProductoAdmin(admin.ModelAdmin):
    list_display=(
        "id",
        "nombre",
        "imagen",
        "contenido",
        # "categorys",
        "mostrar_categorias",
        "precio",
        "disponibilidad",
        "created",
    )
    def mostrar_categorias(self, obj):
        return ", ".join([category.nombre for category in obj.categorys.all()])

    mostrar_categorias.short_description = 'Categorías'
    readonly_fields=("created","updated")
    
    search_fields=("nombre", "contenido", "categorys","precio","created") #campo de busqueda
    list_filter=("created",) #Filtrar
    date_hierarchy="created" #visualizacion del filtro


admin.site.register(product, ProductoAdmin)
admin.site.register(category, CategoryAdmin)