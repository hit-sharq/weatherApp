from django.db import models

class WeatherData(models.Model):
    city = models.CharField(max_length=100)
    country_code = models.CharField(max_length=10)
    coordinate = models.CharField(max_length=50)
    temperature = models.CharField(max_length=20)
    pressure = models.CharField(max_length=20)
    humidity = models.CharField(max_length=20)
    weather_main = models.CharField(max_length=50)
    weather_description = models.CharField(max_length=100)
    icon = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.city}, {self.country_code}"
