# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-23 10:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0003_auto_20180423_1246'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurantlocation',
            name='timestamp',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
