# -*- coding: utf-8 -*-
from pathlib import Path

from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QDialog

import config
from classes.Instagram.InstaBot import InstaBot
from classes.Instagram.instaUser import User
from forms.Ui_AccountDialog import Ui_AccountDialog

class AccountDialogController(QtWidgets.QDialog):
    listFields = {
        'avatarImg': 'label',
        'title': 'label_2',
        'countFollowers': 'label_6',
        'countFollowedBy': 'label_4',
        'countMedia': 'label_8',
    }
    def __init__(self, login):
        super().__init__()
        self.ui = Ui_AccountDialog()
        self.ui.setupUi(self.ui)
        self.account = User(InstaBot().getUserInfoByLogin(login))
        self.loadAccountInfo()

    def getData(self):
        result = self.ui.exec_()
        data = self.getSettings()
        return data, result == QDialog.Accepted

    def getSettings(self):
        return 'ouuuu ess'

    def loadAccountInfo(self):
        self.setIcon()
        self.setTitleText()
        self.setAttr('countFollowedBy', self.account.followsCount)
        self.setAttr('countFollowers', self.account.followed_by)
        self.setAttr('countMedia', self.account.media_count)

    def setAttr(self, refName, value):
        getattr(self.ui, AccountDialogController.listFields[refName]).setText(str(value))

    def setIcon(self):
        imgPath = Path('{}/img/avatars/{}.jpeg'.format(config.resourse_dir_path, self.account.username))
        if imgPath.exists():
            pixmap = QPixmap(imgPath._str)
            if not pixmap.isNull():
                self.getAvatarImg().setPixmap(pixmap.scaled(150, 150))

    def getAvatarImg(self):
        return self.ui.label

    def getTitle(self):
        return self.ui.label_2

    def setTitleText(self):
        self.getTitle().setText("<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">{}</span></p></body></html>".format(self.account.username))