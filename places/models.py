from __future__ import unicode_literals

from django.db import models
from locations.models.city import City

PLACES_TYPES = (
    (u'Teatr', u'Teatr'),
    (u'Muzeum', u'Muzeum'),
    (u'Opera', u'Opera' ),
    (u'Stadion', u'Stadion'),
)


class Place(models.Model):

    name = models.CharField(max_length=500)
    city = models.ForeignKey(City)
    latitude = models.DecimalField(u'latitude', blank=True, null=True, max_digits=6, decimal_places=4)
    longitude = models.DecimalField(u'longitude', blank=True, null=True, max_digits=6, decimal_places=4)
    home_page = models.URLField()
    fb_page = models.URLField()
    open_close_info = models.TextField()
    description = models.TextField()
    place_type = models.CharField(choices=PLACES_TYPES)
