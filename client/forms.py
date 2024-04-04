from django import forms
from Client_User.models import *

class PetForm(forms.ModelForm):
    birth_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = Pets
        fields = ['name', 'species', 'race', 'birth_date', 'gender', 'allergies','image']
        # fields = '__all__'
        

