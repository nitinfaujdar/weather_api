from django.urls import path
from .views import *

urlpatterns = (
    [
        path('get_weather/', WeatherView.as_view(), name="get_weather"),
        path('post_weather_data/', WeatherDataView.as_view(), name='post_weather_data'),
    ])
