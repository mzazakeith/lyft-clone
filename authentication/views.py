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

