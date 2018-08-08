from django.contrib.auth.models import User
from django.db import models
from pyuploadcare.dj.models import ImageField
from django.contrib.auth import get_user_model
from djgeojson.fields import PointField

User = get_user_model()

Gender_Choices = (
    ('F', 'female'),
    ('M', 'male'),
)

Ratings = (
    ('1', 'Poor'),
    ('2', 'Below-Average'),
    ('3', 'Average'),
    ('4', 'Good'),
    ('5', 'Excellent'),
)


class DriverProfile(models.Model):
    profile_pic = ImageField()
    gender = models.CharField(max_length=30, choices=Gender_Choices, default='None', blank=True)
    phone_number = models.PositiveIntegerField()
    user = models.ForeignKey(User)


    @classmethod
    def delete_driver(id, self):
        self.delete()

    @classmethod
    def update_driver(driver):
        driver.update()


class Car(models.Model):
    car_capacity = models.PositiveIntegerField(default=3)
    car_number_plate = models.CharField(max_length=255)
    car_color = models.CharField(max_length=255)
    driver = models.ForeignKey(User)

    @classmethod
    def delete_car(id):
        id.delete()


class driver_location(models.Model):
    current_location = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    user = models.ForeignKey(User)

    @classmethod
    def update_locationr(location):
        location.update()

class Points(models.Model):
    geom = PointField()


class DriverReview(models.Model):
    rate = models.CharField(max_length=30, choices=Ratings, default='None', blank=True)
    user = models.ForeignKey(User)
