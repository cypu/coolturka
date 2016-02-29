# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-29 13:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('locations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('latitude', models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, verbose_name='latitude')),
                ('longitude', models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, verbose_name='longitude')),
                ('home_page', models.URLField()),
                ('fb_page', models.URLField()),
                ('open_close_info', models.TextField()),
                ('description', models.TextField()),
                ('place_type', models.CharField(choices=[('Teatr', 'Teatr'), ('Muzeum', 'Muzeum'), ('Opera', 'Opera'), ('Stadion', 'Stadion')], max_length=100)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='locations.City')),
            ],
        ),
    ]
