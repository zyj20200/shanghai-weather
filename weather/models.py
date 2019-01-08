from django.db import models


class Weather(models.Model):
    area = models.CharField(max_length=128)
    year = models.CharField(max_length=128)
    datetime = models.CharField(max_length=128)
    weather = models.CharField(max_length=128)
    t_low = models.CharField(max_length=128)
    t_high = models.CharField(max_length=128)

    def __str__(self):
        return self.area, self.year, self.datetime, self.weather



