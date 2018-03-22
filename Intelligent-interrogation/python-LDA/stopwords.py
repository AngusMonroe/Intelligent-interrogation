__author__ = 'XJX'
__date__ = '2018.03.13'
# -*- coding: utf-8 -*-

"""
description:
    Wipe off stopwords from data.txt
"""

import re
import codecs
import configparser

conf = configparser.ConfigParser()
conf.read("setting.conf")

def SplitStr(initStr, splitFlag = ' '):
    tmpList = initStr.split(splitFlag)  # 使用spilt(sep = ' ',maxsplit = -1 )分割字符串
    tmpList = list(filter(lambda x: x != '', tmpList))  # 从列表中去除空字符
    return tmpList


def stopword(inputpath, outputpath):

    infile = open(inputpath, 'r')
    outfile = open(outputpath, 'a')
    stoplist = {}.fromkeys([line.strip() for line in open("data/stopword.txt")])
    print(stoplist)
    for line in infile:
        keys = [word for word in SplitStr(line) if word not in stoplist]  # 去停用词
        for key in keys:
            zhPattern = re.compile(u'[\u4e00-\u9fa5]+')
            match = zhPattern.search(key)

            if match:
                outfile.write(key + ' ')
    print('done')

    outfile.close()
    infile.close()

if __name__ == '__main__':
    inputpath = '../data/data.txt'
    outputpath = '../data/output.txt'
    stopword(inputpath, outputpath)

