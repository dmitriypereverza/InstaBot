# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog

from forms.Ui_AccountDialog import Ui_AccountDialog

class AccountDialogController(QtWidgets.QWidget):
    def __init__(self):
        self.ui = Ui_AccountDialog()
        self.ui.setupUi(self)
        self.ui.retranslateUi(self)

    def getData(self):
        result = self.ui.exec_()
        data = self.getSettings()
        return data, result == QDialog.Accepted

    def getSettings(self):
        return 'ouuuu ess'
