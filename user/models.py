from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser): #para colocar propiedades al usuario nuevas
    rh = models.CharField(blank=True, default ='pendiente', max_length=5, null=True) #default =pendiente 