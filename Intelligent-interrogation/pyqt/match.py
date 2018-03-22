# -*- coding: utf-8 -*-
__author__ = 'XJX'
__date__ = '2018.03.20'

"""
description:
    根据新文章匹配相似文章
"""

import os
import re
import jieba
import jieba.analyse
from gensim.models import word2vec
model = word2vec.Word2Vec.load("../../data/ml.model")
stoplist = {}.fromkeys([line.strip() for line in open("../python-LDA/data/stopword.txt")])

def text_to_words(text, key_num):
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
    ans = 0.0
    for index in range(len(txt_key)):
        for index2 in range(len(factor)):
            try:
                ans+= model.similarity(txt_key[index], factor[index2])*factor_coefficient[index2]

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
    return "../../data/MedicalRecordFile/" + str(result[0]) + ".html"


if __name__ == '__main__':
    word = "发热、咳嗽7天。患者7天前因受凉后出现发热，体温最高38.5℃，咳嗽，无痰。无胸闷、胸痛、咯血、喘憋、乏力、盗汗，在北京恒安医院诊断为感冒，给予头孢唑林钠静脉点滴（具体剂量不详）3天，症状未见好转，体温波动于38.0℃之间，就诊于我院，行胸部CT、B超检查，示右侧胸腔积液，门诊以;胸腔积液;收入我科。患者自发病以来神清，精神、体力差，食欲、睡眠尚可，大小便基本正常，体重下降约5公斤。否认肝炎史、疟疾史、结核史，否认高血压史、冠心病史，否认糖尿病史、脑血管病史、精神病史，20年前因行“腭裂修补术”。30年前腿部受轻伤。否认、、输血史，否认过敏史，预防接种史不详。"
    # input = open("../../data/result/40068631X2-0002973626-2-2-0-8.txt", "r", encoding="gbk")
    # word = input.read()
    # input.close()
    aim = match(word, 20, "../python-LDA/data/tmp100/model_twords.dat", 100)
    print(aim)
