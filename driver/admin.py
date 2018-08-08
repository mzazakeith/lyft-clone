from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin
from .models import DriverProfile, driver_location,Points

admin.site.register(DriverProfile)
admin.site.register(driver_location)
admin.site.register(Points, LeafletGeoAdmin)