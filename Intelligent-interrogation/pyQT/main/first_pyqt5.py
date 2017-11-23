# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/xujiaxing/Intelligent-interrogation/mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class ui_MainWindow(object):

    def firtPyQt5_button_click(self):
        print("mdzz")
        QtWidgets.QMessageBox.information(self.bt_ok, "标题", "这是第一个PyQt5 GUI程序")

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
        #self.bt_ok.clicked.connect(mainWindow.show())
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "智能问诊"))
        self.et_describe.setHtml(_translate("MainWindow",
                                            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                            "p, li { white-space: pre-wrap; }\n"
                                            "</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
                                            "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.bt_ok.setText(_translate("MainWindow", "OK"))
        self.label_title.setText(_translate("MainWindow", "请输入您的症状"))
