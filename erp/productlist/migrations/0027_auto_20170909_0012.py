# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-09-08 16:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productlist', '0026_auto_20170906_0052'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShippingTime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=20, verbose_name='目录')),
                ('sku', models.CharField(max_length=20, unique=True)),
                ('name', models.CharField(max_length=200, verbose_name='产品名称')),
                ('image', models.URLField(blank=True, null=True, verbose_name='产品图片')),
                ('date', models.DateField(null=True)),
                ('shiftTime', models.CharField(default='N/A', max_length=10)),
                ('timeIn', models.TimeField(null=True)),
                ('timeOut', models.TimeField(null=True)),
            ],
            options={
                'verbose_name': '海运跟踪',
                'verbose_name_plural': '海运跟踪',
            },
        ),
        migrations.DeleteModel(
            name='HotSale',
        ),
    ]