# -*- coding: utf-8 -*-
__author__ = 'XJX'
__date__ = '2018.03.11'

"""
description:
    copy data from data.txt to train.dat
"""

import codecs
import configparser

conf = configparser.ConfigParser()
conf.read("setting.conf")

if __name__ == '__main__':

    fp = open('data/data.txt', 'r')
    for line in fp:
        with codecs.open('data/train.dat', 'a', 'utf-8') as f:
            f.write(line)
    print('done')
    fp.close()
