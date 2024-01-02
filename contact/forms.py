from contact.models import Contact
from django import forms
from django.core.exceptions import ValidationError

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = (
            'first_name', 'last_name', 'phone', 
            'email', 'description', 'category',
            )
        widgets = {
            'first_name': forms.TextInput(
                attrs={'placeholder': 'John'}),
            'last_name': forms.TextInput(
                attrs={'placeholder': 'Doe'}),
            'phone': forms.TextInput(
                attrs={'placeholder': '(555) 234-5678'}),
            'email': forms.EmailInput(
                attrs={'placeholder': 'example@example.com'}),
            'description': forms.Textarea(
                attrs={'placeholder': 'Type a description here...'}),
        }
        
    def clean(self):
        cleaned_data = self.cleaned_data
        return super().clean()