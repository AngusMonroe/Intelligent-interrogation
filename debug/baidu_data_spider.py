__author__='XJX'
__date__='2017.08.08'

#-*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
import urllib
from urllib import request
import re
import sys
import io
import sys
#reload(sys)

#sys.setdefaultencoding('utf-8')
def getHtml(url):
    return urllib.request.urlopen(url).read().decode('utf-8')
    #request = urllib.Request(url)
    #print('mdzz')
    #response = urllib.urlopen(request)
    #return response.read().decode('utf-8')

file_in = r'C:\Users\JY\Desktop\1.txt'
file_out = r'C:\Users\JY\Desktop\data2.txt'
f = open(file_in,'r')
fp = open(file_out, 'w',encoding = 'utf8')
n = 0
flag = 0
for line in f:
    line = line[:-1]
    if str(line) == '糖尿病性心脏病':
        flag = 1
    if flag == 1:
        try:
            print(str(line))
            url0 = "https://baike.baidu.com/item/"
            url = url0 + urllib.parse.quote(str(line))
            #print(url)
            html = getHtml(url)
            soup = BeautifulSoup(html,'html.parser')
            #print(soup.title)
            if str(soup.title) == '<title>百度百科——全球最大中文百科全书</title>':
                print('404')
                continue
            #fp.write(u"#######################")
            #fp.write(u"\n")
            #fp.write(u"\n")
            #fp.write(u"URL:")
            #p.write(url)
            #fp.write(u"\n")
            #fp.write(u"title:")
            #fp.write(u"\n")
            #print('debug1')
            #soup.title.string = soup.title.string.replace("_","")
            #soup.title.string = soup.title.string.encode('utf-8').replace("百","")
            #soup.title.string = soup.title.string.encode('utf-8').replace("度","")
            #soup.title.string = soup.title.string.encode('utf-8').replace("科","")
            #print('debug2')
            #fp.write(soup.title.string)
            #fp.write(u"\n")
            #fp.write(u"\n")
            #fp.write(u"content:")
            #fp.write(u"\n")
            #print('debug3')
            for text in soup.find_all('div',class_="para"):
                for div_tag in text.find_all('div', class_="description"):
                    div_tag.decompose()
                if text.span:
                    text.span.decompose()
                newstr ="".join(text.get_text().split())
                #newstr = newstr.encode('gbk')
                newstr = re.sub(r'\[[\d]*\]','',newstr)
                newstr = re.sub(r'\[[\d]*-[\d]\]', '', newstr)
                fp.write(newstr)
            fp.write(u"\n")
            #fp.write(u"\n")
            n = n+1
            print(n)
        except:
            print('error')
            continue
    
fp.close()
f.close()
