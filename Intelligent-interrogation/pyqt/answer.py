# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'answer.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5.QtWidgets import QApplication , QMainWindow, QPushButton, QWidget
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPalette,QPixmap,QFont
from PyQt5.QtCore import Qt
from mainwindow import *

class Ui_Answer(QWidget):
    def setupUi(self, Answer, ans):
        Answer.setObjectName("Answer")
        Answer.resize(400, 300)
        # self.tableView = QtWidgets.QTableView(Answer)
        # self.tableView.setGeometry(QtCore.QRect(10, 10, 250, 250))
        # self.tableView.setObjectName("tableView")
        self.pushButton = QtWidgets.QPushButton(Answer)
        self.pushButton.setGeometry(QtCore.QRect(300, 20, 81, 32))
        self.pushButton.setObjectName("pushButton")
        pe = QPalette()
        label1 = QtWidgets.QLabel(Answer)  # 绑定label到窗口
        label1.setText(ans)  # 设置label标签的文字内容
        label1.setGeometry(20, 20, 250, 250)  # 设置控件相对父窗口位置宽高 参数(x,y,w,h)
        label1.setAutoFillBackground(True)  # 设置背景充满，为设置背景颜色的必要条件
        pe.setColor(QPalette.Window, Qt.white)  # 设置背景颜色
        label1.setPalette(pe)

        self.retranslateUi(Answer)
        self.pushButton.clicked.connect(self.close)

        # self.pushButton.clicked.connect(self.pushButton.click)
        QtCore.QMetaObject.connectSlotsByName(Answer)

    def retranslateUi(self, Answer):
        _translate = QtCore.QCoreApplication.translate
        Answer.setWindowTitle(_translate("Answer", "Dialog"))
        self.pushButton.setText(_translate("Answer", "OK"))

