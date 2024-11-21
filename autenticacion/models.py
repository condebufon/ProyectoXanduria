from django.db import models

class Autologin(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    
    
    def __str__(self):
        return f"{self.name} - {self.email}"