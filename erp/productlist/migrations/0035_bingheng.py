# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-07 17:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productlist', '0034_delete_shippingtime'),
    ]

    operations = [
        migrations.CreateModel(
            name='BingHeng',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sku', models.CharField(blank=True, max_length=20, null=True, verbose_name='SKU')),
                ('dayly_sale', models.FloatField(blank=True, null=True, verbose_name='日均销量')),
                ('name', models.CharField(blank=True, max_length=200, null=True, verbose_name='产品名称')),
                ('url', models.URLField(blank=True, null=True, verbose_name='热卖listing链接')),
                ('image', models.URLField(blank=True, null=True, verbose_name='产品图片')),
                ('us_dayly_sale', models.FloatField(verbose_name='US日均销量')),
                ('uk_dayly_sale', models.FloatField(verbose_name='UK日均销量')),
                ('de_dayly_sale', models.FloatField(verbose_name='DE日均销量')),
                ('au_dayly_sale', models.FloatField(verbose_name='AU日均销量')),
            ],
            options={
                'verbose_name': '滨恒产品销售数据10-11月',
                'ordering': ('dayly_sale',),
                'verbose_name_plural': '滨恒产品销售数据10-11月',
            },
        ),
    ]
