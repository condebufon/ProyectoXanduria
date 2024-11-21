from rest_framework import viewsets
from .serializers import userSerializer
from user.models import (User)

class userviewset(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class =userSerializer

   