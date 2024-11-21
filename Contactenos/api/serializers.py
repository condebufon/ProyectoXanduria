from rest_framework import serializers
from Contactenos.models import (ContactMessage)

class contactSerializer(serializers.ModelSerializer):
    class Meta:
        model =ContactMessage
        fields=['id','name', 'email','subject','message']


