# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-09-11 13:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productlist', '0028_auto_20170909_0147'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shippingtime',
            name='shiftTime',
        ),
        migrations.RemoveField(
            model_name='shippingtime',
            name='timeIn',
        ),
        migrations.AlterField(
            model_name='shippingtime',
            name='timeOut',
            field=models.DateField(blank=True, null=True),
        ),
    ]
