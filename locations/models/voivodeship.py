from django.db import models


class Voivodeship(models.Model):

    name = models.CharField(max_length=200)
