# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-23 10:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0002_auto_20180423_0053'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurantlocation',
            name='category',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='restaurantlocation',
            name='location',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='restaurantlocation',
            name='name',
            field=models.CharField(max_length=120),
        ),
    ]
