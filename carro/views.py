from django.shortcuts import render, redirect

# from django.shortcuts import redirect
from .carro import Carro
from tienda.models import Product

# Create your views here.


def agregar_producto(request, producto_id):
    carro = Carro(request)  # Obtener el carrito de compras asociado a la sesión
    producto = Product.objects.get(
        id=producto_id
    )  # Obtener el producto de la base de datos
    carro.agregar(producto=producto)  # Agregar el producto al carrito
    return redirect("tienda")


def eliminar_producto(request, producto_id):
    carro = Carro(request)
    producto = Product.objects.get(id=producto_id)
    carro.eliminar(producto=producto)
    return redirect("tienda")


def restar_producto(request, producto_id):
    carro = Carro(request)
    producto = Product.objects.get(id=producto_id)
    carro.restar_producto(producto=producto)
    return redirect("tienda")


def limpiar_carro(request, producto_id):
    carro = Carro(request)
    carro.limpiar_carro
    return redirect("tienda")


def carrito_total(request):
    carro = Carro(request)
    total = carro.total_precio()  # Llamar a la función para obtener el total

    return redirect("tienda")
    # Renderizar la plantilla con el contexto
