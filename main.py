#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSignal

from classes.Accounts.AccountManager import AccountManager
from classes.Bot import bot
from classes.Log.Log import Logger
from classes.Log.Loggers.TextEditLogger import TextEditLogger
from classes.Thread.threadPull import ThreadsPull
from forms.ui.custom.CustomListView import QAccountList
from forms.ui.startForm import Ui_Form

class MainForm(QtWidgets.QWidget):
    logSendSignal = pyqtSignal(str, name='logSendSignal')
    accountAddSignal = pyqtSignal(str, str, name='accountAddSignal')
    startBotAccount = pyqtSignal(str, name='startBotAccount')
    finishBotAccount = pyqtSignal(int, name='finishBotAccount')

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.registerForeignSignals()
        self.registerInnerSignals()

        self.fillAccountList()

    def registerInnerSignals(self):
        self.ui.pushButton_2.clicked.connect(self.start_bot)

    def registerForeignSignals(self):
        self.logSendSignal.connect(self.log_send)
        self.accountAddSignal.connect(self.add_account_row)
        self.startBotAccount.connect(self.start_bot)
        self.finishBotAccount.connect(self.finishBot)

    def start_bot(self, login):
        Logger().setLoggerType(TextEditLogger(self.logSendSignal))
        ThreadsPull().startOrStopThread(bot.AccountThread(login, self.finishBotAccount))

    def log_send(self, text):
        self.ui.textEdit.insertHtml(text)

    def fillAccountList(self):
        AccountManager(self.accountAddSignal).fillUIAccountList()

    def add_account_row(self, name, icon):
        myQCustomQWidget = QAccountList()
        myQCustomQWidget.setTextUp(name)
        myQCustomQWidget.setStatus('Готов к запуску')
        myQCustomQWidget.setIcon(icon, name)
        myQCustomQWidget.setBotStartSignal(self.startBotAccount)

        myQListWidgetItem = QtWidgets.QListWidgetItem(self.ui.listWidget)
        myQListWidgetItem.setSizeHint(myQCustomQWidget.sizeHint())
        self.ui.listWidget.addItem(myQListWidgetItem)
        self.ui.listWidget.setItemWidget(myQListWidgetItem, myQCustomQWidget)

    def finishBot(self, bot_id):
        widget = self.getAccountRowById(bot_id - 1)
        widget.pushButton_1.setText('Старт')
        widget.setStatus('Готов к запуску')

    def getAccountRowById(self, bot_id):
        row = self.ui.listWidget.item(bot_id)
        widget = self.ui.listWidget.itemWidget(row)
        return widget

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    my_app = MainForm()
    my_app.show()
    sys.exit(app.exec_())