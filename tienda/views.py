from django.shortcuts import render
from tienda.models import Product


def tienda(request):  # Crear la vista llamada 'tienda'
    products = Product.objects.all()  # Obtener todos los productos de la base de datos
    return render(
        request, "tienda.html", {"products": products}
    )  # Renderizar la plantilla 'tienda.html' y pasar los productos como contexto
