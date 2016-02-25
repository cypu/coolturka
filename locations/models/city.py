from django.db import models
from voivodeship import Voivodeship


class City(models.Model):

    name = models.CharField(max_length=200)
    voivodeship = models.ForeignKey(Voivodeship)
