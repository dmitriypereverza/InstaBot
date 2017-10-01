#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

from PyQt5 import QtWidgets, QtSql
from PyQt5.QtCore import pyqtSignal
from PyQt5 import QtCore
from PyQt5.QtWidgets import QListWidgetItem

from classes.Accounts.AccountManager import AccountManager
from classes.Bot import bot
from classes.Log.Log import Logger
from classes.Log.Loggers.TextEditLogger import TextEditLogger
from classes.Thread.threadPull import ThreadsPull
from forms.Controllers.accountDialogController import AccountDialogController
from forms.Controllers.accountListController import AccountListController
from forms.Ui_MainForm import Ui_MainForm

class MainForm(QtWidgets.QMainWindow):
    logSendSignal = pyqtSignal(str, name='logSendSignal')
    accountAddSignal = pyqtSignal(str, str, int, name='accountAddSignal')
    startBotAccount = pyqtSignal(str, name='startBotAccount')
    finishBotAccount = pyqtSignal(int, name='finishBotAccount')

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainForm()
        self.ui.setupUi(self)
        self.openConnection()
        self.registerForeignSignals()
        self.registerInnerSignals()

        self.fillAccountList()

    def openConnection(self):
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('/home/west920/PycharmProjects/InstaBot/classes/Database/people.db')
        db.open()

    def registerInnerSignals(self):
        self.ui.pushButton_2.clicked.connect(self.start_bot)
        self.ui.listWidget.itemDoubleClicked.connect(self.open_account_dialog)

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

    def open_account_dialog(self, item: QListWidgetItem):
        dialog = AccountDialogController(item.data(QtCore.Qt.UserRole))
        dialog.ui.exec_()

    def fillAccountList(self):
        AccountManager(self.accountAddSignal).fillUIAccountList()

    def add_account_row(self, name, icon, id):
        myQCustomQWidget = AccountListController()
        myQCustomQWidget.setTextUp(name)
        myQCustomQWidget.setStatus('Готов к запуску')
        myQCustomQWidget.setIcon(icon, name)
        myQCustomQWidget.setBotStartSignal(self.startBotAccount)

        myQListWidgetItem = QtWidgets.QListWidgetItem(self.ui.listWidget)
        myQListWidgetItem.setSizeHint(myQCustomQWidget.sizeHint())
        myQListWidgetItem.setData(QtCore.Qt.UserRole, id)

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