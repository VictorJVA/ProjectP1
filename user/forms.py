from django import forms
from Client_User.models import *

class AppointmentActionForm(forms.Form):
    appointment_id = forms.IntegerField(widget=forms.HiddenInput)
    ACTION_CHOICES = (
        ('accept', 'accept'),
        ('reject', 'Reject'),
    )
    action = forms.ChoiceField(choices=ACTION_CHOICES, widget=forms.RadioSelect)
        
class AppointmentForm(forms.ModelForm):
    def __init__(self, client_id, *args, **kwargs):
        super(AppointmentForm, self).__init__(*args, **kwargs)
        self.fields['vet_id'].queryset = Vet.objects.filter(client_id=client_id)
        self.fields['pet_id'].queryset = Pets.objects.all()

    class Meta:
        model = Appointment
        fields = ['pet_id', 'vet_id', 'date', 'time', 'reason_appointment']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.Select(choices=[(f'{hour:02d}:00', f'{hour:02d}:00') for hour in range(24)]),
            'pet_id': forms.Select(),
            # 'vet_id': forms.Select(choices=[(vet.pk, vet) for vet in Vet.objects.all()]),
        }