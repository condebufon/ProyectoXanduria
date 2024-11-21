from rest_framework import serializers
from autenticacion.models import Autologin

class autoSerializer(serializers.ModelSerializer):
    class Meta:
        model =Autologin
        fields=['id','name', 'email']


