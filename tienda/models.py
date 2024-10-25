from django.db import models


class category(models.Model):
    nombre = models.CharField(max_length=50)
    imagenCategoria = models.ImageField(
        upload_to="categoria_tienda", null=True, blank=True
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "categoria"
        verbose_name_plural = "categorias"

    def __str__(self):
        return self.nombre


# Create your models here.


class Product(models.Model):
    nombre = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to="tienda", null=True, blank=True)
    categorias = models.ManyToManyField(category)
    contenido = models.CharField(max_length=1000)
    precio = models.CharField(max_length=1000)
    disponibilidad = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "producto"
        verbose_name_plural = "productos"

    def __str__(self):
        return self.nombre
