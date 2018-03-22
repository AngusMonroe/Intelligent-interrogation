# -*- coding: utf-8 -*-
__author__ = 'ZZX'
__date__ = '2018.03.17'

"""
description:
    将用于训练的文章重新归类
"""

import sys
# sys.path.remove('/System/Library/Frameworks/Python.framework/Versions/2.7/Extras/lib/python')
sys.path.append('/Users/xujiaxing/anaconda/lib/python3.6/site-packages')
import os
import jieba
import jieba.analyse
from gensim.models import word2vec
model = word2vec.Word2Vec.load("../../data/ml.model")


def text_to_words(text, key_num):
    txt_key = jieba.analyse.extract_tags(text, key_num, withWeight=False)  # 从输入中提取关键词
    return txt_key


def calc(txt_key, factor):
    weight = []
    for index in range(len(txt_key)):
        try:
            weight.append(model.similarity(txt_key[index], factor[index]))

        except:
            continue

    ans = 0.0
    for i in weight:
        ans += i
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
            # print(words)
            ans.append(words[0])
        if kind == 0:
            return ans
        # print("---------------")
        # print(kind)


# 1.待比较文本 2.某一类共有多少关键词 3.比较关键词路径 4.共有多少类
def manager(text, key_num, factor_path, nkind, filename):
    txt_key = text_to_words(text, key_num)
    value = []
    for kind in range(nkind):
        factor = load(factor_path, kind, key_num)
        value.append(calc(txt_key, factor))
    ans = 0
    big = 0
    for index in range(nkind):
        # print(value[index])
        if value[index] > big:
            big = value[index]
            ans = index

    file = open("../../data/map/" + str(ans) + ".txt", "a", encoding="utf-8")
    file.write(filename + " " + str(big) + "\n")
    print("the kind is:" + str(ans) + "  weight is: " + str(big))


if __name__ == '__main__':
    # ans = load("../python-LDA/data/tmp/model_twords.dat", 2, 20)
    root = "../../data/result/"
    files = os.listdir(root)

    for filename in files:
        txt = open(root + filename, encoding="gbk")
        word = txt.read()
        manager(word, 20, "data/tmp/model_twords.dat", 100, filename)
        # break
        # print(word)

    print("done")
