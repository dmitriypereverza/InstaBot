# -*- coding: utf-8 -*-
from functools import partial
from pathlib import Path

from PyQt5 import QtWidgets, QtGui, QtSql
from PyQt5.QtGui import QPixmap
from PyQt5.QtSql import QSqlTableModel
from PyQt5.QtWidgets import QDialog, QFileDialog, QMessageBox

import config
from classes.Database.Models.Accounts import Accounts
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
                'fileName': 'lineEdit_6',
                'source': 'toolButton_2',
            },
            'Hashtags': {
                'radio': 'radioButton_4',
                'source_type': 'file',
                'fileName': 'lineEdit_7',
                'source': 'toolButton_3',
            },
            'Geo': {
                'radio': 'radioButton_5',
                'source_type': 'file',
                'fileName': 'lineEdit_4',
                'source': 'toolButton_4',
            },
            'Follows': {
                'radio': 'radioButton',
                'source_type': 'file',
                'fileName': 'lineEdit_5',
                'source': 'toolButton_5',
            },
            'FollowedBy': {
                'radio': 'radioButton_2',
                'source_type': 'file',
                'fileName': 'lineEdit_8',
                'source': 'toolButton_6',
            },
        },
        'like': {
            'needLike': 'groupBox_3',
            'firstLike': 'checkBox',
            'limit': 'lineEdit_10',
            'count': 'lineEdit_11',
            'range': 'lineEdit_12',
        },
        'needFollow': 'groupBox_4',
        'isCycleLoop': 'checkBox_2',
        'comment': {
            'needComment': 'groupBox_5',
            'editField': 'lineEdit_9',
        }
    }

    def __init__(self, account_id):
        super().__init__()
        self.ui = Ui_AccountDialog()
        self.account = self.getAccount(account_id)
        self.resultDialog = {}
        self.settingsContainer = {'userSource': {}}
        self.loadAccountInfo()
        self.setInnerConnects()

        self.mapper = self.createMapper(account_id)

        self.initErrorMsg()

    def getAccount(self, id):
        account = Accounts.get(id=id)
        return User(InstaBot().getUserInfoByLogin(account.login))


    def createMapper(self, account_id):
        model = QSqlTableModel()
        model.setTable('tasks')
        model.setFilter('account_id = ' + str(account_id))
        model.select()

        mapModel = QtWidgets.QDataWidgetMapper()
        mapModel.setModel(model)

        mapModel.addMapping(self.getAttr('userSource', 'UserList', 'radio'), model.fieldIndex('source_user_list_active'))
        mapModel.addMapping(self.getAttr('userSource', 'UserList', 'fileName'), 4)
        mapModel.addMapping(self.getAttr('userSource', 'Hashtags', 'radio'), 5)
        mapModel.addMapping(self.getAttr('userSource', 'Hashtags', 'fileName'), 6)
        mapModel.addMapping(self.getAttr('userSource', 'Geo', 'radio'), 7)
        mapModel.addMapping(self.getAttr('userSource', 'Geo', 'fileName'), 8)
        mapModel.addMapping(self.getAttr('userSource', 'Follows', 'radio'), 9)
        mapModel.addMapping(self.getAttr('userSource', 'Follows', 'fileName'), 10)
        mapModel.addMapping(self.getAttr('userSource', 'FollowedBy', 'radio'), 11)
        mapModel.addMapping(self.getAttr('userSource', 'FollowedBy', 'fileName'), 12)

        mapModel.addMapping(self.getAttr('like', 'needLike'), 13)
        mapModel.addMapping(self.getAttr('like', 'firstLike'), 14)
        mapModel.addMapping(self.getAttr('like', 'limit'), 15)
        mapModel.addMapping(self.getAttr('like', 'count'), 16)
        mapModel.addMapping(self.getAttr('like', 'range'), 17)
        mapModel.addMapping(self.getAttr('needFollow'), 18)
        mapModel.addMapping(self.getAttr('comment', 'needComment'), 19)
        mapModel.addMapping(self.getAttr('comment', 'editField'), 20)
        mapModel.addMapping(self.getAttr('isCycleLoop'), 21)
        mapModel.setSubmitPolicy(QtWidgets.QDataWidgetMapper.ManualSubmit)
        mapModel.toFirst()

        return mapModel

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
        self.mapper.submit()
        self.ui.accept()

    def getUserSourseResult(self):
        for key, value in AccountDialogController.listFields['userSource'].items():
            if self.getAttr('userSource', key, 'radio').isChecked():
                if key in self.settingsContainer['userSource']:
                    return dict(type=key, value=self.settingsContainer['userSource'][key]['value'])
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