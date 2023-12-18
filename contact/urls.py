from django.urls import path
from contact import views

# Create your urls here.

app_name = 'contact'

urlpatterns = [
    path('', views.home, name='home')
]
