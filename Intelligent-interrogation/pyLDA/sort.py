# -*- coding: utf-8 -*-

__author__ = 'ZZX'
__date__ = '2018.03.20'

"""
description:
    将目录下所有txt按照某一数值由大到小排序
"""

import os
import re
import math

root = '../../data/map200/'
files = os.listdir(root)

for filename in files:
    f = open(root + filename, 'r')
    s = f.readline()
    data_list = []
    while (s):
        temp = s.split()
        data_list.append((temp[0], float(temp[1])))
        print(data_list)
        s = f.readline()
    data_list = sorted(data_list, key=lambda x:x[1], reverse=True)
    print(data_list)
    f = open(root + filename, 'w')
    f.truncate()
    for elem in data_list:
        f.write(elem[0])
        f.write(" ")
        f.write(str(elem[1]))
        f.write('\n')

print("ok")

