from django.shortcuts import render
from django.shortcuts import redirect
from .carro import Carro
from tienda.models import product

# Create your views here.

def agregar_producto(request, producto_id):
    carro=Carro(request)    #Obtener el carrito de compras asociado a la sesión
    producto=product.objects.get(id=producto_id)    #Obtener el producto de la base de datos
    carro.agregar(producto=producto)    #Agregar el producto al carrito
    return redirect("tienda")

def eliminar_producto(request, producto_id):
    carro=Carro(request)
    producto=product.objects.get(id=producto_id)
    carro.eliminar(producto=producto)
    return redirect("tienda")

def restar_producto(request, producto_id):
    carro=Carro(request)
    producto=product.objects.get(id=producto_id)
    carro.restar_producto(producto=producto)
    return redirect("tienda")

def limpiar_carro(request, producto_id):
    carro=Carro(request)
    carro.limpiar_carro
    return redirect("tienda")