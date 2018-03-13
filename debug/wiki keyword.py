__author__='XJX'
__date__='2017.08.04'

# -*- coding: UTF-8 -*-  
import jieba
import os.path
import os
import codecs
#jieba.load_userdict("/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/jieba/userdict.txt")
#import jieba.posseg as pseg

print('start')

input_txt = open('/users/xujiaxing/downloads/context(2).txt','r',encoding='utf8')
output_txt = open('/users/xujiaxing/downloads/context_done(2).txt','w',encoding='utf8')

#mdzz = 'mdzz'
#output_txt.write(mdzz)
i = 1
for line in input_txt:
    print(i)
    seg = jieba.cut(line.strip(),cut_all=False)
    s =  ' '.join(seg)
    m = list(s)
    for word in m:
        output_txt.write(word)
    i += 1
    
output_txt.close()
input_txt.close()
