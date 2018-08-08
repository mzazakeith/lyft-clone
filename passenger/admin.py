from django.contrib import admin

from .models import PassengerProfile, pass_location

admin.site.register(PassengerProfile)
admin.site.register(pass_location)


