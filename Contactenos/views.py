from django.shortcuts import render  # Importa la función render para renderizar plantillas
from django.conf import settings
from django.core.mail import send_mail


def contacto(request):  # Define la vista 'contacto' que recibe un objeto request
    # return render(request, "contactenos.html")  # Renderiza la plantilla 'contactenos.html' y la devuelve como respuesta
    if request.method == "POST":
        nombre =request.POST["nombre"]
        edad =request.POST["edad"]
        email =request.POST["email"]
        subject=request.POST["subject"] 
        mensaje=request.POST["mensaje"] 
        from_email= settings.EMAIL_HOST_USER
        recipient_list=["soportesgamer@gmail.com"]#Lista con las direcciones de los destinatarios.
        send_mail(subject,mensaje,from_email,recipient_list) #Lista con las direcciones de los destinatarios.
        
    return render(request, "contactenos.html")