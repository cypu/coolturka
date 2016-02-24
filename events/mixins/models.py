from django.db import models


class Event(models.Model):

    name = models.CharField(u'name of event', max_length=255)
    additional_info = models.TextField(u'additional information related to event', max_length=2000)
    start_date = models.DateTimeField(u'start date')
    end_date = models.DateTimeField(u'end date')
    buy_ticket_url = models.CharField(u'URL which allows to buy a ticket')
    ticket_prices = models.TextField(u'ticket prices')
    descritpion = models.TextField(u'event descritpion')
    latitude = models.DecimalField(u'latitude', blank=True, null=True)
    longitude = models.DecimalField(u'longitude', blank=True, null=True)
    tags = models.CharField(u'tags related to event', max_length=255)

    class Meta:
        abstract = True
