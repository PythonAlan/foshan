# -*- coding:UTF-8 -*-
from django.contrib import admin

# Register your models here.

from productlist.models import Product,BingHeng,Product_A
import productlist.config as pd  #参数
from django.contrib.admin.models import LogEntry
import requests
from lxml import etree
from time import sleep
from django.utils.html import format_html


LogEntry.objects.all().delete()

class SecondClass(admin.ModelAdmin):
    def eub_us(self,obj):
        eub_us = (obj.weight*pd.eub_us['weight_rate_up_200']+pd.eub_us['Order Handling'])*pd.eub_us['discount']/pd.exchange_rate['us']
        return round(eub_us,1)
    def wini_us(self,obj):
            if   obj.weight < 85 or obj.weight == 85:
                second_class_wini_us = pd.wini_us[85]
            elif obj.weight > 85 and obj.weight < 114 :
                second_class_wini_us = pd.wini_us[113]
            elif obj.weight > 113 and obj.weight < 141:
                second_class_wini_us = pd.wini_us[141]
            elif obj.weight > 140 and obj.weight < 171:
                second_class_wini_us = pd.wini_us[170]
            elif obj.weight > 170 and obj.weight < 199:
                second_class_wini_us = pd.wini_us[198]
            elif obj.weight > 198 and obj.weight < 227:
                second_class_wini_us = pd.wini_us[226]
            elif obj.weight > 226 and obj.weight < 256:
                second_class_wini_us = pd.wini_us[255]
            elif obj.weight >255 and obj.weight < 284:
                second_class_wini_us = pd.wini_us[283]
            elif obj.weight >283 and obj.weight < 312:
                second_class_wini_us = pd.wini_us[311]
            elif obj.weight >311 and obj.weight < 341:
                second_class_wini_us = pd.wini_us[340]
            elif obj.weight >340 and obj.weight < 369:
                second_class_wini_us = pd.wini_us[368]
            elif obj.weight >368 and obj.weight < 397:
                second_class_wini_us = pd.wini_us[396]
            elif obj.weight >396 and obj.weight < 426:
                second_class_wini_us = pd.wini_us[425]
            elif obj.weight >425 and obj.weight < 453:
                second_class_wini_us = pd.wini_us[425]
            elif obj.weight >453 and obj.weight < 908:
                second_class_wini_us = pd.wini_us[907]
            elif obj.weight >907 and obj.weight < 1361:
                second_class_wini_us = pd.wini_us[1360]
            elif obj.weight >1360 and obj.weight < 1815:
                second_class_wini_us = pd.wini_us[1814]
            elif obj.weight >1814 and obj.weight < 2269:
                second_class_wini_us = pd.wini_us[2268]
            elif obj.weight >2268 and obj.weight < 2722:
                second_class_wini_us = pd.wini_us[2721]
            elif obj.weight >2721 and obj.weight < 3176:
                second_class_wini_us = pd.wini_us[3175]
            elif obj.weight >3175 and obj.weight < 3629:
                second_class_wini_us = pd.wini_us[3628]
            else:
                second_class_wini_us = pd.wini_us[4082]

            return second_class_wini_us
    def cn_uk(self,obj):
        if obj.weight < 20 or obj.weight == 20:
            second_class_gz_uk = pd.gz_under_250_eds_a_uk['1-20']
        elif obj.weight> 20 and obj.weight < 31:
            second_class_gz_uk = pd.gz_under_250_eds_a_uk['21-30']
        elif obj.weight >30 and obj.weight< 41:
            second_class_gz_uk = pd.gz_under_250_eds_a_uk['31-40']
        elif obj.weight> 40 and obj.weight < 51:
            second_class_gz_uk = pd.gz_under_250_eds_a_uk['41-50']
        elif obj.weight>50 and obj.weight < 101:
            second_class_gz_uk = pd.gz_under_250_eds_b_uk['51-100']*obj.weight
        elif obj.weight>100 and obj.weight < 301:
            second_class_gz_uk = pd.gz_under_250_eds_b_uk['101-300']*obj.weight
        else:
            second_class_gz_uk = pd.gz_over_250_4px_track_uk['weight_per_32_kg']*obj.weight+pd.gz_over_250_4px_track_uk['Order Handling']
        return round(second_class_gz_uk/pd.exchange_rate['uk'],1)
    def wini_uk(self,obj):
        second_class_wini_uk = pd.wini_uk['Yodel Home Mini']
        return  second_class_wini_uk
    def cn_de(self,obj):
        if obj.weight <20 or obj.weight ==20:
            second_class_gz_de = pd.gz_under_250_eds_a_de['1-20']
        elif obj.weight> 20 and obj.weight < 31:
            second_class_gz_de = pd.gz_under_250_eds_a_de['21-30']
        elif obj.weight >30 and obj.weight< 41:
            second_class_gz_de = pd.gz_under_250_eds_a_de['31-40']
        elif obj.weight> 40 and obj.weight < 51:
            second_class_gz_de = pd.gz_under_250_eds_a_de['41-50']
        elif obj.weight>50 and obj.weight < 101:
            second_class_gz_de = pd.gz_under_250_eds_b_de['51-100']*obj.weight
        elif obj.weight>100 and obj.weight < 251:
            second_class_gz_de = pd.gz_under_250_eds_b_de['101-250']*obj.weight
        elif obj.weight >250 and obj.weight <1001:
            second_class_gz_de = pd.gz_between_250_1000_YanWen_de['250-1000']*obj.weight+pd.gz_between_250_1000_YanWen_de['Order Handling']
        else:
            second_class_gz_de = pd.gz_between_1kg_2kg_4px_track_de['packet_51_per_kg']*obj.weight+pd.gz_between_1kg_2kg_4px_track_de['Order Handling']
        return round(second_class_gz_de/pd.exchange_rate['de'],1)
    def wini_de(self,obj):
        second_class_wini_de = pd.wini_de['DHL Domestic Paket']
        return second_class_wini_de
    def cn_au(self,obj):
        second_class_gz_au = pd.gz_au['package_per_kg']*obj.weight+pd.gz_au['Order Handling']
        return round(second_class_gz_au/pd.exchange_rate['au'],1)
    def wini_au(self,obj):
        if obj.weight <501:
            second_class_wini_au = pd.wini_AUPOST_au['<=500']
        elif obj.weight>500 and obj.weight<1001:
            second_class_wini_au = pd.wini_AUPOST_au['500-1000']
        else:
            second_class_wini_au = pd.wini_AUPOST_au['>1000']

        return round(second_class_wini_au/pd.exchange_rate['au'],1)



class ProductAdmin(admin.ModelAdmin):
    def volume(self,obj):
        volume = obj.Longest_side*obj.Median_side*obj.Shortest_side/1000000
        return round(volume,4)

    def us_sale_price_0(self, obj) :
        first_class_cost_us = obj.weight*pd.first_class_rate['first_class_rate_us']/pd.exchange_rate['us']
        second_class_cost_us = SecondClass.wini_us(self,obj)
        purchase_price = obj.price/pd.exchange_rate['us']
        sale_price_0 = (first_class_cost_us+second_class_cost_us+purchase_price)/0.85
        return u'<span style="color:red;font-weight:bold">%s</span>' % round(sale_price_0,1)
    us_sale_price_0.short_description = u'US(空)0%$'
    us_sale_price_0.allow_tags = True

    def cn_us_sale_price_0(self, obj) :
        first_class_cost_us = 0
        second_class_cost_us = SecondClass.eub_us(self,obj)  #调用SecondClass类
        purchase_price = obj.price/pd.exchange_rate['us']
        sale_price_0 = (first_class_cost_us+second_class_cost_us+purchase_price)/0.85
        return u'<span style="color:red;font-weight:bold">%s</span>' % round(sale_price_0,1)
    cn_us_sale_price_0.short_description = u'US(本)0%$'
    cn_us_sale_price_0.allow_tags = True


    def us_sea_sale_price_0(self,obj):
        first_class_cost_us = ProductAdmin.volume(self,obj)*pd.sea['us_fee']/pd.exchange_rate['us']
        second_class_cost_us = SecondClass.wini_us(self,obj)
        purchase_price = obj.price/pd.exchange_rate['us']
        sale_price_0 = (first_class_cost_us+second_class_cost_us+purchase_price)/0.85
        return u'<span style="color:red;font-weight:bold">%s</span>' % round(sale_price_0,1)
    us_sea_sale_price_0.short_description = u'US(海)0%$'
    us_sea_sale_price_0.allow_tags = True


    def uk_sale_price_0(self, obj) :
        first_class_cost_uk = obj.weight*pd.first_class_rate['first_class_rate_uk']/pd.exchange_rate['uk']
        second_class_cost_uk = SecondClass.wini_uk(self,obj)
        purchase_price = obj.price/pd.exchange_rate['uk']
        sale_price_0 = (first_class_cost_uk+second_class_cost_uk+purchase_price)/0.85
        return u'<span style="color:green;font-weight:bold">%s</span>' % round(sale_price_0,1)
    uk_sale_price_0.short_description = u'UK(空)0%£'
    uk_sale_price_0.allow_tags = True

    def cn_uk_sale_price_0(self, obj) :
        first_class_cost_uk = 0
        second_class_cost_uk = SecondClass.cn_uk(self,obj)
        purchase_price = obj.price/pd.exchange_rate['uk']
        sale_price_0 = (first_class_cost_uk+second_class_cost_uk+purchase_price)/0.85
        return u'<span style="color:green;font-weight:bold">%s</span>' % round(sale_price_0,1)
    cn_uk_sale_price_0.short_description = u'UK(本)0%£'
    cn_uk_sale_price_0.allow_tags = True

    def uk_sea_sale_price_0(self,obj):
        first_class_cost_uk = ProductAdmin.volume(self,obj)*pd.sea['uk_fee']/pd.exchange_rate['uk']
        second_class_cost_uk = SecondClass.wini_uk(self,obj)
        purchase_price = obj.price/pd.exchange_rate['uk']
        sale_price_0 = (first_class_cost_uk+second_class_cost_uk+purchase_price)/0.85
        return u'<span style="color:green;font-weight:bold">%s</span>' % round(sale_price_0,1)
    uk_sea_sale_price_0.short_description = u'UK(海)0%£'
    uk_sea_sale_price_0.allow_tags = True



    def de_sale_price_0(self, obj) :
        first_class_cost_de = obj.weight*pd.first_class_rate['first_class_rate_de']/pd.exchange_rate['de']
        second_class_cost_de = SecondClass.wini_de(self,obj)
        purchase_price = obj.price/pd.exchange_rate['de']
        sale_price_0 = (first_class_cost_de+second_class_cost_de+purchase_price)/0.85
        return u'<span style="color:blue;font-weight:bold">%s</span>' % round(sale_price_0,1)
    de_sale_price_0.short_description = u'DE(空)0%€'
    de_sale_price_0.allow_tags = True

    def cn_de_sale_price_0(self, obj) :
        first_class_cost_de = 0
        second_class_cost_de = SecondClass.cn_de(self,obj)
        purchase_price = obj.price/pd.exchange_rate['de']
        sale_price_0 = (first_class_cost_de+second_class_cost_de+purchase_price)/0.85
        return u'<span style="color:blue;font-weight:bold">%s</span>' % round(sale_price_0,1)
    cn_de_sale_price_0.short_description = u'DE(本)0%€'
    cn_de_sale_price_0.allow_tags = True

    def de_sea_sale_price_0(self, obj) :
        first_class_cost_de = ProductAdmin.volume(self,obj)*pd.sea['de_fee']/pd.exchange_rate['de']
        second_class_cost_de = SecondClass.wini_de(self,obj)
        purchase_price = obj.price/pd.exchange_rate['de']
        sale_price_0 = (first_class_cost_de+second_class_cost_de+purchase_price)/0.85
        return u'<span style="color:blue;font-weight:bold">%s</span>' % round(sale_price_0,1)
    de_sea_sale_price_0.short_description = u'DE(海)0%€'
    de_sea_sale_price_0.allow_tags = True


    def au_sale_price_0(self, obj) :
        first_class_cost_au = obj.weight*pd.first_class_rate['first_class_rate_au']/pd.exchange_rate['au']
        second_class_cost_au = SecondClass.wini_au(self,obj)
        purchase_price = obj.price/pd.exchange_rate['au']
        sale_price_0 = (first_class_cost_au+second_class_cost_au+purchase_price)/0.85
        return u'<span style="color:orange;font-weight:bold">%s</span>' % round(sale_price_0,1)
    au_sale_price_0.short_description = u'AU(空)0%$'
    au_sale_price_0.allow_tags = True

    def cn_au_sale_price_0(self, obj) :
        first_class_cost_au = 0
        second_class_cost_au = SecondClass.cn_au(self,obj)
        purchase_price = obj.price/pd.exchange_rate['au']
        sale_price_0 = (first_class_cost_au+second_class_cost_au+purchase_price)/0.85
        return u'<span style="color:orange;font-weight:bold">%s</span>' % round(sale_price_0,1)
    cn_au_sale_price_0.short_description = u'AU(本)0%$'
    cn_au_sale_price_0.allow_tags = True

    def au_sea_sale_price_0(self, obj) :
        first_class_cost_au = ProductAdmin.volume(self,obj)*pd.sea['au_fee']/pd.exchange_rate['au']
        second_class_cost_au = SecondClass.wini_au(self,obj)
        purchase_price = obj.price/pd.exchange_rate['au']
        sale_price_0 = (first_class_cost_au+second_class_cost_au+purchase_price)/0.85
        return u'<span style="color:orange;font-weight:bold">%s</span>' % round(sale_price_0,1)
    au_sea_sale_price_0.short_description = u'AU(海)0%$'
    au_sea_sale_price_0.allow_tags = True


    def preview(self,obj):    #show photos in admin

        return '<img src="%s" height="64" width="64" />' %(obj.image)

    preview.allow_tags = True

    preview.short_description = "图片"

    def color_status(self,obj):
        if obj.status == "淘汰":
            color_code = 'red'
        else:
            color_code = 'green'
        return (u'<span style="color:%s;font-weight:bold">%s</span>' %(color_code,obj.status))
    color_status.short_description = u'状态'
    color_status.allow_tags = True





   #show in admin
    list_display = (
        'category',
        'time',
        'sku',
        'preview',
        'owner',
        'name',
        'color_status',
        'price',
        'weight',
        'volume',
        'cn_us_sale_price_0',
        'us_sale_price_0',
        'us_sea_sale_price_0',
        'cn_uk_sale_price_0',
        'uk_sale_price_0',
        'uk_sea_sale_price_0',
        'cn_de_sale_price_0',
        'de_sale_price_0',
        'de_sea_sale_price_0',
        'cn_au_sale_price_0',
        'au_sale_price_0',
        'au_sea_sale_price_0',


    )
    #edited
    fields = (
        'category',
        'time',
        'image',
        'sku',
        'name',
        'status',
        'price',
        'weight',
        'Longest_side',
        'Median_side',
        'Shortest_side',


    )

    search_fields = ('sku','name',)
    ordering = ('sku',)
    list_filter = ('category','status')
    list_per_page = 20


class BingHengAdmin(admin.ModelAdmin):

    def preview(self,obj):    #show photos in admin

        return '<a href="%s" target="_blank" ><img src="%s" height="64" width="64" /></a>' %(obj.url,obj.image)

    preview.allow_tags = True

    preview.short_description = "图片"

    def url(self,obj):
        return u'<a href="%s" target="_blank" ></a>' % (obj.url)
    url.short_description = u'链接'
    url.allow_tags = True


    list_display = (
        'sku',
        'dayly_sale',
        'name',
        'url',
        'preview',
        'us_dayly_sale',
        'uk_dayly_sale',
        'de_dayly_sale',
        'au_dayly_sale',


    )
    fields = (
        'sku',
        'name',
        'url',
        'image',
        'us_dayly_sale',
        'uk_dayly_sale',
        'de_dayly_sale',
        'au_dayly_sale',
    )

    search_fields = ('sku','name',)
    list_per_page = 20

admin.site.register(Product_A,)
admin.site.register(BingHeng,BingHengAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.site_header = "产品信息系统"
admin.site.index_title = "eBayA组产品最低售价表"
#LogEntry.objects.all().delete()#delete recent actions