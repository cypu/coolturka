from django.db import models


class Voivodeship(models.Model):

    name = models.CharField(max_length=25)

    def __unicode__(self):
        return self.name

    @property
    def class_name(self):
        return "pl{}".format(self.pk)

    @property
    def url(self):
        return "#{}".format(self.pk)
