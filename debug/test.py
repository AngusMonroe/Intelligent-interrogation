# -*- coding: utf-8 -*-
import os
import re

root = '../data/'
name1 = 'MedicalRecordFile/'
name2 = 'result/'
files = os.listdir(root + name1)

for filename in files:
    #print(filename)
    htmlfile = open(root + name1 + filename,encoding="utf-8")
    htmlcont = htmlfile.read()
    result0 = re.search("患者病史确认单", htmlcont)
    result1 = re.findall("主[&nbsp;]*诉：[&nbsp]*;</span><span style=\"font-family: 宋体; font-size: 16px;\">(\S+)</span></p>", htmlcont)
    result2 = re.findall("现[&nbsp;]*病[&nbsp;]*史：[&nbsp;]*</span><span style=\"font-family: 宋体; font-size: 16px;\">(\S+)</span>+</p>", htmlcont)
    result3 = re.findall("既[&nbsp;]*往[&nbsp;]*史：[&nbsp;]*</span><span style=\"font-family: 宋体; font-size: 16px;\">(\S+)</span>+</p>", htmlcont)
    if(result0 and result1 and result2 and result3):
        filename2 = filename[0:len(filename) - 5]
        filename2 += '.txt'
        newfile = open(root + name2 + filename2, 'w',encoding="utf-8")
        for r in result1:
            newfile.write(r)
        for r in result2:
            newfile.write(r)
        for r in result3:
            newfile.write(r)

print("ok")

#ans = re.findall('r(run+)', 'rrrrrwww.runnoobrrrunnn.com')
#pattern = 主[&nbsp;]*诉：[&nbsp]*;</span><span style="font-family: 宋体; font-size: 16px;">(\S+)</span></p>
#re.search(txt. pattern)
#现[&nbsp;]*病[&nbsp;]*史：[&nbsp;]*</span>(<span style="font-family: 宋体; font-size: 16px;">(\S+)</span>)+</p>


