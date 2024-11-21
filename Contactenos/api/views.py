from rest_framework.viewsets import ModelViewSet
from .serializers import contactSerializer
from Contactenos.models import ContactMessage
from Contactenos.forms import ContactForm

class contactviewset(ModelViewSet):
    queryset=ContactForm
    serializer_class =contactSerializer

   