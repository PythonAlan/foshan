# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-08 05:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('productlist', '0035_bingheng'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bingheng',
            options={'ordering': ('dayly_sale',), 'verbose_name': '待开发产品销售数据10-11月', 'verbose_name_plural': '待开发产品销售数据10-11月'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('price',), 'verbose_name': '产品销售成本价(0%利润)', 'verbose_name_plural': '产品销售成本价(0%利润)'},
        ),
        migrations.AddField(
            model_name='product',
            name='time',
            field=models.TimeField(default=django.utils.timezone.now, verbose_name='开发时间'),
            preserve_default=False,
        ),
    ]
