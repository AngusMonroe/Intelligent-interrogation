__author__='XJX'
__date__='2017.08.02'
# -*- coding: utf-8 -*-

import sys

from PyQt5.QtWidgets import QApplication , QMainWindow, QPushButton
from PyQt5 import QtCore, QtGui
from main_pyqt5 import *
from answer_pyqt5 import *
from gensim.models import word2vec
import logging

if __name__ == '__main__':
    model =word2vec.Word2Vec.load("/users/xujiaxing/downloads/ml.model")
    print("wow")

    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())