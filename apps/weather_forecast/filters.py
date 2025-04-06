from .models import *
import django_filters

class WeatherFilter(django_filters.FilterSet):
    class Meta:
        model = Weather
        fields = 'location temperature humidity weather_description timestamp'.split()