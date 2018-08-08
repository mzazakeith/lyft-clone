from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from driver.forms import CreateDriverProfileForm, SubmitCarForm
from driver.models import driver_location


@login_required
def submit_car(request):
    current_user = request.user
    if request.method == 'POST':
        form = SubmitCarForm(request.POST, request.FILES)
        if form.is_valid():
            car = form.save(commit=False)
            car.driver = current_user
            car.save()
            return redirect('/')
    else:
        form = SubmitCarForm()
    return render(request, 'profile/car.html', {"form": form, "user": current_user})


@login_required
def create_driver_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = CreateDriverProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()
            driver_location(user=current_user, current_location="None", destination="None").save()
            return redirect(submit_car)
    else:
        form = CreateDriverProfileForm()
    return render(request, 'profile/driver.html', {"form": form, "user": current_user})


