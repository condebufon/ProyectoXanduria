from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=200, required=True)
    email = forms.EmailField(max_length=200, required=True)
    subject = forms.CharField(max_length=200, required=False)  # Hacerlo opcional
    message = forms.CharField(widget=forms.Textarea, required=True)
    