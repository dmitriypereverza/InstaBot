#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import threading

import run
from classes.Log.Log import Logger
from classes.Log.Loggers.TextEditLogger import TextEditLogger
from forms.ui.startForm import Ui_Form
from PyQt5 import QtWidgets

class MainForm(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.startBotButton.clicked.connect(self.start_bot)

    def start_bot(self):
        Logger().setLoggerType(TextEditLogger(self.ui.textEdit))
        t = threading.Thread(target=run.run)
        t.start()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    my_app = MainForm()
    my_app.show()
    sys.exit(app.exec_())