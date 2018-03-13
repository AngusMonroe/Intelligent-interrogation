#-*- coding:utf-8 -*-
#筛选数据
import requests
from bs4 import BeautifulSoup#解析网页
import json
import urllib2
import re
import urllib

#headers = {
#    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
#    'Accept-Encoding':'gzip, deflate, br',
#    'Accept-Language':'zh-CN,zh;q=0.8',
#    'Cache-Control':'max-age=0',
#    'Connection':'keep-alive',
#    'Referer':'http://baike.baidu.com/',
#    'Cookie':'BAIDUID=4B0F3B32E00361E4CDED0F57EB2FB8CF:FG=1; BIDUPSID=4B0F3B32E00361E4CDED0F57EB2FB8CF; PSTM=1479126128; baikedeclare=showed; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; pgv_pvi=1599590400; pgv_si=s6941842432; Hm_lvt_55b574651fcae74b0a9f1cf9c8d7c93a=1500095322,1501054718,1501151630,1501221970; Hm_lpvt_55b574651fcae74b0a9f1cf9c8d7c93a=1501226299',
#    'Host':'baike.baidu.com',
#    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
#}

def getHtml(url):
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    return response.read().decode('utf-8')

f=open("/users/xujiaxing/downloads/1.txt)
p = open("C:\Users\lenono\Desktop\entity_error_error.txt", "a")
file = open("C:\Users\lenono\Desktop\entity_new1.txt", "a")
line = f.readline()
n = 0;
flag1 = 0;
flag2 = 0;
while line:
    url = 'https://baike.baidu.com/item/'+str(line)
    html = getHtml(url)
    soup = BeautifulSoup(html,'html.parser')
    if str(soup.title.string.encode('utf-8')) == str('百度百科——全球最大中文百科全书'):
         m = 11111111111111111111
         print(m)
         p.write(line)
         flag1 = flag1 + 1;
    #if str(soup.title.string.encode('utf-8')) != str('百度百科——全球最大中文百科全书'):
        #file.write(line)

        #flag2 = flag2 + 1;
    n = n+1;
    print(n)
    #for text in soup.find_all('div',class_="para"):
#    fp.write("#######################")
#    fp.write("\n")
#    fp.write("\n")
#    fp.write("URL:")
#    print url
#    fp.write(url)
#    fp.write("\n")
#    fp.write("title:")
#    fp.write("\n")

#    soup.title.string = soup.title.string.replace("_","")
#    soup.title.string = soup.title.string.encode('utf-8').replace("百","")
#    soup.title.string = soup.title.string.encode('utf-8').replace("度","")
#    soup.title.string = soup.title.string.encode('utf-8').replace("科","")
#    print soup.title.string
#    fp.write(soup.title.string.encode('utf-8'))
#    fp.write("\n")
#    fp.write("\n")
#    fp.write("content:")
#    fp.write("\n")
#    for text in soup.select('div[class="para"]'):
#        fp.writelines(text.get_text().encode('utf-8'))
    line = f.readline()

print flag1
print flag2
file.close()
f.close()
p.close()
