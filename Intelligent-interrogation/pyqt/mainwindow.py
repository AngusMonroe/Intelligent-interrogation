# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtPrintSupport , QtWidgets, QtGui, QtWidgets
from gensim.models import word2vec
import pymssql
import Levenshtein
import jieba
import jieba.analyse
import xlrd
import xlwt
import re
from PyQt5.QtWidgets import QApplication , QMainWindow, QPushButton, QDialog, QWidget
from answer import *
from dialog import *


class Ui_MainWindow(object):

    def __init__(self):
        self.childwindow = QtWidgets.QMainWindow()
        self.ans = "您的建议用药有：\n"


    # path: excel绝对路径
    # keys: 五个关键词数组，一定要是utf-8式编码，否则计算时汉字权重为3
    # keysWeight： 五个关键词相关度
    # colsWeight： 关键字匹配到不同列后所乘的权重参数（默认共三列）
    # ansNum： 输出总数
    # 输出: 最有行数（行数从0开始）
    def matchKeyWords(self,path, keys, keysWeight, colsWeight, ansNum):
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
        for i in range(0, ansNum):
            cell_value = sheet1.cell_value(ans[i][1], 2)
            self.ans += cell_value + '\n'
            print(cell_value)
            #print(ans[i][1])

    def firstPyQt5_button_click(self):
        self.ans = "您的建议用药有：\n"
        txt = self.et_describe.toPlainText()

        if txt:
            jieba.load_userdict("../../data/jibingICD.txt")
            txt_key = jieba.analyse.extract_tags(txt, topK=2, withWeight=False)  # 从输入中提取关键词
            print(txt_key)
            model = word2vec.Word2Vec.load("../../data/ml.model")
            if len(txt_key)>1:  #双关键词
                print(model.similarity(txt_key[0], txt_key[1]))
                if model.similarity(txt_key[0], txt_key[1])> 0.5:  #两关键词比较相近，使用两个关键词进行匹配
                    y2 = model.most_similar(txt_key, topn=4)  # 4个最相关的
                    print("和【%s】最相关的词有：\n" % txt_key)
                else: #两关键词差距较大，只使用第一个关键词匹配
                    y2 = model.most_similar(txt_key[0], topn=4)  # 4个最相关的
                    print("和【%s】最相关的词有：\n" % txt_key[0])
            else:  #单关键词
                y2 = model.most_similar(txt_key[0], topn=4)  # 4个最相关的
                print("和【%s】最相关的词有：\n" % txt_key[0])

            key = [0 for x in range(0, 6)]
            i = 1
            key[0] = txt_key[0]
            for item in y2:
                print(item[0], item[1])
                #name = item[0].encode("utf-8")
                key[i] = item[0]
                #key.append((name,i))
                i = i + 1

            path = r'../../data/disease_information.xls'

            #key[1] = u"肾性高血压"
            #key[2] = u"心功能不全"
            #key[3] = u"充血性心力衰竭"
            #key[4] = u"高血压病"
            #key[5] = u"高血脂"
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

            ansNum = 10

            self.matchKeyWords(path, keys, keysWeight, colsWeight, ansNum)

                #ms = MSSQL(host="47.94.12.243", user="sa", pwd="Jiuyi8899", db="Database")
            #reslist = ms.ExecQuery("select 适应症 from data")
            #for i in reslist:
                #TODO 匹配算法
            Ui_Answer().setupUi(self.childwindow,self.ans)
            self.childwindow.show()
            print("test")
        else:
            print("error")
            Ui_Dialog().setupUi(self.childwindow)
            self.childwindow.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 300)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.et_describe = QtWidgets.QTextEdit(self.centralWidget)
        self.et_describe.setGeometry(QtCore.QRect(80, 60, 241, 121))
        self.et_describe.setObjectName("et_describe")
        self.bt_ok = QtWidgets.QPushButton(self.centralWidget)
        self.bt_ok.setGeometry(QtCore.QRect(250, 210, 71, 32))
        self.bt_ok.setObjectName("bt_ok")
        self.label_title = QtWidgets.QLabel(self.centralWidget)
        self.label_title.setGeometry(QtCore.QRect(80, 20, 191, 21))
        self.label_title.setObjectName("label_title")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 400, 22))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        self.bt_ok.clicked.connect(self.firstPyQt5_button_click)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.et_describe.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.bt_ok.setText(_translate("MainWindow", "OK"))
        self.label_title.setText(_translate("MainWindow", "请输入您的症状"))

