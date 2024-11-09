from tienda.models import product
from django.shortcuts import render, get_object_or_404, redirect
from carro.carro import Carro
from user.models import User
from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
User=get_user_model()

from .forms import ProductoForm



def tienda(request):    
    products=product.objects.all()
    return render(request, "tienda.html", {"products":products})

# Crear un nuevo producto
def crear_producto(request):
    if request.method == 'POST':  # verifica si el método de la solicitud es POST
        form = ProductoForm(request.POST, request.FILES) # formulario se llena con los datos que el usuario ha enviado.
        if form.is_valid(): # si todos los datos proporcionados cumplen con las restricciones definidas en el modelo y el formulario
            producto = form.save(commit=False)
            # form.save() # se guarda el nuevo producto en la base de datos
            if not request.FILES.get('imagen'):  # Verificar si no se subió una imagen
            # Asignar una imagen por defecto si no se subió ninguna
                 default_image = open('ruta/a/la/imagen/por_defecto.jpg', 'rb')
                 product.imagen = SimpleUploadedFile(
                'imagen_por_defecto.jpg',
                default_image.read(),
                content_type='image/jpeg'
                )
            producto.save()  # Ahora guardar el producto
            
            return redirect('index')
    else:   # Si el método de la solicitud no es POST, se crea un nuevo formulario vacío.
        form = ProductoForm()  # Aquí se crea el formulario vacío
    return render(request, 'crear_product.html', {'form': form}) # Finalmente, se renderiza la plantilla crear_producto.html, pasando el formulario como context.

# Actualizar un producto
def actualizar_producto(request, id): # recibe dos parámetros: request, que es el objeto de la solicitud HTTP, y id
    producto = get_object_or_404(product, id=id) #Aquí se utiliza para buscar el producto en la base de datos utilizando el id.
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto) #Se crea una instancia del formulario ProductoForm, pasando request.POST para llenar el formulario con los datos enviados, y instance=producto para que el formulario esté asociado con el producto que se va a actualizar.
        if form.is_valid(): # Se comprueba si el formulario es válido.
            form.save()
            return redirect('index') # se renderiza la plantilla actualizar_producto.html
    else:
        form = ProductoForm(instance=producto) #Si el método de la solicitud no es POST, se crea un nuevo formulario y se llena con los datos del producto existente utilizando instance=producto. Esto permite mostrar los datos actuales del producto en el formulario.
    return render(request, 'actualizar_producto.html', {'form': form})

# Eliminar un producto
def eliminar_producto(request, id):
    producto = get_object_or_404(product, id=id)
    if request.method == 'POST':
        producto.delete()
        return redirect('index')
    return render(request, 'crear_product.html', {'producto': producto})