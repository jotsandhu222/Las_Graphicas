# forms.py
from django import forms
from .models import Polo, PoloImage, ContactMessage
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
    
    
class TShirtForm(ModelForm):
    class Meta:
        model = Polo
        #fields = ['name', 'description', 'market_price', 'selling_price']
        fields = '__all__'
        
class PoloImageForm(forms.ModelForm):
    class Meta:
        model = PoloImage
        fields = ['image']
        


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'subject', 'message']
