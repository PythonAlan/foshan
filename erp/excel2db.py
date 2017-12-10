#!/usr/bin/env python3
#antuor:Alan
# -*- coding:UTF-8 -*-

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lyerp.settings")


import django
if django.VERSION >= (1, 7):#自动判断版本
    django.setup()


from productlist.models import Product
import xlrd

data= xlrd.open_workbook('testupload.xlsx') #打开文件
table = data.sheet_by_index(0) #获取工作表
WorkList = []
nrows = table.nrows #行数
ncols = table.ncols #列数
for i in range(1,nrows):
    row = table.row_values(i) #获取每行值
    WorkList.append(
        Product(
            category = row[0],
            image = row[1],
            sku = row[2],
            name = row[3],
            status = row[4],
            price = row[5],
            weight = row[6],
            volume = row[7],

        )
    )
    print(WorkList)
#Product.objects.get_or_create(WorkList)
#Product.objects.update_or_create(WorkList)
Product.objects.bulk_create(WorkList)
print ('数据导入成功')