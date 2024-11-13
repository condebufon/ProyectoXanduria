from django.shortcuts import render, redirect, get_object_or_404
from .forms import ContactForm
from .models import ContactMessage
from django.http import HttpResponseRedirect
from django.urls import reverse


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_message = ContactMessage(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                subject=form.cleaned_data.get('subject'),  # Obtener el asunto si está presente
                message=form.cleaned_data['message'],
                
            )
            contact_message.save()  # Aquí es donde podría fallar si 'subject' no es permitido
            return redirect('index')  # Redirigir a una página de éxito
    else:
        form = ContactForm()

    messages = ContactMessage.objects.all()  # Obtener todos los mensajes
    return render(request, 'contact.html', {'form': form, 'messages': messages})

def message_list(request):
    messages = ContactMessage.objects.all()  # Obtener todos los mensajes
    return render(request, 'messages.html', {'messages': messages})

def message_detail(request, message_id):
    message = get_object_or_404(ContactMessage, id=message_id)  # Obtener el mensaje por ID
    return render(request, 'message_detail.html', {'message': message})

def delete_message(request, message_id):
    message = get_object_or_404(ContactMessage, id=message_id)  # Obtener el mensaje por ID
    message.delete()  # Eliminar el mensaje
    return HttpResponseRedirect(reverse('message_list'))  # Redirigir a la lista de mensajes
