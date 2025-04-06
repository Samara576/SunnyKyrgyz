from django.db import models

class Weather(models.Model):
    location = models.CharField(max_length=100)
    temperature = models.FloatField()
    humidity = models.FloatField()
    weather_description = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)
