from rest_framework import serializers
from tienda.models import (product)

class productSerializer(serializers.ModelSerializer):
    class Meta:
        model =product
        fields=['id','nombre', 'contenido','precio']
