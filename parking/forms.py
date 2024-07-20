from django import forms
from .models import Reservation

class ReservationForm(forms.ModelForm):
    id_number = forms.CharField(label='ID Number', max_length=20)  # Add ID number field

    class Meta:
        model = Reservation
        fields = ['plate_number', 'id_number']

class CancelReservationForm(forms.Form):
    plate_number = forms.CharField(label='Plate Number', max_length=20)
    id_number = forms.CharField(label='ID Number', max_length=20)  # Add ID number field

class ExtendTimeForm(forms.Form):
    extra_time = forms.IntegerField(label='Extra Time (minutes)')
