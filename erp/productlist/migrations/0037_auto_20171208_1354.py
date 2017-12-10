# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-08 05:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productlist', '0036_auto_20171208_1350'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product_A',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=20, verbose_name='目录')),
                ('time', models.TimeField(blank=True, null=True, verbose_name='开发时间')),
                ('sku', models.CharField(max_length=20, unique=True)),
                ('name', models.CharField(max_length=200, verbose_name='产品名称')),
                ('status', models.CharField(blank=True, default='在售', max_length=20, verbose_name='状态')),
                ('description', models.TextField(verbose_name='产品描述')),
                ('image', models.URLField(blank=True, null=True, verbose_name='产品图片')),
                ('owner', models.CharField(default='A组', max_length=20, verbose_name='开发者')),
                ('price', models.FloatField(verbose_name='采购价')),
                ('weight', models.IntegerField(verbose_name='重量g')),
                ('volume', models.FloatField(default=0.001, verbose_name='体积m³')),
            ],
            options={
                'ordering': ('price',),
                'verbose_name': '产品销售成本价(25%利润)',
                'verbose_name_plural': '产品销售成本价(25%利润)',
            },
        ),
        migrations.AlterField(
            model_name='product',
            name='time',
            field=models.TimeField(blank=True, null=True, verbose_name='开发时间'),
        ),
    ]
