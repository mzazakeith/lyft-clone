from django.conf.urls import url, include

from . import views


urlpatterns = [
    url(r'^signup/driver/$', views.driver_signup, name='signup-driver'),
    url(r'^signup/passenger/$', views.passenger_signup, name='signup-passenger'),
    url(r'^',include('driver.urls')),
    url(r'^', include('passenger.urls')),
    url(r'^$', views.landing, name='land'),
    url(r'^home', views.home, name='home'),
    url(r'^userprofile/(?P<user_id>\d+)', views.userprofile, name='profile'),
]