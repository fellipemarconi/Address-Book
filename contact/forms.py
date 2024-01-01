from contact.models import Contact
from django import forms

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('first_name', 'last_name', 'phone', 'email')
        
    def clean(self):
        cleaned_data = self.cleaned_data
        return super().clean()