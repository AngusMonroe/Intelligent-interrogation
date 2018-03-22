# -*- coding:utf-8 -*-

__author__ = 'XJX'
__date__ = '2018.03.19'

import jieba
import jieba.analyse
import re


if __name__ == '__main__':

    jieba.load_userdict("../../data/jibingICD.txt")
    stoplist = {}.fromkeys([line.strip() for line in open("data/stopword.txt")])
    f1 = open('../../data/file.txt', 'r', encoding="utf-8")
    f2 = open('data/data.txt', 'w')

    for line in f1:
        txt_key = jieba.analyse.extract_tags(line, topK=30, withWeight=False)  # 从输入中提取关键词
        for word in txt_key:
            zhPattern = re.compile(u'[\u4e00-\u9fa5]+')
            match = zhPattern.search(word)

            if match:
                f2.write(word + ' ')

        f2.write('\n')

    f1.close()
    f2.close()

    print("done")




