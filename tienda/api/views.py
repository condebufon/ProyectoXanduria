from rest_framework.viewsets import ModelViewSet
from .serializers import productSerializer
from tienda.models import product

class productviewset(ModelViewSet):
    queryset=product.objects.all()
    serializer_class =productSerializer