#!/usr/bin/python3
# -*- coding: utf-8 -*-
import urllib
from pathlib import Path

import requests
import shutil
import validators
from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap

from config import resourse_dir_path

class QAccountList(QtWidgets.QWidget):
    botStartSignal = None

    def __init__(self, parent=None):
        super(QAccountList, self).__init__(parent)
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

        self.setInnerSignal()

        self.setLayout(self.allQHBoxLayout)
        # setStyleSheet
        self.textUpQLabel.setStyleSheet('''
            color: rgb(0, 0, 255);
        ''')
        self.statusLable.setStyleSheet('''
            color: rgb(255, 0, 0);
        ''')

    def setInnerSignal(self):
        self.pushButton_1.clicked.connect(self.push_start_btn)

    def push_start_btn(self):
        if self.sender().text() != "Остановить":
            self.sender().setText("Остановить")
        else:
            self.sender().parent().statusLable.setText("Пытаюсь остановиться...")
        self.botStartSignal.emit(self.sender().parent().textUpQLabel.text())

    def setBotStartSignal(self, signal):
        self.botStartSignal = signal

    def setTextUp(self, text):
        self.textUpQLabel.setText(text)

    def setStatus(self, text):
        self.statusLable.setText(text)

    def setIcon(self, imagePath, login):
        imgPath = Path('{}/img/avatars/{}.jpeg'.format(resourse_dir_path, login))
        if not imgPath.exists():
            if validators.url(imagePath):
                response = requests.get(imagePath, stream=True)
                with open(imgPath._str, 'wb') as out_file:
                    shutil.copyfileobj(response.raw, out_file)
                del response

        pixmap = QPixmap(imgPath._str)
        if not pixmap.isNull():
            self.iconQLabel.setPixmap(pixmap.scaled(48, 48))
