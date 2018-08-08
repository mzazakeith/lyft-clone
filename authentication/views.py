from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect

from driver.forms import LocationForm, ReviewDriverForm
from driver.views import create_driver_profile
from passenger.forms import PickUpLocationForm
from passenger.views import create_passenger_profile
from .forms import DriverSignupForm, PassengerSignupForm
from django.contrib.auth import get_user_model
from driver.models import DriverProfile, driver_location, Car, DriverReview
from passenger.models import PassengerProfile, pass_location
# from django.contrib.auth.models import User
User = get_user_model()


def driver_signup(request):
    if request.method == 'POST':
        form = DriverSignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = True
            user.is_passenger = False
            user.is_driver = True
            user.save()
            return redirect(create_driver_profile)
    else:
        form = DriverSignupForm()
    return render(request, 'registration/driver_signup.html', {'form': form})


def passenger_signup(request):
    if request.method == 'POST':
        form = PassengerSignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = True
            user.is_passenger = True
            user.is_driver = False
            user.save()
            return redirect(create_passenger_profile)
    else:
        form = PassengerSignupForm()
    return render(request, 'registration/passenger_signup.html', {'form': form})


def landing(request):
    return render(request, 'index.html')


@login_required
def home(request):
    locale=driver_location.objects.all()
    cars = Car.objects.all()
    current_user = request.user
    status = request.user.is_passenger
    if status:
        profile = PassengerProfile.objects.get(user=current_user.id)
        location = pass_location.objects.get(user=current_user.id)
        if request.method == 'POST':
            form = PickUpLocationForm(request.POST, request.FILES,instance=pass_location.objects.get(user=request.user.id))
            if form.is_valid():
                location = form.save(commit=False)
                location.user = current_user
                location.save()
                return redirect("/home")
        else:
            form = PickUpLocationForm()
    else:
        profile = DriverProfile.objects.get(user=current_user.id)
        location = driver_location.objects.get(user=current_user.id)
        if request.method == 'POST':
            form = LocationForm(request.POST, request.FILES,instance=driver_location.objects.get(user=request.user.id))
            if form.is_valid():
                location = form.save(commit=False)
                location.user = current_user
                location.save()
                return redirect("/home")
        else:
            form = LocationForm()
    return render(request, "home.html", {"profile": profile, "user": current_user, "form": form, "location":location,"locale":locale,"cars":cars})


@login_required
def userprofile(request, user_id):
    users = User.objects.get(id=user_id)
    profile = DriverProfile.objects.get(user=users)
    car = Car.objects.get(driver=users)
    if request.method == 'POST':
        form = ReviewDriverForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = users
            profile.save()
            return redirect("/userprofile/"+user_id)
    else:
        form = ReviewDriverForm()
    return render(request, 'userprofile.html', {"user": users, "profile": profile, "car":car, "form": form})


