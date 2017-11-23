# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/xujiaxing/Intelligent-interrogation/answer.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!
from PyQt5.QtWidgets import QApplication , QMainWindow, QPushButton
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPalette,QPixmap,QFont
from PyQt5.QtCore import Qt

class Ui_Answer(object):
    def setupUi(self, Answer,ans):
        Answer.setObjectName("Answer")
        Answer.resize(400, 300)
        self.buttonBox = QtWidgets.QDialogButtonBox(Answer)
        self.buttonBox.setGeometry(QtCore.QRect(290, 20, 81, 241))
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        pe = QPalette()
        label1 = QtWidgets.QLabel(Answer)  # 绑定label到窗口
        label1.setText(ans)  # 设置label标签的文字内容
        label1.setGeometry(30, 30, 250, 250)  # 设置控件相对父窗口位置宽高 参数(x,y,w,h)
        label1.setAutoFillBackground(True)  # 设置背景充满，为设置背景颜色的必要条件
        pe.setColor(QPalette.Window,Qt.white)  # 设置背景颜色
        label1.setPalette(pe)


        self.retranslateUi(Answer)
        #self.buttonBox.accepted.connect(Answer.accept)
        #self.buttonBox.rejected.connect(Answer.reject)
        QtCore.QMetaObject.connectSlotsByName(Answer)
        print("gg")

    def retranslateUi(self, Answer):
        _translate = QtCore.QCoreApplication.translate
        Answer.setWindowTitle(_translate("Answer", "Intelligent Interrogation"))

