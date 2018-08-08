from passenger.models import PassengerProfile, pass_location
from django import forms


class CreatePassengerProfileForm(forms.ModelForm):
    class Meta:
        model = PassengerProfile
        exclude = ['user']


class PickUpLocationForm(forms.ModelForm):
    class Meta:
        model = pass_location
        exclude = ['user']