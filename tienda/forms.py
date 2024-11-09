from django import forms
from .models import product

class ProductoForm(forms.ModelForm):
    class Meta:
        model = product
        fields = ['nombre', 'imagen', 'contenido', 'precio', 'categorys']
