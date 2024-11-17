from rest_framework import viewsets
from .serializers import productSerializer
from tienda.models import product

class productviewset(viewsets.ModelViewSet):
    queryset=product.objects.all()
    serializer_class =productSerializer