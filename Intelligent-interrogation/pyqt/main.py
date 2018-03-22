__author__ = 'XJX'
__date__ = '2018.03.16'
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5 import QtCore, QtGui
from mainwindow import *
from answer import *
from gensim.models import word2vec
import logging


if __name__ == '__main__':
    model = word2vec.Word2Vec.load("../../data/ml.model")
    print("wow")

    app = QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
