from django import forms
from Client_User.models import *

class PetForm(forms.ModelForm):
    birth_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = Pets
        fields = ['name', 'species', 'race', 'birth_date', 'gender', 'allergies','image']
        # fields = '__all__'
        
class AppointmentForm(forms.ModelForm):
    def __init__(self, client_id, *args, **kwargs):
        super(AppointmentForm, self).__init__(*args, **kwargs)
        self.fields['pet_id'].queryset = Pets.objects.filter(client_id=client_id)
        self.fields['vet_id'].queryset = Vet.objects.all()

    class Meta:
        model = Appointment
        fields = ['pet_id', 'vet_id', 'date', 'time', 'reason_appointment']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.Select(choices=[(f'{hour:02d}:00', f'{hour:02d}:00') for hour in range(24)]),
            'pet_id': forms.Select(),
            'vet_id': forms.Select(choices=[(vet.pk, vet) for vet in Vet.objects.all()]),
        }