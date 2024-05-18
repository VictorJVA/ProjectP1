from django import forms
from .models import Client,Vet

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'postal_code', 'image']
class Vetform(forms.ModelForm):
    class Meta:
        model = Vet
        fields = ['name','phone','address','postal_code','image']