from typing import Any
from contact.models import Contact
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth import password_validation

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
    
class RegisterUpdateForm(forms.ModelForm):
    first_name = forms.CharField(
        min_length=3,
        max_length=50,
        required=True,
        help_text='Required',
        error_messages={'min_length': 'Please, add more than 3 letters.'}
    )
    last_name = forms.CharField(
        required=True,
        min_length=3,
        max_length=50,
        help_text='Required',
        error_messages={'min_length': 'Please, add more than 3 letters.'}
    )
    password1 = forms.CharField(
        label='Password',
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        help_text=password_validation.password_validators_help_text_html(),
        required=False,
    )
    password2 = forms.CharField(
        label='Confirm Password',
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        help_text='Use the same password as before',
        required=False,
    )
    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'email',
            'username', 
        )
    
    def save(self, commit=True):
        cleaned_data = self.cleaned_data
        user = super().save(commit=False)
        
        password = cleaned_data.get('password1')
        
        if password:
            user.set_password(password)
            
        if commit:
            user.save()
            
        return user
    
    def clean(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        
        if password1 or password2:
            if password1 != password2:
                self.add_error(
                    'password2', 
                    ValidationError('Your password and confirmation password do not match.'
                    , code='invalid'))
        return super().clean()
        
    def clean_email(self):
        email = self.cleaned_data.get('email')
        current_email = self.instance.email
        
        if current_email != email:
            if User.objects.filter(email=email).exists():
                self.add_error(
                    'email',
                    ValidationError('Email is already registered', code='invalid')
                )
        return email
    
    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        
        if password1:
            try:
                password_validation.validate_password(password1)
            except ValidationError as errors:
                self.add_error('password1', ValidationError(errors))
                
        return password1