# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-29 13:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Concert',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='name of event')),
                ('additional_info', models.TextField(max_length=2000, verbose_name='additional information related to event')),
                ('start_date', models.DateTimeField(verbose_name='start date')),
                ('end_date', models.DateTimeField(verbose_name='end date')),
                ('buy_ticket_url', models.CharField(max_length=255, verbose_name='URL which allows to buy a ticket')),
                ('ticket_prices', models.TextField(verbose_name='ticket prices')),
                ('descritpion', models.TextField(verbose_name='event descritpion')),
                ('latitude', models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, verbose_name='latitude')),
                ('longitude', models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, verbose_name='longitude')),
                ('tags', models.CharField(max_length=255, verbose_name='tags related to event')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Excibition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='name of event')),
                ('additional_info', models.TextField(max_length=2000, verbose_name='additional information related to event')),
                ('start_date', models.DateTimeField(verbose_name='start date')),
                ('end_date', models.DateTimeField(verbose_name='end date')),
                ('buy_ticket_url', models.CharField(max_length=255, verbose_name='URL which allows to buy a ticket')),
                ('ticket_prices', models.TextField(verbose_name='ticket prices')),
                ('descritpion', models.TextField(verbose_name='event descritpion')),
                ('latitude', models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, verbose_name='latitude')),
                ('longitude', models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, verbose_name='longitude')),
                ('tags', models.CharField(max_length=255, verbose_name='tags related to event')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Metting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='name of event')),
                ('additional_info', models.TextField(max_length=2000, verbose_name='additional information related to event')),
                ('start_date', models.DateTimeField(verbose_name='start date')),
                ('end_date', models.DateTimeField(verbose_name='end date')),
                ('buy_ticket_url', models.CharField(max_length=255, verbose_name='URL which allows to buy a ticket')),
                ('ticket_prices', models.TextField(verbose_name='ticket prices')),
                ('descritpion', models.TextField(verbose_name='event descritpion')),
                ('latitude', models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, verbose_name='latitude')),
                ('longitude', models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, verbose_name='longitude')),
                ('tags', models.CharField(max_length=255, verbose_name='tags related to event')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Play',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='name of event')),
                ('additional_info', models.TextField(max_length=2000, verbose_name='additional information related to event')),
                ('start_date', models.DateTimeField(verbose_name='start date')),
                ('end_date', models.DateTimeField(verbose_name='end date')),
                ('buy_ticket_url', models.CharField(max_length=255, verbose_name='URL which allows to buy a ticket')),
                ('ticket_prices', models.TextField(verbose_name='ticket prices')),
                ('descritpion', models.TextField(verbose_name='event descritpion')),
                ('latitude', models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, verbose_name='latitude')),
                ('longitude', models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, verbose_name='longitude')),
                ('tags', models.CharField(max_length=255, verbose_name='tags related to event')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Workshop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='name of event')),
                ('additional_info', models.TextField(max_length=2000, verbose_name='additional information related to event')),
                ('start_date', models.DateTimeField(verbose_name='start date')),
                ('end_date', models.DateTimeField(verbose_name='end date')),
                ('buy_ticket_url', models.CharField(max_length=255, verbose_name='URL which allows to buy a ticket')),
                ('ticket_prices', models.TextField(verbose_name='ticket prices')),
                ('descritpion', models.TextField(verbose_name='event descritpion')),
                ('latitude', models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, verbose_name='latitude')),
                ('longitude', models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, verbose_name='longitude')),
                ('tags', models.CharField(max_length=255, verbose_name='tags related to event')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
