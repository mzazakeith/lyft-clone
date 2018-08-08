from django.conf.urls import url, include
from driver import views
# from djgeojson.views import GeoJSONLayerView
# from driver.models import Points

urlpatterns = [
    url(r'^new/driver$', views.create_driver_profile, name='new-driver-profile'),
    url(r'^new/car$', views.submit_car, name='new-car'),

]