from django.shortcuts import (
    render,
)  # Importa la función render para renderizar plantillas
from carro.carro import Carro


def index(request):  # Define la vista 'index' que recibe un objeto request
    carro = Carro(request)  # Obtiene todos los carros
    return render(
        request, "index.html"
    )  # Renderiza la plantilla 'index.html' y la devuelve como respuesta
