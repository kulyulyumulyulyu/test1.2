from .models import Contact
from django.forms import ModelForm, TextInput

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ["name", "telephone"]
        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите имя'
            }),
            "telephone": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите номер телефона'
            }),
        }