# -*- coding: utf-8 -*-
from pathlib import Path

from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QDialog, QFileDialog

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
        'addCommentFileBtn': 'toolButton',
        'commentFileName': 'label_13',
        'addLoginListFileBtn': 'toolButton_2',
        'addLoginListFileName': 'label_38',
        'addHashtagListFileBtn': 'toolButton_3',
        'addHashtagListFileName': 'label_39',
        'addLocationListFileBtn': 'toolButton_4',
        'addLocationListFileName': 'label_40',
    }
    settingsContainer = {
        'userSource': {
            'type': '',
            'value': '',
        },
        'like': {
            'needLike': True,
            'firstLike': True,
            'limit': '',
            'count': '',
            'range': '',
        },
        'follows': {
            'needFollow': True,
        },
        'comments': {
            'needComment': True,
            'commentFilePath': '',
        },
        'other': {
            'isCycleLoop': True,
        }
    }
    def __init__(self, login):
        super().__init__()
        self.ui = Ui_AccountDialog()
        self.ui.setupUi(self.ui)
        self.account = User(InstaBot().getUserInfoByLogin(login))
        self.loadAccountInfo()
        self.setInnerConnects()

    def setInnerConnects(self):
        self.ui.buttonBox.accepted.connect(self.ui.accept)
        self.ui.buttonBox.rejected.connect(self.ui.reject)
        self.getAttr('addCommentFileBtn').clicked.connect(self.getCommentFile)
        self.getAttr('addLoginListFileBtn').clicked.connect(self.getLoginListFile)
        self.getAttr('addHashtagListFileBtn').clicked.connect(self.getHashtagListFile)
        self.getAttr('addLocationListFileBtn').clicked.connect(self.getLocationListFile)

    def getCommentFile(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', '', "Text files (*.txt)")
        AccountDialogController.settingsContainer['comments']['commentFilePath'] = fname[0]
        self.setAttrText('commentFileName', Path(fname[0]).name)

    def getLoginListFile(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', '', "Text files (*.txt)")
        AccountDialogController.settingsContainer['userSource']['type'] = 'LoginList'
        AccountDialogController.settingsContainer['userSource']['value'] = fname[0]
        self.setAttrText('addLoginListFileName', Path(fname[0]).name)

    def getHashtagListFile(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', '', "Text files (*.txt)")
        AccountDialogController.settingsContainer['userSource']['type'] = 'HashtagList'
        AccountDialogController.settingsContainer['userSource']['value'] = fname[0]
        self.setAttrText('addHashtagListFileName', Path(fname[0]).name)

    def getLocationListFile(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', '', "Text files (*.txt)")
        AccountDialogController.settingsContainer['userSource']['type'] = 'LocationList'
        AccountDialogController.settingsContainer['userSource']['value'] = fname[0]
        self.setAttrText('addLocationListFileName', Path(fname[0]).name)

    def getData(self):
        result = self.ui.exec_()
        data = self.getSettings()
        return data, result == QDialog.Accepted

    def getSettings(self):
        return AccountDialogController.settingsContainer

    def loadAccountInfo(self):
        self.setIcon()
        self.setTitleText()
        self.setAttrText('countFollowedBy', self.account.followsCount)
        self.setAttrText('countFollowers', self.account.followed_by)
        self.setAttrText('countMedia', self.account.media_count)

    def setAttrText(self, refName, value):
        self.getAttr(refName).setText(str(value))

    def getAttr(self, refName):
        return getattr(self.ui, AccountDialogController.listFields[refName])

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