import sys
sys.path.remove('/System/Library/Frameworks/Python.framework/Versions/2.7/Extras/lib/python')
#sys.path.remove('/System/Library/Frameworks/Python.framework/Versions/2.7/Extras/lib/python/PyObjC')
sys.path.append('/Users/xujiaxing/anaconda/lib/python3.6/site-packages')

# -*- coding: utf-8 -*-
import Levenshtein
import xlrd
import xlwt
        
#path: excel绝对路径
#keys: 五个关键词数组，一定要是utf-8式编码，否则计算时汉字权重为3
#keysWeight： 五个关键词相关度
#colsWeight： 关键字匹配到不同列后所乘的权重参数（默认共三列）
#ansNum： 输出总数
#输出: 最有行数（行数从0开始）
def matchKeyWords(path, keys, keysWeight, colsWeight, ansNum):     
    #读取excel中相关信息
    data = xlrd.open_workbook(path)
    sheet1 = data.sheet_by_name('sheet1')
    rowsNum = sheet1.nrows #总行数
    colsNum = 3
    
    #初始化value清零
    value = [0 for x in range(0, rowsNum)]
    #对每个关键字，与表格中所有字符串匹配
    for i in range (0, 5):
        key = keys[i]
        for row in range (1, rowsNum):     
            arrRow = sheet1.row_values(row) #第row行字符串
            for col in range(0, 3):
                #计算相似度加入字符串所在行
                value[row] += Levenshtein.jaro(key , arrRow[col]) * colsWeight[col] * keysWeight[i]
    
    #对行数与其对应value组成二元组按value从大到小排序
    ans = []            
    for i in range(0, rowsNum):
        ans.append((value[i], i))
    ans = sorted(ans, reverse = True)
    for i in range(0, ansNum):
        print(ans[i][1])
        
 
path = r'/users/xujiaxing/downloads/data(1).xls'   

key1 = u"肾性高血压"
key2 = u"心功能不全"
key3 = u"充血性心力衰竭"
key4 = u"高血压病"
key5 = u"高血脂"
keys = [key1, key2, key3, key4, key5]

weight1 = 1.0
weight2 = 1.0
weight3 = 1.0
weight4 = 1.0
weight5 = 1.0
keysWeight = [weight1, weight2, weight3, weight4, weight5] 

diseaseWeight = 1.0
symptomWeight = 0.8
drugWeight = 0.6
colsWeight = [diseaseWeight, symptomWeight, drugWeight]

ansNum = 10 

matchKeyWords(path, keys, keysWeight, colsWeight, ansNum)
