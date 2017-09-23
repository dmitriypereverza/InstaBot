#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets

class UI_AccountList(QtWidgets.QWidget):
    def setupUi(self):
        self.textQVBoxLayout = QtWidgets.QVBoxLayout()
        self.textUpQLabel = QtWidgets.QLabel()
        self.statusLable = QtWidgets.QLabel()
        self.textQVBoxLayout.addWidget(self.textUpQLabel)
        self.textQVBoxLayout.addWidget(self.statusLable)
        self.allQHBoxLayout = QtWidgets.QHBoxLayout()
        self.iconQLabel = QtWidgets.QLabel()
        self.allQHBoxLayout.addWidget(self.iconQLabel)
        self.allQHBoxLayout.addLayout(self.textQVBoxLayout, 1)

        self.allQHBoxLayout.addSpacing(1)

        self.pushButton_1 = QtWidgets.QPushButton()
        self.pushButton_1.setObjectName("pushButton_account_start")
        self.pushButton_1.setText("Запустить")
        self.allQHBoxLayout.addWidget(self.pushButton_1)

        self.setLayout(self.allQHBoxLayout)
        # setStyleSheet
        self.textUpQLabel.setStyleSheet('''
            color: rgb(0, 0, 255);
        ''')
        self.statusLable.setStyleSheet('''
            color: rgb(255, 0, 0);
        ''')