from django.contrib import admin
from .models import Weather

class WeatherAdmin(admin.ModelAdmin):
    list_display = ['area', 'year', 'datetime', 'weather', 't_low', 't_high']


admin.site.register(Weather, WeatherAdmin)
