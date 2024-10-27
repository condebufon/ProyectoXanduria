# forms.py
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User = get_user_model()

class UserRegistrationForm(forms.ModelForm): #Un ModelForm automáticamente maneja los campos del modelo que especifiques, en lugar de tener que definirlos manualmente.
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirmation = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField()  # Campo de email visible

    class Meta: # define los metadatos del formulario
        model = User    #  especifica que el formulario está basado en el modelo User
        fields = ['username','email', 'password', 'password_confirmation']

    def clean(self):
        cleaned_data = super().clean()  # Contiene todos los datos del formulario que han sido limpiados (validos).
        password = cleaned_data.get("password")
        password_confirmation = cleaned_data.get("password_confirmation")

        if password and password_confirmation and password != password_confirmation:
            raise forms.ValidationError("Las contraseñas no coinciden.")
