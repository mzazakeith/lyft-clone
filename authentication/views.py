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


