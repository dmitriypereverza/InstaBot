#!/usr/bin/python3
# -*- coding: utf-8 -*-
import urllib
from pathlib import Path

import requests
import shutil
import validators
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtGui import QPixmap

from config import resourse_dir_path

class QAccountList(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(QAccountList, self).__init__(parent)
        self.textQVBoxLayout = QtWidgets.QVBoxLayout()
        self.textUpQLabel = QtWidgets.QLabel()
        self.textDownQLabel = QtWidgets.QLabel()
        self.textQVBoxLayout.addWidget(self.textUpQLabel)
        self.textQVBoxLayout.addWidget(self.textDownQLabel)
        self.allQHBoxLayout = QtWidgets.QHBoxLayout()
        self.iconQLabel = QtWidgets.QLabel()
        self.allQHBoxLayout.addWidget(self.iconQLabel)
        self.allQHBoxLayout.addLayout(self.textQVBoxLayout, 1)

        self.allQHBoxLayout.addSpacing(1)

        self.pushButton_2 = QtWidgets.QPushButton()
        self.pushButton_2.setObjectName("pushButton_account_start")
        self.pushButton_2.setText("Запустить")
        self.allQHBoxLayout.addWidget(self.pushButton_2)

        self.pushButton_2 = QtWidgets.QPushButton()
        self.pushButton_2.setObjectName("pushButton_account_stop")
        self.pushButton_2.setText("Остановить")
        self.allQHBoxLayout.addWidget(self.pushButton_2)

        self.setLayout(self.allQHBoxLayout)
        # setStyleSheet
        self.textUpQLabel.setStyleSheet('''
            color: rgb(0, 0, 255);
        ''')
        self.textDownQLabel.setStyleSheet('''
            color: rgb(255, 0, 0);
        ''')

    def setTextUp(self, text):
        self.textUpQLabel.setText(text)

    def setTextDown(self, text):
        self.textDownQLabel.setText(text)

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
