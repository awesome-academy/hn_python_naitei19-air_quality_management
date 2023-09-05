# air_quality/models.py

from django.db import models

class Location(models.Model):
    name = models.CharField(max_length=100)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    # Add other location-related fields as needed

    def __str__(self):
        return self.name

class Pollutant(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    # Add other pollutant-related fields as needed

    def __str__(self):
        return self.name

class AirQualityData(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    pollutant = models.ForeignKey(Pollutant, on_delete=models.CASCADE)
    timestamp = models.DateTimeField()
    value = models.DecimalField(max_digits=10, decimal_places=2)
    # Add other air quality data-related fields as needed

    def __str__(self):
        return f"{self.location} - {self.pollutant} - {self.timestamp}"

class User(models.Model):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    # Add other user-related fields as needed

    def __str__(self):
        return self.username
