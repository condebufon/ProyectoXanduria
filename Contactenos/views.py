from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail



def contacto(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        subject = request.POST["subject"]
        message = request.POST["message"]
        from_email =  settings.EMAIL_HOST_USER
        recipient_list=["xanduria@outlook.com"]
        send_mail(name, email, subject, message, from_email, ['xanduria@outlook.com'])
        return render(request,"index.html")

    return render(request,"contactenos.html")

#-------------correccion 2 ------------------
# from django.shortcuts import render
# from django.conf import settings
# from django.core.mail import send_mail
# from django.contrib import messages  # Importa el módulo para enviar mensajes

# def contacto(request):
#     if request.method == "POST":
#         nombre = request.POST.get("nombre")
#         edad = request.POST.get("edad")
#         email = request.POST.get("email")
#         subject = request.POST.get("subject")
#         mensaje = request.POST.get("mensaje")
#         from_email = settings.EMAIL_HOST_USER
#         recipient_list = ["xanduria@outlook.com"]

#         # Envío del correo
#         try:
#             send_mail(
#                 subject,
#                 f"Nombre: {nombre}\nEdad: {edad}\nEmail: {email}\nMensaje: {mensaje}",
#                 from_email,
#                 recipient_list,
#                 fail_silently=False,
#             )
#             messages.success(request, "El mensaje ha sido enviado con éxito.")
#         except Exception as e:
#             messages.error(request, f"Error al enviar el mensaje: {str(e)}")

#     return render(request, "contactenos.html")



