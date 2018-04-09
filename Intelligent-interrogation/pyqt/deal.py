import Levenshtein
import xlrd

__author__ = 'XJX'
__date__ = '2018.03.26'
# -*- coding: utf-8 -*-

import sys
from gensim.models import word2vec
import webbrowser
import jieba.analyse
from match import *


model = word2vec.Word2Vec.load("../../data/ml.model")


# 输出: 最有行数（行数从0开始）
def matchKeyWords(path, keys, keysWeight, colsWeight, ansNum, ans):
    # 读取excel中相关信息
    data = xlrd.open_workbook(path)
    sheet1 = data.sheet_by_name('sheet1')
    rowsNum = sheet1.nrows  # 总行数
    colsNum = 3

    # 初始化value清零
    value = [0 for x in range(0, rowsNum)]
    # 对每个关键字，与表格中所有字符串匹配
    for i in range(0, 5):
        key_ = keys[i]
        for row in range(1, rowsNum):
            arrRow = sheet1.row_values(row)  # 第row行字符串
            for col in range(0, 3):
                # 计算相似度加入字符串所在行
                value[row] += Levenshtein.jaro(key_, str(arrRow[col])) * colsWeight[col] * keysWeight[i]

    # 对行数与其对应value组成二元组按value从大到小排序
    arr = []
    for i in range(0, rowsNum):
        arr.append((value[i], i))
    arr = sorted(arr, reverse=True)
    print('您的建议用药有：')
    for i in range(0, ansNum):
        cell_value = sheet1.cell_value(arr[i][1], 2)
        ans += cell_value + '\n'
        print(cell_value)
        # print(ans[i][1])
    return ans

def deal(path1, path2, path3, ans):
    f1 = open(path1, "r", encoding="utf-8")
    f2 = open(path2, "r", encoding="utf-8")
    txt1 = f1.read()
    txt2 = f2.read()
    f1.close()
    f2.close()

    if txt1:
        jieba.load_userdict("../../data/jibingICD.txt")
        stoplist = {}.fromkeys([line.strip() for line in open("../python-LDA/data/stopword.txt")])
        txt_key = jieba.analyse.extract_tags(txt1, topK=2, withWeight=False)  # 从输入中提取关键词
        print(txt_key)
        txt_key = [word for word in list(txt_key) if word not in stoplist]  # 去停用词

        model = word2vec.Word2Vec.load("../../data/ml.model")
        if len(txt_key ) >1:  # 双关键词
            print(model.similarity(txt_key[0], txt_key[1]))
            if model.similarity(txt_key[0], txt_key[1] )> 0.5:  # 两关键词比较相近，使用两个关键词进行匹配
                y2 = model.most_similar(txt_key, topn=4)  # 4个最相关的
                print("和【%s】最相关的词有：\n" % txt_key)
            else: # 关键词差距较大，只使用第一个关键词匹配
                y2 = model.most_similar(txt_key[0], topn=4)  # 4个最相关的
                print("和【%s】最相关的词有：\n" % txt_key[0])
        else:  # 单关键词
            y2 = model.most_similar(txt_key[0], topn=4)  # 4个最相关的
            print("和【%s】最相关的词有：\n" % txt_key[0])

        key = [0 for x in range(0, 6)]
        i = 1
        key[0] = txt_key[0]
        for item in y2:
            print(item[0], item[1])
            # name = item[0].encode("utf-8")
            key[i] = item[0]
            # key.append((name,i))
            i = i + 1

        path = r'../../data/disease_information.xls'

        # key[1] = u"肾性高血压"
        # key[2] = u"心功能不全"
        # key[3] = u"充血性心力衰竭"
        # key[4] = u"高血压病"
        # key[5] = u"高血脂"
        keys = [key[0], key[1], key[2], key[3], key[4]]

        weight1 = 2.0
        weight2 = 1.75
        weight3 = 1.5
        weight4 = 1.25
        weight5 = 1.0
        keysWeight = [weight1, weight2, weight3, weight4, weight5]

        diseaseWeight = 1.0
        symptomWeight = 0.8
        drugWeight = 0.6
        colsWeight = [diseaseWeight, symptomWeight, drugWeight]

        ansNum = 10

        ans = matchKeyWords(path, keys, keysWeight, colsWeight, ansNum, ans)

        # ms = MSSQL(host="47.94.12.243", user="sa", pwd="Jiuyi8899", db="Database")
        # reslist = ms.ExecQuery("select 适应症 from data")

        # if not self.childwindow.isVisible():
        #     self.show()
        f3 = open(path3, "w", encoding="utf-8")
        f3.write(ans)
        f3.close()
        print("test")

    if txt2:
        aim = match(txt2, 20, "../python-LDA/data/tmp100/model_twords.dat", 100)
        print(aim)
        # view = QWebEngineView()
        # channel = QWebChannel()
        # handler = CallHandler()
        # channel.registerObject('pyjs', handler)
        # view.page().setWebChannel(channel)
        # url_string = aim
        # view.load(QUrl(url_string))
        # view.show()
        web = webbrowser.get('chrome')
        web.open_new(aim)

if __name__ == '__main__':
    ans = "您的建议用药有：\n"
    deal('input1.txt', 'input2.txt', 'output.txt', ans)