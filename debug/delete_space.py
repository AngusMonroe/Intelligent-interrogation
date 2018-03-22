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

            # new_file = open(newpath, 'a',encoding="gbk")
            f1 = open(oldpath, 'r',encoding="gbk")
            # ans = f1.readline()
            # print(ans)
            for line in f1.readlines():
                # date_tran1 = re.sub('(&quot)+', '',line)
                # line = line.replace(line, date_tran1)
                # date_tran2 = re.sub('(&nbsp;)+', '',line)
                # line = line.replace(line, date_tran2)
                date_tran = re.sub('[����][\u4e00-\u9fa5]*��[\u4e00-\u9fa5]*[����]', '', line)
                #line = line.replace(line, date_tran)
                print(date_tran)
                # new_file.write(line)
            #
            # new_file.close()
            # f1.close()
            # o.write(newpath + '\n')

        # except:
        #     print('error')
        #     continue

    o.close()

if __name__ == '__main__':
    Extract('../../data/result')
    print("done")
