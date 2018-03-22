#-*- coding:gbk -*-
__author__ = 'XJX'
__date__ = '2018.03.19'


"""
description:
    ��һ��Ŀ¼�������ļ��е�'&quot'��'&nbsp;'ɾ��
    ��Ŀ¼�´���һ����Ŀ¼newdir
    ��Ŀ¼��fileNames.txt����һ���ı��������е�word�ļ���
    ���汾����һ�����ݴ��ԣ��������ͬһ�ļ��ж�β�������������ͻ
"""

import sys
import os
import re
import fnmatch


def Extract(aimpath):

    # print(aimpath)
    # ��Ŀ¼�������ļ�������
    files = os.listdir(aimpath)
    # ��Ŀ�´���һ����Ŀ¼newdir��������ת�����txt�ı�
    New_dir = os.path.abspath(os.path.join(aimpath, 'newdir'))
    if not os.path.exists(New_dir):
        os.mkdir(New_dir)
    # print(New_dir)
    # ����һ���ı��������е�word�ļ���
    fileNameSet = os.path.abspath(os.path.join(New_dir, 'filesName.txt'))
    o = open(fileNameSet, "w")
    for filename in files:
        # try:
            print(filename)
            if not fnmatch.fnmatch(filename, '*.txt'):
                continue
            oldpath = os.path.abspath(os.path.join(aimpath, filename))
            newpath = os.path.join(os.path.join(aimpath, 'newdir'), filename)
            print(newpath)

            new_file = open(newpath, 'a',encoding="gbk")
            f1 = open(oldpath, 'r',encoding="gbk")
            # ans = f1.readline()
            # print(ans)
            for line in f1.readlines():
                date_tran1 = re.sub('(&quot)+', '',line)
                line = line.replace(line, date_tran1)
                date_tran2 = re.sub('(&nbsp;)+', '',line)
                line = line.replace(line, date_tran2)
                date_tran3 = re.sub('[\u4e00-\u9fa5\d��]*��[\u4e00-\u9fa5\d��]*[����]', '', line)
                line = line.replace(line, date_tran3)
                date_tran4 = re.sub('[\u4e00-\u9fa5\d��]*����[\u4e00-\u9fa5\d��]*[����]', '', line)
                line = line.replace(line, date_tran4)
                date_tran5 = re.sub('[\u4e00-\u9fa5\d��]*����[\u4e00-\u9fa5\d��]*[����]', '', line)
                line = line.replace(line, date_tran5)
                print(line)
                new_file.write(line)

            new_file.close()
            f1.close()
            o.write(newpath + '\n')

        # except:
        #     print('error')
        #     continue

    o.close()

def Data(aimpath):
    files = os.listdir(aimpath)
    f = open("/Users/xujiaxing/Documents/GitHub/Intelligent-interrogation/Intelligent-interrogation/python-LDA/data/data.txt", "a", encoding="utf-8")
    for filename in files:
        print(filename)
        if not fnmatch.fnmatch(filename, '*.txt'):
            continue

        oldpath = os.path.abspath(os.path.join(aimpath, filename))
        old_file = open(oldpath, 'r',encoding="gbk")
        data = old_file.read()
        f.write(data + "\n")
        old_file.close()

    f.close()

if __name__ == '__main__':
    # Data(('../../data/result/newdir/'))
    Extract('../../data/result/')
    print("done")
