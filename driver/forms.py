from driver.models import DriverProfile, Car, driver_location, DriverReview
from django import forms


class CreateDriverProfileForm(forms.ModelForm):
    class Meta:
        model = DriverProfile
        exclude = ['user']


class SubmitCarForm(forms.ModelForm):
    class Meta:
        model = Car
        exclude = ['driver']


class LocationForm(forms.ModelForm):
    class Meta:
        model = driver_location
        exclude = ['user']


class ReviewDriverForm(forms.ModelForm):
    class Meta:
        model = DriverReview
        exclude = ['user']
