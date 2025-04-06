from django.contrib import admin
from .models import Weather

@admin.register(Weather)
class WeatherSearch(admin.ModelAdmin):
    list_display = 'location temperature humidity weather_description timestamp'.split()
    list_filter = 'location temperature humidity'.split()
    search_fields = ("Weathers", )


# Register your models here.
