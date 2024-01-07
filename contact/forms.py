from contact.models import Contact
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = (
            'first_name', 'last_name', 'phone', 
            'email', 'description', 'category',
            'picture',
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
            'picture': forms.FileInput(
                attrs={'accept': 'image/*'}),
        }
        
    def clean(self):
        cleaned_data = self.cleaned_data
        return super().clean()
    
class RegisterForm(UserCreationForm):
    first_name = forms.CharField(
        required=True,
        min_length=3,
        max_length=50,
    )
    last_name = forms.CharField(
        required=True,
        min_length=3,
        max_length=50,
    )
    email = forms.EmailField(
        required=True,
        max_length=255,
    )
    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'email',
            'username', 'password1', 'password2'
        )
        
    def clean_email(self):
        email = self.cleaned_data.get('email')
        
        if User.objects.filter(email=email).exists():
            self.add_error(
                'email',
                ValidationError('Email is already registered', code='invalid')
            )
        return email