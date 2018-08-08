@login_required
def create_passenger_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = CreatePassengerProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()
