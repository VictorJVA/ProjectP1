from django import forms
from Client_User.models import *

class PetForm(forms.ModelForm):
    # client_id = forms.ModelChoiceField(queryset=Client.objects.all(), to_field_name="client_id")
    class Meta:
        model = Pets
        fields = ['name', 'species', 'race', 'birth_date', 'gender', 'allergies','image']
        # fields = '__all__'
        

