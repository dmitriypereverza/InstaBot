# -*- coding: utf-8 -*-
from PyQt5 import uic

accountBase, accountForm = uic.loadUiType('/home/west920/PycharmProjects/InstaBot/forms/ui/account.ui')
class Ui_AccountDialog(accountBase, accountForm):

    def __init__(self, parent=None):
        super(accountBase, self).__init__(parent)
        self.setupUi(self)
