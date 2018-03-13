#coding:utf-8
__author__='XJX'
__date__='2017.07.28'

import jieba
import jieba.analyse
import os
import codecs

in_text = r"/Users/xujiaxing/Downloads/temp.txt"
out_text = r"/Users/xujiaxing/Downloads/text.txt"

f1 = open(in_text,'r',encoding='utf8')
s1 = f1.read()
tags = jieba.analyse.extract_tags(s1,topK=20)
s2 = ','.join(tags)
print(s2)
l2 = s2.split(',')
f1.close()
f2 = open(in_text,'r',encoding='utf8')
s2 = ''
for i in f2.readlines():
    s2 = s2 + i
    seg_list = jieba.cut(s2)
    s2 = '|'.join(seg_list)
    f2.close()
    l4 = []
    for word in l2:
        for i in l3:
            if word in i.split('|'):
                l4.append(word+':'+i)

open(out_text,'w',encoding='utf8').close()
f3 = open(out_text,'a',encoding='utf8')
for i in l4:
    l5 = i.split('|')
    s4 = ''
    for word in l5:
        s4 = s4 + word
        f3.write(s4+'\n')
f3.close()
