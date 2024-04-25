from django import forms

class AppointmentActionForm(forms.Form):
    appointment_id = forms.IntegerField(widget=forms.HiddenInput)
    ACTION_CHOICES = (
        ('accept', 'Aceptar'),
        ('reject', 'Rechazar'),
    )
    action = forms.ChoiceField(choices=ACTION_CHOICES, widget=forms.RadioSelect)