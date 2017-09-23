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
from forms.UI_AccountList import UI_AccountList

class AccountListController(UI_AccountList):
    botStartSignal = None

    def __init__(self):
        super().__init__()
        self.setupUi()
        self.setInnerSignal()

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
