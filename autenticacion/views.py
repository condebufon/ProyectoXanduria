# views.py
from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


def Vregistro(request):
    if request.method == "POST":
        form = UserRegistrationForm(
            request.POST
        )  # se crea una instancia del formulario UserRegistrationForm con los datos ingresados por el usuario
        if form.is_valid():
            user = form.save(
                commit=False
            )  # evita que se guarde inmediatamente en la base de datos.
            user.set_password(
                form.cleaned_data["password"]
            )  # cifrar la contraseña ingresada por el usuario antes de guardarla de forma segura en la base de datos
            user.save()  # guarda el usuario
            return redirect("login")
    else:
        form = (
            UserRegistrationForm()
        )  # muestra un formulario vacío para que el usuario pueda registrarse.

    return render(request, "registro/registro.html", {"form": form})


def cerrar_sesion(request):
    logout(request)  # borra la sesión activa del usuario
    return redirect("index")


def Logear(request):
    if request.method == "POST":
        form = AuthenticationForm(
            request, data=request.POST
        )  # se crea una instancia del formulario de autenticación AuthenticationForm con los datos del POST
        if form.is_valid():
            nombreUsuario = form.cleaned_data.get(
                "username"
            )  # Recupera el nombre de usuario (nombreUsuario)
            contra = form.cleaned_data.get(
                "password"
            )  # Recupera el nombre de usuario (contra)
            usuario = authenticate(
                username=nombreUsuario, password=contra
            )  # verifica las credenciales del usuario.
            if (
                usuario is not None
            ):  # Si las credenciales son correctas y el usuario existe
                login(request, usuario)  # autentica al usuario e iniciar la sesión
                return redirect("index")
            else:
                messages.error(request, "Usuario no válido")
        else:
            messages.error(request, "Información incorrecta")

    form = (
        AuthenticationForm()
    )  # muestra un formulario vacío para que el usuario pueda registrarse.
    return render(request, "login/login.html", {"form": form})
