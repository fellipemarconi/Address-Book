from django.urls import path
from contact import views

# Create your urls here.

app_name = 'contact'

urlpatterns = [
    path('', views.index, name='home')
]
