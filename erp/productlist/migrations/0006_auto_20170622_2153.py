# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-22 13:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productlist', '0005_auto_20170622_2142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='weight',
            field=models.IntegerField(verbose_name='重量g'),
        ),
    ]
