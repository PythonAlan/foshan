# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-22 07:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productlist', '0003_auto_20170622_0019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.URLField(blank=True, null=True, verbose_name='产品图片'),
        ),
    ]