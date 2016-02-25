from django.db import models
from voivodeship import Voivodeship


class City(models.Model):

    name = models.CharField(max_length=200)
    voivodeship = models.ForeignKey(Voivodeship)
    latitude = models.DecimalField(u'latitude', blank=True, null=True, max_digits=6, decimal_places=4)
    longitude = models.DecimalField(u'longitude', blank=True, null=True, max_digits=6, decimal_places=4)