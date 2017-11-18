__author__='XJX'
__date__='2017.07.26'

# -*- coding: UTF-8 -*-  
# How to read from an Excel using xlrd module  
import xlrd
import xlwt
import jieba
from xlutils.copy import copy
import os.path


# 打开指定路径中的xls文件  
xlsfile = r'/users/xujiaxing/desktop/data.xls'  
book = xlrd.open_workbook(xlsfile,formatting_info=True)  # 得到Excel文件的book对象
  
# 得到sheet对象  
sheet0 = book.sheet_by_index(0)     # 通过sheet索引获得sheet对象  
sheet_name0 = book.sheet_names()[0]  # 获得指定索引的sheet名字  
print (sheet_name0)  
sheet0 = book.sheet_by_name(sheet_name0)     # 通过sheet名字来获取，当然如果知道sheet名字就可以直接指定  

sheet1 = book.sheet_by_index(1)     # 通过sheet索引获得sheet对象  
sheet_name1 = book.sheet_names()[1]  # 获得指定索引的sheet名字  
print (sheet_name1)  
sheet1 = book.sheet_by_name(sheet_name1)     # 通过sheet名字来获取，当然如果知道sheet名字就可以直接指定  

wb = copy(book) 
sheet = wb.get_sheet(1)

# 获得行数和列数  
nrows = sheet0.nrows    # 行总数  
print(nrows)

k = 1
for j in range(1nrows):
    cell_value = sheet0.cell_value(j, 3)
    print(cell_value)
    word = list(jieba.cut(cell_value,cut_all=False))#精确模式
    for n in word:
        sheet.write(k,1,j)
        sheet.write(k,2,n)
        print(j)
        print(n)
        k += 1
    j += 1
    #book.save("/Users/xujiaxing/Desktop/data.xls")
    wb.save("/Users/xujiaxing/Desktop/data.xls")

