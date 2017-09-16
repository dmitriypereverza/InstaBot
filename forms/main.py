#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import threading
import run
from collections import namedtuple
from PyQt5.QtCore import pyqtSignal
from classes.Log.Log import Logger
from classes.Log.Loggers.TextEditLogger import TextEditLogger
from forms.ui.custom.CustomListView import QAccountList
from forms.ui.startForm import Ui_Form
from PyQt5 import QtWidgets

class MainForm(QtWidgets.QWidget):
    logSendSignal = pyqtSignal(str, name='logSendSignal')
    accountAddSignal = pyqtSignal(str, str, str, name='accountAddSignal')

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.registerForeignSignals()
        self.registerInnerSignals()

    def registerInnerSignals(self):
        self.ui.pushButton_2.clicked.connect(self.start_bot)

    def registerForeignSignals(self):
        self.logSendSignal.connect(self.log_send)
        self.accountAddSignal.connect(self.add_account_row)

    def start_bot(self):
        Logger().setLoggerType(TextEditLogger(self.logSendSignal))
        t = threading.Thread(target=run.run)
        t.daemon = True
        t.start()

    def log_send(self, text):
        self.ui.textEdit.insertHtml(text)

    def add_account_row(self, index, name, icon):
        Account = namedtuple('Account', ['index', 'name', 'icon'])
        account = Account(index, name, icon)
        myQCustomQWidget = QAccountList()
        myQCustomQWidget.setTextUp(account.index)
        myQCustomQWidget.setTextDown(account.name)
        myQCustomQWidget.setIcon(account.icon)
        myQListWidgetItem = QtWidgets.QListWidgetItem(self.ui.listWidget)
        myQListWidgetItem.setSizeHint(myQCustomQWidget.sizeHint())
        self.ui.listWidget.addItem(myQListWidgetItem)
        self.ui.listWidget.setItemWidget(myQListWidgetItem, myQCustomQWidget)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    my_app = MainForm()
    my_app.show()
    sys.exit(app.exec_())