from django import forms
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['full_name', 'email', 'message']
        widgets = {
            'full_name': forms.TextInput(attrs={
                'placeholder': 'Full name*',
                'class': 'form-input'
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Email*',
                'class': 'form-input'
            }),
            'message': forms.Textarea(attrs={
                'placeholder': 'Enter your Message*',
                'class': 'form-textarea'
            }),
        }
