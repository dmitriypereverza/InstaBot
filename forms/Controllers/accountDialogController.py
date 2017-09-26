# -*- coding: utf-8 -*-
from functools import partial
from pathlib import Path

from PyQt5 import QtWidgets, QtGui
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QDialog, QFileDialog, QMessageBox

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
        'userSource': {
            'UserList': {
                'radio': 'radioButton_3',
                'source_type': 'file',
                'fileName': 'label_38',
                'source': 'toolButton_2',
            },
            'Hashtags': {
                'radio': 'radioButton_4',
                'source_type': 'file',
                'fileName': 'label_39',
                'source': 'toolButton_3',
            },
            'Geo': {
                'radio': 'radioButton_5',
                'source_type': 'file',
                'fileName': 'label_40',
                'source': 'toolButton_4',
            },
            'Follows': {
                'radio': 'radioButton',
                'source_type': 'text',
                'source': 'lineEdit_4',
            },
            'FollowedBy': {
                'radio': 'radioButton_2',
                'source_type': 'text',
                'source': 'lineEdit_5',
            },
        },
    }
    # settingsContainer = {
    #     'userSource': {
    #     },
    #     'like': {
    #         'needLike': True,
    #         'firstLike': True,
    #         'limit': '',
    #         'count': '',
    #         'range': '',
    #     },
    #     'follows': {
    #         'needFollow': True,
    #     },
    #     'comments': {
    #         'needComment': True,
    #         'commentFilePath': '',
    #     },
    #     'other': {
    #         'isCycleLoop': True,
    #     }
    # }
    def __init__(self, login):
        super().__init__()
        self.ui = Ui_AccountDialog()
        self.account = User(InstaBot().getUserInfoByLogin(login))
        self.resultDialog = {}
        self.settingsContainer = {'userSource': {}}
        self.loadAccountInfo()
        self.setInnerConnects()

        self.initErrorMsg()

    def initErrorMsg(self):
        self.error_msg = QMessageBox()
        self.error_msg.setIcon(QMessageBox.Critical)
        self.error_msg.setWindowTitle("Error")
        self.error_msg.setDetailedText("")

    def setInnerConnects(self):
        self.ui.buttonBox.accepted.connect(self.accept)
        self.ui.buttonBox.rejected.connect(self.ui.reject)

        for key, userSource in AccountDialogController.listFields['userSource'].items():
            if userSource['source_type'] == 'file':
                self.getAttr('userSource', key, 'source').clicked.connect(partial(self.getFile, key))

    def accept(self):
        self.resultDialog = self.getSettings()
        if self.resultDialog:
            self.ui.accept()

    def getData(self):
        result = self.ui.exec_()
        return self.resultDialog, result == QDialog.Accepted

    def getSettings(self):
        resultDialog = {}

        userSourseResult = self.getUserSourseResult()
        if userSourseResult:
            resultDialog['sourceUser'] = userSourseResult

        return resultDialog

    def getUserSourseResult(self):
        for key, value in AccountDialogController.listFields['userSource'].items():
            if self.getAttr('userSource', key, 'radio').isChecked():
                if value['source_type'] == 'file':
                    if key in self.settingsContainer['userSource']:
                        return dict(type=key, value=self.settingsContainer['userSource'][key]['value'])
                    self.error_msg.setText("Заполните все поля источника данных")
                    self.error_msg.exec_()
                elif value['source_type'] == 'text':
                    text = self.getAttr('userSource', key, 'source').text()
                    if text:
                        return dict(type=key, value=text)
                    self.error_msg.setText("Заполните все поля источника данных")
                    self.error_msg.exec_()


    def getFile(self, type):
        fname = QFileDialog.getOpenFileName(self, 'Open file', '', "Text files (*.txt)")
        self.settingsContainer['userSource'][type] = {'value': fname[0]}
        self.setAttrText(self.getAttr('userSource', type, 'fileName'), Path(fname[0]).name)

    def loadAccountInfo(self):
        self.setIcon()
        self.setTitleText()
        self.setAttrText(self.getAttr('countFollowedBy'), self.account.followsCount)
        self.setAttrText(self.getAttr('countFollowers'), self.account.followed_by)
        self.setAttrText(self.getAttr('countMedia'), self.account.media_count)

    def setAttrText(self, attr, value):
        attr.setText(str(value))

    def getAttr(self, *args):
        value = AccountDialogController.listFields
        for arg in args:
            value = value[arg]

        return getattr(self.ui, value)

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