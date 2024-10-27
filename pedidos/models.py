from django.db import models

from django.contrib.auth import get_user_model

from tienda.models import product

from django.db.models import F, Sum, FloatField
# Create your models here.

User=get_user_model()

class Pedido(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    create_at=models.DateTimeField(auto_now_add=True)

    def __st__(self):
        return self.id

    @property
    def  total(self):
        return self.lineapedido_set.aggregate(
            total=Sum(F("precio")*F("cantidad"), Output_field=FloatField())
        )["total"]

    class Meta:
        db_table='pedidos'
        verbose_name='Pedido'
        verbose_name_plural='Pedidos'
        ordering=['id']

class LineaPedido(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    producto=models.ForeignKey(product, on_delete=models.CASCADE)
    pedido=models.ForeignKey(Pedido, on_delete=models.CASCADE)
    cantidad=models.IntegerField(default=1)
    create_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.cantidad } unidades de {self.producto.nombre}'

    class Meta:
        db_table='Linea Pedido'
        verbose_name='Linea Pedido'
        verbose_name_plural='Lineas Pedidos'
        ordering=['id']