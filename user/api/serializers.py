from rest_framework import serializers
from user.models import User

class userSerializer(serializers.ModelSerializer):
    class Meta:
        model =User
        fields=['id','rh', 'grupo',]


