# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-30 18:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productlist', '0018_delete_importfile'),
    ]

    operations = [
        migrations.CreateModel(
            name='HotSsle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=20, verbose_name='目录')),
                ('sku', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=200, verbose_name='产品名称')),
                ('image', models.URLField(blank=True, null=True, verbose_name='产品图片')),
                ('our_hot_listing', models.URLField(blank=True, null=True, verbose_name='热卖listings')),
                ('competitor_us_url', models.URLField(blank=True, null=True, verbose_name='竞争对手（美）')),
                ('competitor_us_price', models.FloatField(blank=True, null=True, verbose_name='售价$')),
                ('competitor_uk_url', models.URLField(blank=True, null=True, verbose_name='竞争对手（英）')),
                ('competitor_uk_price', models.FloatField(blank=True, null=True, verbose_name='售价£')),
                ('competitor_de_url', models.URLField(blank=True, null=True, verbose_name='竞争对手（德）')),
                ('competitor_de_price', models.FloatField(blank=True, null=True, verbose_name='售价€')),
                ('competitor_au_url', models.URLField(blank=True, null=True, verbose_name='竞争对手（澳）')),
                ('competitor_au_price', models.FloatField(blank=True, null=True, verbose_name='售价$')),
            ],
            options={
                'ordering': ('sku',),
                'verbose_name': '热卖跟踪',
                'verbose_name_plural': '热卖跟踪',
            },
        ),
    ]
