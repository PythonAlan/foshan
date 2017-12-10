#!/usr/bin/env python3
#antuor:Alan
# -*- coding:UTF-8 -*-

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lyerp.settings")


import django
if django.VERSION >= (1, 7):#自动判断版本
    django.setup()


from productlist.models import BingHeng
import xlrd

data= xlrd.open_workbook('testupload1.xlsx') #打开文件
table = data.sheet_by_index(0) #获取工作表
WorkList = []
nrows = table.nrows #行数
ncols = table.ncols #列数
for i in range(1,nrows):
    row = table.row_values(i) #获取每行值
    WorkList.append(
        BingHeng(
            sku = row[0],
            dayly_sale = row[1],
            name = row[2],
            url = row[3],
            image  = row[4],
            us_dayly_sale = row[5],
            uk_dayly_sale = row[6],
            de_dayly_sale = row[7],
            au_dayly_sale = row[8],

        )
    )
    print(WorkList)
#Product.objects.get_or_create(WorkList)
#Product.objects.update_or_create(WorkList)
BingHeng.objects.bulk_create(WorkList)
print ('数据导入成功')