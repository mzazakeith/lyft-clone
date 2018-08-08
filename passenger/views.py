@login_required
def create_passenger_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = CreatePassengerProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()
            pass_location(user=current_user,pickup_location="Garden Of Eden").save()
            return redirect('/')
    else:
        form = CreatePassengerProfileForm()
    return render(request, 'profile/passenger.html', {"form": form , "user":current_user})
