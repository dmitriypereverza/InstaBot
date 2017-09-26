#!/usr/bin/python3
# -*- coding: utf-8 -*-
from PyQt5 import uic

accountListBase, accountListForm = uic.loadUiType('/home/west920/PycharmProjects/InstaBot/forms/ui/accountList.ui')
class UI_AccountList(accountListBase, accountListForm):

    def __init__(self, parent=None):
        super(accountListBase, self).__init__(parent)
        self.setupUi(self)