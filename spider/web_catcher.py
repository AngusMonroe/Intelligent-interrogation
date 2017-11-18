__author__='XJX'
__date__='2017.07.19'

import re
import urllib.request
import urllib
import xlwt
  
#网址
url1 = "http://drugs.medlive.cn/drugref/html/"
url2 = ".shtml"
i = 1
book=xlwt.Workbook(encoding='utf-8')
sheet1=book.add_sheet('sheet1',cell_overwrite_ok=True)
heads=[u'药品名称',u'所属类别',u'性状',u'适应症',u'用法用量',u'不良反应',u'注意事项',u'url']
ii=0
for head in heads:
    sheet1.write(0,ii,head)
    ii+=1
for n in range(2,14579):
    url = url1 + str(n) + url2
    
    try:
        #抓取页面
        urlop = urllib.request.urlopen(url,timeout=100)
    except Exception:
        print("超时")
        continue
    #判断是否为html页面
    if 'html' not in urlop.getheader('Content-Type'):
        continue

    #避免程序异常中止, 用try..catch处理异常
    try:
        #转换为utf-8码
        data = urlop.read().decode('utf-8')
        #print(data)
    except:
        continue

    #正则表达式提取页面中所有队列, 并判断是否已经访问过, 然后加入待爬队列
    linkre1 = re.compile("<label class=\"w110\">【通用名称】</label>\\s*\\s*(.*?)\\s*\\s*<")
    for x in linkre1.findall(data):##返回所有有匹配的列表
        sheet1.write(i,0,x)
        print(x)

    linkre2 = re.compile("class=\"have-h\">\\s*(.*?)\\s*</a>\\s*</p>\\s*</div>")
    for x in linkre2.findall(data):##返回所有有匹配的列表
        sheet1.write(i,1,x)
        #print(x)

    linkre3 = re.compile("性状：</a>\\s*</div>\\s*<div class=\"more-infomation\">\\s*<p>(.*?)</p>\\s*</div>")
    for x in linkre3.findall(data):##返回所有有匹配的列表
        sheet1.write(i,2,x)
        #print(x)
    
    linkre4 = re.compile("适应症：</a>\\s*</div>\\s*<div class=\"more-infomation\">\\s*<p>(.*?)</p>\\s*</div>")
    for x in linkre4.findall(data):##返回所有有匹配的列表
        sheet1.write(i,3,x)
        #print(x)

    linkre5 = re.compile("用法用量：\\s*</a>\\s*</div>\\s*<div class=\"more-infomation\">\\s*<p>(.*?)</p>\\s*</div>")
    for x in linkre5.findall(data):##返回所有有匹配的列表
        sheet1.write(i,4,x)
        #print(x)

    linkre6 = re.compile("不良反应：</a>\\s*</div>\\s*<div class=\"more-infomation\">\\s*<p>(.*?)</p>\\s*</div>")
    for x in linkre6.findall(data):##返回所有有匹配的列表
        sheet1.write(i,5,x)
        #print(x)

    linkre7 = re.compile("注意事项：</a>\\s*</div>\\s*<div class=\"more-infomation\">\\s*<p>(.*?)</p>\\s*</div>")
    for x in linkre7.findall(data):##返回所有有匹配的列表
        sheet1.write(i,6,x)
        #print(x)

    sheet1.write(i,7,x)
    print(url)
    i += 1
    book.save("/Users/xujiaxing/Desktop/data.xls")

