from rest_framework.viewsets import ModelViewSet
from .serializers import autoSerializer
from autenticacion.models import Autologin

class autoViewset(ModelViewSet):
    queryset=Autologin.objects.all
    serializer_class =autoSerializer

   