from django.db import models

# Create your models here.

class category(models.Model):
    nombre          =models.CharField(max_length=50)
    imagenCategoria =models.ImageField(upload_to='Categoria_Tienda', null=True, blank=True)
    created         =models.DateTimeField(auto_now_add=True)
    updated         =models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='categoria'
        verbose_name_plural='categorias'

    def __str__(self):
        return self.nombre

class product(models.Model):
    nombre          =models.CharField(max_length=50)
    imagen          =models.ImageField(upload_to='media/tienda', null=True, blank=True)
    categorys       =models.ManyToManyField(category)
    contenido       =models.CharField(max_length=1000)    
    precio          =models.FloatField()
    disponibilidad  =models.BooleanField(default=True)
    created         =models.DateTimeField(auto_now_add=True)
    updated         =models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='producto'
        verbose_name_plural='productos'

    def __str__(self):
        return self.nombre