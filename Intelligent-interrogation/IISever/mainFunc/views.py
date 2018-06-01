#coding:utf-8
import webbrowser

import Levenshtein
import jieba
import jieba.analyse
import re
import xlrd
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.
from gensim.models import word2vec


def matchKeyWords(path, keys, keysWeight, colsWeight, ansNum):
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
    ans = []
    for i in range(0, rowsNum):
        ans.append((value[i], i))
    ans = sorted(ans, reverse=True)
    print('您的建议用药有：')
    res = ''
    for i in range(0, ansNum):
        cell_value1 = sheet1.cell_value(ans[i][1], 2)
        # cell_value2 = sheet1.cell_value(ans[i][1], 3)
        ans += cell_value1 + '\n'
        res = res + cell_value1 + ',' + 'http://drugs.medlive.cn/drugref/drug_info_search.do?q=' + cell_value1 + ';'
        print(cell_value1)
        # print(ans[i][1])
    return res


def solve(txt1):
    if txt1:
        jieba.load_userdict("../../data/jibingICD.txt")
        stoplist = {}.fromkeys([line.strip() for line in open("../python-LDA/data/stopword.txt")])
        txt_key = jieba.analyse.extract_tags(txt1, topK=2, withWeight=False)  # 从输入中提取关键词
        print(txt_key)
        txt_key = [word for word in list(txt_key) if word not in stoplist]  # 去停用词

        model = word2vec.Word2Vec.load("../../data/ml.model")
        if len(txt_key)>1:  # 双关键词
            print(model.similarity(txt_key[0], txt_key[1]))
            if model.similarity(txt_key[0], txt_key[1])> 0.5:  #两关键词比较相近，使用两个关键词进行匹配
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

        ansNum = 5

        res = matchKeyWords(path, keys, keysWeight, colsWeight, ansNum)

        # ms = MSSQL(host="47.94.12.243", user="sa", pwd="Jiuyi8899", db="Database")
        # reslist = ms.ExecQuery("select 适应症 from data")

        print("test")
        return res


# 1.待比较文本 2.某一类共有多少关键词 3.比较关键词路径 4.共有多少类
def match(text, key_num, factor_path, nkind):
    txt_key = text_to_words(text, key_num)
    value = []
    for kind in range(nkind):
        factor = load(factor_path, kind, key_num)
        factor_coefficient = load2(factor_path, kind, key_num)
        value.append(calc(txt_key, factor, factor_coefficient))
    print("value:")
    print(value)
    ans = 0
    big = 0.0
    for index in range(nkind):
        # print(value[index])
        if value[index] > big:
            big = value[index]
            ans = index

    print("the kind is:" + str(ans) + "  weight is: " + str(big))

    f1 = open("../../data/map100/" + str(ans) + ".txt", "r", encoding="utf-8")
    line = f1.read()
    result = re.findall("(\S+).txt", line)
    print(result)
    f2 = open("../../data/result/newdir/" + str(result[0]) + ".txt", "r", encoding="gbk")
    aim = f2.read()

    f1.close()
    f2.close()

    # return aim
    return str(result[0]) + ".html"


def text_to_words(text, key_num):
    stoplist = {}.fromkeys([line.strip() for line in open("../python-LDA/data/stopword.txt")])

    txt_key = jieba.analyse.extract_tags(text, key_num, withWeight=False)  # 从输入中提取关键词
    txt_key = [word for word in list(txt_key) if word not in stoplist]  # 去停用词

    del_word = []
    for word in txt_key:
        result = re.findall("[^\u4e00-\u9fa5]+", word)
        if (result):
            del_word.append(word)
    for word in del_word:
        txt_key.remove(word)
    # print(txt_key)

    return txt_key


def calc(txt_key, factor, factor_coefficient):
    model = word2vec.Word2Vec.load("../../data/ml.model")
    ans = 0.0
    for index in range(len(txt_key)):
        for index2 in range(len(factor)):
            try:
                ans += model.similarity(txt_key[index], factor[index2])*factor_coefficient[index2]

            except:
                continue

    return ans


# kind从1开始
def load(factor_path, kind, key_num):
    f = open(factor_path)
    kind += 1
    while(1):
        ans = []
        kind -= 1
        f.readline()
        for i in range(key_num):
            str = f.readline()
            words = str.split()
            #print(words)
            ans.append(words[0])
        if kind == 0:
            return ans
        # print("---------------")
        # print(kind)


def load2(factor_path, kind, key_num):
    f = open(factor_path)
    kind += 1
    while (1):
        ans = []
        kind -= 1
        f.readline()
        for i in range(key_num):
            str = f.readline()
            words = str.split()
            if(len(words)==2):
               ans.append(float(words[1]))
            else:
                ans.append(0.0)
        if kind == 0:
            return ans
            # print("---------------")
            # print(kind)


@csrf_exempt
def main_text(request):
    if(request.method=="POST"):
        data=request.POST.get('string')  # data为输入的字符串
        # 接口

        result = solve(data)
        #
        return HttpResponse(
            json.dumps({
                "status": 1,
                "result": result
            })
        )

@csrf_exempt
def main_file(request):
    file = request.FILES.get('file')
    if file:  # 处理附件上传到方法
        txt = file.read().decode()
        txt = txt.replace('&nbsp;', '')
        linkre = re.findall("<span style=\"font-family: 宋体; font-size: 16px;font-weight: bold;\">主诉：</span>(\s*)<span style=\"font-family: 宋体; font-size: 16px;\">(\S+)</span>", txt)  # 匹配目标标题
        if not linkre:
            print('23333')
        aim = ''
        if linkre:
            print(linkre)
            word = linkre[0][1]
            word = word.replace('<span style="font-family: 宋体; font-size: 16px;font-weight: bold;">主诉：</span>', '')
            word = word.replace('<span style ="font-family: 宋体; font-size: 16px;">', '')
            word = word.replace('</span>', '')

            if word:
                aim = match(word, 20, "../python-LDA/data/tmp100/model_twords.dat", 100)
                print(aim)

        # 接口 file为输入文件(非路径)
        result = 'X-0.html'
        if aim:
            result = aim
        return HttpResponse(
            json.dumps({
                "status": 1,
                "result": result
            })
        )
