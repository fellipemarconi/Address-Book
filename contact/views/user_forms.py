from django.shortcuts import render
from contact.forms import RegisterForm

def register(request):
    form = RegisterForm()
    
    context = {
        'form': form
    }
    
    return render(request, 'contact/register.html', context)