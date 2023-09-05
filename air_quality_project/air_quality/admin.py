# air_quality/admin.py

from django.contrib import admin
from .models import Location, Pollutant, AirQualityData, User

admin.site.register(Location)
admin.site.register(Pollutant)
admin.site.register(AirQualityData)
admin.site.register(User)
