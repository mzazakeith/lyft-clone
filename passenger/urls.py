from django.conf.urls import url, include
from passenger import views

urlpatterns = [
    url(r'^new/passenger$', views.create_passenger_profile, name='new-passenger-profile'),

]