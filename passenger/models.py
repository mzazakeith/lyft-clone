from django.contrib.auth.models import User
from django.db import models
from pyuploadcare.dj.models import ImageField
from django.contrib.auth import get_user_model

User = get_user_model()

Gender_Choices = (
    ('F', 'female'),
    ('M', 'male'),
)


class PassengerProfile(models.Model):
    profile_pic = ImageField()
    gender = models.CharField(max_length=30, choices=Gender_Choices, default='None', blank=True)
    phone_number = models.PositiveIntegerField()
    National_id = models.PositiveIntegerField()
    user = models.ForeignKey(User)
