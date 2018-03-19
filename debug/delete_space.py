# -*- coding:utf-8 -*-
__author__ = 'XJX'
__date__ = '2018.03.19'


"""
description:
    将一个目录下所有文件中的'&quot'和'&nbsp;'删除
    该目录下创建一个新目录newdir
    新目录下fileNames.txt创建一个文本存入所有的word文件名
    本版本具有一定的容错性，即允许对同一文件夹多次操作而不发生冲突
"""

import sys
sys.path.remove('/System/Library/Frameworks/Python.framework/Versions/2.7/Extras/lib/python')
sys.path.append('/Users/xujiaxing/anaconda/lib/python3.6/site-packages')
import os
import re
import fnmatch


def Extract(aimpath):

    # print(aimpath)
    # 该目录下所有文件的名字
    files = os.listdir(aimpath)
    # 该目下创建一个新目录newdir，用来放转化后的txt文本
    New_dir = os.path.abspath(os.path.join(aimpath, 'newdir'))
    if not os.path.exists(New_dir):
        os.mkdir(New_dir)
    # print(New_dir)
    # 创建一个文本存入所有的word文件名
    fileNameSet = os.path.abspath(os.path.join(New_dir, 'fileNames.txt'))
    o = open(fileNameSet, "w", encoding="utf-8")
    for filename in files:
        # try:
            print(filename)
            if not fnmatch.fnmatch(filename, '*.txt'):
                continue
            oldpath = os.path.abspath(os.path.join(aimpath, filename))
            newpath = os.path.join(os.path.join(aimpath, 'newdir'), filename)
            print(oldpath)

            new_file = open(newpath, 'w', encoding="utf-8")
            f1 = open(oldpath, 'r+', encoding="utf-8")
            ans = f1.readline()
            print(ans)
            for line in f1.readlines():
                print(line)
                date_tran1 = re.sub('(&quot)+', '')
                line = line.replace(line, date_tran1)
                date_tran2 = re.sub('(&nbsp;)+', '')
                line = line.replace(line, date_tran2)
                new_file.write(line)

            new_file.close()
            f1.close()
            o.write(newpath + '\n')

        # except:
        #     print('error')
        #     continue

    o.close()

if __name__ == '__main__':
    Extract('../data/result')
    print("done")
