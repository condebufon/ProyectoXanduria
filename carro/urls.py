from django.urls import path
from . import views

app_name = "carro"  # Define un nombre para la aplicación, útil para referenciar las rutas en las plantillas y vistas.


urlpatterns = [
    path("agregar/<int:producto_id>/", views.agregar_producto, name="agregar"),
    path("eliminar/<int:producto_id>/", views.eliminar_producto, name="eliminar"),
    path("restar/<int:producto_id>/", views.restar_producto, name="restar"),
    path("limpiar/", views.limpiar_carro, name="limpiar"),
    path(
        "total/", views.carrito_total, name="total"
    ),  # Ruta para ver el total del carrito
]
