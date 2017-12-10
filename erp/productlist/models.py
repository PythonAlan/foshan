# -*- coding:UTF-8 -*-
from django.db import models
from django.utils.safestring import mark_safe
from django.conf import settings
import datetime
from django.contrib.contenttypes.fields import GenericForeignKey
import os

import requests
from lxml import etree


class Product(models.Model):
    category = models.CharField(u'目录',max_length=20)
    time = models.TimeField(u'开发时间',null=True,blank=True)
    sku = models.CharField(max_length=20,unique=True)
    name = models.CharField(u'产品名称',max_length=200)
    status = models.CharField(u'状态',max_length=20,default="在售",blank=True)
    Longest_side = models.FloatField(u'长cm',null=True,blank=True)
    Median_side = models.FloatField(u'中cm',null=True,blank=True)
    Shortest_side = models.FloatField(u'短cm',null=True,blank=True)
    image = models.URLField(u'产品图片',null=True,blank=True)
    owner = models.CharField(u'开发者',max_length=20, default="A组")
    price = models.FloatField(u'采购价',)
    weight = models.IntegerField(u'重量g')
    # volume = models.FloatField(u'体积m³',default=0.001)




    class Meta:
        ordering = ('price',)
        verbose_name = '产品销售成本价(0%利润)'
        verbose_name_plural = '产品销售成本价(0%利润)'

    def __str__(self):
        return self.name


class BingHeng(models.Model):
    sku = models.CharField(u'SKU',max_length=20,null=True,blank=True)
    dayly_sale = models.FloatField(u'日均销量',null=True,blank=True)
    name = models.CharField(u'产品名称',max_length=200,null=True,blank=True)
    url = models.URLField(u'热卖listing链接',null=True,blank=True)
    image = models.URLField(u'产品图片',null=True,blank=True)
    us_dayly_sale = models.FloatField(u'US日均销量',)
    uk_dayly_sale = models.FloatField(u'UK日均销量',)
    de_dayly_sale = models.FloatField(u'DE日均销量',)
    au_dayly_sale = models.FloatField(u'AU日均销量',)


    class Meta:
        ordering = ('dayly_sale',)
        verbose_name = '待开发产品销售数据10-11月'
        verbose_name_plural = '待开发产品销售数据10-11月'

    def __str__(self):
        return self.name



class Product_A(models.Model):
    category = models.CharField(u'目录',max_length=20)
    time = models.TimeField(u'开发时间',null=True,blank=True)
    sku = models.CharField(max_length=20,unique=True)
    name = models.CharField(u'产品名称',max_length=200)
    status = models.CharField(u'状态',max_length=20,default="在售",blank=True)
    description = models.TextField(u'产品描述')
    image = models.URLField(u'产品图片',null=True,blank=True)
    owner = models.CharField(u'开发者',max_length=20, default="A组")
    price = models.FloatField(u'采购价',)
    weight = models.IntegerField(u'重量g')
    volume = models.FloatField(u'体积m³',default=0.001)




    class Meta:
        ordering = ('price',)
        verbose_name = '产品销售成本价(25%利润)'
        verbose_name_plural = '产品销售成本价(25%利润)'

    def __str__(self):
        return self.name

# class ImportFile(models.Model):
#
#     file = models.FileField(upload_to='File')
#     name = models.CharField(max_length=50, verbose_name=u'文件名')
#
#     class Meta:
#         ordering = ('price',)
#         verbose_name = '产品导入'
#         verbose_name_plural = '产品导入'
#
#     def __str__(self):
#         return self.name