from django.shortcuts import render
from tienda.models import product

# Create your views here.

def tienda(request):    
    products=product.objects.all()
    return render(request, "tienda.html", {"products":products})
