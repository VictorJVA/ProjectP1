from django import forms
from Client_User.models import *

class PetForm(forms.ModelForm):
    birth_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = Pets
        fields = ['name', 'species', 'race', 'birth_date', 'gender', 'allergies','image']
        # fields = '__all__'
        
class AppointmentForm(forms.ModelForm):
    def __init__(self, vet_id, *args, **kwargs):
        super(AppointmentForm, self).__init__(*args, **kwargs)
        self.fields['time'].widget.choices = [(time, time.strftime('%H:%M')) for time in vet_id.available_time_slots(datetime.now().date())]

    class Meta:
        model = Appointment
        fields = ['pet_id', 'vet_id', 'date', 'time', 'reason_appointment']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.Select(),
            'pet_id': forms.Select(),
            'vet_id': forms.Select(),
        }