# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-13 13:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productlist', '0021_hotsale_competitor_us_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hotsale',
            name='competitor_us_price',
        ),
    ]
