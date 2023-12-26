from django.shortcuts import render, get_object_or_404, redirect
from contact.models import Contact
from django import forms
from django.http import Http404
from django.db.models import Q
from django.core.paginator import Paginator

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('first_name', 'last_name', 'phone', 'email')

def create(request):
    if request.method == 'POST':
        
        context = {
            'form': ContactForm(request.POST),
        }
    
        return render(request, 'contact/create.html', context=context)
    
    context = {
            'form': ContactForm(request.POST),
        }
    
    return render(request, 'contact/create.html', context=context)